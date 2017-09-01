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
#### Create Single Pages (About/Homelab)

This wasn't so hard to do once I got it setup, but it took a while for me to realize how to actually do that. My confusion came from the fact that I didn't realize I needed to setup a layout for the pages.


#### Setting up an RSS Feed 

It turns out that [Hugo ships with its own RSS 2.0 template](https://gohugo.io/templates/rss/) by default. When I first saw this, I thought that I might still have to make a page or something for the feed, like I did for the about/homelab pages. This was not the case. Each "content" section (*ex: post or pages*) has an RSS automatically generated at `/section-name/index.rss`. I don't need a feed for my static pages, so I just found the [feed for my posts](http://ryan.himmelwright.net/post/index.xml). I wanted to make it easily accessible, so I added a menu link. I added the other static pages to the menu by adding `menu = "main"` to the page's font matter at the top of the markdown file. Without a defined markdown file for the rss feed page, I needed another way to add to the navigation menu. I was able to do this by adding the following code to the bottom of my `config.toml` file:

```
[[menu.main]]
  name = "RSS"
  url = "/post/index.xml"
  weight = 0

```

This is how both the `Home` and `Archives` links have both already been added to the navigation bar. I adjusted the weight to get the `RSS` link to show up at the end of the menu, and that was it.

#### Check how the posts display

-- I need to edit the `<!-- more -->` tags to be `<!--more-->` in hugo (no *whitespace*). I just noticed this issue.

<img alt="Hugo Logo" src="../../img/posts/website-switched-to-hugo/bad-summary.png" style="width: 100%; float: right; margin: 0px 15px 5px 5px;"/>

<img alt="Hugo Logo" src="../../img/posts/website-switched-to-hugo/post-page.png" style="width: 100%; float: right; margin: 0px 15px 5px 5px;"/>


<img alt="Hugo Logo" src="../../img/posts/website-switched-to-hugo/good-summary.png" style="width: 100%; float: right; margin: 0px 15px 5px 5px;"/>



#### Small tweaks

