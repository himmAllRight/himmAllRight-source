+++
title  = "Creating Tests For This Website: Pages"
date   = "2020-02-23"
author = "Ryan Himmelwright"
image  = "img/posts/creating-website-tests-pages/pnc-arena.jpeg"
caption = "PNC Arena, Raleigh NC"
tags   = ["website", "hugo", "dev", "python", "testing"]
draft  = "False"
Comments = "True"
+++

As this website grows, there is an increasing amount of complexity. More posts,
more images, and more links. I've gotten better at breaking work up into
separate branches (instead of pushing everything straight to `master`), but
even that isn't enough to ensure everything works as expected when publishing
something new. Then, I thought of something obvious... I could setup some
simple testing... for my website.

<!--more-->

## What to Test

After editing a page or drafting a new post, I often wonder "how can I be
*sure* everything will still work when I publish this change"? I question if
every post file is *actually* being served as a web page. Or worse... I fear
that a post that isn't *ready* to be published might *accidentally* get pushed
with an unrelated website fix.

*(Yes, this is a completely unreasonable fear given that ALL of my
website source files, drafts included, are publicly hosted on Github.
Nonetheless, the fear exists)*

This will be a multi-post serries, so in this first one we will focus on:

- Configuring the test environment
- Building up the testing framework
- Writing some basic tests to ensure:
    - The pages I *want* to be served are
    - Pages and posts that are not ready, are *not* being served

As my website is currently compiled using [hugo](https://gohugo.io), the tests
will be centered around that framework. However, most of the information can be
applied to testing websites using other static website generators, are they are
all quite similar.


## Setting up the env

I will be using
[pytest](https://docs.pytest.org/en/latest/contents.html) for the testing
framework, and to make all the
python dependencies a bit easier to manage, I will also use
[pipenv](https://github.com/pypa/pipenv). Lastly, I usually work on a
[Fedora](https://getfedora.org) computer, VM, or at the very least in a Fedora
[podman](https://podman.io) container. So, some of my instructions use `dnf`,
but feel free to adjust to your package manager accordingly.

#### Install `pipenv`

First, lets install `pipenv`, which is easy enough in Fedora:

``` bash
sudo dnf install pipenv
```


#### Install needed packages inside `pipenv shell`

After installing, create a pipenv shell and enter it:

```bash
pipenv shell
```

Install `pytest` and `requests` in the pip environment:

```bash
pip install pytest requests
```


## Creating the Test Framework

With the environment setup, we can start building up the test framework. We
will start by defining come constants, then use those when building helper
functions. Lastly, we will use the helper functions to piece together the
`conftest.py` and `test_pages.py` files.


### Defining Constants

First, lets define some constants we can use throughout the test framework. In
the future, I might switch these to be set optionally with  CLI arguments, but
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

As you can see, in my `constants.py` file I have 4 variables defined:

- `BASE_URL`: this is the base url for the website when running `hugo serve`.
    For most, it will default to `http://localhost:1313`, but I have this as
    a constant because I usually run my `hugo serve` command with the `-b` to
    change it to an ip address so I can view it from other computers.
- `SITE_PAGES`: This is a list of paths that come *after* the baseurl for pages that
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

First, lets create `utils.py`. The helper functions will need to use
`listdir`, as well as the `path` function from the `os` module. They will also
need the regex functions. So, lets make those imports at the top of the file:

```python
from os import listdir, path
import re
```

#### get_file_names

Lets define a helper function named `get_file_names`:

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

When provided a file path (`src`), this function will return a list of all the
file names in the directory. Optionally, the `extension` parameter can be
supplied to only return files of that extension type (for exapmple, `md`). This
function will be used to grab the names of all the post source files.

... and that's all we need in `utils.py`... for now!

### Conftest

Now lets start digging into test-related stuff, by first creating a
`conftest.py` file. This file will mostly hold the fixtures we will use for the
tests. In our particular setup, they will gather lists of pages to run multiple
calls of each test against by using `@pytest.fixture(params)`.

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
`non_live_post_urls`. This pair creates a list of posts that have a markdown
file in the `/post/` directory, but are *not* listed in the `POST_NAMES`
constant (so in practice, not really to be published).

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

First, the `non_live_post_urls` helper function returns a list of non-listed
post files. That  list is then used in `non_live_post_url` as the
`pytest.fixture(params)` object, much like `SITE_PAGES` and `POST_NAMES` were
for the previous
fixtures.


### Finally... Some Tests!

Phew. Okay. With *all of that* defined... lets create the first test file. When
`pytest` runs, it will try to grab tests recursively from all the files down
the current directory, starting with `test`. This first set of tests will be
checking whether a web page is being served (or not), so lets name the file
`test_pages.py`. Again, start with the required imports. This time we only need
`pytest` and `requests`.

```python
import pytest
import requests
```

##### Testing Pages

The first test will check that each page defined in the `SITE_PAGES` constant
is being served. More specifically, we will use the `requests` module to ensure
not only that the page is served, but returns a [200
status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200). This
actually requires very little code to accomplish (Gotta love python) :
```python
def test_page_served(page_url):
    """Checks that the website pages are available"""
    response = requests.get(page_url)
    assert response.status_code == 200
```

We simply define a function, `test_page_served()`, and because it is in
`test_pages.py`, it will be assumed to be a test by `pytest`. We provide the
`page_url` fixture we previously defined in `conftest.py` as the only
parameter. This will call the `test_page_served` test for each url
in the list generated by `page_url`. Next, we use `requests.get()` to make a
page request. Lastly, we `assert` that the `status_code` from our response is
`200`. If it is, the test passes, if not, it fails.


##### Testing Posts

Next, lets test that all of the *posts* are being served. This test works
*exactly* the same as *test_page_served*, except we are using the `post_url`
fixture instead of `page_url` to supply the links to test:

```python
def test_post_served(post_url):
    """Checks that the desired posts are available"""
    response = requests.get(post_url)
    assert response.status_code == 200
```

*(While I could combine these cases into a single test function, I decided to
keep them separate for flexibility in the future)*

##### Lets Get Fancy: Testing Unapproved Posts Are *NOT* Served


For the last test, lets get a little bit more complicated and ensure that post files
*not* listed in the approved list are *not* being served. Well... it
turns out all the "fancy" code required for this test case already occured in
the `non_live_post_urls` helper function. The *test* function itself, is
essentially the same as what we've already encountered *except* that we are
now checking for a `404` return status instead of `200`:
```python
def test_non_defined_posts_not_served(non_live_post_url):
    """Checks that a non-defined post is NOT available"""
    response = requests.get(non_live_post_url)
    assert response.status_code == 404
```
That defines all of the tests for this first set! Don't let only having three
test functions fool you, they should generate over 70 test results when run!
(For my website, at the time of writing this post)

### Lets Run Some Tests!

Finally, we should be able to run the tests. To do so, first ensure that you
are in the pipenv by running `pipenv shell`, *or* you can run the tests from
outside the pipenv using `pipenv run COMMAND`. Next, call:

```shell
pytest -v .
```

The `-v` flag runs pytest in *'verbose'* mode, which I like to do as it shows
the results for each test run, rather than each *file*.

<center>
<video style="max-width:100%;" controls>
  <source src="../../img/posts/creating-website-tests-pages/passing-tests.mp4" type="video/mp4">
</video>
<div id="caption">Running the pages tests. All 72 passed.</div>
</center>

So it looks like all the tests are passing! To be sure, Lets do a quick check to
make sure they work as expected... I'll mark this post with `draft = "False"`,
but *not* add it to the approved lists, and the test for this page *should*
fail...

<center>
<a href="/img/posts/creating-website-tests-pages/failed-test.png">
<img alt="Checking a test fails when we want it to" src="/img/posts/creating-website-tests-pages/failed-test.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">Checking that a test fails when we want it to.</div>
</center>

Awesome, it failed! I guess all there is left to do is to finish up this post, so I
can add it to the approved posts lists and publish it! Stay tuned!
