{:title "Using Cryogen for Website"
 :date "2016-04-13"
 :layout :post
 :author "Ryan Himmelwright"
;; :draft true
 :tags ["Website" "Cryogen" "Clojure"]}

Ever since resurrecting my personal website, I have experimented with several
static website generators. Thus far, I have tried
[org-page](https://github.com/kelvinh/org-page),
[Jekyll](http://jekyllrb.com/) (_several_ times), and even (almost) made 
[my own emacs org-page solution](https://github.com/himmAllRight/ryBlog/blob/master/org-blog.el). Now that I have
started using the [clojure](http://clojure.org/) programming language, I have come across
[cryogen](http://cryogenweb.org/). As you may have already guessed, this site is now
being generated using cryogen.

<!-- more -->


## Emacs/org-mode Solutions

![emacs logo](../../img/posts/using-cryogen-for-website/Emacs-icon.png)
![org-mode unicorn](../../img/posts/using-cryogen-for-website/org-mode-unicorn.png)

About a year ago, obsession with
[emacs](https://www.gnu.org/software/emacs/) (and more importantly,
org-mode) eventually led me to try out
[org-page](https://github.com/kelvinh/org-page) while revitalizing my
personal website. The idea of writting web page content in .org files
was _very_ appealing and I wanted to gain a bit more experience
writting emacs lisp, so it seemed like a good choice. Overall,
org-page was a good learning experience, but I found the documentation
and support to be lacking. It seemed to be more of a [personal
project](http://kelvinh.github.io/), rather than a fully supported
framework. while I know [other people](http://cmacr.ae/) were able to
get it working, org-page simply wasn't working for me.


For over a year now, I have used org-mode at work each week to track
my hours and to take notes. I can then export the org files to html, creating
a full index of my work notes/logs. After digging deeper into org-page, realized it was just a fancy wrapper around
the org-project functions I used at work. So, I decided to implment
[my own emacs org-page solution](https://github.com/himmAllRight/ryBlog/blob/master/org-blog.el)
(well, _half_ implement. I guess I never fully finished it...). While
creating my own solution helped me learn even more about org-mode (which
helped with my work notes), I ultimately abandoned this method for my
personal website. Using my own solution quickly became a pain
because any computer I wanted use to generate and publish the site
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

[Cryogen](http://cryogenweb.org/) is a static website generator
written in [Clojure](https://clojure.org/).  If you already have
[Leiningen](http://leiningen.org/) installed (which if using Clojure,
you should), starting a new Cryogen application is as easy as entering
`lein new cryogen project-name` into a terminal. Once the project is
created, you can `cd` into the directory and run `lein ring
server`. Clojure will then fire up a local webserver of the compiled
project (by default on port 3000). Whenever a change made to a project
file is saved, the cryogen server re-compiles the project and updates
the webserver. As a result, makes it easy to edit see changes
live. Cryogen has a rather large, but simple [directory
structure](http://cryogenweb.org/docs/structure.html) that is used to
organize the project. Coming from Jekyll, this takes a bit of getting
used to, but I think it helps keep everything organized once you learn
it.

The one thing I _really_ like about Cryogen is the fact
that... well... it's clojure. This means that things can feel more
"lisp-y" from time to time. For example, in Jekyll, the preferences
and configuration of the website are kept inside a yaml configuration
file. Similarly, the meta-data and information for a page or blog post
are defined in a very specific yaml header at the top of the markdown
files. Cryogen follows a similar concept, except instead of yaml
headers, cryogen simply uses a p-list for it's
[configuration setup](http://cryogenweb.org/docs/configuration.html).

To change a post's information (ex: title, author, date), simply
change the keywords in the list at the top of the post's markdown
file. The flexability of setup also means that figuring out show to
setup use my own configuration was a breeze. For programmers that have
previously used Clojure or LISP in general, the configuration in
Cryogen is very intuitive and very natural.

The only _downside_ (sort of) I have experienced while using Cryogen
is that being a smaller community, there isn't much out there in terms
of templetes and themes (at least that I was able to find). So, while
I was able to easily setup an amazing looking website using Jekyll (by
using someone else's theme), I am forced to be a bit more hands on
using cryogen. Initially, I thought this was a negative, but after
spending some time hacking away at the theme and cleaning off my rusty
css/html skills, I think I have the site looking _good enough_ for
now. As a bonus, I am starting to re-learn web design. However, I am
_slowly_ catching up, so "modern" design features like mobil support
might not happen right away. It's not the best looking site, but I
like and and think it gives off a personal touch, which I guess is
good in a personal website. 

That's about it. That's why my site suddenly looked different one
weekend. I look forward to using both Clojure and Cryogen more for not
only this website, but other personal projects as well.