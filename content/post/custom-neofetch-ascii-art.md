+++
title  = "Custom Neofetch ASCII Art"
date   = "2019-04-30"
author = "Ryan Himmelwright"
image  = "img/posts/custom-neofetch-ascii-art/downtown-raleigh.jpg"
caption= "Downtown Raleigh NC"
tags   = ["Linux", "Dotfiles", "Customization", "Shell"]
draft  = "False"
Comments = "True"
+++

I have been using [neofetch](https://github.com/dylanaraps/neofetch) as my
command-line system information tool for a few years now. While browsing
[/r/unixporn](https://reddit.com/r/unixporn/), I noticed that several
of the submissions did not have distro logos in their neofetch/screenfetch
ascii art. I knew that neofetch was customizable, but have never dug
into it myself. So I decided to change that.

<!--more-->



### Custom Neofetch ASCII Art

I started my neofetch investigation the same way one should start researching
*any* Linux command-line tool: `man neofetch`. Inside the man pages, I was
greeted with all sorts of customization options. Eventually, I scrolled down to
the section I wanted, `IMAGE BACKEND`.

There I learned that a custom image could be specified using the `--source` flag.
For example, to set the art to an ascii charmeleon file I *just happen* to have
on my desktop, I tried:

```shell
neofetch --source /home/ryan/Documents/Pokemon-ascii/5.txt
```

AAAAAND... It didn't work. It was still the Fedora logo. Clearly, I was still
missing something.

After some browsing, I found the [ASCII art
page](https://github.com/dylanaraps/neofetch/wiki/Custom-Ascii-art-file-format)
on neofetch's Github wiki. Reading it, I noticed that I was missing the `${c1}`
in my pokemon ascii files. So, I made a copy of the file and added `S{c1}` to
the top:

```
➜  welcome-messages git:(master) ✗ head charmeleon
${c1}
                      ,-'`\
                  _,"'    j
           __....+       /               .
       ,-'"             /               ; `-._.'.
      /                (              ,'       .'
     |            _.    \             \   ---._ `-.
     ,|    ,   _.'  Y    \             `- ,'   \   `.`.
     l'    \ ,'._,\ `.    .              /       ,--. l
  .,-        `._  |  |    |              \       _   l .
```
<div class="caption">head output of my modified charmeleon ascii file</div>

AAAAAND... It worked!

### Adding a Shell Alias


<a href="/img/posts/custom-neofetch-ascii-art/charmeleon-neofetch.png"><img alt="Custom Charmeleon ASCII art for my desktop's neofetch output" src="/img/posts/custom-neofetch-ascii-art/charmeleon-neofetch.png" style="max-width: 100%;"/></a>
<div class="caption">Custom Charmeleon ASCII art for my desktop's neofetch output</div>

Lastly, I wanted the charmeleon ascii art to be the *default* neofetch output on my
desktop. While I'm sure that I could have accomplished this *properly* by
editing the `~/.config/neofetch/config.conf` file I learned about, for now...
creating an alias seemed easier XD. So I added the following line to my
`~/.zshrc`:

```bash
alias neofetch='neofetch --source /home/ryan/Documents/ascii/pokemon/charmeleon'
```

Now whenever I call plain `neofetch` on my desktop, it runs with the charmeleon
art.

### Conclusion

So that's it. A nice *short* post for once! Despite the size, I hope if was
useful. If you haven't heard of neofetch before, go check it out. If you have,
I encourage you to go digging through the man pages. I promise you won't regret
it.  Enjoy!
