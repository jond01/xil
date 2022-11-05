"""
Scrape Bank Hapoalim exchange data publicly visible on
https://www.bankhapoalim.co.il/he/foreign-currency/exchange-rates
"""
from datetime import datetime
from zoneinfo import ZoneInfo

import pandas as pd

IL_TZ = ZoneInfo("Israel")
_POALIM_GET_URL = "https://www.bankhapoalim.co.il/he/coin-rates"
_DATE_QUERY = "?date="
_POALIM_QUERY = _POALIM_GET_URL + _DATE_QUERY
_DATE_FORMAT = "%Y-%m-%d"  # YYYY-MM-DD
# _IRRELEVANT_COLS = ["CHANGE", "DATE_CHALIFIN", "DT_VALID", "TAX_ORDER"]
_RELEVANT_COLS = [
    "KOD_MATBEA",
    "DT_ERECH",
    "SHAAR_YATZIG",
    "SHAAR_CHK_KNIA",
    "SHAAR_CHK_MECHIRA",
    "SHAAR_CASH_KNIA",
    "SHAAR_CASH_MECHIRA",
    "AHUZ_SHINUI",
    "NAME_HEB",
]


def _get_url(t: datetime) -> str:
    return _POALIM_QUERY + t.strftime(_DATE_FORMAT)


def get_df(t: datetime | None = None, filter_cols: bool = True) -> pd.DataFrame:
    """
    Get poalim exchange data from now or a specified date t as a pandas DataFrame.
    If filter_cols is true, only the relevant columns will be returned.
    """
    if t is None:
        # TODO: on Sunday and Saturday there are no exchange rates, choose the last
        #  active day. To check the day use t.weekday() and compare to:
        #  import calendar, calendar.SATURDAY or calendar.SUNDAY
        t = datetime.now(IL_TZ)

    df = pd.read_json(_get_url(t))
    if filter_cols:
        df = df[_RELEVANT_COLS]
    return df


if __name__ == "__main__":
    df = get_df(datetime(2022, 10, 25))
    with pd.option_context(
        'display.max_rows', None, 'display.max_columns', None, 'display.width', None
    ):
        print(df)
    print(df.iloc[0])