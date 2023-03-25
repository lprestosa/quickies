"""
https://yahooquery.dpguthrie.com/guide/ticker/intro/
poc of yahooquery package --Python wrapper for an unofficial Yahoo Finance API
"""

from yahooquery import Ticker



def get_financials(tick):
    # Retrieve each company's profile information
    ticker = Ticker(tick)
    dict_ap = ticker.asset_profile
    dict_bs = ticker.balance_sheet()
    dict_is = ticker.income_statement()
    dict_cf = ticker.cash_flow()
    print(dict_ap)
    print(dict_bs)
    print(dict_is)
    print(dict_cf)

tick = 'AAPL'

get_financials(tick)