import pytest
import requests

from constants import BASE_URL
from flaky import flaky


@flaky
def test_md_links(post_md_link):
    """Checks that the markdown links are not broken."""
    if post_md_link.startswith("http") or post_md_link.startswith("https"):
        url = post_md_link
    else:
        url = BASE_URL + post_md_link.lower()
    response = requests.get(url)
    assert response.status_code != 404, f"The link {post_md_link} is not found."
    assert response.status_code != 403, f"The link {post_md_link} is forbidden."
