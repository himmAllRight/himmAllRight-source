+++
title  = "Creating Tests For This Website: Links"
date   = "2020-03-29"
author = "Ryan Himmelwright"
image  = "img/posts/creating-website-tests-links/pnc-arena3.jpeg"
caption = "PNC Arena, Raleigh NC"
tags   = ["website", "hugo", "dev", "python", "testing"]
draft  = "True"
Comments = "True"
+++

In my previous two posts, I created a [test framework for my
website](/post/creating-website-tests-pages/), and [automated it using
Jenkins](/post/creating-website-tests-ci/). But we can do better. One of the
most annoying things when maintaining (or even reading) something on the
internet, are broken links. While I cannot control the *availability* of
content outside the website, I *can* choose to remove links if they are
broken. So, in this post, we will add tests to ensure that links in our posts
are working. Well, at least the
[markdown](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf) ones.

<!--more-->

## What to Test

<center>
<a href="/img/posts/creating-website-tests-links/google-404-error.png">
<img alt="Google 404 Error Page" src="/img/posts/creating-website-tests-links/google-404-error.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">Google 404 Error Page</div>
</center>

For this test set, we will be scanning the content files of all of the posts, and
grabbing every markdown link defined in them. With the links known, we
will then make a request to each one to check the its availability. If we
can connect, the test passes. If not (ex: we get a 404 or something), it fails.


### Adding Utility Functions

Before we are able to write the test function, we first need to add to the
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
parameter. Next, it loops through all the data in the content dictionary,
strips the newline characters, and then grabs all the regex matches.

Unfortunately, the regex expression can't properly match markdown formated urls
with parenthesis in them, so we have to check if each match has a `(` in it. If
it does, the url is thrown away because we cannot be sure we matched the full
`url`. If there are no parenthesis, the url as added to our saved list. After
parsing all the values of the content dictionary, a list of the matched urls is
returned.

### Adding to conftest.py

With our new utility functions defined, we can add a new fixture (and it's
helper function), to the `conftest.py` file. Lets start with the fixture's
helper function, `post_md_link()`:

```python
def post_md_links():
    """Returns the md_link object of the md links in all the posts."""
    all_post_files = get_file_paths(POST_DIR)
    all_post_contents = get_file_content(all_post_files)
    all_post_md_links = get_md_links(all_post_contents)
    # Return de-dup list
    return list(set(all_post_md_links))
```

This function uses all the utility functions we just wrote above, to extract
all of the markdown links from all of the markdown files found at the location
our `POST_DIR` constant specifies. It then returns a de-duplicated list of all
the links.


With that helper function to generate the markdown links list, we can define
the fixture, `post_md_link`:

```python
@pytest.fixture(params=post_md_links())
def post_md_link(request):
    """Returns the md_link object for a md link found in a post."""
    return request.param
```

Similar to the fixtures in the [pages
tests](/post/creating-website-tests-pages/), this one will allow tests to map
across all the links found in the markdown pages, so a test will run for each
link.


### Writing the markdown link test

Finally, time to write the *one and only test function* in this post:

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

Because I link to both internal and external links in my posts, I have to prep
my urls a bit. So, I first check if the link starts with `http` (which would
also match ones starting with `https`). If it does, we don't have to do
anything. If it doesn't, we can assume the link is an ineternal one (ex:
`/post/creating-website-tests-links/`), and we need to prepend it with the
`BASE_URL` constant.

With a proper url, we can use the `requests.get()` to attempt retrieve a
response code from the page. If we get a response, I then assert that the
`status_code` is *not* `404` or `403`.

Note: I started by asserting that each link returned a `200` status, but
quickly learned that because I was testing mostly external links, it was a bad
idea. I never got all the tests to pass because they would often return odd
500-level errors for issues that quite frankly, doesn't matter to me. For
example, one site kept return a 500-level error I think because their servers
were 'under slightly higher load'... but when I went to the link, the page
loaded fine.

In the end, I decided I wasn't testing the issues the websites I linked to were
having, but instead just wanted to make sure my links weren't *broken*. So, I
now just ensure I'm not getting `404` or `403`'s, and I'm happy with that.


## Limitations

While I am very happy with the coverage these tests provide, they do have some
limitations to keep in mind:

- They cannot match urls with parens
- Currently only checking pages are not `403` and `404` errors. This means I
    could possibly still have broken links due to permission errors and such. I
    plan to expand this assert list in the future to cover issues better.
- I'm currently only testing markdown links. This doesn't grab and html links I
    have in my posts.
    - On a similar note, because I link most of my images with html, it also
        isn't testing if my images are broken.
    - I'd like to eventually add tests for both of these issues eventually, but
        decided testing the markdown links was the best place to start.
- Sometimes tests fail because a site is down. No biggie, just consider waiting
    a bit and running them again before deciding to remove the link.

## Conclusion

<center>
<a href="/img/posts/creating-website-tests-links/passing-links-tests.png">
<img alt="Passing tests, including new link tests" src="/img/posts/creating-website-tests-links/passing-link-tests.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">Passing tests, including the new markdown link tests</div>
</center>

That's it. By adding a few easy helper functions, a new fixture, and a *single*
test function, We've expanded my test results from 70 to over 420 test results
(and growing).

More important that the number of tests, is *what* those results
tell us. In this case, a failing test tells me that one of my markdown links
*might* be broken. These tests have *already* been beneficial to me, as I ended
updating/removing probably about 100 or so bad links from my posts while
adding these tests. So, I'd say it was worthwhile!
