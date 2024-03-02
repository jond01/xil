# pylint: disable=missing-module-docstring, missing-function-docstring
import pandas as pd
import pytest

from xil._currencies import CurrencyCode
from xil.discount import get_discount_df


@pytest.fixture(name="df")
def df_fixture() -> pd.DataFrame:
    return get_discount_df()


@pytest.fixture(name="currencies")
def currencies_fixture() -> set[str]:
    return {
        CurrencyCode.EUR.value,
        CurrencyCode.ETB.value,
        CurrencyCode.LKR.value,
        CurrencyCode.NGN.value,
        CurrencyCode.KRW.value,
        CurrencyCode.BGN.value,
        CurrencyCode.AUD.value,
        CurrencyCode.CHF.value,
        CurrencyCode.CNY.value,
        CurrencyCode.GBP.value,
        CurrencyCode.MXN.value,
        CurrencyCode.EGP.value,
        CurrencyCode.SAR.value,
        CurrencyCode.HUF.value,
        CurrencyCode.CAD.value,
        CurrencyCode.HKD.value,
        CurrencyCode.INR.value,
        CurrencyCode.PEN.value,
        CurrencyCode.USD.value,
        CurrencyCode.XPD.value,
        CurrencyCode.IDR.value,
        CurrencyCode.RUB.value,
        CurrencyCode.TRY.value,
        CurrencyCode.XPT.value,
        CurrencyCode.SEK.value,
        CurrencyCode.TWD.value,
        CurrencyCode.HRK.value,
        CurrencyCode.NOK.value,
        CurrencyCode.SAL.value,
        CurrencyCode.THB.value,
        CurrencyCode.SGD.value,
        CurrencyCode.CZK.value,
        CurrencyCode.PHP.value,
        CurrencyCode.NZD.value,
        CurrencyCode.XAU.value,
        CurrencyCode.LBP.value,
        CurrencyCode.PLN.value,
        CurrencyCode.XAG.value,
        CurrencyCode.BRL.value,
        CurrencyCode.CLP.value,
        CurrencyCode.JPY.value,
        CurrencyCode.ZAR.value,
        CurrencyCode.ARS.value,
        CurrencyCode.DKK.value,
        CurrencyCode.JOD.value,
        CurrencyCode.RON.value,
    }


@pytest.mark.live
def test_df(df: pd.DataFrame, currencies: set[str]) -> None:
    assert set(df.index) == currencies
    for method in ("cash", "transfer"):
        assert (df[(method, "sell")] >= df[(method, "buy")]).all()
