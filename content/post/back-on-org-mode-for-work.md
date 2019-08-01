+++
title  = "Back On org-mode For Work"
date   = "2019-07-31"
author = "Ryan Himmelwright"
image  = "img/posts/back-on-org-mode-for-work/eno-rocks.jpg"
caption= "Eno State Park, Durham NC"
tags   = ["Linux", "Notes", "Organization", "Applications",]
draft  = "True"
Comments = "True"
+++

Last month, I wrote about my [switch to Joplin](post/switched-to-joplin-notes/)
for my personal and work notes. While there were many features I liked about
the system, I had a few issues which caused concern for using the application
long-term for all my notes. While I am still using Joplin for all of my
personal notes, I have switched back to `org-mode` for my notes at work. Why
have I switched at work, but *not* at home?

<!--more-->

## Use Cases
To better understand why Joplin works well for me at home but not work, lets
first the different features between Joplin and emacs org-mode.

### Joplin Features
#### "Notes"-Style
<a href="/img/posts/back-on-org-mode-for-work/joplin-gui.png">
<img alt="Joplin GUI" src="/img/posts/back-on-org-mode-for-work/joplin-gui.png" style="max-width: 100%;"/></a>
<div class="caption">Joplin uses a traditional "note" layout, with blank text
boxes organized into notebooks.</div>

Joplin organizes notes in a traditional "notes" style. Each note starts as a
big, blank text-box that the user fills in. These notes are further organized
into "notebooks", which is simply a list of one or notes. While the notes are written
in markdown, which allows the user format them in any way, the system doesn't
really support features like collapsible sections or outlines.

#### Simple Markdown Format -- Sharable
The markdown editor in Joplin may not support collapsing sections, but it does
a great job at supporting other features, like simple code highlighting and web
links. Additionaly, being markdown the contents can be easily exported,
transferred, or even shared with other applications and/or people. This is
handy when grabbing snippets from the web, which may already be in a markdown
friendly format.

#### Shared across Computer and Mobile Devices
<a href="/img/posts/back-on-org-mode-for-work/joplin-android.png">
<img alt="Joplin Android GUI" src="/img/posts/back-on-org-mode-for-work/joplin-android.png" style="max-width: 100%;"/></a>
<div class="caption">The Notebook and Notes views on the Android client.</div>

Lastly, the Joplin application is available on all platforms, including mobile.
Furthermore, it syncs the notes across all devices. This makes it easy to take
write some notes at a computer, and then have available on a phone while
traveling.

### Org-mode use cases
#### Logging-Style Notes
Emacs' org-mode by comparison allows for more of a `log-style` note-taking.
This is due to it being very *task* oriented. It encourages outline
organization of notes, allowing "tasks" to be collapsed in a hierarchical
fashion. These items can be marked as "TODO" or "DONE" using the built in todo
system, or tagged. While org-mode can be used to take "normal" style notes, it
really shines when working in a task or outline based structure.

#### Quick Notes, Keybinds
Another feature of org mode is it's note drawer. By pressing a particular key
combination (as one tends to do in Emacs), a new buffer will open up to take a
note in. I can write text, or even add a code snippet (if I really want, I can
write the code snippet *in the mode of that language* When done, I can simply
press `C-c C-c`, and the buffer will close, inserting my note under a
time-stamped entry as part of the `logbook` item I started the note in.

This quick logging feature, along with the power of all the key-binding
customization, makes logging and take notes fast, efficient, and enjoyable.

#### Todo/SCRUM Board tasks


#### Exporting/Archiving Weekly Logs


## Home vs Work Notes
### Home Use Case
#### Various topics which don't pile up a ton over time


### Work Use Case



### Future Plans
