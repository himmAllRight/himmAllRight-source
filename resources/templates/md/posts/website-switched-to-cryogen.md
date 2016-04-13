{:title "Using Cryogen for Website"
 :date "2016-04-03"
 :layout :post
 :author "Ryan Himmelwright"
;; :draft true
 :tags ["Website" "Cryogen" "Clojure"]}

Ever since resurrecting my personal website, I have experimented with several
static website generators. Thus far, I have used
[org-page](https://github.com/kelvinh/org-page),
[Jekyll](http://jekyllrb.com/) (_several_ times), and even made (sort of)
[my own emacs org-page solution](https://github.com/himmAllRight/ryBlog/blob/master/org-blog.el). Now that I have
started using [clojure](http://clojure.org/), I have come across
[cryogen](http://cryogenweb.org/). As you might have guessed, this site is now
being generated using cryogen.

<!-- more -->


## Emacs/org-mode Solutions

![emacs logo](../../img/posts/using-cryogen-for-website/Emacs-icon.png)
![org-mode unicorn](../../img/posts/using-cryogen-for-website/org-mode-unicorn.png)

When I revitalized my personal website, my obsession with
[emacs](https://www.gnu.org/software/emacs/) (and more importantly,
org-mode) eventually led me to try out
[org-page](https://github.com/kelvinh/org-page). The idea of writting
web pages and blog posts in .org files was _very_ appealing. Overall,
org-page was nice, but I found the documentation and support to be
lacking. It seemed to be more of a [personal
project](http://kelvinh.github.io/), rather than a fully supported
framework. while I know [other people](http://cmacr.ae/) were able
to get it working, org-page simply wasn't working for me.


For over a year now, I have used org-mode at work each week to track
my time and take notes. I then export the org files to html, creating
a full index of my work notes/logs. After digging deeper to figure out
how org-page worked, and realized it was just a fancy wrapper around
the org-project functions I already used. So, I decided to implment
[my own emacs org-page solution](https://github.com/himmAllRight/ryBlog/blob/master/org-blog.el)
(well, _half_ implement. I guess I never fully finished it...). While
creating my own solution helped me learn more about org-page (which
helped with my work notes), I ultimately abandoned this method for my
personal website. Using my own solution quickly became a pain
because any computer I wanted to generate and publish the site from
had to have a _.emacs_ file set up _just right_ to work.



## Jekyll

![jekyll logo](../../img/posts/using-cryogen-for-website/jekyll.png)

My first experience with [Jekyll](http://jekyllrb.com/) was about two
years ago, right after I graduated college. It was the first true
static website generator that I tried and I absolutely loved the
concept. You see, I taught myself how to build websites in the early
to mid 2000's when I was in middle school, and apparently never
developed beyond that point.During college, I maintained a personal
site by hand. It was super simplistic html that used tables for the
layout, and css for coloring. That's about it. Using a static website
generator like Jekyll for the first time was amazing, since it
automatically produced static webpages that looked _much_ better than
anything I could do by hand. It was what my 12-year-old-self longed for. I
eventually stopped using Jekyll because I was unable to get the
theming quite right, and ... well ... I started _really_ getting into
emacs. But you've already heard that story.

After taking a breif hiatus from Jekyll to adventure deeper into emacs
land, I return. This time, I was able to find and configure a
[sick theme](https://github.com/joshgerdes/jekyll-uno) that fit my needs. My
personal website looked the best probably ever has, and I really
enjoyed it. However, I have recently gotten frusterated using Jekyll
(again). It is great static website generator, but because I don't
often develop in Ruby (right now), setting up the proper ruby gems
environment and dependencies on [my computers](../../pages/homelab/)
can be very frusterating. Additionally, I have been learning
[clojure](http://clojure.org/) and while digging through
different clojure projects, I found [cryogen](http://cryogenweb.org/).


## Cryogen

![Cryogen logo](../../img/posts/using-cryogen-for-website/cryogen.png)


