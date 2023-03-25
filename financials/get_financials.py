import os
import pandas as pd
import pandas_datareader.data as web
import yfinance as yf


def get_financial_statements(ticker):
    # Create a Ticker object for the company
    company = yf.Ticker(ticker)
    period = "1y"

    # Extract the balance sheet for the last four quarters
    balance_sheet = company.balance_sheet(period=period)

    # Extract the income statement for the last four quarters
    income_statement = company.financials(period=period)

    # Extract the cash flow statement for the last four quarters
    cash_flow = company.cashflow(period=period)

    # Save the financial statements to a CSV file
    if not os.path.exists("data/financials"):
        os.makedirs("data/financials")
    balance_sheet.to_csv(f"data/financials/{ticker}_bs.csv")
    income_statement.to_csv(f"data/financials/{ticker}_is.csv")
    cash_flow.to_csv(f"data/financials/{ticker}_cf.csv")


# Read the list of tickers from a file
tickers = pd.read_csv('data/sp500.csv', header=None, names=['Ticker'])['Ticker'].tolist()

# Loop through the tickers and download the financial statements
for ticker in tickers:
    print(f"Processing {ticker}...")
    get_financial_statements(ticker)
