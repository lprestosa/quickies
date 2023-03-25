import requests
import csv

# Send a GET request to download the JSON file
url = 'https://www.sec.gov/files/company_tickers.json'
response = requests.get(url)

# Parse the JSON data
data = response.json()

# Define the output CSV file name and header fields
output_file = 'company_tickers.csv'
header_fields = ['cik', 'ticker', 'company_name']

# Save the JSON data to a CSV file
with open(output_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=header_fields)
    writer.writeheader()
    for key, value in data.items():
        row = {
            'cik': value['cik_str'],
            'ticker': value['ticker'],
            'company_name': value['title'],
        }
        writer.writerow(row)
