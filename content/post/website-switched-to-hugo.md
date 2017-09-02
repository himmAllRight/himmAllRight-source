+++
title = "Website Switched to Hugo"
date = "2017-08-31"
author = "Ryan Himmelwright"
image = "img/header-images/st-lucia-cannon.jpg"
tags  = ["Website", "Hugo", "Go",]
draft = true
+++
 
So in my [last post](../website-transition-to-hugo/), I stated that I should be switching to generating the production website using [Hugo](https://gohugo.io) *within a few days*... and then I pushed *that* post to the website using Hugo. If you remember, I ended that post listing off a few tasks that I wanted to complete before switching the site. Here is how I eventually completed each one.
 
<!--more-->

<img alt="Hugo Logo" src="../../img/posts/website-switched-to-hugo/hugo-logo.png" style="width: 40%; float: right; margin: 0px 15px 5px 5px;"/>

### Create Single Pages (About/Homelab)

This wasn't so hard to do once I got it setup, but it took a while for me to realize how to actually do that. My confusion came from the fact that I didn't realize I needed to setup a layout for the pages.

After realizing I needed to setup layouts, I created a new layout directory in my theme directory for each of my pages to add: `/layouts/about/` and `/layouts/homelab/`. I then copied the `/layouts/post/single.html` the two directories file to use as a template for the two new layouts(`/layouts/about/about-page.html` and `/layouts/homelab/homelab-page.html`, respectively). I just needed a basic page that would inject the `.Content`. I also tweaked the header slightly to display an "*updated on*" date, rather than a "*posted on*" date.

With the templates made, in order to generate the pages, I made a new `/content/pages/` category, and added  `about.md` and `homelab.md` files to it. In both files, I defined the `type` and `layout` parameters, so that my layouts would be used. Lastly, I added declared that each page would be part of the main menu using the `menu` parameter.

```yaml
---
title: About
date: 2017-08-28T09:51:18-04:00
type: about
menu : 
  main:
    weight: -150
layout: about-page
image: img/header-images/park-books.jpg
---

```


### Setting up an RSS Feed 

It turns out that [Hugo ships with its own RSS 2.0 template](https://gohugo.io/templates/rss/) by default. When I first saw this, I thought that I might still have to make a page or something for the feed, like I did for the about/homelab pages. This was not the case. Each "content" section (*ex: post or pages*) has an RSS automatically generated at `/section-name/index.rss`. I don't need a feed for my static pages, so I just found the [feed for my posts](http://ryan.himmelwright.net/post/index.xml). I wanted to make it easily accessible, so I added a menu link. I added the other static pages to the menu by adding `menu = "main"` to the page's font matter at the top of the markdown file. Without a defined markdown file for the rss feed page, I needed another way to add to the navigation menu. I was able to do this by adding the following code to the bottom of my `config.toml` file:

```yaml
[[menu.main]]
  name = "RSS"
  url = "/post/index.xml"
  weight = 0

```

This is how both the `Home` and `Archives` links have both already been added to the navigation bar. I adjusted the weight to get the `RSS` link to show up at the end of the menu, and that was it.

### Check how the posts display

One task I needed to complete was going through and editing each post. The main issue that needed to be fixed in posts, which I [explained in the previous post](../website-transition-to-hugo/#image-size), was that the image tags needed to be switched from markdown to html syntax.

While editing the posts, I noticed that the [post summaries](../website-transition-to-hugo/#summary-setup) weren't displaying the content that I intended them to. I have hugo setup so that I manually cut off the summary location using a `<--more-->` tag in the markdown.But it didn't appear to be doing that.

<a href="../../img/posts/website-switched-to-hugo/summary-fix-spread.png"><img alt="Hugo Logo" src="../../img/posts/website-switched-to-hugo/summary-fix-spread.png" style="width: 100%; float: right; margin: 0px 15px 5px 5px;"/></a>

- *A: An over-extended post summary*.
- *B: The extra content of the post that was included in the summary*.
- *C: The corrected post summary.*

  
Some of the summaries seemed to extend beyond the cutoff point, including the next section header, and some of the section's content. 
After some further inspection, I noticed that I had added a space on either side of the "more" in the `<!-- more --> tags. So, I had to go through and delete the spaces.


### Next/Prev Posts

The main "*Small Tweak*" that I wanted to figure out was setting up navigation links at the bottom of each post page. So, I added some code between the  `{{ .Content }}` and `{{ partial "coments,html" .}}` tags of my theme's `/layout/post/single.html` file. I first made a line with `if` statements to establish "Next Post" and "Prev Posts" headers. Then on a second line, I put the actual links using `with` statements. The `if` and `when` statements are required so that previous and next posts only get linked *if they exist*. So the first and last post will only display one of the two links.

```html
<!-- Next Post/ Previous Post Labels -->
{{ if .NextInSection }}
    <div style="float: left;">Next Post:</div>
{{ end }}
{{ if .PrevInSection }}
     <div style="float: right;">Prev Post:</div>
{{ end }}

<br>

<!-- Next Post/ Previous Post Links -->
{{ with .NextInSection }}
    <a href="{{ .Permalink }}" style="float: left;">{{ .Title }}</a>
{{ end }}
{{ with .PrevInSection }}
    <a href="{{ .Permalink }}" style="float: right;">{{ .Title }}</a>
{{ end }}

```

### Conclusion

Just like the last post, I have continued to enjoy using Hugo. It is simple to use, but at the same time provides an immense level power and control. 
