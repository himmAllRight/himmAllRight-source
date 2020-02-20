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

```python
@pytest.fixture(params=SITE_PAGES)
def page_url(request):
    """Returns the page urls for testing."""
    return BASE_URL + request.param
```

```python
@pytest.fixture(params=POST_NAMES)
def post_url(request):
    """Returns the post urls for testing."""
    return BASE_URL + "/post/" + request.param.lower()
```

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

```python
@pytest.fixture(params=non_live_post_urls())
def non_live_post_url(request):
    """Returns the url of a non-defined post file"""
    return BASE_URL + "/post/" + request.param.lower()
```

### Finally... Some Tests!

- Briefly explain how pytest test files work
- Create and define `test_pages.py`

##### Testing Pages

- Create and explain `test_page_served` test function

##### Testing Posts

- Create and explain `test_post_served` test function

##### Lets Get Fancy: Testing Unapproved Posts Are *NOT* Served

- Explain why I want a test like this
- Show how we can use those `util` functions from earlier to get what we want
- Create and explain how the `test_non_defined_posts_not_served` test function
    works


### Lets Run Some Tests!

- Show how to run tests using `pipenv run` or from `pipenv shell`
- Run the tests, and show the output
- Maybe purposely show a failed test as an example


## Conclusion

- Wrap it up!
- Maybe hint at the next post in this serries

