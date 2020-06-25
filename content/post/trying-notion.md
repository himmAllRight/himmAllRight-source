+++
title   = "Trying out Notion"
date    = "2020-06-26"
author  = "Ryan Himmelwright"
image   = "img/posts/trying-notion/journals.jpeg"
tags    = ["notes","organization", "applications",]
draft   = "True"
Comments = "True"
+++

The past year or two has been a whirlwind of trying various notes and planning
systems. I started by attempting to switch everything to [joplin
notes](/post/switched-to-joplin-notes/) only to switch [back to org-mode for my
work notes](/post/back-on-org-mode-for-work/) a few months later. Around that
same time, I also started using [trello](https://trello.com) to organize my
personal and home life into task boards. This system worked well, but felt very
disjointed, spreading my notes, goals, and tasks all over the place. However, that all might
be able to change, as I've started using [Notion](https://notion.so).

<!--more-->

## Quick History

Before diving into my experience with Notion, lets first describe the system
I'm coming from, highlighting some of it features and pitfalls.

### Previous System

<a href="/img/posts/trying-notion/trello_weekly_board.png">
<img alt="Trello Weekly Board" src="/img/posts/trying-notion/trello_weekly_board.png" style="max-width: 100%;"/></a>
<div class="caption">My Trello Weekly Task Board</div>

Most recently, personal and professional notes & task planning system consisted
of three applications: Trello, Emacs (org-mode), and Joplin. They broke down as
follows:

**Trello**: I had several boards for planning my weekly, monthly, and
quarterly personal and home tasks.I also had a few boards to keep track of
projects ideas (for example, post ideas, books to read, online courses to take,
etc).


**Emacs org-mode**: I continued to use emacs org-mode for basically all the
things I just said I used trello for... but for my professional work life.
During my day job, I like to break my work down into tasks, and often logs
quick thoughts and notes under each task while I am doing it. While I could log
notes into Trello cards, it wasn't nearly as easy to open up and record stream
of consciousness as it is in org mode.

**Joplin**: I previously attempted to make Joplin my universal planning system,
but it failed. It was a bit too messy for my goal and task planning compared to
something like Trello or even org mode (with my
[ry-org-scrum](https://github.com/himmAllRight/ry-org-scrum) package installed
;) ). However, it was a great cross-platform notes application... so I've been
using it for that. Any personal or work 'note' that isn't directly related to a
single card or task has been stored in Joplin.

### Issues with system

<a href="/img/posts/back-on-org-mode-for-work/scrum-board.png">
<img alt="Joplin Android GUI" src="/img/posts/back-on-org-mode-for-work/scrum-board.png" style="max-width: 100%;"/></a>
<div class="caption">I love emacs and org mode... but it really isn't an option
on mobile OSes</div>

While this system has *worked* for a bit now, it does have it's issues.

#### Couldn't share items across systems
The biggest issue I had with this system was that it was made from several
disconnected systems. This meant that my notes and information were spread all
over the place. I tried to keep notes and task 'logs' separate, but I started
to fine that while working on projects, I wanted to create a longer, organized,
reference 'note' about a subject.

The biggest problem with seperate systems was that once I split information, I
wasn't able to link it. If the genesis of a note spurred from logs I took
working on a task, it would be conceivable that the two should be linked. With
seperate systems however, this wasn't easy and even if implemented was messy.


#### Have to setup everything on every device

*(I know this complaint is a very minor one. But when thinking of my systems, I
want to make them better, even if that means finding even the slightest rough
edge to smooth out)*

Another issue using multiple systems was that *all three* had to be setup and
configured, *on every device*. While I have [automated my emacs
setup](http://ryan.himmelwright.net/post/org-babel-setup/), both joplin and
emacs required me configuring their sync solution, every time.

On the surface, Trello's setup makes it appear as though I wouldn't have this
setup issue if I used 3 web apps. Just login. Sure, but even then having to log
into multiple apps during the setup of a new device is a pain, especially
because this is usually done while trying to also login to *everything else*.
On a computer it isn't that bad... but on a phone...

Additional, I tend to make many of my most used web-apps into fake desktop apps
using [Nativefier](https://github.com/jiahaog/nativefier). Which yes, would
mean 3x nativefier setups even if it was all webapps.


#### Not accessible outside my systems

Lastly, my main issue was that apart from Trello, these systems weren't really
accessable from devices beside my own. In addition, Emacs wasn't even available
on my mobile devices. While good from a security standpoint, I don't like
having all my notes and information only available when I sit down at a
desktop. If I'm working on a family member's machine, or helping configure
something elsewhere, I want to be able to access my notes on my phone, or even
a private browser tab on their machine.

### Desires

With these issues defined, what is it that I actually want to see in my note
taking and task organization system?

<a href="/img/posts/back-on-org-mode-for-work/joplin-gui.png">
<img alt="Joplin GUI" src="/img/posts/back-on-org-mode-for-work/joplin-gui.png" style="max-width: 100%;"/></a>
<div class="caption">Joplin Notes</div>

- **Consolidated into one system**: I don't want to have to setup multiple apps
    and logins on all my systems.
- **Cross platform (mobile too)**: Despite only wanting once system, I want it
    supported on all my devices, including mobile.
- **Kanban board support**: I really enjoy moving and displaying  my task items
    in a board view.
- **Normal notes too**: In addition to task cards, I also want support for
    traditional, long-form permanent notes. Ideally tasks *can* be linked to
    notes, but the notes don't *have* to be task-bound.
- **Easy to jump in, add a log note, and get out**: Lastly is a feature that
    I love in org-mode. I want to be able to quickly jump into a note, hit a
    keyboard shortcut to drop in a timestamp, and take a quick log note.

## Notion
<a href="/img/posts/trying-notion/notion_window.png">
<img alt="Notion in iOS" src="/img/posts/trying-notion/notion_window.png" style="max-width: 100%;"/></a>
<div class="caption">Notion window in macOS, displaying my page for this page. The UI looks the same on the web and in my 'Nativfier' app in Linux.</div>

### What I like so far
- FLEXIBLE
<a href="/img/posts/trying-notion/now_timestamp.png">
<img alt="logging using @now" src="/img/posts/trying-notion/now_timestamp.png" style="max-width: 100%;"/></a>
<div class="caption">Easy logging using `@now`</div>
- Easy logging using `@now` (like I had in org-mode)
*Picture of Notion - Database (list + Dashboard views?)*
- Databases
    - Multiple views of same data
    - Linkable
- Templates



<a href="/img/posts/trying-notion/ios_notion.png">
<img alt="Notion in iOS" src="/img/posts/trying-notion/ios_notion.png" style="max-width: 100%;"/></a>
<div class="caption">Notion views in iOS. Navigation, my 'Areas' card views,
daily log page properties, and a task 'board' view.</div>


- Have it on all my devices, or online
- Free trial, and affordable for pro -- updated. Free for personal :)

### Downsides/Concerns

*Picture of Notion -- Something confusing?, or maybe export options*

- All my eggs in one basket/not open or hosted (but neither was trello)
- Can take a bit of time to learn how to best use it (but hey, I'm coming
    mostly from emacs XD )
- Cost for pro (that could raise in price) (but technically was trello, I just
    didn't think it was worth it since it only did part of what I needed. Also,
    my hosting for joplin notes was being provided by a service I pay for
    [fastmail], which I happened to already use for something else.)
- No command-line client (Honestly for this type of system, it's less and less
    important for me, especially if there is a webapp. I tend to not run my
    laptops without xorg or a windowing system anymore.

## Conclusion
