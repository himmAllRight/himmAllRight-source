+++
title  = "Resolving Issue #26"
date   = "2019-12-15"
author = "Ryan Himmelwright"
image  = "img/posts/issue26/lowes-plants-cart.jpeg"
caption= "Lowes, Durham, NC"
tags   = ["website", "hugo"]
draft  = "False"
Comments = "True"
+++

While working on a post a couple of weeks ago, I noticed that for some unknown
reason, my website wasn't rendering correctly. After some back-tracking, I
remembered that I had updated the container I work in to a Fedora 31 base
image, which has a newer version of `hugo`.  So, I filed the problem as [issue
#26](https://github.com/himmAllRight/himmAllRight-source/issues/26), and
finished my post in a Fedora 30 container for the time being.  Here is a quick
explanation of how I *eventually* came back and resolved issue #26.

<!--more-->

### The Problem

<a href="/img/posts/issue26/correct-website-homepage.png">
<img alt="The correct website homepage index" src="/img/posts/issue26/correct-website-homepage.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">What the website homepage is *supposed* to look like</div>

My website has two types of content: *posts*, and *pages*. *Pages* are the
'normal' content of the website, like the [About](/pages/about/) and
[Homelab](/pages/homelab/) pages. *Posts* on the other hand, are the dated
'blog' posts I write (like the one you are currently reading). When everything
is working, my hugo template takes the newest `x` number of post files from the
*posts* directory, and lists them on the homepage with a small summary. (See
image above)

<a href="/img/posts/issue26/broken-website-homepage.png">
<img alt="What the broken homepage" src="/img/posts/issue26/broken-website-homepage.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">The broken homepage</div>

However, after the `hugo` version in my website container updated from
`v0.56.6` to `v0.58.3`, the post list on the homepage broke.  Specifically,
instead of listing the recent posts, the homepage just listed a single "post"
named...  "Posts" (see image above).

This indicated that something changed between those two versions that made my
template out of date. However, I wasn't sure if the problem was in the
website's page content, or if it was from an issue in the template I used.

### Finding a Fix

To find out, I grabbed some other [hugo templates](https://themes.gohugo.io),
and temporarily switched my config to render the website with them. This was
actually a bit more complicated than I thought it would be. Hugo templates
rely on a all sorts of configuration variables being defined in order to work properly.
Additionally, not every template had a recent post section like I did, so they
didn't help to isolate the issue at all. Lastly, if the template was older...
it had the same rendering issue mine did. Eventually, I found a newer, but
rather bare-bones template that had a similar home page layout to my own. When
I rendered my site with it... it had a working recent posts list on the home
page!

This proved 1) the issue was somewhere in my *template code* and 2) a fix was
possible.

### Coding a Solution

Studying the `layouts/index.html` file in each template, I noticed the working
template used a different method to gather and display the recent posts. My
template used a basic in-line piece of code that grabbed a range of the latest
posts to be rendered, right then and there.

```html
<div class="container">
      <div class="row">
        <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
          {{ $posts := or .Site.Params.PostSummariesFrontPage 4 }}
          {{ range first $posts (where .Data.Pages "Type" "post") }}
              {{ .Render "summary"}}
          {{ end }}
```

By comparison, the the newer template used an improved setup. It first
defined variables at the top of the layout page to calculate all the recent
post lists, and then simply referred to *that* when rendering the summaries. So,
I read up a bit on the hugo documentation to better learn how variables and
some of the basic functions worked.

Eventually I was able to come up with my own solution, defining the following
variables at the top of the page:

```go
{{ $mainSections := .Site.Params.mainSections | default (slice "post") }}
{{ $section := where .Site.RegularPages "Section" "in" $mainSections }}
{{ $section_count := len $section }}
```

I then referred to the variables further down where I render the recent
post summaries:

```html
<div class="container">
  <div class="row">
    <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
      {{ range (first $n_posts $section) }}
          {{ .Render "summary"}}
      {{ end }}
```

and... it worked! Done!


### Conclusion

For as quick and easy as this post implies, the fix was actually a giant pain.
It took a long time to figure out where the problem was occurring, but in the
end I'm happy with the solution. In fact, I used a [similar
approach](https://github.com/himmAllRight/himmAllRight-source/pull/30)
afterwards to fix [issue
#28](https://github.com/himmAllRight/himmAllRight-source/issues/28)! Assuming
hugo doesn't suddenly break me again, see you in the next post!
