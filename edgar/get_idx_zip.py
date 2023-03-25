import zipfile
import pandas as pd

import requests

# Define the URL for the "idx.zip" file
url = 'ftp://ftp.sec.gov/edgar/full-index/idx.zip'

# Send a GET request to download the file
response = requests.get(url, )

# Save the file to your local computer
with open('idx.zip', 'wb') as f:
    f.write(response.content)


# Extract the contents of the "idx.zip" file
with zipfile.ZipFile('idx.zip', 'r') as zip_ref:
    zip_ref.extractall('idx')

# Define the paths to the index files
master_idx_path = 'idx/master.idx'
company_idx_path = 'idx/company.idx'

# Read the master index file into a pandas DataFrame
master_cols = ['cik', 'company_name', 'form_type', 'date_filed', 'filename']
master_data = pd.read_csv(master_idx_path, sep='|', header=None, names=master_cols)

# Save the master index data to a CSV file
master_data.to_csv('master_idx.csv', index=False)
