+++
title   = "Organizing my Emacs config with Org-Babel"
date    = "2018-06-08"
author  = "Ryan Himmelwright"
image   = "img/header-images/golden-co-mountains.jpg"
caption = "Golden, CO"
tags    = ["Linux", "Programming", "Dev", "Emacs","dotfiles"]
draft   = true
+++

In my [previous post](../emacs-update-evil-usepackage/), I completely
redid my emacs configuration from scratch, building it around the use
of evil mode and use-package. As I was wrapping, I discovered yet
another emacs package that has forever changed how I maintain my emacs
configuration... [org-babel](https://orgmode.org/worg/org-contrib/babel/intro.html).

<!--more-->

## Org Babel
Org-babel is an emacs package that lets take an
[org-mode](https://orgmode.org/) file, and evaluate all of the [code
blocks](https://orgmode.org/org.html#Literal-examples) contained in
it. This means I can write an annotated org file filled with
`emacs-lisp` code blocks, and export just the emacs-lisp code... my
`.emacs` file...

## Setup

Installing babel couldn't be simpler. If you are running `>=Emacs24`,
a current version of Org-mode with Babel is already available by
default. In order to generate our `.emacs` config from a `.org` file,
we need to first setup that `config.org` file, and then tell the
`.emacs` one to use it.

### config.org

Start by creating a `.org` file to use for all of the configuration
content. This can be named anything, and exist anywhere really, but I
like to keep mine in the emacs section of my [dotfiles
repo](https://github.com/himmAllRight/dotfiles), named
`config.org`. This file functions like any other org file, so I
decided to add a small header at the top... because why not?

```org
#+TITLE: My Emacs Configuration
#+AUTHOR: Ryan Himmelwright
#+EMAIL: ryan@himmelwright.net
#+OPTIONS: num:nil 
```

After that, I broke down my configuration by creating org headings for
the different sections of my configuration. For example, I started
with `Repos & Core Packages`, `Core Setup`, `Evil Mode`, `Ivy`,
`Writing`, `Development`... and so on.

*Note: Use "\*" to create headings in org mode. Each "\*" corresponding
to the HTML heading levels. Ex: `*` == `<h1>`, `**` == `<h2>`, etc.*

Under each heading, I started transferring my emacs code. I turned the
comments that described each code piece into normal org text, and
wrapped the `emacs-lisp` code snippet in an org code block. For
example:


<a href="../../img/posts/org-babel-setup/config-org-example1.png"><img src="../../img/posts/org-babel-setup/config-org-example1.png" style="max-width: 100%; float: left; margin: 0px 15px 0px 0px;" alt="Example snippet of my org-babel config.org file" /></a>
<br clear="all">
<div class="caption">Example snippet of my org-babel config.org file</div>

Use the `#+BEGIN_SRC emacs-lisp` and `#+END_SRC` org tags to
encapsulate the `emacs-lisp` code. Continue to do this until all of
the desired emacs-lisp code is contained inside org code blocks.

##### Easy Org Code Blocks

<a href="../../img/posts/org-babel-setup/easy-org-mode-code.gif"><img
src="../../img/posts/org-babel-setup/easy-org-mode-code.gif"
style="max-width: 100%; float: left; margin: 0px 15px 0px 0px;"
alt="Example snippet of my org-babel config.org file" /></a> <br
clear="all"> <div class="caption">Code block can be easil created with
`<s` and `TAB`.</div>

**Note:** In org mode, you can just write `<s` and hit `TAB` and
org-mode will expand it out into the source code `BEGIN` and `END`
tags. Just don't forget to add `emacs-lisp` to the `BEGIN_SRC` tag.


### .emacs

For the contents of `.emacs`, just call `package-initialize` and then
have `org-babel` load the file, like so:

```emacs-lisp
(package-initialize)
(org-babel-load-file "~/dotfiles/emacs/config.org")
```

That's it. Assuming the `config.org` is complete, emacs should now
load up using the code snippets from *it*, instead of needing to have
everything in the `.emacs` file. These are the only two lines
needed. However, do note that emacs will still write the
`#'custom-set-variables` to the bottom of the `.emacs` file. That's
fine. If anything, it makes it easier to source control the *actual*
configuration file, since emacs isn't constantly adding to it.



## What I like

### Organized

<a href="../../img/posts/org-babel-setup/org-expand-example.gif"><img
src="../../img/posts/org-babel-setup/org-expand-example.gif"
style="max-width: 100%; float: left; margin: 0px 15px 0px 0px;"
alt="Example snippet of expanding org headers to easily find code."
/></a> <br clear="all"> <div class="caption">Expanding org headers to
easily find code.</div>

Org mode's hierarchical structure inherently organizes the contents of
files. Using it for my emacs configuration is no different. I can use
org headers to easily break down my file into sections, and
sub-sections, which I can expand and collapse as needed. For example,
my `config.org` is currently over 500 lines long, but with all the
headers collapsed, it is less than 20. From there I can just expand to
the section I need.

### Maintainable

Being so organized, the `config.org` file is very easy to maintain. If
I want to edit a setting, I can just search through the headers for
the section, and then edit either the code block, or text. If I want
to add a new item, I can just insert a new header, add a code block
for what I want, any maybe some text to explain what it does for
future reference. Done. Most importantly, the structure helps prevent
it from turning into an in-production *"scratch code"* file...

### Easy to Read
#### In Code
#### Exported
#### On Github

## My maintained config

