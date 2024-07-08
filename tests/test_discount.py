# pylint: disable=missing-module-docstring, missing-function-docstring
import pandas as pd
import pytest

from xil._currencies import CurrencyCode
from xil.discount import get_discount_df


@pytest.fixture(name="df")
def df_fixture() -> pd.DataFrame:
    return get_discount_df()


@pytest.fixture(name="currencies")
def currencies_fixture() -> set[CurrencyCode]:
    return {
        CurrencyCode.EUR,
        CurrencyCode.ETB,
        CurrencyCode.LKR,
        CurrencyCode.NGN,
        CurrencyCode.KRW,
        CurrencyCode.BGN,
        CurrencyCode.AUD,
        CurrencyCode.CHF,
        CurrencyCode.CNY,
        CurrencyCode.GBP,
        CurrencyCode.MXN,
        CurrencyCode.EGP,
        CurrencyCode.SAR,
        CurrencyCode.HUF,
        CurrencyCode.CAD,
        CurrencyCode.HKD,
        CurrencyCode.INR,
        CurrencyCode.PEN,
        CurrencyCode.USD,
        CurrencyCode.XPD,
        CurrencyCode.IDR,
        CurrencyCode.RUB,
        CurrencyCode.TRY,
        CurrencyCode.XPT,
        CurrencyCode.SEK,
        CurrencyCode.TWD,
        CurrencyCode.HRK,
        CurrencyCode.NOK,
        CurrencyCode.SAL,
        CurrencyCode.THB,
        CurrencyCode.SGD,
        CurrencyCode.CZK,
        CurrencyCode.PHP,
        CurrencyCode.NZD,
        CurrencyCode.XAU,
        CurrencyCode.PLN,
        CurrencyCode.XAG,
        CurrencyCode.BRL,
        CurrencyCode.CLP,
        CurrencyCode.JPY,
        CurrencyCode.ZAR,
        CurrencyCode.ARS,
        CurrencyCode.DKK,
        CurrencyCode.JOD,
        CurrencyCode.RON,
    }


@pytest.mark.live
def test_df(
    df: pd.DataFrame, currencies: set[CurrencyCode], drop_ngn: bool = True
) -> None:
    assert set(df.index) == currencies
    if drop_ngn:
        # There's an issue with Nigerian naira
        df = df.drop(index=CurrencyCode.NGN)
    for method in ("cash", "transfer"):
        assert (df[(method, "sell")] >= df[(method, "buy")]).all()
