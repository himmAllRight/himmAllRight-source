+++
title  = "Creating Tests For This Website: Pages"
date   = "2020-02-16"
author = "Ryan Himmelwright"
image  = "img/posts/fedora-kde-tb3/leaves.jpeg"
caption = "Durham, NC"
tags   = ["website", "hugo", "dev", "python", "testing"]
draft  = "True"
Comments = "True"
+++

As I grow this website, there are more and more moving parts. More pages, more
posts, more images, and more links. I've gotten better about breaking work up
into separate branches (instead of doing everything in `master`), but even that
isn't enough to ensure everything works as expected when generating this staic
website. Then it hit me... I could write some simple testing... for my website.

<!--more-->

## What to Test

When editing a page on this website, or publishing a new post, I often wonder
"How can I be *sure* everything is working"? I worry if every post file is *actually*
being served as a web page, or worse... what if a post that isn't *ready* to be
published is *accidentally* pushed with a website fix? (By the way, this is a
completely unreasonable fear, given that ALL of my website source files, drafts included are
publicly hosted on Github. Nonetheless, the fear exists).

I also wonder if all the images and links I've referenced in my posts over the
years... still work. However, solving that issue is for another post. In this
post, we are going to focus on:

- Setting up the test environment
- Building the testing framework
- Writing some basic tests to ensure:
    - The pages I *want* to be served are
    - Pages and post that are not ready, are *not* being served

As my website is currently compiled using [hugo](https://gohugo.io), the tests
will be centered around that framework. However, most of the information can be
applied to testing most statically generated websites, as they are all quite
similar.


## Setting up the env

For my test framework, I will be using
[pytest](https://docs.pytest.org/en/latest/contents.html), and to make all the
python stuff a bit easier to manage, I will be using
[pipenv](https://github.com/pypa/pipenv). I also tend to be working on a
[Fedora](https://getfedora.org) computer, or at least in a Fedora
[podman](https://podman.io) container, so some of my instructions use `dnf`.
Adjust to your package manager accordingly, if needed.



- Install `pipenv`
- Install needed packages inside `pipenv shell`


## Creating the Test Framework


### Defining Constants

- Create and define the `constants.py` file
- Maybe only define or partially fill in some of them, and come back later?

### Writing Some Helper Utility Functions

- Create and define the `utils.py` file
- Define the file helper functions and explain why we will need them


### Conftest

- Create and define the `conftest.py` file
- Explain briefly what the conftest is
- Define each of my pytest fixtures, and any helper functions
  - `page_url`
  - `post_url`
  - `non_live_post_url` and `non_live_post_urls` helper function


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

