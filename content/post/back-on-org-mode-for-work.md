+++
title  = "Back On org-mode For Work"
date   = "2019-08-04"
author = "Ryan Himmelwright"
image  = "img/posts/back-on-org-mode-for-work/eno-rocks.jpg"
caption= "Eno State Park, Durham NC"
tags   = ["Linux", "Notes", "Organization", "Applications",]
draft  = "True"
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
links. Additionaly, being formated in markdown, the note contents can be easily
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
Emacs' org-mode by comparison allows for more of a `log-style` note-taking.
This is due to it being very *task* oriented. It encourages outline
organization of notes, allowing "tasks" to be collapsed in a hierarchical
fashion. These items can be marked as "TODO" or "DONE" using the built in todo
system, or tagged. While org-mode can be used to take "normal" style notes, it
really shines when working in a task or outline based structure.

#### Quick Notes, Keybinds

<a href='../../img/posts/back-on-org-mode-for-work/note-demo.gif'>
<img alt="Demonstration of logging a quick note." src="../../img/posts/back-on-org-mode-for-work/note-demo-pre.png" onmouseover="this.src='../../img/posts/back-on-org-mode-for-work/note-demo.gif'" onmouseout="this.src='../../img/posts/back-on-org-mode-for-work/note-demo-pre.png'" style="max-width: 100%;"/>
</a>
<div class="caption">Notes and code blocks can be easily added using
key-binding shortcuts.</div>

Another feature of org mode is it's note drawer. By pressing a particular key
combination (as one tends to do in Emacs), a new buffer will open up to take a
note in. I can write text, or even add a code snippet (if I really want, I can
write the code snippet *in the mode of that language* When done, I can simply
press `C-c C-c`, and the buffer will close, inserting my note under a
time-stamped entry as part of the `logbook` item I started the note in.

This quick logging feature, along with the power of all the key-binding
customization, makes logging and take notes fast, efficient, and enjoyable.

#### Todo/SCRUM Board tasks

<a href="/img/posts/back-on-org-mode-for-work/scrum-board.png">
<img alt="Joplin Android GUI" src="/img/posts/back-on-org-mode-for-work/scrum-board.png" style="max-width: 100%;"/></a>
<div class="caption">I wrote a package that lets me view org tasks in a
scrum board.</div>

As mentioned, org-mode has a powerful [todo]() system. Users can configure how
they want to group the task items, beyond just a basic `TODO`/`DONE`. Using
this flexability (and some lisp knowledge), I wrote myself an [org-mode scrum
board](https://github.com/himmAllRight/ry-org-scrum) generator. This package
takes all of my various `TODO` items, and organizes them into scrum task board.
Again, making org-mode great for task tracking and logging workflows.

#### Exporting/Archiving Weekly Logs
Lastly, the big "feature" org mode has that I find to be missing in Joplin is
the ability to better organize long-term sets of notes. With a logging style of
note-taking, notes can often be organized by a range in time. For example,
week, month, and years. Naturally, these systems are hierarchical and Joplin's
notebook/note organization only truely allows for note systems to be 2 levels
deep. Being text files in a traditional filesystem however, org-mode can better
organize this data, allowing it to be more maintainable over time.

Additionally, org files can be linked, so everything can still be quickly
navigated, even if it spans hundreds of note files over several years.

## Home vs Work Notes

Now with some of each note system's features broken down, how do they
contribute to my preference across different note environments (personal vs.
work).

#### Home
<a href="/img/posts/back-on-org-mode-for-work/joplin-travel-notes.jpg">
<img alt="Joplin Android GUI" src="/img/posts/back-on-org-mode-for-work/joplin-travel-notes.jpg" style="max-width: 100%; width: 350px; float: right; padding: 15px 0px 10px 20px"/></a>

My personal notes tend to be organized as more traditional notes. I make large
groups, such as 'Home', 'Tech', 'Travel', and stash notes into each. In a note,
I tend to organize information on a topic and store it for later. For example,
I may have a notebook for online classes, and then a note for each class where
I jot stuff down as I progress.

For another example, I have a notebook called 'Travel' which contains a note for
each trip I plan to take.  In the note, can store information I need to
remember, such as flight numbers, or hotel addresses. Below, I then store other
information while planning and researching before leaving. This may include
places to to eat, or activities I want to do (with links to the websites).

Joplin's mobile platform support is particularly useful here, as I am able to
write up notes on my desktop, and then read the notes from my phone on the go.

#### Work

By contrast, my work notes tend to be a mix of task-list and logbook for each
week. Each week and day are planned out by moving `TODO` tasks from one day to
the next, and changing the status as I work on each one. As I work, I log notes
under each task about my progress, as well as any issues/solutions I experience
on the way. While the notes are mostly rambeling, logging thoughts as I work
often helps me quickly identify issues, and figure out solutions.

<a href="/img/posts/back-on-org-mode-for-work/exported-notes.png">
<img alt="My notes exported as linked html pages" src="/img/posts/back-on-org-mode-for-work/exported-notes.png" style="max-width: 100%;"/></a>
<div class="caption">The index page of my exported weekly work notes.</div>

Most importantly, due to organizing notes by *week* rather than topic, it is
best if I can archive the notes in more of a tree layout. Org notes are plain
text files, so I can save them on my hard drive any way I want, which allows me
to organize the notes as `/work/archive/YEAR/MONTH/week-of{date}.org`.
Additionally, I can export the notes to linked html files, which is very
useful for going back and looking at my previous notes, which I require with my
work flow.


### Conclusion

So that's about it. I've switched back to emacs org-notes for my work notes...
but remain using Joplin for my personal and home notes. So far... I'm loving
it. I think that I switched to joplin because org-mode wasn't ideal for my
personal notes. However, it turned out that it was lacking for my work
notes. That's okay. It turns out that those two use cases are completely
different, and as such work best using different tools.

So, moving forward, I plan to keep using Joplin for my personal notes, and
emacs org-mode for my work notes. Perfect.
