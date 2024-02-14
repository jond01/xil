# pylint: disable=missing-module-docstring, missing-function-docstring
from datetime import date
import calendar

import pytest

from xil.poalim import IL_TZ, _get_url


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

