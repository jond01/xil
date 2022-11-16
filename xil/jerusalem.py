"""
Jerusalem bank exchange data

https://www.bankjerusalem.co.il/capital-market/rates
"""
import pandas as pd

_JERUSALEM_URL = "https://www.bankjerusalem.co.il/capital-market/rates"
_HEADER = None  # the table's header is not recognized

df = pd.read_html(_JERUSALEM_URL, header=_HEADER)[0]

idx0 = pd.MultiIndex.from_product(
    [["currency"], ["name", "official rate", "change (%)"]]
)
idx1 = pd.MultiIndex.from_product([["cash", "transfer"], ["sell", "buy"]])
idx = idx0.append(idx1)
df.columns = idx
