+++
title   = "Running my Website Tests in Parallel with Pytest-Parallel"
date    = "2020-08-14"
author  = "Ryan Himmelwright"
image   = "img/posts/pytest-parallel-website-tests/mushroom.jpeg"
caption = "Durham, NC"
tags    = ["website", "hugo", "testing", "python", "jenkins",]
draft   = "False"
Comments = "True"
+++

Being the good little QE that I am, I recently added some basic testing for my
website. Now when I make changes to my website's source repo, some
[automated](/post/creating-tests-ci) tests run to verify that the site's [pages
are being served](/post/creating-website-tests-pages/), and that that
(markdown) [links are not broken](/post/creating-website-tests-links). It works
well enough, running through the 450 or so generated tests. However, one recent
afternoon I realized... I should parallelize them.

<!--more-->

## Why Parallelize?

Not all tests can be parallelized, but if they *can* handle concurrent runs, it
might be worth trying to figure it out.  All of my website tests do a single
thing: check if a page exists or not.  Additionally, each check does not
inferfere with the others. Checking if one link is available doesn't change the
state of a second one. Ultimately, this means that It doesn't matter if I run
one or all of the tests, at the same time.

With any luck, this should speed up how long it takes all of the tests to run.


## Adding pytest-parallel

So running my website tests in parallel wasn't actually that hard. I just had
to add a new pip package. I found a few, but the most promising one seemed to be
`pytest-parallel`, which simply adds the option to run pytest runs with
parallel workers. To test it out, I installed the package with a pip command:
```python
pip install pytest-parallel --user
```

Once I found it it *worked*, I updated the `Pipfile` for my website test repo:
```python
[packages]
pytest = "*"
requests = "*"
pytest-parallel = "*"
```

That's it! To run the test in parallel, just add the `--workers` flag with a
number to the `pytest` call. For example:

```bash
pytest --workers 12 -vv .
```
This will run my normal test run (`pytest -vv .`), across 12 parallel workers.


## Improvements

So, did this actually improve anything? Yep ☺.
<center>
<a href="/img/posts/pytest-parallel-website-tests/pipeline-time-decrease.png">
<img alt="Time decrease in Jenkins test pipline" src="/img/posts/pytest-parallel-website-tests/pipeline-time-decrease.png" style="max-width: 100%;"/></a>
<div class="caption">Time decreases in Jenkins Test Pipeline</div>
</center>

Using 12 workers, my test pipeline in Jenkins went from taking around 4:30-5
minutes, all the way down to under 1:30 on average, and sometimes only a
minute! The tests themselves went from taking a few minutes to under 30
seconds! All 450+ of them!

## Conclusion

That's all I have. One day I thought I should parallelize my website tests, and
it turns it it was quite easy to do, especially considering the results I saw
from it. Again, while it is not always possible to run tests concurrently, if
it is for yours... try it out!
