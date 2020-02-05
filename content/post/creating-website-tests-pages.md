+++
title  = "Creating Tests For This Website: Pages"
date   = "2020-02-09"
author = "Ryan Himmelwright"
image  = "img/posts/fedora-kde-tb3/leaves.jpeg"
caption = "Durham, NC"
tags   = ["website", "hugo", "dev", "python", "testing"]
draft  = "True"
Comments = "True"
+++


<!--more-->

## What to Test


## Setting up the env

- Install `pipenv`
- Install needed packages inside `pipenv shell`


## Defining Constants

- Create and define the `constants.py` file
- Maybe only define or partially fill in some of them, and come back later?

## Writing Some Helper Utility Functions

- Create and define the `utils.py` file
- Define the file helper functions and explain why we will need them


## Conftest

- Create and define the `conftest.py` file
- Explain briefly what the conftest is
- Define each of my pytest fixtures, and any helper functions
  - `page_url`
  - `post_url`
  - `non_live_post_url` and `non_live_post_urls` helper function


## Finally... Some Tests!

- Briefly explain how pytest test files work
- Create and define `test_pages.py`

#### Testing Pages

- Create and explain `test_page_served` test function

#### Testing Posts

- Create and explain `test_post_served` test function

#### Lets Get Fancy: Testing Unapproved Posts Are *NOT* Served

- Explain why I want a test like this
- Show how we can use those `util` functions from earlier to get what we want
- Create and explain how the `test_non_defined_posts_not_served` test function
    works


## Lets Run Some Tests!

- Show how to run tests using `pipenv run` or from `pipenv shell`
- Run the tests, and show the output
- Maybe purposely show a failed test as an example


## Conclusion

- Wrap it up!
- Maybe hint at the next post in this serries
