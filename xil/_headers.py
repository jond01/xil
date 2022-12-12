"""
Shared functionalities for retrieving URLs' data when headers are needed
"""
import http.client
import urllib.request

USER_AGENT = "\
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/107.0.0.0 Safari/537.36"

UA_HEADER = {"User-Agent": USER_AGENT}


def get_url_response(
    url: str, default_headers: bool = True
) -> http.client.HTTPResponse:
    """
    Return the response from a URL with custom headers
    """
    if default_headers:
        headers = UA_HEADER
    else:
        headers = {}
    request = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(request)  # type: ignore[no-any-return]
