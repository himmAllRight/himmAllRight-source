+++
title   = "Switching Hugo's Markdown Handler"
date    = "2020-05-30"
author  = "Ryan Himmelwright"
image   = "img/posts/switching-hugo-md-handler/duke-park-sky.jpeg"
caption = "Duke Park, Durham NC"
tags    = ["hugo","website", "markdown",]
draft   = "True"
Comments = "True"
+++

While writing the [previous post](/post/rx580-upgrade/), I stumbled on a
frustrating issue. After saving a large chunk of the draft, it appeared that
hugo wasn't rendering the additions. I tried it on several computers, including
fresh installs, and they all suddenly appeared to not render my changes,
despite the files containing the updates.

<!--more-->

### The Actual Issue

When I first noticed the problem, I *though* it wasn't rendering any of my most
recent changes, which consisted of adding some images and a paragraph or two.
After I slowed down and inspected the page in more detail however, I noticed
that the updated text *was* present. Just the images were missing.

With this bit of information, I was able to better search for a solution.
After spending a few minutes reading through some irrelevant stackoverflow.com
posts, I eventually found [this wonderful
post](https://jdhao.github.io/2019/12/29/hugo_html_not_shown/). The problem it
described matched my issue exactly. Basically, recent versions of [hugo]() had
switched from using [blackfriday](https://github.com/russross/blackfriday) to
[goldmark](https://github.com/yuin/goldmark/) to render the markdown content as
html. Unlike blackfriday, goldmark does not render raw html tags by default.
I use raw html to define the images in my post, and thus they didn't render.

### A Simple Solution

The post offered two solutions to fix the problem (both simple). For now, I
just applied the easier of the two: switching back to blackfriday to render my
markdown.  To switch back, I just added the following line to my `config.toml`:

```toml
[markup]
  defaultMarkdownHandler = "blackfriday"
```

The alternative solution, is to override goldmark's default setting, and allow
raw html tag rendering. This can be accomplished by instead adding these lines
to the `config.toml`:

```toml
[markup]
  defaultMarkdownHandler = "goldmark"
  [markup.goldmark]
    [markup.goldmark.renderer]
      unsafe = true
```

I'm sure that the hugo team had valid reasons for the switch, but until I have
time to read up on those reasons, and to verify that goldmark doesn't break
rendering anything else in my website.

### Conclusion

With that change, the problem was solved. While the solution was so easy, it
took a few days of head banging to figure out what was actually happening.
Hopefully this post will help others figure out the fix quicker than I did. At
the very least... it will remind me what I did when I eventually go to switch
to goldmark.

