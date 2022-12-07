"""
FIBI - First International Bank of Israel (HaBank HaBeinleumi)

The exchange rates page
https://www.fibi.co.il/wps/portal/FibiMenu/Marketing/Private/ForeignCurrency/Trade/Rates
includes static data from:
https://apps.fibi.co.il/Matach/matach.aspx
"""
import pandas as pd

from xil._currencies import currency_from_heb_name
from xil._headers import get_url_response

_FIBI_URL = "http://apps.fibi.co.il/Matach/matach.aspx"
_ENCODING = "iso-8859-8"
_MATCH = "המחאות"
_HEADER = [0, 1]
_ATTRS = {"class": "clsPart"}
_RELEVANT_COLS = [
    ("מטבע", "מטבע"),
    ("יחידה", "יחידה"),
    ("יציג", "יציג"),
    ("בנקנוטים", "מכירה"),
    ("בנקנוטים", "קניה"),
    ("המחאות", "מכירה"),
    ("המחאות", "קניה"),
]
_IDX0 = pd.MultiIndex.from_product([["currency"], ["name", "amount", "official rate"]])
_IDX1 = pd.MultiIndex.from_product([["cash", "transfer"], ["sell", "buy"]])
_IDX = _IDX0.append(_IDX1)

with get_url_response(_FIBI_URL) as response:
    dfs = pd.read_html(
        response,  # type: ignore[arg-type]
        match=_MATCH,
        header=_HEADER,
        encoding=_ENCODING,
        attrs=_ATTRS,
    )

df = dfs[0]  # It is guaranteed to have at least one element - otherwise an exception
df = df[_RELEVANT_COLS]
df.columns = _IDX
df[("currency", "code")] = df[("currency", "name")].apply(currency_from_heb_name)
df = df.drop(labels=("currency", "name"), axis=1)
df = df.set_index(("currency", "code"))
