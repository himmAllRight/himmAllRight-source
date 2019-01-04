+++
title  = "Shell Shit: Find, Grep, and Command Substitution"
date   = "2019-01-05"
author = "Ryan Himmelwright"
image  = "img/header-images/ww1-park-x230.jpg"
caption= "World War I Memorial Park, North Attleboro, MA"
tags   = ["Linux", "Shell",]
draft  = "True"
Comments = "True"
+++

Applications can leave their junk files all over the place. While I
appreciate that all of the `.swp`, `.retry`, and `"conflict"` files are there to
help me when things go wrong... sometimes I just want to clean up my
file system. So, here is a simple string of commands I often use to declutter
my files.

<!--more-->

### There are many ways

First, lets clarify something. I know there are *MANY* ways to accomplish this.
The method described in this post is to share **one** solution I use, that
might help someone that currently knows **zero**.

### The commands

#### `find`

`find` is a classic UNIX command, that searches for files in a directory
hierarchy. By default, it writes out the absolute file path for each file it
finds.

Example:

#### `grep`

Another classic, searches for a pattern in each file provided, **or** text it
is passed through a pipe (this is important for our use-case).

Example:

#### Command Substitution
  [it is preferred to use $(..) instead of \`..\`](http://mywiki.wooledge.org/BashFAQ/082)

Example:

### Creating the Dream Team

### Examples
