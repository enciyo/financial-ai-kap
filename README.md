# Financial AI Analysis

This project is a Flask web application that allows users to analyze financial data of companies listed on BIST (Borsa Istanbul) using AI.

## Features

- Input API key and company symbols to fetch financial data.
- Analyze financial data using AI.
- Display analysis results and financial data in a user-friendly format.

## Requirements

- Python 3.8+
- Flask
- pandas
- google-genai
- pykap
- markdown
- Frozen-Flask

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/financial-ai-analysis.git
   cd financial-ai-analysis
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Set the environment variables:
   ```sh
   export FLASK_APP=run.py
   ```

## Usage

1. Run the Flask application:
   ```sh
   flask run
   ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Enter your API key and company symbols to analyze the financial data.

## Deployment

### Deploy to GitHub Pages

1. Freeze the Flask application:
   ```sh
   python freeze.py
   ```

2. Create a `gh-pages` branch and push the static files:
   ```sh
   git checkout --orphan gh-pages
   git reset --hard
   git add build/*
   git commit -m "Deploy to GitHub Pages"
   git push origin gh-pages
   ```

3. Configure GitHub Pages:
   Go to the repository settings on GitHub, scroll down to the "GitHub Pages" section, and select the `gh-pages` branch as the source.

Your static site should now be available at `https://yourusername.github.io/financial-ai-analysis`.

### GitHub Actions Deployment

This project includes a GitHub Actions workflow to automate the freezing and deployment process.

1. Ensure the workflow file is located at `.github/workflows/deploy.yml`.

2. Push your changes to the `main` branch:
   ```sh
   git add .
   git commit -m "Set up GitHub Actions for deployment"
   git push origin main
   ```







This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.## License3. The GitHub Actions workflow will automatically freeze the Flask application and deploy it to GitHub Pages.
