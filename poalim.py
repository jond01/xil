from datetime import datetime
from zoneinfo import ZoneInfo

import pandas as pd

IL_TZ = ZoneInfo("Israel")
_POALIM_GET_URL = "https://www.bankhapoalim.co.il/he/coin-rates"
_DATE_QUERY = "?date="
_POALIM_QUERY = _POALIM_GET_URL + _DATE_QUERY
_DATE_FORMAT = "%Y-%m-%d"  # YYYY-MM-DD


def _get_url(t: datetime) -> str:
    return _POALIM_QUERY + t.strftime(_DATE_FORMAT)


def get_df(t: datetime | None = None) -> pd.DataFrame:
    if t is None:
        # TODO: on Sunday and Saturday there are no exchange rates, choose the last
        #  active day. To check the day use t.weekday() and compare to:
        #  import calendar, calendar.SATURDAY or calendar.SUNDAY
        t = datetime.now(IL_TZ)

    return pd.read_json(_get_url(t))


if __name__ == "__main__":
    df = get_df(datetime(2022, 10, 25))
    print(df)
    print(df.iloc[0])
