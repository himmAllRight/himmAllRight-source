{:title "Using Cryogen for Website"
 :date "2016-04-03"
 :layout :post
 :author "Ryan Himmelwright"
;; :draft true
 :tags ["Website" "Cryogen" "Clojure"]}

Ever since resurrecting my personal website, I have experimented with several
static website generators. Thus far, I have used
[org-page](https://github.com/kelvinh/org-page),
[Jekyll](http://jekyllrb.com/) _several_ times, and even made 
[my own emacs org-page solution](https://github.com/himmAllRight/ryBlog/blob/master/org-blog.el). Now that I have
started to learn [clojure](http://clojure.org/), I come across
[cryogen](http://cryogenweb.org/). Needless to say, this site is now
being generated using cryogen.

<!-- more -->


## Emacs/org-mode Solutions

![emacs logo](../../img/posts/using-cryogen-for-website/Emacs-icon.png)
![org-mode unicorn](../../img/posts/using-cryogen-for-website/org-mode-unicorn.png)

When I first revitalized my personal website, my obsession with
[emacs](https://www.gnu.org/software/emacs/) (and more importantly,
org-mode) led me to first try out h
[org-page](https://github.com/kelvinh/org-page). The idea of writting 
web pages and blog posts in .org files was _very_ appealing. Org-page was 
great, but I found the documentation and support to be lacking. It 
seemed to be more of a [personal project](http://kelvinh.github.io/), 
rather than a supported framework, and while I know 
[other people](http://cmacr.ae/) 
were able to get it working, org-page simply wasn't working for me.


For over a year now, I have used org-mode at work to track my time and 
take notes every week, which I then export to html. After digging to
figure out how org-page worked, and realized it was just a fancy
wrapper that utilized the org-project functions, I decided to implment
[my own emacs org-page solution](https://github.com/himmAllRight/ryBlog/blob/master/org-blog.el)
(well, _half_ implement. I guess I never fully finished it...). While
I learned more about org-page, and was able to use that for my work
notes, I ultimately abandoned this method for my personal
website. Using my own org-mdoe solution quickly became a pain because
any computer I wanted to generate and publish the site
from had to have a _.emacs_ file set up _just right_. 



## Jekyll

![jekyll logo](../../img/posts/using-cryogen-for-website/jekyll.png)

I first used [Jekyll](http://jekyllrb.com/) about two years ago right
after I graduated college. It was the first true static website
generator that I tried and I loved the concept. During college, I
maintained a personal site by hand. It was super simple html that used
tables for the layout, and css for coloring. You see, I taught myself
how to build websites in the early to mid 2000's when I was in middle
school, and apparently never developed beyond that point. Using a
static website generator like Jekyll for the first time was
amazing. It was what my 12 year old self longed for. I eventually
stopped using Jekyll because I was unable to get a good theme working,
and ... well ... I started _really_ getting into emacs. But you
already know that story.

After taking a breif hiatus from Jekyll adventure deeper into emacs
land, I return. This time, I was able to find and configure a
[sick theme](https://github.com/joshgerdes/jekyll-uno). My personal
website looked the best it probably ever has, and I really enjoyed
it. However, I've recently have gotten frusterated again using
Jekyll. It is great static website generator, but as I don't often
develop in Ruby (right now), setting up the proper ruby gems
environment and dependencies on [my computers](../../pages/homelab/)
can be very frusterating. Additionally, I have been learning
[clojure](http://clojure.org/) lately and while digging through
different clojure projects, I found
[cryogen](http://cryogenweb.org/). 


## Cryogen

![Cryogen logo](../../img/posts/using-cryogen-for-website/cryogen.png)

Talk about setting up cryogen and how I am bad at css...
