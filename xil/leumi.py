"""
Leumi's official exchange web page:
https://www.leumi.co.il/Lobby/currency_rates/40806/
embeds the table from:
https://www.bankleumi.co.il/vgnprod/currency/new_shaar_muskamim.html
which in turn consumes its data from:
https://www.bankleumi.co.il/vgnprod/currency/ajax/new_shaar_muskamim_data.json

Historical data by currency ID:
https://www.bankleumi.co.il/vgnprod/currency/ExchangeRateByCurrency.aspx?in_matbea=1

For business data:
https://biz.leumi.co.il/portal/site/Business/home_03/currency_rates/12283/
the table is embedded from the static page:
https://www.bankleumi.co.il/vgnprod/ltrade_new_shaar_muskamim_multilang_vgn_HE.html

Looks like the business data is identical to the private data.
"""
import pandas as pd

from xil._headers import UA_HEADER

_LEUMI_URL = "\
https://www.bankleumi.co.il/vgnprod/currency/ajax/new_shaar_muskamim_data.json"


s = pd.read_json(_LEUMI_URL, typ="series", storage_options=UA_HEADER)
# pylint: disable-next=no-member
date = s.yatzigDate  # Hour in `s.topHeaderText`
df = pd.DataFrame.from_records(s.data)

print(date, df, sep="\n")
