"""
Test the _df_normalizer module.
"""
# pylint: disable=missing-function-docstring
from contextlib import AbstractContextManager
from itertools import product
from unittest.mock import Mock, patch

import pandas as pd
import pytest

from xil._df_normalizer import (
    _CURRENCY_CODE_KEY,
    _CURRENCY_KEY,
    _CURRENCY_NAME_KEY,
    DataFrameNormalizer,
)


@pytest.fixture(name="currencies_df")
def fixture_currencies_df() -> pd.DataFrame:
    df = pd.DataFrame(
        [['דולר ארה"ב', 1, 3.41], ["ין יפני", 100, 2.65]],
        columns=[_CURRENCY_NAME_KEY, (_CURRENCY_KEY, "amount"), ("transfer", "sell")],
    )
    return df


@pytest.fixture(name="currencies_df_with_code")
def fixture_currencies_df_with_code(currencies_df: pd.DataFrame) -> pd.DataFrame:
    DataFrameNormalizer(currencies_df).add_code_from_name()
    return currencies_df


def _patch_normalizer_attr(attr: str) -> AbstractContextManager[Mock]:
    return patch.object(DataFrameNormalizer, attr, autospec=True)


def test_drop_name(currencies_df: pd.DataFrame) -> None:
    assert _CURRENCY_NAME_KEY in currencies_df.columns
    DataFrameNormalizer(currencies_df).drop_currency_name()
    assert _CURRENCY_NAME_KEY not in currencies_df.columns


def test_set_index(currencies_df_with_code: pd.DataFrame) -> None:
    DataFrameNormalizer(currencies_df_with_code).set_code_index()
    assert currencies_df_with_code.index.name == _CURRENCY_CODE_KEY


def test_add_code(currencies_df: pd.DataFrame) -> None:
    assert _CURRENCY_CODE_KEY not in currencies_df.columns
    DataFrameNormalizer(currencies_df).add_code_from_name()
    assert _CURRENCY_CODE_KEY in currencies_df.columns


def test_preprocess_names(currencies_df: pd.DataFrame) -> None:
    names = currencies_df[_CURRENCY_NAME_KEY]
    with patch.object(DataFrameNormalizer, "_preprocess_names", autospec=True) as mock:
        DataFrameNormalizer(currencies_df).add_code_from_name()
        mock.assert_called_once_with(names)


@pytest.mark.parametrize(
    ("add_code", "set_code", "drop_name"), product([True, False], repeat=3)
)
def test_norm(
    currencies_df: pd.DataFrame,
    add_code: bool,
    set_code: bool,
    drop_name: bool,
) -> None:
    df_normalizer = DataFrameNormalizer(currencies_df)
    with (
        _patch_normalizer_attr("add_code_from_name") as mock_add_code,
        _patch_normalizer_attr("set_code_index") as mock_set_index,
        _patch_normalizer_attr("drop_currency_name") as mock_drop_name,
    ):
        df_normalizer.norm(add_code=add_code, set_code=set_code, drop_name=drop_name)
        for (param, mock) in [
            (add_code, mock_add_code),
            (set_code, mock_set_index),
            (drop_name, mock_drop_name),
        ]:
            if param:
                mock.assert_called_once_with(df_normalizer)
            else:
                mock.assert_not_called()
