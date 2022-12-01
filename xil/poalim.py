"""
Scrape Bank Hapoalim exchange data publicly visible on
https://www.bankhapoalim.co.il/he/foreign-currency/exchange-rates
"""
# pylint: disable=invalid-name

from datetime import datetime
from zoneinfo import ZoneInfo

import pandas as pd

from xil._currencies import currency_from_heb_name

IL_TZ = ZoneInfo("Israel")
_POALIM_GET_URL = "https://www.bankhapoalim.co.il/he/coin-rates"
_DATE_QUERY = "?date="
_POALIM_QUERY = _POALIM_GET_URL + _DATE_QUERY
_DATE_FORMAT = "%Y-%m-%d"  # YYYY-MM-DD
# _IRRELEVANT_COLS = ["CHANGE", "DATE_CHALIFIN", "DT_VALID", "TAX_ORDER"]
_RELEVANT_COLS = [
    "NAME_HEB",
    "SHAAR_YATZIG",
    "AHUZ_SHINUI",
    "SHAAR_CHK_KNIA",
    "SHAAR_CHK_MECHIRA",
    "SHAAR_CASH_KNIA",
    "SHAAR_CASH_MECHIRA",
]
_IDX0 = pd.MultiIndex.from_product(
    [["currency"], ["name", "official rate", "change (%)"]]
)
_IDX1 = pd.MultiIndex.from_product([["transfer", "cash"], ["buy", "sell"]])
_IDX = _IDX0.append(_IDX1)


def _get_url(t: datetime) -> str:
    return _POALIM_QUERY + t.strftime(_DATE_FORMAT)


def get_df(t: datetime | None = None, filter_cols: bool = True) -> pd.DataFrame:
    """
    Get poalim exchange data from now or a specified date t as a pandas DataFrame.
    If filter_cols is true, only the relevant columns will be returned.
    """
    # pylint: disable=redefined-outer-name

    if t is None:
        # pylint: disable-next=fixme
        # TODO: on Sunday and Saturday there are no exchange rates, choose the last
        #  active day. To check the day use t.weekday() and compare to:
        #  import calendar, calendar.SATURDAY or calendar.SUNDAY
        t = datetime.now(IL_TZ)

    df = pd.read_json(_get_url(t))
    if not filter_cols:
        return df

    df = df[_RELEVANT_COLS]
    df.columns = _IDX
    df[("currency", "code")] = (
        df[("currency", "name")]
        .apply(lambda x: x.strip("100 "))  # remove "100" from "100 ין יפני"
        .apply(currency_from_heb_name)
    )
    df = df.set_index(("currency", "code"))
    df = df.drop(labels=("currency", "name"), axis=1)
    return df


if __name__ == "__main__":
    df = get_df(datetime(2022, 10, 25), filter_cols=True)
    with pd.option_context(
        "display.max_rows", None, "display.max_columns", None, "display.width", None
    ):
        print(df)
    print(df.iloc[0])
