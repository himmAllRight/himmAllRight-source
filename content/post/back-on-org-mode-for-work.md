+++
title  = "Back On org-mode For Work"
date   = "2019-08-07"
author = "Ryan Himmelwright"
image  = "img/posts/back-on-org-mode-for-work/eno-rocks.jpg"
caption= "Eno State Park, Durham NC"
tags   = ["Linux", "Notes", "Organization", "Applications",]
draft  = "False"
Comments = "True"
+++

Last month, I wrote about my [switch to Joplin](post/switched-to-joplin-notes/)
for both my personal and work notes. While I enjoyed many features in Joplin, I
also had a few concerns about using the system long-term for all my notes.
As of last week, I am still using Joplin for all of my personal notes, but have switched
back to `org-mode` for my notes at work. Why?

<!--more-->

## Use Cases
To better understand why Joplin works well for me at home but can't effectively
replace org-mode at work, lets first list some different features between Joplin and
emacs org-mode.

### Joplin Features
#### "Notes"-Style Focused
<a href="/img/posts/back-on-org-mode-for-work/joplin-gui.png">
<img alt="Joplin GUI" src="/img/posts/back-on-org-mode-for-work/joplin-gui.png" style="max-width: 100%;"/></a>
<div class="caption">Joplin uses a traditional "note" layout, with blank text
boxes organized into notebooks.</div>

Joplin organizes notes in a traditional "notes" style. Each note starts as a
big, blank text-box that the user fills in. These notes are further organized
into "notebooks", which are simply a list of one or more notes. The notes are
formatted with markdown, but the application doesn't seem to support features
like collapsible sections.

#### Simple Markdown Format -- Sharable
The markdown editor in Joplin may not support collapsing sections, but it does
a great job at supporting other features, like simple code highlighting and web
links. Additionally, being formated in markdown, the note contents can be easily
exported, transferred, or even shared with other applications and/or people.
This is handy when grabbing snippets from the web, which may already be in a
markdown friendly format.

#### Shared across Computer and Mobile Devices
<a href="/img/posts/back-on-org-mode-for-work/joplin-android.png">
<img alt="Joplin Android GUI" src="/img/posts/back-on-org-mode-for-work/joplin-android.png" style="max-width: 100%;"/></a>
<div class="caption">The Notebook and Notes views on the Android client.</div>

Lastly, the Joplin application is available on all platforms (including
mobile), and manages the system to sync the notes across all devices. This
makes it a breeze to write a note at a computer, and then have it immediately
available on a phone afterwards.

### Org-mode use cases
#### Logging-Style Notes
By comparison, Emacs' org-mode can be very *task* oriented, allowing for a more
'log-style' note-taking system. It encourages outline organization of notes,
organized under "tasks" which can be collapsed in a hierarchy. The
tasks can be marked "TODO" or "DONE" using the built in TODO system, or
tagged for organization. While org-mode can be used when writing "normal" notes, it really
shines when working as a task/note system.

#### Quick Notes, Key-bindings

<a href='../../img/posts/back-on-org-mode-for-work/note-demo.gif'>
<img alt="Demonstration of logging a quick note." src="../../img/posts/back-on-org-mode-for-work/note-demo-pre.png" onmouseover="this.src='../../img/posts/back-on-org-mode-for-work/note-demo.gif'" onmouseout="this.src='../../img/posts/back-on-org-mode-for-work/note-demo-pre.png'" style="max-width: 100%;"/>
</a>
<div class="caption">Notes and code blocks can be easily added using
key-binding shortcuts.</div>

Another feature in org mode is the note drawer. By pressing a key combination
(as one tends to do in Emacs), a new buffer will open up to take a note in. The
contents of the note may be text, or even a code snippet (*in the emacs mode of
that language*). When done, I can simply press `C-c C-c` and the buffer will
close, inserting the note with a time-stamped entry as part of the `logbook`
for the task I opened the note in.

This quick logging feature, along with the power of all the key-binding
customization, makes note logging fast, efficient, and enjoyable.

#### TODO/SCRUM Board tasks

<a href="/img/posts/back-on-org-mode-for-work/scrum-board.png">
<img alt="Joplin Android GUI" src="/img/posts/back-on-org-mode-for-work/scrum-board.png" style="max-width: 100%;"/></a>
<div class="caption">I wrote a package that lets me view org tasks in a
scrum board.</div>

As mentioned, org-mode has a powerful
[todo](https://orgmode.org/manual/TODO-items.html) system. Users can configure
how task items should be grouped beyond just a basic `TODO`/`DONE`. Using this
flexability (and some lisp knowledge), I wrote an [scrum board generator for
org-mode](https://github.com/himmAllRight/ry-org-scrum). This package takes all
of my `TODO` items, and organizes them into scrum task board. This feature
helps organize my daily and weekly task lists.

#### Exporting/Archiving Weekly Logs
The big "feature" org mode has that I find lacking in Joplin, is the
ability to better organize long-term sets of notes. With a logging style of
note-taking, notes are often organized by a specific range in time (day, week,
month). These systems are naturally structured hierarchically and Joplin's notebook/note
organization only allows for systems to be 2 levels deep. However, org files are stored
as text files on a traditional file system.

Lastly, org files can be linked (and exported as html files), so any note can
still be quickly navigated to, even if the archive spans hundreds of note files over
several years.

## Home vs Work Notes

Now with some of each note system's features broken down, how do they
fit with my preferences across different note taking use-cases? (mostly personal vs.
work)

#### Home
<a href="/img/posts/back-on-org-mode-for-work/joplin-travel-notes.jpg">
<img alt="Joplin Android GUI" src="/img/posts/back-on-org-mode-for-work/joplin-travel-notes.jpg" style="max-width: 100%; width: 350px; float: right; padding: 15px 0px 10px 20px"/></a>

My personal notes tend to be organized as more traditional notes. I make large
groups, such as 'Home', 'Tech', 'Travel', and stash notes into each. In a note,
I tend to organize information on a topic and store it for later. For example,
I may have a notebook for online classes, and then a note for each class.

For another example, I have a notebook called 'Travel' which contains a note
for each trip I plan.  In the note, I store information that I will need, such
as flight numbers, or hotel addresses. Below important information, I jot down
ideas while planning and researching before leaving. This may include places to
to eat, or activities I want to do (with links to the websites).

Joplin's mobile platform support is particularly useful here, as I am able to
write up notes on my desktop, and then read them from my phone on the go.

#### Work

By contrast, my work notes are a mix of task-list and logbook for each
week. I plan each week by moving `TODO` tasks from one day to
the next, and changing the status as I work on each one. As I work, I log notes
under each task about my progress, as well as any issues/solutions I experience
on the way. While the notes are mostly rambling, logging thoughts as I work
helps me to quickly identify issues, and solve problems faster.

<a href="/img/posts/back-on-org-mode-for-work/exported-notes.png">
<img alt="My notes exported as linked html pages" src="/img/posts/back-on-org-mode-for-work/exported-notes.png" style="max-width: 100%;"/></a>
<div class="caption">The index page of my exported weekly work notes.</div>

Most importantly, due to organizing notes by *week* rather than topic, it is
best if I can archive the notes in more of a tree layout. Org notes are plain
text files, so I can save them on my hard drive any way I want. For example, I
have my work notes organized as `./work/archive/{YEAR}/{MONTH}{DAY}/week-of-{date}.org`.
Each week, I also export the finished notes to linked html files, which is very
useful for going back and looking at my previous notes.

### Conclusion

That's it. I've switched back to emacs org-notes for my work tasks,
but remain on Joplin for my personal and home notes. So far... I'm loving
it. I think that I switched to Joplin because org-mode wasn't ideal for my
personal notes. However, Joplin was lacking for my work
notes. That's okay. I learned that my home vs. work notes are two completely
different use cases, and as a result should use different tools.

So, moving forward, I plan to keep using Joplin for my personal notes, and
emacs org-mode for my work tasks. Perfect.
