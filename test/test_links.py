import pytest
import requests

from constants import BASE_URL


@pytest.mark.skip
def test_md_links(post_md_link_pair):
    """Checks that the markdown links are not broken."""
    md_file = post_md_link_pair[0]
    if post_md_link[1].startswith("http") or post_md_link[1].startswith("https"):
        url = post_md_link_pair[1]
    else:
        url = BASE_URL + post_md_link_pair[1]

    response = requests.get(url)
    assert response.status_code == 200, f"The link {url} in {md_file} is broken."
