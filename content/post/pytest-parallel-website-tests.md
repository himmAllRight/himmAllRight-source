+++
title   = "Running my Website Tests in Parallel with Pytest-Parallel"
date    = "2020-08-10"
author  = "Ryan Himmelwright"
image   = "img/posts/pytest-parallel-website-tests/mushroom.jpeg"
caption = "UNC-Chapel Hill Campus, Chapel Hill, NC"
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

Not all tests can be parallelized

## Adding pytest-parallel



## Improvements


## Conclusion
