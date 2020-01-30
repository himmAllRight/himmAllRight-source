import pytest
import requests

def test_page_served(page_url):
    """Checks that the website pages are available"""
    response = requests.get(page_url)
    assert response.status_code == 200

def test_post_served(post_url):
    """Checks that the desired posts are available"""
    response = requests.get(post_url)
    assert response.status_code == 200


def test_non_defined_posts_not_served(non_live_post_url):
    """Checks that a non-defined post is NOT available"""
    response = requests.get(non_live_post_url)
    assert response.status_code != 200
