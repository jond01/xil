"""
Utilities for currency conversion and standardization.
"""
import sys
from enum import Enum

if sys.version_info >= (3, 11):
    from enum import StrEnum  # pragma: no cover
else:

    class StrEnum(str, Enum):
        """String enum"""


class CurrencyCode(StrEnum):
    """3 letter currency codes of relevant currencies (ISO 4217)"""

    ILS = "ILS"  # Israeli New Shekel
    USD = "USD"  # US Dollar
    GBP = "GBP"  # British Pound
    JPY = "JPY"  # Japanese Yen
    EUR = "EUR"  # Euro
    AUD = "AUD"  # Australian Dollar
    CAD = "CAD"  # Canadian Dollar
    DKK = "DKK"  # Danish Krone
    NOK = "NOK"  # Norwegian Krone
    ZAR = "ZAR"  # South African Rand
    SEK = "SEK"  # Swedish Krona
    CHF = "CHF"  # Swiss Franc
    HKD = "HKD"  # Hong Kong Dollar
    SGD = "SGD"  # Singapore Dollar
    NZD = "NZD"  # New Zealand Dollar
    TRY = "TRY"  # Turkish Lira
    JOD = "JOD"  # Jordanian Dinar
    AED = "AED"  # UAE Dirham
    EGP = "EGP"  # Egyptian Pound


_HEB_CURRENCY_NAME_TO_CODE: dict[str, CurrencyCode] = {
    "שקל חדש": CurrencyCode.ILS,
    'דולר ארה"ב': CurrencyCode.USD,
    "לירה שטרלינג": CurrencyCode.GBP,
    'ליש"ט': CurrencyCode.GBP,
    'ליש"ט בריטי': CurrencyCode.GBP,
    "יין יפני": CurrencyCode.JPY,
    "ין יפני": CurrencyCode.JPY,
    "אירו": CurrencyCode.EUR,
    "דולר אוסטרלי": CurrencyCode.AUD,
    "דולר קנדי": CurrencyCode.CAD,
    "כתרים דניים": CurrencyCode.DKK,
    "כתר דני": CurrencyCode.DKK,
    "כתר נורבגי": CurrencyCode.NOK,
    "כתר נורווגי": CurrencyCode.NOK,
    'רנד דרא"פ': CurrencyCode.ZAR,
    'ראנד דרא"פ': CurrencyCode.ZAR,
    "רנד דרום אפריקני": CurrencyCode.ZAR,
    "רנד ד. אפריקני": CurrencyCode.ZAR,
    "ראנד דרום אפריקה": CurrencyCode.ZAR,
    "כתר שוודי": CurrencyCode.SEK,
    "כתר שבדי": CurrencyCode.SEK,
    "פרנק שוויצרי": CurrencyCode.CHF,
    "פרנק שויצרי": CurrencyCode.CHF,
    "דולר הונג קונג": CurrencyCode.HKD,
    "דולר סינגפור": CurrencyCode.SGD,
    "דולר סינגפורי": CurrencyCode.SGD,
    "דולר ניו זילנד": CurrencyCode.NZD,
    "דולר ניוזלנדי": CurrencyCode.NZD,
    "דולר ניו זילנדי": CurrencyCode.NZD,
    "דולר ניוזילנד": CurrencyCode.NZD,
    "לירה טורקית": CurrencyCode.TRY,
    "לירה טורקית חדשה": CurrencyCode.TRY,
    "דינר ירדני": CurrencyCode.JOD,
    "דירהם אמירתי": CurrencyCode.AED,
    "לירה מצרית": CurrencyCode.EGP,
}


class CurrencyNotSupportedError(ValueError):
    """Raised when a currency is not supported"""


def currency_code_from_heb_name(heb_currency_name: str) -> CurrencyCode:
    """Converts a Hebrew currency name to a currency code"""
    try:
        return _HEB_CURRENCY_NAME_TO_CODE[heb_currency_name]
    except KeyError as exc:
        raise CurrencyNotSupportedError(
            f"Unknown currency name: '{heb_currency_name}'"
        ) from exc


def currency_from_heb_name(heb_currency_name: str) -> str:
    """Converts a Hebrew currency name to a currency string"""
    # noinspection PyTypeChecker
    return currency_code_from_heb_name(heb_currency_name).value


def optional_currency_from_heb_name(heb_currency_name: str) -> str | None:
    """
    Converts a Hebrew currency name to a currency string or None if not supported.
    Prefer using this function over `currency_from_heb_name` when the currency is
    not guaranteed to be supported.
    """
    try:
        # noinspection PyTypeChecker
        return currency_code_from_heb_name(heb_currency_name).value
    except CurrencyNotSupportedError:
        return None
