+++
title  = "Resolving Issue #26"
date   = "2019-12-14"
author = "Ryan Himmelwright"
image  = "img/posts/setup-mosh/north-buchanan-boulevard.jpeg"
caption= "North Buchanan Boulevard, Durham, NC"
tags   = ["website", "hugo"]
draft  = "False"
Comments = "True"
+++

A couple weeks ago I was working on a post when I noticed that, practically
overnight, my website wasn't rendering correctly. The home page wasn't
displaying my recent posts, but instead just listed a single "post" named...
"Posts". After some back-tracking, I determined that I had updated the
container I work in to at Fedora 31 base, and the hugo version was newer in it.
So, I filed the problem as [issue
#26](https://github.com/himmAllRight/himmAllRight-source/issues/26) for the
website repo, and finished my post in a Fedora 30 container for the time being.
Here is a quick explanation of how I *eventually* resolved issue #26.

<!--more-->


