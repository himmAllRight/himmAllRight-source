import requests

def test_index(base='http://192.168.1.5:1313'):
    """Checks that the home page is available"""
    response = requests.get(base)
    assert response.status_code == 200


def test_about_me(base='http://192.168.1.5:1313', path='/pages/about/'):
    """Checks that the about me page is available"""
    response = requests.get(base + path)
    assert response.status_code == 200


def test_homelab(base='http://192.168.1.5:1313', path='/pages/homelab/'):
    """Checks that the homelab page is available"""
    response = requests.get(base + path)
    assert response.status_code == 200
