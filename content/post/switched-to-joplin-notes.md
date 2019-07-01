+++
title  = "Switched to Joplin Notes"
date   = "2019-06-30"
author = "Ryan Himmelwright"
image  = "img/posts/switched-to-joplin-notes/lafayette-pardee-flowers.jpg"
caption= "Pardee Hall - Lafayette College, Easton PA"
tags   = ["Linux", "Notes", "Organization", "Applications",]
draft  = "False"
Comments = "True"
+++

As a [massive fan](/post/org-babel-setup/) of emacs's
[org-mode](https://orgmode.org/), it should be no surprise that I've been using
it for my personal and work planning/notes over the last few years.  However,
as my daily emacs usage has slowly dropped, and the support for `.org` files
outside of emacs remains low (other than [Github README
files](https://github.com/himmAllRight/dotfiles/tree/master/emacs)), I started
to look for a more standard system. The last few months, I've been using
[Joplin](https://joplinapp.org/). Here are my thoughts.

<!--more-->

## Previous System - Org-mode

<a href="/img/posts/switched-to-joplin-notes/org-mode-notes.png">
<img alt="Emacs with a note opened in org-mode." src="/img/posts/switched-to-joplin-notes/org-mode-notes.png" style="max-width: 100%;"/></a>
<div class="caption">Emacs with a note opened in org-mode</div>

Previously, I had been taking all of my notes using org-mode in emacs. Each
week, I made a new `.org` file for my work notes, and another for my personal
planning/notes. I would then list my [todo
items](https://orgmode.org/manual/TODO-items.html), usually grouped by day,
category, or both. I would also
[tag](https://orgmode.org/manual/Tags.html) each item, for better organization.

As I worked on each task, I could quickly add time-stamped notes using the
built-in [logbook drawer](https://orgmode.org/manual/Drawers.html) shortcut. In
these notes, I would ramble, or paste a [code
snippet](https://orgmode.org/manual/Working-with-source-code.html) to save for
later. As work on each item progressed, I could set the `TODO` status to
`Working On` `Finished`, `Removed`, or any other state I had pre-defined.
Eventually, I [wrote an emacs-lisp
script/package](https://github.com/himmAllRight/ry-org-scrum) that took the
`todo` items in my `org` file, and dumped them into a SCRUM board at the top of
the file.


<a href="/img/posts/switched-to-joplin-notes/org-notes-export-pages.png">
<img alt="Pictured of org notes exported to HTML" src="/img/posts/switched-to-joplin-notes/org-notes-export-pages.png" style="max-width: 100%;"/></a>
<div class="caption">org-notes allowed me to link and export my notes to
HTML</div>

Lastly, org files can be [exported](https://orgmode.org/manual/Exporting.html)
to all sorts of file types (md, html, pdf, latex). By combining the export
feature with [internal
linking](https://orgmode.org/manual/Internal-links.html), I was able to create
an organized system for my archived notes. I created an `index.org` file which
linked to each week's notes. Every week, I would archive the html export of a
note, and add it to the index list. This meant I could browse my old notes as a
website.

### What I liked

- `org-mode` is great.
- I could take all of my notes in a simple markdown language (org)
- Good code-block support
- Note linking
- Exported to html (or txt, md, pdf, or anything really)
- My previous notes were all exported to an archive website

### Issues
- I _had_ to use emacs for any edits
- Not supported on mobile devices
- As I used more `.md` syntax for other applications, I found myself fumbling between `org` and `md` syntax often.
- Syncing issues (mostly Nextcloud issues. Seafile helped, but it still occurred)

All in all, I loved taking notes in org-mode. However, I wanted something that
could be used on *all* my devices, and was more easily translatable outside of
"emacsOS".

## The Switch - Joplin

<a href="/img/posts/switched-to-joplin-notes/joplin-window.png">
<img alt="Window of the Joplin GUI application" src="/img/posts/switched-to-joplin-notes/joplin-window.png" style="max-width: 100%;"/></a>
<div class="caption">Joplin GUI window (in 'split mode')</div>

### About Joplin

Joplin is an open source note-taking and to-do application. It synchronizes and
organizes markdown notes into notebooks, across many platforms (Android, iOS,
macOS, Linux, and Windows). It even has both a GUI *and* terminal client.  So,
I decided to give it a try.


### My Setup

When configuring joplin, a sync system has to be defined (well, *should*. Notes
can also be saved locally). There are a few supported options including using
Nextcloud. I had previously synced my org notes using Nextcloud, but eventually
moved away from it due to repeated file conflict issues. So I wanted to try
something different.

<center>
<a href="/img/posts/switched-to-joplin-notes/fastmail_logo.png">
<img alt="Window of the Joplin GUI application" src="/img/posts/switched-to-joplin-notes/fastmail_logo.png" style="max-width: 70%;"/></a>
<div class="caption">Joplin GUI window (in 'split mode')</div>
</center>

While researching Joplin, I learned that I could sync notes to the WebDav
server on the [fastmail](https://www.fastmail.com) account I have for email. I
wasn't using any of the account's file storage, so I figured I this would be a
good way to get use out of a service I'm already paying for. It works great!

### What I like
#### Syncs on *all* my devices
What I have enjoyed most about this setup is that my notes sync to all of my
devices. Most importantly, I can *read* the notes on every device. With
previous systems, the files would sync everywhere, but I still couldn't always
easily read them.

#### CLI and GUI versions
Similarly, I like that Joplin has both a GUI and CLI client. I
mostly use the GUI, but enjoy having the CLI as an option because it means I
can always ssh into a machine and take notes. Additionally, the
cli client allows me to take/edit notes using my own terminal editors such as
emacs *or* vim. This is quite convenient, and I should probably start using
Joplin this way more often.

#### Markdown Note Exports

<center>
<a href="/img/posts/switched-to-joplin-notes/export-options.png">
<img alt="Joplin cli application" src="/img/posts/switched-to-joplin-notes/export-options.png" style="max-width: 100%;"/></a>
</center>
<div class="caption">Export options in Joplin GUI</div>

I like that notes are formatted in markdown. This provides some
consistency when writing, but ensures that my notes are in a format that is
standardized. Additionally, joplin allows easy exporting of
the notes to other formats such as `json` or as `pdf`s.

#### Easy enough to use
Lastly, Joplin has been easy to use. After setup, I just have to open the app,
and start typing away (maybe with a sync or two). While my last setup required
the user to be somewhat of an emacs/org guru... this doesn't.


### Issues I'm still figuring out/Anticipate

<a href="/img/posts/switched-to-joplin-notes/joplin-cli.png">
<img alt="Joplin cli application" src="/img/posts/switched-to-joplin-notes/joplin-cli.png" style="max-width: 100%;"/></a>
<div class="caption">Joplin CLI window </div>

#### Setup is a pain

While configuring sync can be a pain, it's not my biggest gripe with the Joplin
setup process. It's adding a new system. By default, if I configure a new
device with my sync solution (my laptop or phone for example) and then sync, it
will load up all of the crap default example tags and notes, which then pull
down to all of my systems. This is extremely frustrating because I have to keep
deleting them.  This is multiplied by the fact that it happens with *each
client* I setup. So if I setup the gui and cli on my laptop, it will happen
*twice* (2x each default tags/notes will show up on all my systems).

*Semi-Solution*:

A *slight* work-around I have been able to use when setting up a new computer
is to simply copy the config files from an existing system to the new one.
These folders can be found at `~/.config/joplin/`, `~/.config/Joplin/`, and/or
`~/.config/joplin-desktop/`. This also means that the new system *should* have less
it needs to sync down from the server on the first sync.

#### Long term archiving

The **big** problem I have... and think I will continue to have with Joplin, is
the long-term organization of notes. Part of this is my inability to figure out an
efficient and organized way to handle my "log" notes.

This problem partially stems from Joplin's shallow organizational
structure. There are notebooks, and notes. That's it. Unlike having
a file structure where I can do something like
`archive/2019/June/Weekly_Plans/`, I can't really go that deep with Joplin, so
I end up just having a single notebook with *all* my weekly plan notes listed
in it.

One remaining solution might be to get more aggressive with the tagging
feature, and see if I can create a more organized system using that. I might be
able to tag each note with a month/year, and then truncate my log notes each
month. The only problem with this is that it doesn't seem like I can select
*multiple* tags at a time, which would mean *all* of my notes for a month
will be shown under the tag. That would be a deal breaker for me :( .

## Conclusion

In summary, I think that Joplin *is* a great open source notes solution.  If
someone needs a system to keep a bunch of normal notes synced across all their
devices, this is it. I however, might need to try out something else long-term.
On the bright side, there are a bunch of features in Joplin that love and will
definitely look for... in my next solution.


