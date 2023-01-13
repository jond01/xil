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
from typing import Callable

import pandas as pd

from xil._currencies import currency_from_heb_name
from xil._headers import UA_HEADER

_LEUMI_URL = "\
https://www.bankleumi.co.il/vgnprod/currency/ajax/new_shaar_muskamim_data.json"
_IDX0 = pd.MultiIndex.from_product(
    [["currency"], ["name", "official rate", "change (%)"]]
)
_IDX1 = pd.MultiIndex.from_product([["transfer", "cash"], ["buy", "sell"]])
_IDX = _IDX0.append(_IDX1)


def get_leumi_df(url: str = _LEUMI_URL) -> pd.DataFrame:
    """Get Leumi Bank exchange rates"""
    series = pd.read_json(url, typ="series", storage_options=UA_HEADER)
    # date = s.yatzigDate  # Hour in `s.topHeaderText`
    # pylint: disable-next=redefined-outer-name
    df = pd.json_normalize(series.data)
    df = df[
        [
            "currencyName",
            "yatzig",
            "percent",
            "hamchaot.knia",
            "hamchaot.mechira",
            "mezuman.knia",
            "mezuman.mechira",
        ]
    ]
    df.columns = _IDX
    df = df.loc[df[("currency", "name")] != "סל המטבעות", :]
    # fix " in "דולר ארה&quot;ב" (defined on a separate line with a type hint for mypy)
    name_norm: Callable[[str], str] = lambda x: x.replace("&quot;", '"')
    df[("currency", "code")] = (
        df[("currency", "name")]
        .apply(lambda x: x.strip("100 "))  # remove "100" from "100 ין יפני"
        .apply(name_norm)
        .apply(currency_from_heb_name)
    )
    df = df.set_index(("currency", "code"))
    df = df.drop(labels=("currency", "name"), axis=1)
    return df


if __name__ == "__main__":
    df = get_leumi_df()
    print(df)
