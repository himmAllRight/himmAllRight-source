+++
title   = "Running my Website Tests in Parallel with Pytest-Parallel"
date    = "2020-08-16"
author  = "Ryan Himmelwright"
image   = "img/posts/pytest-parallel-website-tests/mushroom.jpeg"
caption = "Durham, NC"
tags    = ["website", "hugo", "testing", "python", "jenkins",]
draft   = "False"
Comments = "True"
+++

Not too long ago, I added some basic testing for my website. Now when I push
changes to my website's source repo, [automated
tests](/post/creating-website-tests-ci) run to verify that the site's [pages
are being served](/post/creating-website-tests-pages/), and that the (markdown)
[links are not broken](/post/creating-website-tests-links). It works well
enough through the 450 or so generated tests. However, one recent afternoon I
realized... I should parallelize them.

<!--more-->

## Why Parallelize?

Not all tests can be parallelized, but if they *can* handle concurrent runs, it
might be worth trying to figure it out.  All of my current website tests do a
single thing: check if a page can be reached, or not. Furthermore, each check
does not interfere with the others. Checking if one link is available does not
change the state of a second one. Ultimately, this means that I could in
theory, run all of the tests at the same time.


## Adding pytest-parallel

It turns out getting my website tests to run in parallel wasn't actually that
hard. I just added a new pip package. I found a few, but the most
promising one seemed to be `pytest-parallel`, which simply adds the option to
start pytest runs using parallel workers. To test it out, I installed the package
using the following pip command:
```python
pip install pytest-parallel --user
```

Once I verified that it *worked*, I updated the `Pipfile` in the website test
repo to include the `pytest-parallel` package:
```python
[packages]
pytest = "*"
requests = "*"
pytest-parallel = "*"
```

That's it! To run the tests in parallel, just add the `--workers` flag with a
number to the `pytest` call. For example:

```bash
pytest --workers 12 -vv .
```
This will run my normal test run (`pytest -vv .`), across 12 parallel workers.


## Improvements

So, did this actually improve anything? Yep, quite a bit ☺.
<center>
<a href="/img/posts/pytest-parallel-website-tests/pipeline-time-decrease.png">
<img alt="Time decrease in Jenkins test pipline" src="/img/posts/pytest-parallel-website-tests/pipeline-time-decrease.png" style="max-width: 100%;"/></a>
<div class="caption">Time decreases in Jenkins Test Pipeline</div>
</center>

Using 12 workers, my test pipeline in Jenkins went from taking around 4.5-5
minutes, all the way down to under 1.5 on average, and sometimes only a minute!
These times include some other steps, but the tests themselves went from
taking a few minutes to under 30 seconds! All 450+ of them!

## Conclusion

That's all I have. One day I thought I should parallelize my website tests, and
it turned out to be quite easy to do. Considering the results, I'm glad I did.
Again, while it is not always possible to run tests concurrently, if it is for
yours... try it out!
