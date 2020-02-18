+++
title  = "Creating Tests For This Website: Links"
date   = "2020-03-07"
author = "Ryan Himmelwright"
image  = "img/posts/creating-website-tests-pages/pnc-arena.jpeg"
caption = "PNC Arena, Raleigh NC"
tags   = ["website", "hugo", "dev", "python", "testing"]
draft  = "True"
Comments = "True"
+++


<!--more-->

## What to Test

## Adding to the Test Framework


### Adding Some More Helper Utility Functions

(I accidentally wrote these for the last post before realizing they weren't
needed for those tests)

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


