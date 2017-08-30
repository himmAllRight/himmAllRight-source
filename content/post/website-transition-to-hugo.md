+++
title = "Transitioning Website to Hugo"
date = "2017-08-27"
author = "Ryan Himmelwright"
image = "img/header-images/st-lucia-fort1.jpg"
tags  = ["Website", "Hugo", "Cryogen", "Go",]
+++
 
 While I have loved using [Cryogen](http://cryogenweb.org) to create this website for over a year and a half now, I have started the transition to using another static website generator. Specifically, I have been experimenting with [Hugo](https://gohugo.io). This post will detail why I am switching, what I have ported over thus far, and what still needs to be completed before generating the official site with hugo.
 
<!-- more -->
 
### From Cryogen to Hugo

My departure from Cryogen really has nothing to do with the project itself. It is a prime example of what [clojure](https://clojure.org/) is capable of, and I feel that more people should give it a shot. Recently though, I've been itching to switch up my website's theme a bit. While I fancy my [Immutable Theme](../new-theme-immutable/) I created a couple months ago, it isn't quite doing what I had hoped for. I love dark themes, but the type of posts I've been creating really don't look good with them. I like to add diagrams, code snippets, and images to all of my posts. Diagram posts look wonderful with a white background, but are garbage in a dark theme. This difference was glaring last week as I switched between my markdown editor's preview window (default white theme), and the website's live preview view, while writing my [reverse tunnels](../simple-reverse-ssh-tunnel/) post.

Similar to the logic I employed earlier this month when [switching back to Solus](../back-to-solus/), I thought that if I was going to scrap my theme and start from scratch, I might as well check out different website generator. I had been keeping an eye on the various site generators, but the one I considered the most (and even dabbled with a bit last month), was [Hugo](https://gohugo.io). 
### What I've Done So Far

I started the process of transporting my website from cryogen to hugo. So far, my experience with Hugo has been great. Here is what I've done:

#### Installed & Setup a test Hugo site

Obtaining and installing Hugo on my computers was very simple, as it was in the reops (Solus). I just had to run the command:

```bash
sudo eopkg it hugo
```

After I had hugo installed, I experimented with creating new website projects for a few minutes before finally creating one to start my transition. To create a new website, I used the command:

```bash
hugo new site ryan-hugo-test
```

This created a new directory with all the project's default core files, and adhering to the required hugo [directory structure](https://gohugo.io/content-management/organization/).

Like cryogen, hugo can spin up a website in a test server during development. To do this, use the command:

```
hugo serve -D
```

*Note: I used the `-D` flag to additionally include any files marked as "drafts."*


#### Setup a Theme and started tweaking it

With the hugo site generated, I wanted to setup a proper theme. After sampling a handful of demo sites from hugo's [theme page](https://gohugo.io/themes/), I decided on the [startbootstrap-clean-theme](https://themes.gohugo.io/startbootstrap-clean-blog/). I've seen it used on other sites, and I think it is a commonly used theme with other site generators. However, it is clean and simple, with a white-background base like I wanted. Additionally, I love having header images for posts and pages. It lets me better personalize the website by exclusively using images I've photographed myself.

To get the theme, I cloned it from git:

```
git clone git@github.com:humboldtux/startbootstrap-clean-blog.git
```

*Note: this particular theme has an abundant amount of features, so it is a good idea to copy the provided example config.toml and build off of it. This is one reason why I started with configuring the theme right off the bat.*

Before I started ripping into the theme too much, I copied the theme directory to make my own version, and set the `theme` line in my `config.toml` to reflect the change. I also went through all the lines of the example `config.toml` and  changed them accordingly.

With the theme setup, and the configuration edited, I started making some minor tweak to the site. The main tweak I made was to add the `Summary` contents to the post list on the home page. I currently use this feature in Cryogen, so all of my posts are written to support it. Summaries are baked into hugo, but I needed to edit the theme to include it on the posts page. To achieve this, I edited the `/layouts/post/summary.html` file of the theme slightly:

original:

```html
<div class="post-preview">
  <a href="{{ .Permalink }}">
    <h2 class="post-title">{{ .Title }}</h2>
    <h3 class="post-subtitle">{{ .Description }}</h3>
  </a>
  <p class="post-meta">
      {{ partial "meta.html" .}}
 </p>
</div>
<hr>
```
with post summaries:

```html
<div class="post-preview">
    <a href="{{ .Permalink }}">
        <h2 class="post-title">{{ .Title }}</h2>
        <h3 class="post-subtitle">{{ .Description }}</h3>
    </a>
    <p class="post-meta">
        {{ partial "meta.html" .}}
        <div class="summary">
            {{ .Summary }}
        </div>
    </p>
    <p class="post-meta"> 
        <a href="{{ .Permalink }}"> Click to Read More --></a>
    </p>
</div>
<hr>
```

I also setup and fixed the code syntax highlighting. I first installed pygments, which again was *very* easy to do on my Solus computers:

```
sudo eopkg it pygments
```

After that, I just made sure that the language was specified at the start of each code snippet. I ran into an issue where the colors for the code were poorly selected, resulting in some invisable text. Apparently, this is a common issue, and I found some *.css* code to add to the `pre` section of my `/static/css/clean-blog-min.css` file that resolved the issue.

If all went well, the code above should have proper syntax highlighting.

#### Dumped my Backlog of Posts and altered the header content

To test out if the website worked properly, I wanted to import all of my posts. First... I needed to figure out where to put them. Hugo has a slightly different file structure, but I eventually figured out that I could create a `/content/post/` directory, and dump them there.

Cryogen, written in [clojure](https://clojure.org/), uses a clojure map for the post's meta data. Hugo on the other hand, uses a several [font matter formats](https://gohugo.io/content-management/front-matter/) (`toml`, `yaml`, `json`) for meta data. So, I had to convert the post headers. I'm sure that there was a simple, programmatic way, or even a tool, created to accomplish this... but I just did it by hand. It wasn't so bad. I used emacs.

After importing the markdown files for the posts, I needed to add all the images the posts contain. Again, this took a tiny bit of research to figure out the file structure, but I quickly learned that anything in the `/static/` directory gets copied to the site's root directory when the site is compiled. So, I was able to copy my cryogen `/img/` folder directly to `/static/img/` in hugo, and all my image paths worked out-of-the-box!

Unfortunately, I immediately noticed that some images in the posts were massive, and not constrained to the content width. I looked for a solution, and tried editing the `css`, but I eventually just started to convert the markdown syntax images, to use normal html `<img>` tags, with a `width=100%` parameter. Ultimately, this gives me a bit more power with how I set images anyway.

#### Made a bunch of header images

After fixing my in-post images, I started to play with post/page header images. I figured out where they were located in the theme, and added two of my own to replace the defaults. I read that a header image can be set with the `image == "..."` option in a post/page's font matter... so I went a little crazy. I stayed up late browsing through some of my photos, and converting them to header images (I did this by shading them a just a tad, so the overlaying text is legible). 


### What Needs to be Done

This post has turned out to be a giant monster, so I'll be brief here and turn the sub-sections into a quick list instead.

* **Create Single Pages (About/Homelab)** - I still need to figure out and create my website's single pages. These include the *About Me* and *Homelab* pages. The content of those pages has also been slipping out of date... but I won't let that hold me up from switching the site over first.

* **Setting up an RSS Feed** - Similar to the task above, I want to make sure I have an RSS feed for the blog configured, and accessible in the main menu.

* **Check how the posts display** - I need to go through the posts and make sure they are displaying content correctly. I'll check that links work, images aren't massive, code syntax languages are set, etc. This actually shouldn't be as bad as it sounds because I've done much of it already.

* **Small tweaks** - There are bound to be a few tweaks here or there that I'll notice and want to changed (*example from above: I've already added the post summaries to the home page post list*). One item that comes to mind is adding *next* and *previous* post markers at the bottom of each post. Again, I won't let that hold me up though.


Well, that's about it. I'll work now on editing and publishing this post, and with any luck, the website should switch over to the Hugo generated one within a few days. I hope you enjoy it!
