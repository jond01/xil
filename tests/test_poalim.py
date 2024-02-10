# pylint: disable=missing-module-docstring, missing-function-docstring
from datetime import datetime

import pytest

from xil.poalim import IL_TZ, _get_url


@pytest.mark.parametrize(
    ("t", "expected_url"),
    [
        (
            datetime(2345, 10, 30, tzinfo=IL_TZ),
            "https://www.bankhapoalim.co.il/he/coin-rates?date=2345-10-30",
        ),
        (
            datetime(2020, 4, 8, 16, 0, 4, tzinfo=IL_TZ),
            "https://www.bankhapoalim.co.il/he/coin-rates?date=2020-04-08",
        ),
    ],
)
def test_get_url(t: datetime, expected_url: str) -> None:
    assert _get_url(t) == expected_url
