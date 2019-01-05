+++
title  = "Shell Stuff: Easy File Cleanup"
date   = "2019-01-05"
author = "Ryan Himmelwright"
image  = "img/header-images/ww1-park-x230.jpg"
caption= "World War I Memorial Park, North Attleboro, MA"
tags   = ["Linux", "Shell",]
draft  = "False"
Comments = "True"
+++

Applications can leave their junk files all over the place. While I
appreciate that all of the `.swp`, `.retry`, and `"conflict"` files are there to
help me when things go wrong... sometimes I just want to clean up my
file system. So... here is a simple string of commands I often use to declutter
my files.

<!--more-->

*DISCLAIMER:* I know there are *MANY* ways to accomplish this.  The method
described in this post is to share **one** efficient solution I use, that might
help someone that currently knows **zero**.

### The commands

First, lets quickly meet the commands we will be using:

### Find

`find` is a classic UNIX command that searches for files in a directory
hierarchy. By default, it writes out the file path for each file/directory that
it finds.

#### Example

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

### Grep

Another classic. Basically, `grep` searches for a pattern in each file
provided. In addition to files, it can search text passed through a pipe (this
is important for our use, but more on that later).

#### Example

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

Lastly, *command substitution* is taking one command, and using it's output as
*part* of *another command*. Traditionally, this was done by calling the
substitution command \`inside backticks\`, but it [is now preferred to use
$(COMMAND) instead of backticks](http://mywiki.wooledge.org/BashFAQ/082).

#### Example
```text
➜ echo I am at: `pwd`
I am at: /tmp/demo
```

or (preferred):

```test
➜ echo I am at: $(pwd)
I am at: /tmp/demo
```

### Pipes

An [unix pipe](https://en.wikipedia.org/wiki/Pipeline_(Unix) ) (`|`) directs the
*output* of one command, to be used as the *input* for another command. Pipes
can be used to chain together several commands, forming a *pipeline*.

#### Example
The output of `ls` can be fed as input to `wc` (word count) to create a
pipeline command that returns the number of files/directories in the current directory.
```shell
➜ ls
dirA  dirB  file1  file2

➜ ls | wc -l
4
```

### Putting It All Together

Now that we know all the parts, how does it all fit together? One particular
shell chain I find convenient is pairing `find` and `grep` to recursively get
all the paths of a particular file type, and then use it in a command
substitution to pass that result on to another command (such as `rm`).

```shell
COMMAND $(find . | grep SEARCHSTRING)
```

This is the combination I use to clean up my directories. While working on
writing ansible playbooks, I can generate a few `*.retry` files, as well as
some `*.swp` files from editing in vim.

#### Example

```bash
➜ find . | grep .retry          ## Find *.retry files
./file1.retry
./dirA/file5.retry
./dirA/file3.retry

➜ rm $(find . | grep .retry)    ## Delete *.retry files

➜ find . | grep .retry          ## Check that they were deleted

➜
```

### Summary

That's it. A small post for a *simple* but **powerful** command line set.  If
you haven't used this team of commands before, give it a try sometime! Have
fun!
