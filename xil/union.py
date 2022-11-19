"""
Union bank ("Igud") foreign exchange data:
https://www.unionbank.co.il/Igud/שוק-ההון-ומטח/מטבע-חוץ/שערי-מטח

Pending Deprecation Note:
Union bank is being merged into Mizrahi-Tefahot bank these days - this module is
expected to be deprecated in the foreseeable future.
"""
from pathlib import Path

import pandas as pd

from xil._headers import get_url_response, UA_HEADER

_UNION_URL = "\
http://www.unionbank.co.il/Igud/%D7%A9%D7%95%D7%A7-%D7%94%D7%94%D7%95%D7%9F-%D7%95%D7%9E%D7%98%D7%97/%D7%9E%D7%98%D7%91%D7%A2-%D7%97%D7%95%D7%A5/%D7%A9%D7%A2%D7%A8%D7%99-%D7%9E%D7%98%D7%97"

# The "rbzid" cookie is required for rendering the HTML on Union bank website.
# Note that it may be outdated
_UNION_COOKIE_HEADER = {
    "Cookie": "\
rbzid=tj1/yktlbTJ1tw1pMf21e3oDjy0XYos7/HzuSgXRuRmIkH1bs5xYEW2wAfxl6ap9YMO2sSUHK9IfejKaQ5g8T4yqkKBD6lUEMW9xy+m+AAbyKX0CIZlBl6pSQNftM767DC2qeSCmet0mPZsIs6WiCCtefXogJNcc8QImoXIIgqHHYzNPqu6mHVmyBawZ9EqAh8NIwBl3mNQhmPcQbQMMqLoe+3wkHM3ExAeqp9vCzTijAnb1YlZH2UG7c0JD5kDXS6bhKKejD7ydPk6LgdN3XFlLeKOwDHyIyzM8xNHKcVU="
}

_UNION_HEADERS = UA_HEADER | _UNION_COOKIE_HEADER
_HEADER = [0, 1]

with get_url_response(_UNION_URL, headers=_UNION_HEADERS) as response:
    df = pd.read_html(response, header=_HEADER)[0]

df = df.drop(("Unnamed: 7_level_0", "מכירה"), axis=1)  # empty (NaNs) column

idx0 = pd.MultiIndex.from_product([["currency"], ["name", "official rate", "change"]])
idx1 = pd.MultiIndex.from_product([["cash", "transfer"], ["buy", "sell"]])
idx2 = pd.MultiIndex.from_tuples((idx0[-1],))
idx = idx0[:-1].append(idx1).append(idx2)
df.columns = idx
df = df[idx0.append(idx1)]