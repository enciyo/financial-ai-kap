import os

import markdown
import pandas as pd
from flask import Flask, render_template, request, session
from pykap.bist import BISTCompany
from pykap.bist_company_list import bist_company_list

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'supersecretkey')  # Use environment variable for secret key

api_key_cache = {}


@app.route('/')
def index():
    api_key = session.get('api_key') or api_key_cache.get('api_key')
    symbols = get_symbols()
    return render_template('index.html', api_key=api_key, symbols=symbols)


@app.route('/table', methods=['GET', 'POST'])
def table():
    if request.method == 'POST':
        api_key = request.form['api_key']
        session['api_key'] = api_key
        api_key_cache['api_key'] = api_key
        symbols = request.form.getlist('symbols[]')
    else:
        symbols = request.args.getlist('symbols')
    data = fetch_data_for_symbols(symbols)
    analysis = get_ai_result(data)
    data_html = {symbol: df.to_html(classes='table table-striped') for symbol, df in data.items()}
    return render_template('table.html', data=data_html, analysis=analysis)


def get_ai_result(data: dict):
    api_key = session.get('api_key') or api_key_cache.get('api_key')
    if not api_key:
        return "API key not set"
    from google import genai
    client = genai.Client(api_key=api_key)
    chat = client.chats.create(model='gemini-2.0-flash')
    msg = "Şirketin/şirketlerin finansman verileri:\n"
    for symbol, df in data.items():
        msg += f"\n{symbol}:\n"
        msg += df.to_string()
    msg += "\nBu Şirketin/şirketlerin finansal durumu hakkında ne düşünüyorsunuz? Önce her şirketi ayrı değerlendir, sonra beraber değerlendir. Sonuçları sadece markdown olarak ver"

    response = chat.send_message(message=msg)

    response_html = markdown.markdown(response.text)
    return response_html


def get_symbols():
    return bist_company_list()


def fetch_data_for_symbols(symbols):
    all_data = {}
    for symbol in symbols:
        comp = BISTCompany(symbol)
        data = comp.get_financial_reports()
        results = {}
        for period, values in data.items():
            for result_key, result_value in values['results'].items():
                if result_key not in results:
                    results[result_key] = {}
                results[result_key][period] = result_value
        df = pd.DataFrame(results).T
        all_data[symbol] = df
    return all_data



