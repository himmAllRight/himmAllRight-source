+++
title   = "Leaving Notion"
date    = "2021-05-20"
author  = "Ryan Himmelwright"
image   = "img/posts/leaving-notion/obx_pipe_algae.jpeg"
caption = "Kill Devil Hills, NC"
tags    = ["Application", "Organization", "Notes"]
draft   = "True"
Comments = "True"
+++

After using [Notion](https://notion.so) for my notes and daily planning over
the [last year](/post/trying-notion/), there are a few issues with it that have
worn on me.  Over time, my uneasiness with the application has built up to the
point where I have decided to switch away Notion completely. Here's why.

<!--more-->

## Background

<center>
<a href="../../img/posts/leaving-notion/dahsboard.png"><img alt="my notion dashboard" src="../../img/posts/leaving-notion/dashboard.png" style="max-width: 100%;"/></a>
<div class="caption">My Notion Dashboard Page</div>
</center>

Before getting into it, I want to state that for the most part, I have *loved*
using Notion. It took a few iterations of figuring out how I wanted everything
organized, but after my most recent system overhaul, I have it arranged perfectly.

In have everything stored in a handful of databases: Areas, Projects, Tasks, and
Notes.  The items in each of these DBs are then all connected together. For
example, *tasks* and *notes* are usually linked in a
*project*, which is all associated with a particular *area* (`Home`, `Learning`,
*`Social`, and so on).

In the most recent iteration, I moved away from linking tasks to a daily journal
object. Instead, I assigned *everything* a date, and created dashboard pages
with date filters to see the *Weekly* and *Daily* boards of my tasks.  All in
all, it was a remarkably efficient system... except for when it wasn't... 


## What I liked about Notion

<center>
<a href="../../img/posts/leaving-notion/project_tasks.png"><img alt="My tasks of a goal" src="../../img/posts/leaving-notion/project_tasks.png" style="max-width: 100%;"/></a>
<div class="caption">My tasks in a goal project</div>
</center>

I'll run through these quickly, as many of the statements echo my [original
notion post](/post/trying-notion/)...

### Easy to use and setup
I can have Notion easily configured on *all* my devices. All I have to do for
setup, is install the app and log in. I even have the option to access it in a
web browser, if I cannot install it as an app on a device.

### The flexibility
As described in the *Background* section above, the flexibility of Notion 
allowed me to tailor it to whatever I needed. Notion wasn't as much of a
*system* itself, as much as it was a *tool* that let me build my *own* system.
It felt like a modern evolution of emacs org-mode, which is a good thing.

### Templates
With such a malleable system, it helps when the more intricate components can be
automated and simplified. Luckily, Notion has a template system, which is what
really allowed me to custom system *usable*. My frequent tasks were all
templated to save me time when entering them into the system. Without them,
Notion would have been a giant pain to maintain.

### Everything can be linked
I loved being able to link everything together. Seeing all the associated tasks
and notes of a project in a dashboard was game changing for how I think about
organizing information in a system. As an example, I would plan out monthly
goals and link each task to it. This way, at the end of a month I was able
to go back and see *exactly* if and when I had completed each task for that
goal.


## What I didn't like about Notion

### Requires Notion Servers Being Available
Notion is completely hosted online and does not have a current solution for
[working
offline](https://www.notion.so/How-can-I-use-Notion-offline-de55148f97c84de3b6e71aa058906be4).
While this can be *convienient*, as I don't have to worry about syncing data, it
does mean that if the Notion service goes down... I can't access *anything*.

I used Notion for my tasks, notes, and everything else. When it went down, I
couldn't even do basic things like check my TODO list, or jot down a quick note
in my system. I had to record everything elsewhere, and then go back later to
transfer it into Notion *after* the service was available. While *the service*
didn't go down often, I still faced this problem whenever *my* internet went
out, or I was traveling and didn't have a connection. Combined, this happened
often enough to be annoyed by it.

### Access to the data

<center>
<a href="../../img/posts/leaving-notion/exporting_data.png"><img alt="Exporting Notion Data" src="../../img/posts/leaving-notion/exporting_data.png" style="max-width: 100%;"/></a>
<div class="caption">Exporting Notion Data</div>
</center>

On a similar note, all of the data and content resides in Notion servers, and in
a non-standard format. As a result, any important data-related responsibility
fall's entirely on their shoulders, and I have to accept whatever level of
security the do, or fail to do.

While data security is very important, my biggest concern is that all of the
database data is in a non-standard format. The page content is in markdown-ish,
but the only way to view everything organized properly in the databases (without
hassle, as far as I know), is within Notion.  There are no raw files I can
easily open or convert. They have an exporting system, but every time I tried to
use it, it froze. So even while in theory you *can* export everything to `md`
and `csv` files...  I couldn't. (*Update on this below*)

In particular, I am most worried about data formatting. If Notion ever disbands
as a company, or is acquired by a company that slowly shifts direction (or
honestly, if Notion themselves shift the product over time)... I'm stuck. If I
want to move to a different system, I can't easily reformat/import the data into
a new system. This alone has been a nagging hesitancy in the back of my head,
the entire time I've used Notion.

<center>
<a href="../../img/posts/leaving-notion/export_in_obsidian.png"><img alt="Exported data in Obsidian" src="../../img/posts/leaving-notion/export_in_obsidian.png" style="max-width: 100%;"/></a>
<div class="caption">Exported Notion Data in Obsidian Notes</div>
</center>

**Update**: 

So while taking screenshots, I tried again to export the data. This time, it
made it all the way through the process successfully. I was then able to take
the data and run it through the [Notion-to-Obsidian-Converter
script](https://github.com/connertennery/Notion-to-Obsidian-Converter) (spoiler
for what I'm using now 😆), and import it into an Obsidian vault. While this is
nice to have as an archive, by default it isn't useful in how it's formatted and
would be a lot of work to truly convert all the data. This is mostly due to how
I've organized by Notion notes, but still... it is a mess and I don't even know
where to begin in understanding it.

### Buggy Issues. Particularly With Templates

<center>
<a href="../../img/posts/leaving-notion/templates.png"><img alt="My Notion templates" src="../../img/posts/leaving-notion/templates.png" style="max-width: 100%;"/></a>
<div class="caption">My Notion templates when creating a new page</div>
</center>

Lastly, problem that ultimate pushed me to the edge, confirming my decision to
switch away from Notion, was the annoying bugs and glitches I kept experiencing.
Unfortunately, some of my favorite features of Notion, were also my biggest
obstacles.

For example, there were many times when templates just did not work.  I would
create a new item and apply a template... but the content would
*not* load. This was an issue I experienced very frequently. Considering how
much I relied on templates, I would have to either wait till a later time when
it would work again, or manually setup everything. Neither of these choices were
*productive*.

The last straw, inciting action to switch, happened at the end of a week not too
long ago. I noticed mid-week, that all of the database links for my week's items
(linking tasks to their projects, or even the link for what *area* a task
belonged to (ex: health, home, learning))... were missing. Nothing was connected. 
  
 Normally, this is set automatically with the templates, so I chalked it up to
 template issues, *again*, and manually connected everything. That Friday, I had
 off from work, so I sat down to plan out my vacation day. I quickly noticed
 that the items weren't linked... *again*. That was enough. I spent the rest of
 my vacation day researching alternatives for Notion. (and trying to export my
 data... but I already stated how that went 😖).

## Conclusion

<center>
<a href="../../img/posts/leaving-notion/task_board.png"><img alt="Notion task board" src="../../img/posts/leaving-notion/task_board.png" style="max-width: 100%;"/></a>
<div class="caption">My Notion Task Board</div>
</center>

I think Notion is a great product, but with a few trade-offs.  I recognize that
many of the items that I feel strongly about, won't be concerns for others. In
fact, I was able to overlook many of them *because* of how great of a tool it
was.

Over the past year however, my concerns about access to the data have really
been nagging in the back of my mind. Every day that passed, I felt the guilt of
having an ever-growing collection of notes that was equally growing in how
painful it would be to loose/convert if I switched away from Notion. On top of
that, every time I experienced issues with my templates, I wanted to switch
away from Notion. So now I finally have.

It's been a great year using a great tool. Notion is an excellent tool if you
can manage not always having access to it, and if you are okay with the chance
it might all go away someday. But for my planning and notes system, I just can't
afford to use something that doesn't give me ownership of the standardized raw
files it uses.
