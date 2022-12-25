# -*- coding: utf-8 -*-
"""Build an Equal-Weight S&P 500 Index Fund.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zVAguryCfEjqGaN75WkMlZDNG7SSYJGu

https://colab.research.google.com/
"""

import requests 

symbol = "GOOG"

IEX_CLOUD_API_TOKEN = "Tpk_303eba2884a34a0e937ec42ab848532a"

api_url = f"https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}"

data = requests.get(api_url).json()

print(data)

data