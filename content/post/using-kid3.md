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

Over the past few months, I have set out on the task of cleaning up and
organizing my Music library. My goal was to get rid of all the random files,
and ensure that every item had the proper metadata so that it would
self-organize properly in the various music players I use. This task, would
not have been possible without the amazing open source (and cross-platform!)
tool, [kid3](https://kid3.kde.org).

<!--more-->

## The Problem

*Maybe example of messy files/poorly tagged ones in music library?*

In order to properly clean up the files in my music library, I needed a way to
edit the metadata tags of the files themselves. Music applications use these
tags grab a information about a song, like it's title, artist, album, ect from
the file. With this information, they are able to organize and sort everything
by artist, album, year, genre, or by any other bit of data.

In the past, I had used a tool called eztag to edit the metadata of my files.
However, when I quickly searched the Fedora repos, it didn't turn up. So, I
started to look for a new tool. Ideally, I needed something that would be easy
to learn, as I didn't want to spend a bunch of time learning a complicated new
tool. After very minimal searching, I found [kid3](https://kid3.kde.org).

## Kid3

*Screenshot of kid3?*

As a [Fedora Plasma](https://spins.fedoraproject.org/kde/) use, I was happy to
learn that kid3 appears to actually be made by the KDE team. It is an application that I think I had used before, but I didn't realize how easy it actually was to use. To use, you can just drag and drop the files into it, and then add/edit any of the data in the tags, and save. New tags can even be added if they don't exist.

I started using kid3 on my Linux desktop, but one night wanted to work in the
other room on my macBook, and thought that I would probably have to find a
different tool to use on macOS. While searching for tools, I learned that kid3
actually has a macOS build! In fact, in addition to Linux, the KDE team has
official kid3 builds for macOS, Windows, and Android! I love when a good tool is truly cross-platform.

## Efficiently Editing Album Tags

*screenshot of editing multiple files at once*

After using kid3 it for a bit, I fell into a workflow that made the tedious task
of editing multiple files into a single album easier do. In particular, I
learned that I could select multiple files, and edited a field for all of the
selected items at one time.  Using this technique, I was able to write the
artist, album, and year only once, instead of 10+ times for each album. This
made it *much more* efficient than methods I had previously used while editing
metadata.

### Conclusion

*Screenshot showing my cleaned library*

That's it. This was a short post, but I think it was worth it. I love when I find a great open source, cross platform tool that does *exactly* what I need. Kid3 is one of those gems applications. If you need to edit some audio tags, check it out. It certainly made my life much easier 🙂.