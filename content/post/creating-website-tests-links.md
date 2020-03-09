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

In my previous two posts, I started a [test framework for my website](/post/creating-website-tests-pages/), and
[automated it using Jenkins](/post/creating-website-tests-ci/).

<!--more-->

## What to Test

## Adding to the Test Framework


### Adding Some More Helper Utility Functions

(I accidentally wrote these for the last post before realizing they weren't
needed for those tests)

#### get_file_paths

Now, lets define our first helper function, `get_file_paths`:

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
supplied to only return files of that extension type (for example, `md`). This
will be used to grab the paths of all of the website page/post source files.


#### get_file_content

Now lets define `get_file_content`. This function will take the file lists
generated from `get_file_paths`, grab the content from those files,
and return a directory of all the data.

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

The directory returned uses the filename as the key, and the content set to the
value. For example:

```python
{
  'post1.md': 'This is the text of post1.',
  'post2.md': "This is the text of post2. Basically the same ol' stuff."
}

```

#### get_md_links

Lastly, lets define `get_md_links`. This function take the content dictonary
that `get_file_content` returns, and uses some [regular
expression](https://en.wikipedia.org/wiki/Regular_expression) magic to match

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

### Adding to conftest.py


```python
def post_md_links():
    """Returns the md_link object of the md links in all the posts."""
    all_post_files = get_file_paths(POST_DIR)
    all_post_contents = get_file_content(all_post_files)
    all_post_md_links = get_md_links(all_post_contents)
    # Return de-dup list
    return list(set(all_post_md_links))
```

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

## Conclusion
