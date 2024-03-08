# pylint: disable=missing-module-docstring, missing-function-docstring, redefined-outer-name
import calendar
from datetime import date

import pandas as pd
import pytest

from xil._currencies import CurrencyCode
from xil.poalim import _get_url, get_df


def _is_weekend(t: date) -> bool:
    """Return True if the day is Saturday or Sunday, otherwise False"""
    return t.weekday() in (calendar.SATURDAY, calendar.SUNDAY)


@pytest.mark.parametrize(
    ("t", "expected_url"),
    [
        (
            date(2345, 10, 30),
            "https://www.bankhapoalim.co.il/he/coin-rates?date=2345-10-30",
        ),
        (
            date(2020, 4, 8),
            "https://www.bankhapoalim.co.il/he/coin-rates?date=2020-04-08",
        ),
    ],
)
def test_get_url(t: date, expected_url: str) -> None:
    assert _get_url(t) == expected_url


@pytest.mark.live
@pytest.mark.parametrize(
    "t",
    [
        pytest.param(date(2024, 2, 3), id="Saturday 2023-02-03"),
        pytest.param(date(2024, 2, 4), id="Sunday 2023-02-04"),
    ],
)
def test_weekend_emptiness(t: date) -> None:
    """Weekend in this context is Saturday and Sunday"""
    assert _is_weekend(t)
    assert get_df(t).empty, "The df is nonempty"


@pytest.fixture()
def df() -> pd.DataFrame:
    return get_df()


@pytest.fixture()
def multi_date_df() -> pd.DataFrame:
    return get_df(keep_last_date_only=False)


@pytest.fixture()
def expected_currencies() -> list[CurrencyCode]:
    return [
        CurrencyCode.USD,
        CurrencyCode.GBP,
        CurrencyCode.CHF,
        CurrencyCode.DKK,
        CurrencyCode.EUR,
        CurrencyCode.NOK,
        CurrencyCode.CAD,
        CurrencyCode.AUD,
        CurrencyCode.JPY,
        CurrencyCode.JOD,
        CurrencyCode.TRY,
    ]


@pytest.mark.live
def test_df(df: pd.DataFrame, expected_currencies: list[CurrencyCode]) -> None:
    assert (df.index == expected_currencies).all(), "The currencies are not as expected"
    assert (df[("transfer", "sell")] > df[("transfer", "buy")]).all()
    assert (df[("cash", "sell")] > df[("cash", "buy")]).all()
    assert (df[("cash", "sell")] > df[("transfer", "sell")]).all()
    assert (df[("transfer", "buy")] > df[("cash", "buy")]).all()


@pytest.mark.live
def test_multi_date_df(multi_date_df: pd.DataFrame) -> None:
    assert len(multi_date_df.date.unique()) > 1, "Multiple dates are expected"
