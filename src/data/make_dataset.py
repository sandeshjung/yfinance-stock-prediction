import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import yfinance as yf

from pandas_datareader import data as pdr

yf.pdr_override()

from datetime import datetime 

tech_list = ['AAPL','GOOG','MSFT','AMZN']

end=datetime.now()
start = datetime(end.year-1, end.month-1, end.day)

for stock in tech_list:
    globals()[stock] = yf.download(stock, start,end)
    
company_list = [AAPL, GOOG, MSFT, AMZN]
company_name = ["APPLE", "GOOGLE", "MICROSOFT", "AMAZON"]

for company, con_name in zip(company_list, company_name):
    company['company_name'] = company_name
    