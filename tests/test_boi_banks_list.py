"""
Test the known list of banks against the Bank of Israel (BOI) online list
"""

import ssl
import urllib.request

import pandas as pd
import pytest

BOI_XML_URL = "\
https://www.boi.org.il/en/BankingSupervision/BanksAndBranchLocations/Lists/BoiBankBranchesDocs/banking_corporations_en.xml"

KNOWN_BANKS_SET = {
    "Bank Hapoalim B.M",
    "Bank Leumi Le-Israel B.M",
    "Bank Massad Ltd",
    "Bank Yahav  for Government Employees Ltd",
    "Bank of Jerusalem Ltd",
    "Israel Discount Bank Ltd",
    "Mercantile Discount Bank ltd",
    "Mizrahi Tefahot Bank Ltd",
    "One Zero Digital Bank LTD",
    "The First International Bank of Israel Ltd",
    "Union Bank of Israel Ltd",
}


@pytest.fixture(name="boi_banks_set")
def fixture_boi_banks_set() -> set[str]:
    """Get the set on Israeli banks from BOI online XML"""
    ctx = ssl.create_default_context()
    ctx.set_ciphers("DEFAULT")
    with urllib.request.urlopen(BOI_XML_URL, context=ctx) as response:
        df = pd.read_xml(response)
    return set(df[df["Category"] == "COMMERCIAL BANKS"]["Name"])


def test_boi_banks(boi_banks_set: set[str]) -> None:
    """Test the online set vs. the hard-coded one"""
    assert (
        boi_banks_set == KNOWN_BANKS_SET
    ), "Mismatch between the updated banks list data from BOI and the saved data"
