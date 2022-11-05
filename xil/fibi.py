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
_TIME_IDX = 3
_DATA_IDX = 4

req = urllib.request.Request(_FIBI_URL, headers=UA_HEADER)
with urllib.request.urlopen(req) as response:
    dfs = pd.read_html(response, header=0, encoding=_ENCODING)

time_str = dfs[_TIME_IDX].columns[0]
df = dfs[_DATA_IDX]
