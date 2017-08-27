{:title "Transitioning Website to Hugo"
 :date "2017-08-27"
 :layout :post
 :author "Ryan Himmelwright"
 :tags ["Website" "Hugo" "Go"]}
 
 While I have loved using cryogen for over a year and a half now, I thikng I have started to make the transition to using another static website generator for this website, specifically Hugo. This post will detail why I am switching, what I have done so far, and what still needs to be completed before moving the site over.
 
<!-- more -->
 
### From Cryogen to Hugo




### What I've Done So Far


##### - Installed & Setup a test Hugo site

Getting and installing Hugo on my computers was very simple. It was in my reops :) (Solus), so I just had to run the command:

```
sudo eopkg it hugo
```

After I had hugo installed, I experimented with creating new website projects for a bit before finally creating one to start my transition. To create a new website, I used the command:

```
hugo new site ryan-hugo-test
```

This created a new directory containing all the required hugo directory structure and files for the website.

Like cryogen, hugo can spin up the website in a test server during development. To do this, use the command:

```
hugo serve -D
```

*Note: I used the `-D` flag to unclude any files marked as "drafts."*


##### - Setup a Theme and started tweaking it

With the hugo site generated, I wanted to get a theme going. After sampling a handfull of demo's from hugo's [theme page](https://gohugo.io/themes/), I decided on the [startbootstrap-clean-theme](). I've seen it used on other sites before, and I think is a common one on other site generators. However, it is a nice and simple there, that is white-background based like I wanted. Additionally, I love having header images for posts, and I can photo's I've taken to personalize the site a bit more.

To get the them, I cloned it down from git:

```
git clone ...
```

*Note: with this particular theme, there are an abundant amount of features, so it is a good idea to copy their example config.toml. This is one reason why I started with the theme right off the bat.*

Before I started ripping into the theme too much, I copied the theme directory to make my own version, and set the `theme` line in my `config.toml` to reflect the change. I also went through the example all the lines in the themes's `config.toml` and  changed them accordingly.

With the new theme setup, and the configuration edited, I started making some minor tweaks. The main tweak I made was to add the `Summary` contents to the posts list on the home page. I currently use this in cryogen, so all of my posts are written to support that. The feature is baked into hugo, but I needed to edit the theme to include it on the posts page. To do this, I edited the `/layouts/post/summary.html` file of the theme slighly to add the summaries:

origonal:

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

I also setup and altered the code syntax highlighting. For this, I had to install pygments, which again was *very* easy to do on my Solus computers:

```
sudo eopkg it pygments
```

After that, I just had to make sure that I specified the language at the start of my code snippets. I also ran into an issue where the colors for the code snippers weren't great, and some text was un-readable. This seems to be a common issue, and I found a good code snippet to add to the `pre` section of my `/static/css/clean-blog-min.css` file that resolved the issue.

If all went well, the code syntax highlighting should be demonstrated in the code snippets above.

##### - Dumped my Backlog of Posts and altered the header content

To test out how the website works, and to eventually switch my site completly over to hugo, I needed to import all of my posts. First, needed to figure out where to put them. Hugo has a slightly different file structure, but I eventually figured out that I could dump them in a `/content/posts/` directory.

Cryogen, which is written in [clojure](), used a clojure p-list for the post's header and meta data. However, Hugo uses a typical `.toml` header syntax... ????... So, I had to convirt them. I'm sure there was a simple programatic way, or possibly even a tool created to do this but I just did it by hand. It wasn't so bad. I used emacs.

After importing the posts markdown files, I needed to add the images that they contained. Again, this took a bit of research to figure out the file structure, but I quickly learned that anything in the `/static/` directory gets copied to the site's root directory when the site is compiled. So, I was able to directly copy my `/img/` folder from cryogen to `/static/img/` in hugo, and all my image paths worked perfectly!

Unfortunately, I immediatly noticed that the images in the posts were massive, and not constrained to the content width. I looked for a solution and tried editing the `css`, but I eventually just started to convert my images which used markdown syntax, to use normal html `<img>` tags, with a `width=100%` in them. Ultamately, this gives me a bit more power with how I set images and have contemplated switching my images to use this method in the past anyway.

##### - Made a bunch of header images

After fixing my in post images, I started to play with post header images. I figured out where they were located in the theme, and two of my own to replace the defaults. I read that a post's header image can be set with the `image == "..."` option at the top of the file... so I went a little crazy. I stayed up late browsing through some of my photos, and converted them to header images by shading them a bit (So the overlaying text is ledgeable). 

I love this feature, and want all of the post header images of my site to have been personally taken by myself. This is my personal website afterall.


### What Needs to be Done

##### Create Single Pages (About/Homelab)

##### Check how the posts display

##### Small tweaks
