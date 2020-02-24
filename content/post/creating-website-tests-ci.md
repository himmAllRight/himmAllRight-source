+++
title  = "Creating Tests For This Website: CI"
date   = "2020-02-29"
author = "Ryan Himmelwright"
image  = "img/posts/creating-website-tests-pages/pnc-arena.jpeg"
caption = "PNC Arena, Raleigh NC"
tags   = ["website", "hugo", "dev", "python", "testing", "jenkins"]
draft  = "True"
Comments = "True"
+++

In the [last post](/post/creating-website-tests-pages/), I setup some simple
testing to ensure pages were being served correctly. However, the problem is
that I can't trust myself to want to run the tests before merging a branch into
`master`. Luckily, I  can have [Jenkins](https://jenkins.io) do all that
*responsible* stuff for me. In this post, we will take that test framework...
and automate it.

<!--more-->


