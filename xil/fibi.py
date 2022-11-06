"""
FIBI - First International Bank of Israel (HaBank HaBeinleumi)

The exchange rates page
https://www.fibi.co.il/wps/portal/FibiMenu/Marketing/Private/ForeignCurrency/Trade/Rates
includes static data from:
https://apps.fibi.co.il/Matach/matach.aspx
"""
import urllib.request

import pandas as pd

from xil._headers import UA_HEADER

_FIBI_URL = "http://apps.fibi.co.il/Matach/matach.aspx"
_ENCODING = "iso-8859-8"
_MATCH = "Spot"
_HEADER = [0, 1]
_ATTRS = {"class": "clsPart"}
_RELEVANT_COLS = [
    ("Spot", "נמוך"),
    ("Spot", "גבוה"),
    ("Same day", "נמוך"),
    ("Same day", "גבוה"),
    ("יחידה", "יחידה"),
    ("מטבע", "מטבע"),
]

req = urllib.request.Request(_FIBI_URL, headers=UA_HEADER)
with urllib.request.urlopen(req) as response:
    dfs = pd.read_html(
        response, match=_MATCH, header=_HEADER, encoding=_ENCODING, attrs=_ATTRS
    )

df = dfs[0]  # It is guaranteed to have at least one element - otherwise an exception
df = df[_RELEVANT_COLS]
