"""
Utilities for currency conversion and standardization.
"""
from enum import Enum


class StrEnum(str, Enum):
    """String enum"""

    # This is built into Python 3.11


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


_HEB_CURRENCY_NAME_TO_CODE: dict[str, CurrencyCode] = {
    "שקל חדש": CurrencyCode.ILS,
    'דולר ארה"ב': CurrencyCode.USD,
    "לירה שטרלינג": CurrencyCode.GBP,
    'ליש"ט': CurrencyCode.GBP,
    "יין יפני": CurrencyCode.JPY,
    "ין יפני": CurrencyCode.JPY,
    "אירו": CurrencyCode.EUR,
    "דולר אוסטרלי": CurrencyCode.AUD,
    "דולר קנדי": CurrencyCode.CAD,
    "כתרים דניים": CurrencyCode.DKK,
    "כתר דני": CurrencyCode.DKK,
    "כתר נורבגי": CurrencyCode.NOK,
    'רנד דרא"פ': CurrencyCode.ZAR,
    'ראנד דרא"פ': CurrencyCode.ZAR,
    "כתר שוודי": CurrencyCode.SEK,
    "פרנק שוויצרי": CurrencyCode.CHF,
    "דולר הונג קונג": CurrencyCode.HKD,
    "דולר סינגפור": CurrencyCode.SGD,
    "דולר ניו זילנד": CurrencyCode.NZD,
    "דולר ניוזלנדי": CurrencyCode.NZD,
    "לירה טורקית": CurrencyCode.TRY,
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


if __name__ == "__main__":
    print(currency_code_from_heb_name("שקל חדש"))
