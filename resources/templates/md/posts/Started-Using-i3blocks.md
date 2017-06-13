{:layout :post
:title  "Refreshing my i3 setup with i3blocks"
:date "2017-06-08"
:author "Ryan Himmelwright"
:tags ["Linux" "i3" "customization" "Solus"]
:draft? false
}

The last couple of weeks I have shifted back to using the i3 window mangers. When I first fired it up again, my fingers danced across the keyboard, remembering all of the personalized keybindings I have cultivated in my i3 configuration over the years. It is a simple, beautiful setup... except for one part. My i3status bar was looking rather blaned and dated, expecially comparted some of the i3 setups posted by all the cool kids over at [/r/unixporn](https://www.reddit.com/r/unixporn/). So, I decided it was time for a refreash.

<!-- more -->

## i3status

![One of my simple i3status setups](../../img/posts/starting-i3/i3status.png)
<div id="caption">One of my simple i3status setups</div>

When I first configured i3 seceral years ago, I used i3status because it was easy to setup with i3 and did what it needed by default. Over time, I learned how to create and modify [my own .i3status.conf](https://github.com/himmAllRight/dotfiles/blob/master/i3/.config/i3/i3status.conf) so that I could tweak it to play nice with my occasionaly unstandared configurations (ex: `/Data` partitions and such). While i3status served me well for many years, using the same-old setup has become boring. I started to notice several other really nice looking status bar tools being used in i3 setups, and wanted to try them out.

## Polybar

![The example polybar](../../img/posts/starting-i3/polybar.png)
<div id="caption">The example polybar</div>

The first bar I saw and tried was [polybar](https://github.com/jaagr/polybar). I started with it because some of the examples or it are really awesome. It is a bar that looks very modern and has an infinate number of features. I got it setup and was able to use the example bar just fine. However, when I started to configure my own, I started to run into issues with it being able to detect my workspaces and other elements. After some frustration, I put it aside for a bit and decided to see what else is out there.

## i3blocks
Next, I learned of [i3blocks](https://github.com/vivien/i3blocks). It appeared to have everything I wanted for by status bar, but yet was simple and respected the [i3bar protocol](https://i3wm.org/docs/i3bar-protocol.html). So I tried it out.

### Downloading from the Repos
Just like installing any other package on Linux, I decided to first check to see it it was in the [Solus Repos](https://dev.solus-project.com/):

```
sudo eopkg sr i3block
```

and it was, so I installed it from there.

### Finding a Git Repos

### Forking my own for Solus Tweaks

## Conclusion

![The example polybar](../../img/posts/starting-i3/myi3blocks.png)
<div id="caption">My current i3blocks setup</div>
