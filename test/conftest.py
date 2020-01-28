import pytest

BASE_URL = 'http://192.168.1.5:1313'
SITE_PAGES = [
    '/',
    '/pages/about/',
    '/pages/homelab/'
]

POST_NAMES = [
    '25-days-of-c',
    'Ansible-On-Pi-Cluster',
    'ato2019',
    'back-on-arch',
    'back-on-org-mode-for-work',
    'back-to-solus',
    'charmeleon-desktop-design',
]


@pytest.fixture(params=SITE_PAGES)
def page_url(request):
    """Returns the page urls for testing."""
    return BASE_URL + request.param


@pytest.fixture(params=POST_NAMES)
def post_url(request):
    """Returns the post urls for testing."""
    return BASE_URL + '/post/' + request.param.lower()
