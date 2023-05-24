"""
Test the _headers module.
"""

import ssl
from typing import Generator
from unittest.mock import Mock, patch
from urllib.request import Request

import pytest
from hypothesis import given, provisional, settings  # , HealthCheck, strategies

from xil._headers import _DEFAULT_CONTEXT, UA_HEADER, get_url_response

_url = settings(max_examples=1)(given(url=provisional.urls()))


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


# @given(url=provisional.urls())
# @settings(max_examples=1)#suppress_health_check=[HealthCheck.function_scoped_fixture])
@_url
@pytest.mark.parametrize(
    ("default_headers", "expected_headers"), [(False, {}), (True, UA_HEADER)]
)
def test_get_url_response_headers(
    url: str,
    default_headers: bool,
    expected_headers: dict[str, str],
    # mock_urlopen: Mock,
) -> None:
    """Test the get_url_response request headers"""
    print(url)
    with patch("urllib.request.urlopen", autospec=True) as mock_urlopen:
        get_url_response(url, default_headers)
    mock_urlopen.assert_called_once()
    actual_request = mock_urlopen.call_args.args[0]
    expected_request = Request(url=url, headers=expected_headers)
    assert _compare_requests(
        actual_request, expected_request
    ), "The actual request is different than expected"


@given(url=provisional.urls())
@pytest.mark.parametrize("default_headers", [False, True])
@pytest.mark.parametrize(
    ("set_context", "expected_context"), [(False, None), (True, _DEFAULT_CONTEXT)]
)
def test_get_url_response_context(
    url: str,
    default_headers: bool,
    set_context: bool,
    expected_context: ssl.SSLContext | None,
    mock_urlopen: Mock,
) -> None:
    """Test that get_url_response sets an SSL context when it is asked to"""
    get_url_response(url, default_headers=default_headers, set_context=set_context)
    mock_urlopen.assert_called_once()
    assert mock_urlopen.call_args.kwargs == {
        "context": expected_context,
    }, "The context passed to urlopen is different than expected"
