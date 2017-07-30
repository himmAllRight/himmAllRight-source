{:layout :post
:title  "Dabbling with GOlang"
:date "2017-07-29"
:author "Ryan Himmelwright"
:tags ["Dev" "GO"]
:draft? false
}

After spending so much of my dedicated learning time messing with system activities like [setting up a new home network](../issues-setting-up-ubiquiti-network/), [configuring git servers](../creating-a-git-remote/), and [switching my OS](../solus-to-fedora/), I have to itch to do a little bit home programming. Maybe even dabble with a new language I've been eyeing up. After very little internal debate, I decided to just [Gopher](https://golang.org) it (I'm so sorry).

<!-- more -->

## What is GO
<img src="../../img/posts/dabbling-with-go/gopher.png" style="width: 30%; float: right; margin: 0px 10px 0px 10px;"/)

Go (also known as golang) is an open source programming language developed by a team at Google (Robert Griesemer, Rob Pike, and Ken Thompson) in 2007.Being distributed under a [BSD-like license](https://golang.org/LICENSE), Go is also developed by community developers all over the world. 


Like C, it is a statically typed and compiled language. Unlike C however, Go includes garbage collection and memory safety features, as well as other design that are more reminiscent of dynamic languages like python (ex: type inference and package `import` statements). Lastly, go implements '[goroutines](https://tour.golang.org/concurrency/1)', which are a light-weight "threads", used for its concurrent programming implementation, making it an extremely relevant language for modern computing.

The Go project sums all of this up much nicer than I have on their [documentation page](https://golang.org/doc/):

> The Go programming language is an open source project to make programmers more productive.
>Go is expressive, concise, clean, and efficient. Its concurrency mechanisms make it easy to write programs that get the most out of multicore and networked machines, while its novel type system enables flexible and modular program construction. Go compiles quickly to machine code yet has the convenience of garbage collection and the power of run-time reflection. It's a fast, statically typed, compiled language that feels like a dynamically typed, interpreted language. 

## Reasons to Try
I've wanted to try [GO](https://golang.org/) as I find it to be an interesting potential language for myself. I thought about trying go in the past, but ultimately ended up trying out [rust](https://www.rust-lang.org/en-US/) first. Rust is a great language, although it can be quite complicated to learn. Go on the otherhand, is apparently a bit simplier and quick to grasp. When the Solus project announced that it was a language they are trying to fully support and use for build tools, my interest was peaked higher, but I was busy on other projects at the time. This week, Ikey made a patreon post talking about the new repo manager he's been writting... in go. So, my interest is yet again peaked.

## Installing
I first went to the golan [install page](https://golang.org/doc/install) to figure out if there was any odd things to install. It didn't appear so. I was on my NixOS laptop at the itme, so I installed go with the command: 

```
nix-env -i go
```

On Alakazam, it was

```
sudo dnf install golang
```

I then walked through the [test your install](https://golang.org/doc/install#testing) steps, and built a simple "hello world" app to make sure it was working properly. This was especially important, given that I was on nixOS which can sometimes be picky with system paths and such. Luckily, everything worked fine.


## First Steps
After confirming my install, I went back and looked at the [Learning Go section](https://golang.org/doc/#learning) of the documentation. The first item was [A Tour of Go](https://tour.golang.org/welcome/1) so I started there (Although I am really interested to eventually get to the [effective go](https://golang.org/doc/effective_go.html) documentation)


### Interesting things
- `gofmt` tool looks neat. I'm picky about propery layout so I like this.
- "naked" returns. You can name return values, and a "return" without arguments returns these values. As the point out, this should only be done for small functions, and I can see why (I'm thinking lambda style functions...)

example:
```
func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}
```
### Notes
#### Variables
- Types come after variable names
- `var` used to declare variables, at package and function level
- Inside a function, can use short assignment `:=` instead (ex: `k := 3`)

#### Basic Types


#### Constants
- Declared with the `const` keyword
- Cannot be declared with `:=`

### Playing
I played around with the language a little bit. It really is easy to pick up the basics and get going...

```
package main

import (
	"fmt"
	"runtime"
)

func main() {
	fmt.Printf("hello, world\n")
	getOS()
	fmt.Printf("\n") // I know this is dumb

	x, y := 74, 83
	sum := sumInts(x, y)
	fsum := factorial(sum)

	fmt.Printf("sum: %v\n", sum)
	fmt.Printf("Factorial of sum(%v): %v\n", sum, fsum)
}

func sumInts(x int, y int) int {
	sum := x + y
	return sum
}

func factorial(n int) int {
	if n <= 1 {
		return 1
	} else {
		return n + factorial(n-1)
	}
}

func getOS() {
	os := runtime.GOOS
	fmt.Printf("OS: %v\n", os) // impure
}

```
