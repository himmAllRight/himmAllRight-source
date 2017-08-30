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



#### Create Single Pages (About/Homelab)



#### Setting up an RSS Feed 

It turns out that [Hugo ships with its own RSS 2.0 template](https://gohugo.io/templates/rss/) by default. When I first saw this, I thought that I might still have to make a page or something for the feed, like I did for the about/homelab pages. This was not the case. Each "content" section (*ex: post or pages*) has an RSS automatically generated at `/section-name/index.rss`. I don't need a feed for my static pages, so I just found the [feed for my posts](http://ryan.himmelwright.net/post/index.xml). I wanted to make it easily accessable, so I added a menu

#### Check how the posts display

-- I need to edit the `<!-- more -->` tags to be `<!--more-->` in hugo (no *whitespace*). I just noticed this issue.


#### Small tweaks

