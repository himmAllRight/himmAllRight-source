+++
title   = "Leaving Notion"
date    = "2021-05-16"
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

I'll go through these quickly, as many of them echo my [original notion
post](/post/trying-notion/)...

### Easy to use and setup. 
I can have it easily configured on all my devices. I just by install the app and
log in. I even have the option to access it in a web browser, if I cannot
install it on a device.

### The flexibility
As described in the *Background* section above, the flexibility of Notion really
allowed me to customize it to whatever I needed. It wasn't as much of a system
itself, as much as it was a tool that let me build my *own* system (much like
what I've experience with emacs org-mode in the past).

### Templates. 
With such a malleable system, it helps if the more intricate components can be
automated and simplified with templates. Luckily, the template system in Notion
was very powerful, and is what really allowed me to build  up my own system. My
commonly setup items were all templated to save me time when entering new items
into my system. Without them, Notion would have been a giant pain to maintain.

### All my thoughts and ideas can be linked. 
I loved being able to link everything together. Being able to see all the tasks
linked to a project, and all of the associated notes of the project from a
dashboard was game changing in how I think about organizing my goals, plans, and
notes in a system. For example, I planned out monthly goals and linked each
tasks to them, so at the end of the month, I was able to go back and see
*exactly* if and when I had completed each task for that goal.


## What I didn't like about Notion

### Availability to data relies on their servers being available
Notion is completely hosted online. While this can be *convenient*, Notion also
does not currently have a viable solution for [working
offline](https://www.notion.so/How-can-I-use-Notion-offline-de55148f97c84de3b6e71aa058906be4).
This means that if the Notion service goes down... I can't access *anything.

Because I use notion for my tasks, notes, and everything else, it meant if it
went down, I couldn't even check what I had TODOs I had recorded for the day, or
quickly jot a note down about something I was working on. I had to record
everything somewhere, and go back and transfer it into Notion whenever the
service came back up. While *the service* didn't go down often, this problem
would also happen whenever my internet went out, or I was traveling and didn't
have a connection. Combined, this meant I faced this issue often enough to be
annoyed/concerned by it.

### Access to the data

<center>
<a href="../../img/posts/leaving-notion/exporting_data.png"><img alt="Exporting Notion Data" src="../../img/posts/leaving-notion/exporting_data.png" style="max-width: 100%;"/></a>
<div class="caption">Exporting Notion Data</div>
</center>

A similar issue to everything being hosted by Notion, is that all of the data
and content is controlled by Notion, and in a non-standard format. This means
any important data-related responsibility fall's entirely on their shoulders,
and I have to accept whatever level of security they want to do.

While data security is very important, the problem that most concerns me is that
all the data is in a non-standard format in the databases. While the page
content is in markdown-ish format, the only way to see everything organized
properly in the databases (without hassle, as far as I know), is in notion.
There are no raw files I can easily view or convert. They have an exporting
system, but every time I tried to use it, it froze. I tried this on several
computers, many times, and with both export types available to me. So even while
in theory you *can* export everything to `md`... I couldn't.

What has me most concerned about this data formatting, is that if Notion every
disbands as a company, or is acquired by a company that slowly shifts their
direction over time (or honestly, if Notion themselves shift how they work over
time)... I'm stuck. If I want to move to a different system, I can't easily
reformat/import my data into a new system either. This reason alone has been a
hesitancy in the back of my head, my entire time using Notion.

<center>
<a href="../../img/posts/leaving-notion/export_in_obsidian.png"><img alt="Exported data in Obsidian" src="../../img/posts/leaving-notion/export_in_obsidian.png" style="max-width: 100%;"/></a>
<div class="caption">Exported Notion Data in Obsidian Notes</div>
</center>

**Update**: So while taking screenshots, I tried again to export the data, and
this time it made it all the way through successfully. I was able to then take the data and run it through the [Notion-to-Obsidian-Converter script](https://github.com/connertennery/Notion-to-Obsidian-Converter) (spoiler for what I'm using now 😆), and then import it into a notion vault. While this is nice to have as an archive, by default it isn't very useful in how it's formatted. This is partly due to how I've organized by Notion notes, but still... it's just a bunch of linked items, that I am not really even sure how it's linked.

### Buggy Issues, particularly with templates

<center>
<a href="../../img/posts/leaving-notion/templates.png"><img alt="My Notion templates" src="../../img/posts/leaving-notion/templates.png" style="max-width: 100%;"/></a>
<div class="caption">My Notion templates when creating a new page</div>
</center>

The problem that ultimate pushed me to the edge, making me actually decide to
switch away from Notion, was just the annoying bugs glitches I kept
experiencing. Unfortunately, some of my favorite features, were the ones that
seemed the buggiest and most often game me problems

For example, there were many times when templates just didn't seem not to work.
I would create a new item and apply a template... but the template content would
*not* load. This was an issue I experienced very frequently. Considering how
much I relied on templates, I would have to either wait till a later time when
it would work again, or manually setup everything. Neither of these choices were
very *productive*.

The last straw prompting me to switch occurred at the end of one week not too
long ago. I noticed mid-week that all of the database links for each item that
week (linking tasks to their projects, or even the link for what *area* a task
belonged to (ex: health, home, learning)... were missing. Nothing was linked. 
  
 Normally, this linking is set automatically with the templates, so I chalked it
 up template issues, *again*, and manually connected everything. At the end of
 the week, on a Friday I had off from work, I sat down to plan out my vacation
 day and noticed that the items weren't linked *again*. So, I spent the rest of
 my vacation day researching alternatives for Notion. (and trying to export my
 data... but I already stated how that went 😖).

## Conclusion

<center>
<a href="../../img/posts/leaving-notion/task_board.png"><img alt="Notion task board" src="../../img/posts/leaving-notion/task_board.png" style="max-width: 100%;"/></a>
<div class="caption">My Notion Task Board</div>
</center>

So in conclusion, I think Notion is a great product, but with a  few trade-offs.
I recognize that many of the items that I feel strongly about, won't be concerns
for others. In fact, I was able to overlook many of them *because* of how great

Over the past year however, my concerns about access to the data have really
been nagging in the back of my mind. Every day that passed, I felt the guilt of
having an ever-growing collection of notes that was equally growing in how
painful it would be to loose/convert if I switched away from Notion. On top of
that, every time I experienced issues with my templates. I wanted to switch
away from Notion. So now I am.

It's been a great year using a great tool. Notion is an excellent tool if you
can manage not always having access to it, and if you are okay with the chance
it might all be lost/go away someday. But for my planning and note system, I
just can't afford to use something that give me ownership of the standardized
raw files it uses.
