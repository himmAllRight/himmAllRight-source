+++
title  = "Creating Tests For This Website: Pages"
date   = "2020-02-21"
author = "Ryan Himmelwright"
image  = "img/posts/creating-website-tests-pages/pnc-arena.jpeg"
caption = "PNC Arena, Raleigh NC"
tags   = ["website", "hugo", "dev", "python", "testing"]
draft  = "True"
Comments = "True"
+++

As this website grows, there is an increasing amount of complexity. More posts,
more images, and more links. I've gotten better about breaking work up into
separate branches (instead of doing everything in `master`), but even that
isn't enough to ensure everything works as expected when generating this staic
website. Then the obvious hit me... I could write some simple testing... for my
website.

<!--more-->

## What to Test

After editing a page, or drafting a new post, I often wonder "how can I be
*sure* everything will still work when I publish this change"? I question if
every post file is *actually* being served as a web page. Or worse... I fear
that a post that isn't *ready* to be published might *accidentally* get pushed
with an unrelated website fix.

*(Yes, this is a completely unreasonable fear given that ALL of my
website source files, drafts included, are publicly hosted on Github.
Nonetheless, the fear exists)*

As this will likely be a multi-post serries, In this post, we are going to
focus on:

- Setting up the test environment
- Building the testing framework
- Writing some basic tests to ensure:
    - The pages I *want* to be served are
    - Pages and post that are not ready, are *not* being served

As my website is currently compiled using [hugo](https://gohugo.io), the tests
will be centered around that framework. However, most of the information can be
applied to testing websites using other static website generators, are they are
all quite similar.


## Setting up the env

For my test framework, I will be using
[pytest](https://docs.pytest.org/en/latest/contents.html). To make all the
python stuff a bit easier to manage, I will also be using
[pipenv](https://github.com/pypa/pipenv). Lastly, I usually work on a
[Fedora](https://getfedora.org) computer, VM, or at the very least in a Fedora
[podman](https://podman.io) container. So, some of my instructions use `dnf`,
but feel free to adjust to your package manager accordingly.

#### Install `pipenv`

``` bash
sudo dnf install pipenv
```


#### Install needed packages inside `pipenv shell`

Create a pipenv shell and enter it:

```bash
pipenv shell
```

Install pytest in the shell, and (maybe) `requests`:

```bash
pip install pytest requests
```


## Creating the Test Framework

With the environment setup, we can start building up the test framework. We
will start by defining come constants, then use those when building some helper
functions. Lastly, we will use those helper functions to piece together out
`conftest.py` and `test_pages.py` files.


### Defining Constants

First, lets define some constants we can use throughout our test framework. In
the future, I might switch these to be optionally set using  CLI arguments, but
for now... they're just static constant variables defined in a file.

So first, create a new file in the `tests` directory named `constants.py`. In
that file, lets dump our contants:

```python
BASE_URL = "http://localhost:1313"

SITE_PAGES = ["/", "/pages/about/", "/pages/homelab/"]

POST_DIR = "./content/post/"
POST_NAMES = [
    "25-days-of-c",
    ...
    <Removed middle of list because it's long>
    ...
    "ZFS-Backups-To-LUKS-External",
]
```

As you can see, in my `constants.py` file I have 4 constants defined:

- `BASE_URL`: this is the base url for the website when running `hugo serve`.
    For most, this will default to `http://localhost:1313`, but I have this as
    a constant because I usually run my `hugo serve` command with the `-b` to
    change it to an ip address so I can view it from other computers.
- `SITE_PAGES`: This is the paths that come *after* the baseurl for pages that
    we well be testing. For example, I want to make sure that my "about me"
    page is being served, which is at `baseurl/pages/about/`, so
    `/pages/about/` is one of the values in this constant.
- `POST_DIR`: This is the directory for where the post *files* are located.
- `POST_NAMES`: This is a list of the names of the post *files* (without the
    `.md`)

Add in your values for the variables, and remember to save the file.

### Writing Some Helper Utility Functions

With those constants defined, we should be ready to write some helper
functions. These are normal python functions that will be called from tests or
even test fixture functions.

First, lets create `utils.py`. The helper functions will need to use the
`listdir`, as well as the `path` functions from the `os` module, in addition to
the regex functions. So, lets make those imports at the top of the file:

```python
from os import listdir, path
import re
```

#### get_file_names

Next, lets define `get_file_names`, which is the same as `get_file_paths` but
returns just the file *name* rather than the full *path*.
```python
def get_file_names(src, extension=None):
    """Collects the names of all files of a directory"""
    file_list = []
    root_path = path.expanduser(src)
    for file in listdir(root_path):
        # If extension provided, check file has that extension
        if extension:
            if file.endswith(extension):
                file_list.append(file)
        # Otherwise, add everything
        else:
            file_list.append(file)
    return file_list
```

(In fact, the two functions are *so similar*, I'll probably combine the
functionality into one... for now, please just deal with the redundancy)

... and that's all we need in `utils.py`... for now!

### Conftest

Now lets start digging into test-related stuff, by first creating a
`conftest.py` file. This file will mostly hold the fixtures we will use for our
tests. In our particular setup, they will gather lists of pages to run multiple
runs of each test against by using `@pytest.fixture(params)`.

But first, lets import a few things at the top of `conftest.py`:

```python
import pytest
from os import path

from constants import BASE_URL, SITE_PAGES, POST_DIR, POST_NAMES
from utils import get_file_names
```

The imports include the `os.path()` function, some of the constants we
defined, and the `get_file_names()` helper function. Oh, And of course
`pytest` ;) .


#### page_url

```python
@pytest.fixture(params=SITE_PAGES)
def page_url(request):
    """Returns the page urls for testing."""
    return BASE_URL + request.param
```

The first fixture, `page_url`, is very basic. It creates a list of all of the
website pages (not posts), by combining the `BASE_URL` with each of the values
defined in the `SITE_PAGES` constant. This list will later be used to
paramaterize a single test across all of the page links.



#### post_url


```python
@pytest.fixture(params=POST_NAMES)
def post_url(request):
    """Returns the post urls for testing."""
    return BASE_URL + "/post/" + request.param.lower()
```

The next fixture, `post_url` is basically the same as `page_url`, except it
creates a list of all the *posts* using the `POST_NAMES` constant. Again, this
will be used to expand a single test into many, one for each post.

#### non_live_post_url

```python
@pytest.fixture(params=non_live_post_urls())
def non_live_post_url(request):
    """Returns the url of a non-defined post file"""
    return BASE_URL + "/post/" + request.param.lower()
```

Lastly, we have `non_live_post_url` with its accompanying helper function,
`non_live_post_urls`. This pair creates a list of posts that we have a markdown
file for in the `/post/` directory, but are *not* listed in the `POST_NAMES`
constant (so theoretically, not really to be published).

```python
def non_live_post_urls():
    """Returns the urls of md files that should not be live."""
    all_post_md_names = list(
        map(lambda name: name.lower().split(".md")[0], get_file_names(POST_DIR))
    )
    live_post_names = list(map(lambda name: name.lower(), POST_NAMES))
    non_live_post_names = set(all_post_md_names).difference(set(live_post_names))
    return list(non_live_post_names)
```

First, `non_live_post_urls` the list of non-listed post files. That returned
list is then used in `non_live_post_url` as the `pytest.fixture(params)`
object, much like `SITE_PAGES` and `POST_NAMES` were for the previous
fixtures.


### Finally... Some Tests!

Phew. Okay. With *all of that* defined... lets create the first test file. When
`pytest` runs, it will try to grab tests from all the files recursively down
the current directory starting with `test`. This first set of tests will be
testing whether a web page is being served (or not), so lets name the files
`test_pages.py`. Again, start with the required imports. This time we only need
`pytest` and `requests`.

```python
import pytest
import requests
```

##### Testing Pages

The first test will check that each page defined in the `SITE_PAGES` constant
is being served. More specifically, we will use the `requests` module to ensure
that not only is the page being served, but returns a [200
status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200). As far
as the code goes, there is not much to it:

```python
def test_page_served(page_url):
    """Checks that the website pages are available"""
    response = requests.get(page_url)
    assert response.status_code == 200
```

We simply define a function, `test_page_served()`, and because it is in
`test_pages.py`, it will be assumed to be a test by `pytest`. We provide the
`page_url` fixture we previously defined in `conftest.py` as the only
parameter. This will call the `test_page_served` test once, for each url
in the list generated by `page_url`. Next, we use `requests.get()` to make a
page request. Lastly, we `assert` that the `status_code` from our response is
`200`. If it is, the test passes, if not, it fails.


##### Testing Posts

Next, lets test that all of the *posts* are being served. This test work
*exactly* the same as *test_page_served*, except we are using the `post_url`
fixture instead of `page_url` to supply the links to test:

```python
def test_post_served(post_url):
    """Checks that the desired posts are available"""
    response = requests.get(post_url)
    assert response.status_code == 200
```

*(While I could combine these cases into a single test function, I decided to
keep them separate in case I wanted to add to a particular test case, but not
the other)*

##### Lets Get Fancy: Testing Unapproved Posts Are *NOT* Served


For the last test, get a little bit more complicated and test that post files
that are *not* listed in the approved list are *not* being served. Well... it
turns out all the "fancy" code required for this test case already occured in
the `non_live_post_urls` helper function. The *test* function itself, is
essentially the same as what we've already encountered *except* that we are
checking for a `404` status instead of a `200`:
```python
def test_non_defined_posts_not_served(non_live_post_url):
    """Checks that a non-defined post is NOT available"""
    response = requests.get(non_live_post_url)
    assert response.status_code != 200
```
That defines all of the test for this first set! Don't let having three
functions fool you, they should generate over 80 test results when run!

### Lets Run Some Tests!

- Show how to run tests using `pipenv run` or from `pipenv shell`
- Run the tests, and show the output
- Maybe purposely show a failed test as an example


## Conclusion

- Wrap it up!
- Maybe hint at the next post in this serries

