+++
title  = "Shell Stuff: Find, Grep, and Command Substitution"
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

### `find`

`find` is a classic UNIX command, that searches for files in a directory
hierarchy. By default, it writes out the absolute file path for each file it
finds.

Example:

```text
➜  tree
.
├── dirA
│   ├── file3
│   ├── file4
│   └── file5
├── dirB
│   └── file6
├── file1
└── file2

2 directories, 6 files

➜  find .
.
./file2
./file1
./dirB
./dirB/file6
./dirA
./dirA/file5
./dirA/file4
./dirA/file3
```

### `grep`

Another classic. Basically, `grep` searches for a pattern in each file
provided, **or** text it is passed through a pipe (this is important for our
use-case).

Example:

```text
➜  cat file1
This is a fake file
with a few lines of content.

However, I want search for something
without opening it...

Secret: 12345

I wonder if I will be able to get it...


➜  grep Secret file1
Secret: 12345
```

### Command Substitution

Lastly, command substitution is taking one command, and using it's output as
part of another command. Historically, this used to be done by calling the
substitution command inside back-tics (\`command\`), but it [is now preferred to
use $(COMMAND) instead of backticks](http://mywiki.wooledge.org/BashFAQ/082).

Example:

```text
➜ echo I am at: `pwd`
I am at: /tmp/demo
```

or (preferred):

```test
➜ echo I am at: $(pwd)
I am at: /tmp/demo
```

#### Pipes?

### Creating the Dream Team

### Examples
