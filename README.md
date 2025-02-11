# Financial AI KAP

Bu proje, BIST şirketlerinin finansal verilerini analiz etmek için bir Flask uygulaması kullanır.

## Gereksinimler

- Python 3.7+
- Flask
- pandas
- markdown
- pykap

## Kurulum

1. Depoyu klonlayın:

    ```sh
    git clone https://github.com/kullaniciadi/financial-ai-kap.git
    cd financial-ai-kap
    ```

2. Sanal ortam oluşturun ve etkinleştirin:

    ```sh
    python -m venv venv
    source venv/bin/activate  # Windows için: venv\Scripts\activate
    ```

3. Gerekli paketleri yükleyin:

    ```sh
    pip install -r requirements.txt
    ```

4. Ortam değişkenlerini ayarlayın:

    ```sh
    export SECRET_KEY='supersecretkey'  # Windows için: set SECRET_KEY=supersecretkey
    ```

## Kullanım

1. Uygulamayı başlatın:

    ```sh
    python run.py
    ```

2. Tarayıcınızda `http://127.0.0.1:5000` adresine gidin.

3. API anahtarınızı girin ve analiz etmek istediğiniz sembolleri seçin.

## Notlar

- API anahtarınızı almak için [Google AI Studio](https://aistudio.google.com/app/apikey) adresini ziyaret edin.
- Uygulama, sembollerin finansal verilerini almak ve analiz etmek için `pykap` kütüphanesini kullanır.
