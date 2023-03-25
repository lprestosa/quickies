import requests

def get_company_attributes(ticker):
    # Send a GET request to download the JSON file
    url = 'https://www.sec.gov/files/company_tickers.json'
    response = requests.get(url)

    # Parse the JSON data
    data = response.json()

    # Loop through the companies and return the matching attributes
    for key, value in data.items():
        if value['ticker'].lower() == ticker.lower():
            return value

    # Return None if the ticker symbol was not found
    return None

attributes = get_company_attributes('AAPL')
if attributes:
    print('CIK:', attributes['cik_str'])
    print('Ticker:', attributes['ticker'])
    print('Company Name:', attributes['title'])