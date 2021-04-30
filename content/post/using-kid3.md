+++
title   = "Using kid3 Audio Tag Editor"
date    = "2021-04-30"
author  = "Ryan Himmelwright"
image   = "img/posts/using-kid3/dunes_trail_header.jpeg"
caption = "Jockey's Ridge Stage Park, Nags Head, NC"
tags    = ["Application", "filesystem", "open source", "audio"]
draft   = "True"
Comments = "True"
+++

A few months ago, I set out to finally clean up and organize my music library.
My goal was to get rid of all the random files, and ensure that every item was
properly tagged so that it would accurately self-organize in the music players I
use. This would not have been possible without the open source tool,
[kid3](https://kid3.kde.org).

<!--more-->

## The Problem

In order to clean up my music library, I needed a method to edit the metadata
tags of the files. Music applications use these tags to grab information about a
song. For example, a song's title, artist, album name, and release year are all
contained in the a music file's tags.  Using this information, a music
player is able to organize and sort the music by artist, album, year, genre, or
by any other bit of data it knows.

In the past, I used a tool called `easytag` to edit the metadata of my files.
However, after not being able to initially find it (I had the wrong name 😆), I
started to look for a new tool. I desired something easy to use, as I did not
want to waste a bunch of time learning a complicated new tool. After very
little searching, I found [kid3](https://kid3.kde.org).

## Kid3

<center>
<a href="../../img/posts/using-kid3/kid3.png"><img alt="kid3 window" src="../../img/posts/using-kid3/kid3.png" style="max-width: 100%;"/></a>
<div class="caption">kid3 window</div>
</center>

As a [Fedora Plasma](https://spins.fedoraproject.org/kde/) user, I was happy to
learn that kid3 appears to be maintained directly by the KDE team.  To use kid3,
just drag and drop the files into it, add/edit any of the tag info, and save.
New tags can also be added if they aren't listed.

I started using kid3 on my Linux desktop, but one night wanted to work in the
other room on my macBook. I sadly assumed I would have to find a different tool
to use on macOS. However, while searching a new tool, I learned that kid3 has a
macOS build! In fact, in addition to Linux, the KDE team has official kid3
builds for macOS, Windows, and Android! I love a good cross-platform tool.


## Efficiently Editing Album Tags

<center>
<a href="../../img/posts/using-kid3/multi-edit.png"><img alt="Editing multiple files in kid3" src="../../img/posts/using-kid3/multi-edit.png" style="max-width: 100%;"/></a>
<div class="caption">Editing multiple files in kid3</div>
</center>

After using kid3 it for a bit, I fell into a workflow that made the tedious task
of grouping multiple files into single albums easier do. In particular, I
learned that I could select multiple files, and edit a field to apply to all of
the selected items at one time.  Using this technique, I was able to write the
artist, album, and year only once, instead of 10+ times for each album. This
made it *much more* efficient than methods I had previously used while editing
metadata.

### Conclusion

<center>
<a href="../../img/posts/using-kid3/tagged_music.png"><img alt="A custom album tagged in kid3" src="../../img/posts/using-kid3/tagged_music.png" style="max-width: 100%;"/></a>
<div class="caption">A 'home-made' file tagged in kid3, now properly sorted in my music player</div>
</center>

That's all I have. This was a short post, but I think it was worth it. I love
when I find a great open source, cross platform tool that does *exactly* what I
need. Kid3 is a gem application. If you need to edit some audio
tags, check it out. It certainly made my life much easier 🙂.