"""
Discount bank

https://www.discountbank.co.il/DB/private/general-information/foreign-currency-transfers/exchange-rates
"""
import pandas as pd

_DISCOUNT_URL = "\
https://www.discountbank.co.il/DB/private/general-information/foreign-currency-transfers/exchange-rates"

df = pd.read_html(_DISCOUNT_URL, header=[0, 1])[0]

idx0 = pd.MultiIndex.from_product([["currency"], ["amount", "code", "official rate"]])
idx1 = pd.MultiIndex.from_product([["transfer", "cash"], ["buy", "sell"]])
idx = idx0.append(idx1)
df.columns = idx
