import pytest

from os import path

from constants import BASE_URL, SITE_PAGES, POST_DIR, POST_NAMES

from utils import (
    get_file_content,
    get_md_links,
    get_file_names,
    get_file_paths,
)


@pytest.fixture(params=SITE_PAGES)
def page_url(request):
    """Returns the page urls for testing."""
    return BASE_URL + request.param


@pytest.fixture(params=POST_NAMES)
def post_url(request):
    """Returns the post urls for testing."""
    return BASE_URL + "/post/" + request.param.lower()


def non_live_post_urls():
    """Returns the urls of md files that should not be live."""
    all_post_md_names = list(
        map(lambda name: name.lower().split(".md")[0], get_file_names(POST_DIR))
    )
    live_post_names = list(map(lambda name: name.lower(), POST_NAMES))
    non_live_post_names = set(all_post_md_names).difference(set(live_post_names))
    return list(non_live_post_names)


@pytest.fixture(params=non_live_post_urls())
def non_live_post_url(request):
    """Returns the url of a non-defined post file"""
    return BASE_URL + "/post/" + request.param.lower()


def post_md_links():
    """Returns the md_link object of the md links in all the posts."""
    all_post_files = get_file_paths(POST_DIR)
    all_post_contents = get_file_content(all_post_files)
    return get_md_links(all_post_contents)


@pytest.fixture(params=post_md_links())
def post_md_link(request):
    """Returns the md_link object for a md link found in a post."""
    return request.param
