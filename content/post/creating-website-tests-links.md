+++
title  = "Creating Tests For This Website: Links"
date   = "2020-03-15"
author = "Ryan Himmelwright"
image  = "img/posts/creating-website-tests-links/pnc-arena3.jpeg"
caption = "PNC Arena, Raleigh NC"
tags   = ["website", "hugo", "dev", "python", "testing"]
draft  = "True"
Comments = "True"
+++

In my previous two posts, I started a [test framework for my
website](/post/creating-website-tests-pages/), and [automated it using
Jenkins](/post/creating-website-tests-ci/). But we can do better. One of the
most annoying things when maintaining (or even reading) something on the
internet, is broken links. While we cannot control the availablity of content
outside our website, we *can* choose to remove links if they are broken. So, in
this post, we will setup tests that will ensure that links in our posts are
working. Well, at least the
[markdown](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf) ones.

<!--more-->

## What to Test

For this test set, we will be scanning all of our post's markdown files, and
grabbing all of the markdown link defined in them. With then links known, we
will then proceed to make a request to each one to check its availablity. If we
can connect, the test passes. If not (we get a 404 or something), it fails.


## Adding to the Test Framework


### Utility Functions

Before we are able to write the test function, we first need to expand out
utility functions. These will allow us to get the post's file paths, grab their
content, and extract all the markdown links from that content.

#### get_file_paths

First, lets define a new helper function, `get_file_paths`:

```python
def get_file_paths(src, extension=None):
    """Collects the paths of all files of a directory"""
    file_list = []
    root_path = path.expanduser(src)
    for file in listdir(root_path):
        # If extension provided, check file has that extension
        if extension:
            if file.endswith(extension):
                file_list.append(path.join(root_path, file))
        # Otherwise, add everything
        else:
            file_list.append(path.join(root_path, file))
    return file_list
```

When provided a file path (`src`), this function will return a list of all the
file paths in that directoy. Optionally, the `extension` parameter can be
supplied to only return files of that extension type (in our case, `md`). This
will be used to grab the paths of all of the website post source files.


#### get_file_content

Now lets define `get_file_content`. This function will take the file lists
generated from `get_file_paths`, grab the content from those files,
and return a dictionary of all the data.

```python
def get_file_content(file_list):
    """Grabs all the content from a list of file paths."""
    content_all_files = {}
    for file in file_list:
        f = open(file, "r")
        file_content = f.read()
        content_all_files[path.basename(file)] = file_content
    return content_all_files
```

The returned dictionary uses the filename as the key, and the content set to the
value. For example:

```python
{
  'post1.md': 'This is the text of post1.',
  'post2.md': "This is the text of post2. Basically the same ol' stuff."
}

```

#### get_md_links

Lastly, lets define `get_md_links`. This function takes the content dictionary
returned by `get_file_content`, and uses some [regular
expression](https://en.wikipedia.org/wiki/Regular_expression) magic to match
the markdown links:

```python
def get_md_links(content_dict, regex="\[.*?\]\((.*?)\)"):
    """Parses the dictionary of content strings, and pulls out the url of any links."""
    p = re.compile(regex)
    all_links = []
    for file in content_dict:
        content = content_dict[file].replace("\n", "")
        match_iter = p.finditer(content)
        for match in match_iter:
            # Regex can't properly match urls with parens in them, so skip.
            if "(" not in match.group(1):
                all_links.append(match.group(1))
    return all_links
```

First, the function compiles the regular expression defined by the `regex`
parameter. Next, it loops through all the data in the content dictionary, and
strips the newline characters, and then grabs all the regex matches.

Unfortunately, our regex expression can't properly match markdown formated urls
with parenthesis in them, so we have to check if each match has a `(` in it. If
it does, the url is thrown away because we cannot be sure we matched the full
`url`. If there are no parenthesis, the url as added to our saved list. After
parsing all the values of the content dictionary, a list of the matched urls is
returned.

### Adding to conftest.py

With our new utility functions defined, we can add a new fixture (and it's
helper function), to the `conftest.py` file.

```python
def post_md_links():
    """Returns the md_link object of the md links in all the posts."""
    all_post_files = get_file_paths(POST_DIR)
    all_post_contents = get_file_content(all_post_files)
    all_post_md_links = get_md_links(all_post_contents)
    # Return de-dup list
    return list(set(all_post_md_links))
```returns

```python
@pytest.fixture(params=post_md_links())
def post_md_link(request):
    """Returns the md_link object for a md link found in a post."""
    return request.param
```


### Writing the markdown link test

```python
def test_md_links(post_md_link):
    """Checks that the markdown links are not broken."""
    if post_md_link.startswith("http") or post_md_link.startswith("https"):
        url = post_md_link
    else:
        url = BASE_URL + post_md_link.lower()
    response = requests.get(url)
    assert response.status_code != 404, f"The link {post_md_link} is not found."
    assert response.status_code != 403, f"The link {post_md_link} is forbidden."
```


#### (Optional) Marking test with @flaky

```python
from flaky import flaky


@flaky
def test_md_links(post_md_link):
```

## Limitations

- Cannot match urls with parens

## Conclusion
