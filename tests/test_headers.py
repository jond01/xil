"""
Test the _headers module.
"""

from typing import Generator
from unittest.mock import Mock, patch
from urllib.request import Request

import pytest

from xil._headers import UA_HEADER, get_url_response


@pytest.fixture(name="url")
def fixture_url() -> str:
    """A tests URL that can be used (no actual call is made)"""
    return "http://httpbin.org/get"


@pytest.fixture(name="mock_urlopen")
def fixture_mock_urlopen() -> Generator[Mock, None, None]:
    """Mock the call to an external URL"""
    with patch("urllib.request.urlopen", autospec=True) as mock:
        yield mock


def _compare_requests(request1: Request, request2: Request) -> bool:
    """
    This is required since two Request objects with the same data are not equal.
    Compare here only the attributes of interest.
    """
    return (
        request1.full_url == request2.full_url and request1.headers == request2.headers
    )


@pytest.mark.parametrize(
    ("default_headers", "expected_headers"), [(False, {}), (True, UA_HEADER)]
)
def test_get_url_response(
    url: str,
    default_headers: bool,
    expected_headers: dict[str, str],
    mock_urlopen: Mock,
) -> None:
    """Test the get_url_response function"""
    get_url_response(url, default_headers)
    mock_urlopen.assert_called_once()
    actual_request = mock_urlopen.call_args.args[0]
    expected_request = Request(url=url, headers=expected_headers)
    assert _compare_requests(
        actual_request, expected_request
    ), "The actual request is different than expected"
