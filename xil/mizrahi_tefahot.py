"""
Mizrahi-Tefahot Bank scraper foreign exchange rates data:
https://www.mizrahi-tefahot.co.il/brokerage/foreignexchange/
Exchange calculator:
https://www.mizrahi-tefahot.co.il/brokerage/currancyexchange/
"""
import pandas as pd

from xil._currencies import currency_from_heb_name

_MIZRAHI_TEFAHOT_URL = "https://www.mizrahi-tefahot.co.il/brokerage/foreignexchange/"
_IDX0 = pd.MultiIndex.from_product([["currency"], ["name", "amount", "official rate"]])
_IDX1 = pd.MultiIndex.from_product([["cash", "transfer"], ["buy", "sell"]])
_MIZRAHI_TEFAHOT_IDX = _IDX0.append(_IDX1)


def get_mizrahi_teafhot_df(url: str = _MIZRAHI_TEFAHOT_URL) -> pd.DataFrame:
    """Get Mizrahi Tefahot Bank exchange rates"""
    df = pd.read_html(url, header=0)[0]
    df.columns = _MIZRAHI_TEFAHOT_IDX
    df[("currency", "code")] = df[("currency", "name")].apply(currency_from_heb_name)
    df = df.drop(labels=("currency", "name"), axis=1)
    df = df.set_index(("currency", "code"))
    return df


if __name__ == "__main__":
    print(get_mizrahi_teafhot_df())
