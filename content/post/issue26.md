+++
title  = "Resolving Issue #26"
date   = "2019-12-14"
author = "Ryan Himmelwright"
image  = "img/posts/issue26/lowes-plants-cart.jpeg"
caption= "Lowes, Durham, NC"
tags   = ["website", "hugo"]
draft  = "False"
Comments = "True"
+++

A couple of weeks ago while writing a post, I noticed that for some unknown
reason, my website wasn't rendering correctly. After some back-tracking, I
determined that I had updated the container I work in to at Fedora 31 base, and
the hugo version was newer in it.  So, I filed the problem as [issue
#26](https://github.com/himmAllRight/himmAllRight-source/issues/26), and
finished my post in a Fedora 30 container for the time being.  Here is a quick
explanation of how I *eventually* came back and resolved issue #26.

<!--more-->

### The Problem

<a href="/img/posts/issue26/correct-website-homepage.png">
<img alt="The correct website homepage index" src="/img/posts/issue26/correct-website-homepage.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">What the website homepage is *supposed* to look like</div>

My website has two types of content: *posts*, and *pages*. The *pages* are the
'normal' page content of the website, like the [About](/pages/about/) and
[Homelab](/pages/homelab/) pages. *Posts* are the other hand, are the dated
conent pages I make, like this one you are currently reading. When everything
is working, the hugo template I use takes the newest *x* number of posts from the
*posts* directory, and lists them on the homepage with a small summary. (See
image above)

<a href="/img/posts/issue26/broken-website-homepage.png">
<img alt="What the broken homepage" src="/img/posts/issue26/broken-website-homepage.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">The broken homepage</div>

However, after the `hugo` version in my website container updated from `v0.56.6` and
`v0.58.3`, the post lists on the homepage broke.
Specifically, instead of listing the recent post, the homepage just listed a
single "post" title named...  "Posts" (see image above).

This meant that something changed between those two versions that made my
template out of date. However, I wasn't sure if the problem was in the
website's page content, or if it was from an issue in the template I used.

### Finding a Fix

To find out, I found some other hugo templates and temporarily switched config
to render the website with them. This was actually a bit more complicated than
I thought it would be, as hugo templates rely on a bunch of configuration
variables define in order to work properly. Also, not every template used the
same recent post mechanism I did, so they didn't help isolate the issue at all.
Lastly, if it was an older template... it had the same rendering issue mine
did. Eventually, I found a newer, but rather bare-bones template that had a
similar home page layout to my own. When I rendered my site with it... I had a
proper recent posts list on the home page!

This proved 1) the issue was somewhere in my tempalte code and 2) a fix was
possible.

### Coding a Solution

Comparing the `layouts/index.html` file of each of the templates, I noticed the
working template used a different method to gather and display the recent
posts. My template used a basic in-line piece of code that grabbed a range of
the latest posts, right then and there.

```html
<div class="container">
      <div class="row">
        <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
          {{ $posts := or .Site.Params.PostSummariesFrontPage 4 }}
          {{ range first $posts (where .Data.Pages "Type" "post") }}
              {{ .Render "summary"}}
          {{ end }}
```

The newer template however had a better setup by defining variables at the top
of the layout page to calculate all the recent post math, and the simply
refered to *that* to render the summaries. So, I read a bit of the hugo
documentation to learn how variables and some of the basic functions worked.

Eventually, I was able to come up with my own solution by defining the
following variables at the top of the page:

```go
{{ $mainSections := .Site.Params.mainSections | default (slice "post") }}
{{ $section := where .Site.RegularPages "Section" "in" $mainSections }}
{{ $section_count := len $section }}
```

and then using them further down where I render the recent post summaries:

```html
<div class="container">
  <div class="row">
    <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
      {{ range (first $n_posts $section) }}
          {{ .Render "summary"}}
      {{ end }}
```

Then... it worked!

### Conclusion

For as quick and easy of a fix this post implys, this was actually a giant
pain. I just wanted to catch up on my backlog of posts, but I couldn't publish
anything until the website was fixed. It took a long time to figure out where
the problem was occuring, but in the end I'm happy with the solution. Assuming
my website doesn't suddenly break again, see you in the next post!
