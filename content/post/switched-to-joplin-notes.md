+++
title  = "Switched to Joplin Notes"
date   = "2019-06-16"
author = "Ryan Himmelwright"
image  = "img/posts/switched-to-joplin-notes/lafayette-pardee-flowers.jpg"
caption= "Pardee Hall - Lafayette College, Easton PA"
tags   = ["Linux", "Notes", "Organization", "Applications",]
draft  = "True"
Comments = "True"
+++

As a [huge fan](/post/org-babel-setup/) of emacs's
[org-mode](https://orgmode.org/), it should be no surprise that I've been using
it for all of my personal and work planning/notes over the last few years.
However, as my daily emacs use slowly dropped and the support for `.org` files
outside of emacs remains low (besides [Github README
files](https://github.com/himmAllRight/dotfiles/tree/master/emacs)), I started
to look for a more standard system. [Joplin](https://joplinapp.org/) is what
I've been testing the last few months. Here are my thoughts.

<!--more-->

## Previous System - Org-mode

<a href="/img/posts/switched-to-joplin-notes/org-mode-notes.png">
<img alt="Emacs with a note opened in org-mode." src="/img/posts/switched-to-joplin-notes/org-mode-notes.png" style="max-width: 100%;"/></a>
<div class="caption">Emacs with a note opened in org-mode</div>

Previously, I had been taking all of my notes using org-mode in emacs. Each
week, I would make a new `.org` file for my work notes and another for my
personal planning/notes. I would then list my [todo items](https://orgmode.org/manual/TODO-items.html), usually grouped by day, category, or both. Often, I would also [tag](https://orgmode.org/manual/Tags.html) each item, for organization.

As I worked on each item, I could quickly add time stamped notes using the
build-in [logbook drawer](https://orgmode.org/manual/Drawers.html) command. In
these notes, I would ramble on, or even past a [code snippet](https://orgmode.org/manual/Working-with-source-code.html) to save for later. As work on each task progressed, I could switch the `TODO` status to `Working On` `Finished`, `Removed`, or any other state I had pre-defined. Eventually, I [wrote an emacs-lisp script/package](https://github.com/himmAllRight/ry-org-scrum) that took  todo items in my `org` file, and dumped them into a SCRUM board at the top of the file.

#### `TODO`:

*Linked notes, archive, and exporting*

### What I liked

<a href="/img/posts/switched-to-joplin-notes/org-notes-export-pages.png">
<img alt="Pictured of org notes exported to HTML" src="/img/posts/switched-to-joplin-notes/org-notes-export-pages.png" style="max-width: 100%;"/></a>
<div class="caption">org-notes allowed me to link and export my notes to
HTML</div>

- `org-mode` is great.
- I could take all my notes in a simple markdown
- Simple code-block support
- Note linking
- Exported to html (or txt, md, pdf, or anything really)
- My previous notes were all exported to an archive website

### Issues
- Basically _had_ to use emacs for any edits
- Note supported on mobile devices
- As I used more `.md` syntax for stuff, I found myself fumbling between `org` and `md` syntax often.
- Syncing issues (mostly Nextcloud issues. Seafile helped, but still)


## The Switch - Joplin
### About Joplin

<a href="/img/posts/switched-to-joplin-notes/joplin-window.png">
<img alt="Window of the Joplin GUI application" src="/img/posts/switched-to-joplin-notes/joplin-window.png" style="max-width: 100%;"/></a>
<div class="caption">Joplin GUI window (in 'split mode')</div>


### My Setup


### What I like


### Issues I'm still figuring out/Anticipate

<a href="/img/posts/switched-to-joplin-notes/joplin-cli.png">
<img alt="Joplin cli application" src="/img/posts/switched-to-joplin-notes/joplin-cli.png" style="max-width: 100%;"/></a>
<div class="caption">Joplin CLI window </div>



## Conclusion
