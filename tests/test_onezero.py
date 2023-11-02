# pylint: disable=missing-module-docstring, missing-function-docstring
import pandas as pd
import pytest

from xil._currencies import CurrencyCode
from xil.onezero import get_onezero_df


@pytest.fixture(name="df")
def df_fixture() -> pd.DataFrame:
    return get_onezero_df()


@pytest.mark.live
def test_df(df: pd.DataFrame) -> None:
    assert (
        df.index == [CurrencyCode.EUR, CurrencyCode.USD]
    ).all(), "The currencies are not as expected"
    assert (
        df[("transfer", "buy")] < df[("currency", "official rate")]
    ).all(), "The buy rate is not lower than the official rate"
    assert (
        df[("currency", "official rate")] < df[("transfer", "sell")]
    ).all(), "The sell rate is not higher than the official rate"
