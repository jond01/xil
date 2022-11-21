"""
Mercantile bank

https://www.mercantile.co.il/MB/private/foregin-currency/exchange-rate

The structure is identical Discount's, but the data is different.
"""
# pylint: disable-next=fixme
# TODO: avoid code duplication between this module and `discount`.

import pandas as pd

_MERCANTILE_URL = "\
https://www.mercantile.co.il/MB/private/foregin-currency/exchange-rate"

df = pd.read_html(_MERCANTILE_URL, header=[0, 1])[0]

idx0 = pd.MultiIndex.from_product([["currency"], ["amount", "code", "official rate"]])
idx1 = pd.MultiIndex.from_product([["transfer", "cash"], ["buy", "sell"]])
idx = idx0.append(idx1)
df.columns = idx
