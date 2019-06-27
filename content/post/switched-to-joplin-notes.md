+++
title  = "Switched to Joplin Notes"
date   = "2019-06-26"
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


<a href="/img/posts/switched-to-joplin-notes/org-notes-export-pages.png">
<img alt="Pictured of org notes exported to HTML" src="/img/posts/switched-to-joplin-notes/org-notes-export-pages.png" style="max-width: 100%;"/></a>
<div class="caption">org-notes allowed me to link and export my notes to
HTML</div>

Lastly, org files can be [exported](https://orgmode.org/manual/Exporting.html)
to all sorts of file types (md, html, pdf, latex). By combining exporting with
[internal linking](https://orgmode.org/manual/Internal-links.html), I was able
to create a nice system for my archived notes. I created an `index.org` file
which linked to each week's notes (each note file also linked back to the
index). Each week, I would archive the html export of a note, and add it to the
index list. This meant I could browse my old notes as a website.

### What I liked

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

All in all, I loved taking notes in org-mode. However, I wanted something that
could be used on *all* my devices, and was able to more easily translate
outside of emacsOS.

## The Switch - Joplin

<a href="/img/posts/switched-to-joplin-notes/joplin-window.png">
<img alt="Window of the Joplin GUI application" src="/img/posts/switched-to-joplin-notes/joplin-window.png" style="max-width: 100%;"/></a>
<div class="caption">Joplin GUI window (in 'split mode')</div>

### About Joplin

Joplin is a free and open source note taking/to-do application. It syncs and organizes
markdown notes into notebooks, across all platforms (Android, iOS, macOS,
Linux, and Windows). It even have a terminal application in addition to the GUI
one.

I decided to try it out because it was an open source markdown editor that was
supported on *so many* platforms.


### My Setup

When configuring joplin, a sync system has to be defined (well, *should*. Notes
*can* be saved locally). There are a few supported options, including using
Nextcloud, which is what I had used for my org notes, but eventually moved away
from due to file conflict issues.

<center>
<a href="/img/posts/switched-to-joplin-notes/fastmail_logo.png">
<img alt="Window of the Joplin GUI application" src="/img/posts/switched-to-joplin-notes/fastmail_logo.png" style="max-width: 70%;"/></a>
<div class="caption">Joplin GUI window (in 'split mode')</div>
</center>

The past few years, I have used [fastmail](https://www.fastmail.com) for my
personal email. While researching Joplin, I learned that I could sync the notes
to my fastmail account's WebDav server. I wasn't using any of my account's file
storage, so I figured I might as well. It works great!

### What I like
#### Syncs on *all* my devices
What I have enjoyed most about this setup is that my notes sync to all of my
devices. More importantly, I can *read* the notes on every device. With
previous systems, the *files* might sync everywhere, but I still couldn't read
them.

#### CLI and GUI versions
Similarly, I like that Joplin has both a GUI and CLI client. While I have
mostly used the GUI client, I enjoy having the CLI because it means I always
have the option to ssh home into a machine and take notes. Additionally, the
cli client allows me to take/edit notes with my own terminal editors such as
emacs *or* vim. This is very convenient, and I should honestly try using
Joplin in the way *more*.

#### Markdown Note Exports

<center>
<a href="/img/posts/switched-to-joplin-notes/export-options.png">
<img alt="Joplin cli application" src="/img/posts/switched-to-joplin-notes/export-options.png" style="max-width: 100%;"/></a>
</center>
<div class="caption">Export options in Joplin GUI</div>

I like that the notes are formatted in markdown. This provides me with some
consistency when writing, but also means that my notes are in a format that is
very standardized. Additionally, I like that joplin allows easy exporting of
the notes to other formats such as `json` or as `pdf`s.

#### Easy enough to use
Lastly, Joplin has been easy to use. After setup, I just have to open the app,
and start typing away (maybe with a sync or two). While my last setup required
one to be somewhat of an emacs/org guru to use... this doesn't.


### Issues I'm still figuring out/Anticipate

<a href="/img/posts/switched-to-joplin-notes/joplin-cli.png">
<img alt="Joplin cli application" src="/img/posts/switched-to-joplin-notes/joplin-cli.png" style="max-width: 100%;"/></a>
<div class="caption">Joplin CLI window </div>

#### Setup is a pain

For as easily as Joplin is to *use*, it can be a bit of a pain to setup. First,
configuring the sync solution *can* be a bit confusing for a non-technical
person. I'll note that I do use a slightly more confusing sync system, and I'm
sure that something like Dropbox is much easier. Still, the application could
benefit from a setup wizard or something to help people get started.

The main issue I have with the setup however isn't configuring sync. It's
adding a new system. By default, if I configure a new device with my sync
solution (my laptop or phone for example) and then sync it, it will load up all
of the crap default example tags and notes, which then pull down on all of my
systems. This is extremely frustrating because I have to keep deleting them.
This is multiplied by the fact that it happens with *each* client I setup. So
if I setup the gui on my laptop, it will happen and then when I setup the cli,
it will happen *again*.

A *slight* work-around I have been able to use when setting up a new computer
is to simply copy the config files from an existing system to the new one.
These folders can be found at `~/.config/joplin/`, `~/.config/Joplin/`, and/or
`~/.config/joplin-desktop/`. This also means that the new system *should* have less
it needs to sync down from the server on the first sync.

#### Long term archiving

The **big** problem I have... and think I will continue to have with Joplin, is
long-term organization of notes. Part of this is my inability to figure out an
efficient way to organized way to handle my new "log" notes (where I take quick
notes about items I'm working on. Previously I used to take them under my todo
items, but decided to break them out into their own notes in Joplin).

Part of this problem however is caused my Joplins shallow organization
structure. There are 1) notebooks, and then 2) notes. That's it. Unlike having
a file structure where I can do something like
`archive/2019/June/Weekly_Plans/`, I can't really go that deep with Joplin, so
I end up just having a single notebook with *all* my weekly plan notes listed
in it.

One remaining solution might be to get more aggressive with the tagging
feature, and see if I can create a more organized system using that. I might be
able to tag each note with a month/year, and then cut off my log notes each
month. The only problem with this is that it doesn't seem like I can select
*multiple* tags at a time... which would mean *all* of my notes for a month
will me shown under the tag... which would be a deal breaker for me :( .

## Conclusion

So in conclusion, I think that Joplin *is* a great open source notes solution.
If someone needs a system to keep a bunch of normal *notes* synced across all
their devices, this is it. I however, have requirements that are a bit more
complicated, and might have to try out something else as a result. There are a
bunch of features I learned from Joplin that I didn't have with org-mode that I
will definitely look for... in my next solution.


