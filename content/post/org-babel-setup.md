+++
title    = "Organizing my Emacs config with Org-Babel"
date     = "2018-06-22"
author   = "Ryan Himmelwright"
image    = "img/header-images/golden-co-mountains.jpg"
caption  = "Golden, CO"
tags     = ["Linux", "Programming", "Dev", "Emacs","dotfiles"]
Comments = "True"
draft    = true
+++

In my [previous post](../emacs-update-evil-usepackage/), I completely
redid my emacs configuration from scratch, building it around the use
of evil mode and use-package. As I was wrapping up, I learned of yet
*another* emacs package that wil forever change how I maintain my
emacs
configuration... [org-babel](https://orgmode.org/worg/org-contrib/babel/intro.html).

<!--more-->

## Org Babel
Org-babel is an emacs package, that lets take an
[org-mode](https://orgmode.org/) file, and evaluates all of the [code
blocks](https://orgmode.org/org.html#Literal-examples) contained
within it. This means I can write an annotated org file, filled with
`emacs-lisp` code blocks, and export just the emacs-lisp code. After
testing it out, I realized that the main emacs lisp file I use is... my
`.emacs` file...

## Setup

Installing babel couldn't be simpler. If you are running Emacs version
24 or higher, and a current version of Org-mode, Babel is already
available by default. In order to generate an `.emacs` config from an
`.org` file, we need to first setup a `config.org` file, and then tell
`.emacs` to load it with org-babel.

### config.org

First, start by creating an `.org` file to use for all of the
configuration content. This can be named anything, and exist anywhere,
but I like to keep mine in the emacs section of my [dotfiles
repo](https://github.com/himmAllRight/dotfiles), named
`config.org`. This file functions like any other org file, so I added
a small header section at the top... because why not?

```org
#+TITLE: My Emacs Configuration
#+AUTHOR: Ryan Himmelwright
#+EMAIL: ryan@himmelwright.net
#+OPTIONS: num:nil 
```

After that, I broke down my file by creating org headings for the
different groups of the configuration. For example, I started with the
headings `Repos & Core Packages`, `Core Setup`, `Evil Mode`, `Ivy`,
`Writing`, `Development`... etc.

*Note: In org-mode, use "\*" to create headings. Each contiguous "\*"
corresponds to the equivalent HTML heading level. Ex: `*` == `<h1>`,
`**` == `<h2>`, and so on.*

I started transferring the emacs-lisp code from my previous `.emacs`
file, to under each heading in `config.org`. As I transferred text, I
transformed the comments that described each code snippet into normal
org text, and wrapped the `emacs-lisp` inside an org code block.

<a href="../../img/posts/org-babel-setup/config-org-example1.png"><img src="../../img/posts/org-babel-setup/config-org-example1.png" style="max-width: 100%; float: left; margin: 0px 15px 0px 0px;" alt="Example snippet of my org-babel config.org file" /></a>
<br clear="all">
<div class="caption">Example snippet of my org-babel config.org file</div>

To create a code block, use the `#+BEGIN_SRC emacs-lisp` and
`#+END_SRC` org tags to encapsulate the `emacs-lisp` code. Continue to
do this until all of the desired emacs-lisp code is contained inside
org code blocks. 



##### Side Note: Easy Org Code Blocks

<a href="../../img/posts/org-babel-setup/easy-org-mode-code.gif"><img
src="../../img/posts/org-babel-setup/easy-org-mode-code.gif"
style="max-width: 100%; float: left; margin: 0px 15px 0px 0px;"
alt="Example snippet of my org-babel config.org file" /></a> <br
clear="all"> <div class="caption">Code block can be easily created
with `<s` and `TAB`.</div>

In org-mode, you can write `<s`, then hit `TAB` and it will expand
into the `BEGIN_SRC` and `END_SRC` tags. Just don't forget to add
`emacs-lisp` to the `BEGIN_SRC` tag!


### .emacs

For the contents of `.emacs`, call `package-initialize` and then have
`org-babel` load the `config.org` file.

```emacs-lisp
(package-initialize)
(org-babel-load-file "~/dotfiles/emacs/config.org")
```

That's it. Assuming the `config.org` is complete, emacs should now
initialize using the code snippets from *it*. While these are the only
two *required* lines, do note that emacs will still write the
`#'custom-set-variables` to the bottom of the `.emacs` file. That's
fine. If anything, it makes it easier to source control the *actual*
configuration file, since emacs isn't constantly adding to it,
changing the diff.


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

It should go without saying that the organization and maintainability
of org-mode configurations make them extremely *readable*. Not only is
the source code easier to read, but org files can be
[exported](https://orgmode.org/manual/Exporting.html) to all sorts of
outputs (HTML, LaTeX, OpenDocument, etc). Combined with a style-sheet,
these outputs can look *very* sharp... especially for a "`.emacs`
file"! 

<a href="../../img/posts/org-babel-setup/github-config.png"><img
src="../../img/posts/org-babel-setup/github-config.png"
style="max-width: 100%; float: left; margin: 0px 15px 0px 0px;"
alt="Example of how Github renders org files as a markdown" /></a> <br
clear="all"> <div class="caption">Github renders org files as a markdown.</div>

Beyond normal `org` exporting, [Github](http://www.github.com) does
something awesome... in their web viewer they *render* `org` files as
a known markup language! This means that if you click on a `*.org`
file on Gihub's web interface, it will display well-formatted version
of the content, instead of defaulting to the raw org text.

## Speaking of Github...

While I have always maintained my emacs configuration in [my dotfiles
repo](https://github.com/himmAllRight/dotfiles), org-babel let me step
up my game a bit. My current [dotfile
system](http://localhost:1313/post/new-dotfiles/) has all of my emacs
files in a separate `emacs` folder. On Github, each directory in a repo
can contain a `README` file (or.... a symlink to a file...) that will
be displayed below the list of files.


## My Maintained Config
<a href="../../img/posts/org-babel-setup/github-emacs.png"><img
src="../../img/posts/org-babel-setup/github-emacs.png"
style="max-width: 100%; float: left; margin: 0px 15px 0px 0px;"
alt="Example of how Github renders org files as a markdown" /></a> <br
clear="all"> <div class="caption">Github renders org files as a
markdown.</div>

In the emacs section of my dotfiles, I have created a symlink,
`README.org`, to my `config.org` file.

```bash 
sudo ln -s config.org README.org
```

Github recognizes this, so my `README` file "contains" whatever the
contents of `config.org` are. Now, when one visits the [emacs
section](https://github.com/himmAllRight/dotfiles/tree/master/emacs) of my dotfiles
repo,
an organized, well-formatted, and always up-to-date version of my
"`.emacs` file is displayed as the `README`.

The Github integration is the cherry on top of a new emacs
configuration system I was already ecstatic about. I've been an
org-mode fan for years, and org-babel is one more feature to add to my
growing list of reasons *why* I love it. I highly recommend checking
it out.
