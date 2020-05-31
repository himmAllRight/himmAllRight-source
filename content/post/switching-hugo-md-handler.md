+++
title   = "Switching Hugo's Markdown Handler"
date    = "2020-05-31"
author  = "Ryan Himmelwright"
image   = "img/posts/switching-hugo-md-handler/duke-park-sky.jpeg"
caption = "Duke Park, Durham NC"
tags    = ["hugo","website", "markdown",]
draft   = "False"
Comments = "True"
+++

While writing my [previous post](/post/rx580-upgrade/), I hit a frustrating
issue. After saving a large chunk of the draft, it appeared that hugo wasn't
rendering the new additions. I verified on several computers, including fresh
installs. None of them  would generate the updated post, despite the source
files containing the changes. Ugh.

<!--more-->

### The Actual Issue

When I first noticed the problem, I *though* hugo wasn't rendering *any* of my
recent changes, which consisted of adding some images and a paragraph or two.
However, after inspecting the page in greater detail, I did see that the
updated text *was* present. Only the images were missing.

With this information, I was able to search for a solution.
After spending a few minutes reading some irrelevant stackoverflow
posts, I eventually found [this wonderful blog
post](https://jdhao.github.io/2019/12/29/hugo_html_not_shown/). The problem it
described matched my issue exactly.

It explained that recent versions of [hugo](https://gohugo.io) had switched
from using [blackfriday](https://github.com/russross/blackfriday) to
[goldmark](https://github.com/yuin/goldmark/), to render the markdown content.
Unlike blackfriday, by default goldmark does not render raw html tags.  I use
raw html to define the images in my post, and thus they were no longer
rendering.

### A Simple Solution

The post offered two solutions to fix the problem. For now, I just applied the
easier of the two: reverting back to blackfriday to render my markdown.  To
make the switch, I added the following line to my `config.toml`:

```toml
[markup]
  defaultMarkdownHandler = "blackfriday"
```

The alternative solution, is to override goldmark's default setting and allow
raw html tag rendering. This can be accomplished by instead adding these lines
to the `config.toml`:

```toml
[markup]
  defaultMarkdownHandler = "goldmark"
  [markup.goldmark]
    [markup.goldmark.renderer]
      unsafe = true
```

I'm sure that the hugo team had valid reasons for the switch. With that said,
until I have time to read up on those reasons, and to verify that goldmark
doesn't break rendering anything else in my website, I'm going to stick with
blackfriday.

### Conclusion

With that change the problem was solved. While the solution was easy, it
took a few days of head banging to figure out exactly what was happening.
Hopefully this post will help others figure out the fix quicker than I did. Or,
at the very least... it will remind me what I did when I eventually switch to
goldmark.

