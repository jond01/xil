"""
Union bank ("Igud") foreign exchange data:
https://www.unionbank.co.il/Igud/שוק-ההון-ומטח/מטבע-חוץ/שערי-מטח

Pending Deprecation Note:
Union bank is being merged into Mizrahi-Tefahot bank these days - this module is
expected to be deprecated in the foreseeable future.
"""
import pandas as pd

from xil._currencies import optional_currency_from_heb_name
from xil._headers import UA_HEADER, get_url_response

_UNION_URL = "\
http://www.unionbank.co.il/Igud/%D7%A9%D7%95%D7%A7-%D7%94%D7%94%D7%95%D7%9F-%D7%95%D7%9E%D7%98%D7%97/%D7%9E%D7%98%D7%91%D7%A2-%D7%97%D7%95%D7%A5/%D7%A9%D7%A2%D7%A8%D7%99-%D7%9E%D7%98%D7%97"
_HEADER = [0, 1]

# The "rbzid" cookie (https://www.reblaze.com/) is required for rendering the HTML on
# Union bank website. Note that it must be updated to a valid value, as this cookie
# expires after a few days.
_UNION_RBZID_COOKIE = "\
XD5oSc9AOoHxYtF8x5nsKrrmZ9ahj6TlIb9sBbQsGjDU6i37/SKgK9TOw3/V5n/ImOLL/G8vjtq/6tgtIscGzCIedCS0siLy7PX7sYtI5S15eEy64oaBtznWHUHGeC1dJqHo4801y0/s/pgjLNcGuka7rLeiWXFIoNUkpHVOpyxQaI6ciQFcqJi5pFTx1mMDBWYerF4yc8bVqBJipSgvX8+pOSrAZrGo/pTac9H6l54FzSYEECrYvHdbDI/3ME1lHfFWj94olKb8SQSJhZzoGA="


def _get_union_cookie_header(rbzid: str | None = None) -> dict[str, str]:
    """Get Union bank cookie header - only the required rbzid cookie"""
    if rbzid is None:
        rbzid = _UNION_RBZID_COOKIE
    return {"Cookie": f"rbzid={rbzid}"}


def _get_union_headers(rbzid: str | None = None) -> dict[str, str]:
    """Get the required Union bank headers"""
    return UA_HEADER | _get_union_cookie_header(rbzid)


def get_union_df(url: str = _UNION_URL, rbzid: str | None = None) -> pd.DataFrame:
    """Get Union bank exchange rates"""
    # pylint: disable=redefined-outer-name

    with get_url_response(url, headers=_get_union_headers(rbzid)) as response:
        df = pd.read_html(response, header=_HEADER)[0]  # type: ignore[arg-type]

    df = df.drop(("Unnamed: 7_level_0", "מכירה"), axis=1)  # empty (NaNs) column

    idx0 = pd.MultiIndex.from_product(
        [["currency"], ["name", "official rate", "change"]]
    )
    idx1 = pd.MultiIndex.from_product([["cash", "transfer"], ["buy", "sell"]])
    idx2 = pd.MultiIndex.from_tuples((idx0[-1],))
    idx = idx0[:-1].append(idx1).append(idx2)  # pylint: disable=no-member
    df.columns = idx
    df = df[idx0.append(idx1)]

    name_idx = ("currency", "name")
    amount_idx = ("currency", "amount")
    code_idx = ("currency", "code")

    df[[amount_idx, name_idx]] = df[name_idx].str.split("  ", expand=True)
    df[amount_idx] = df[amount_idx].str.lstrip("*")
    df[code_idx] = df[name_idx].apply(optional_currency_from_heb_name)
    # Drop rows with unknown currencies. The next line is correct type-wise, wrong stubs
    df = df.loc[df[code_idx].notna(), :]  # type: ignore[index]
    df = df.drop(labels=name_idx, axis=1)
    df = df.set_index(code_idx)
    df = df.reindex(columns=["currency", "cash", "transfer"], level=0)
    return df


if __name__ == "__main__":
    df = get_union_df()
    print(df)
