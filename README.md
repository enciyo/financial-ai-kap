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
   export FLASK_ENV=production  # For development use `development`
   export SECRET_KEY=your_secret_key
   ```

## Usage

1. Run the Flask application:
   ```sh
   flask run
   ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Enter your API key and company symbols to analyze the financial data.

## Deployment

To deploy the application to a production environment, you can use services like Heroku, AWS, or Azure. Make sure to set the necessary environment variables and configure the server to run the Flask application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
