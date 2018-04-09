+++
title  = "Starting Clojure, as a Common Lisp Deveoper"
date   = "2018-04-20"
author = "Ryan Himmelwright"
image  = "img/header-images/container-building-umich.jpg"
tags   = ["Programming", "Linux", "LISP", "Clojure",]
draft  = true
+++

I have started to get into clojure again. This is just a spot for me to take
notes for now. I'll turn this into a post that is mostly notes to myself about
the basics of clojure, but also comparing it to what I know about common lisp.
So sort of a "clojure from a common lisp developer". This might be the first
post of a series...

<!--more-->



## Install Clojure

`lein` setup

maybe install Java if not already?

## Configuring and Using Spacemacs Cider


## Language

- Normal lisp syntax, for the most part
  - Parens
  - no `,`
  - Operator followed by operands (prefix**
  - Simple, Nested structure
  
  **NOTE: I'll probably keep comparing clojure to common-lisp... since that's
  what I know and use at my day job.**
  
### Control Flow

#### If

`if` seems to work the same as in common lisp, and has the form:

>(if boolean-form
>    then-form
>    optional-else-form)

So, the first thing provided is the boolean form. If it evalutates to `true` (or
a "truthy" value, just as in Common Lisp), the second form is evaluated and
returned. Otherwise, the second form is evaluated and returned (if provided.
Otherwise, returns `nil`).

```clojure
user> (if true
        "True Condition"
        "False Condition")
=> "True Condition"
user> (if false
        "True Condition"
        "False Condition")
=> "False Condition"
```

Notice that just as in common lisp, both the if and else conditional branches
can only have one form. The way around this in common lisp is to wrap multiple
forms using a function like `progn`, a `let` closure, or to use `if*` instead
(my preferred method recently). In clojure, `do` can be used.

#### do

Do wraps up multiple forms into a single one and evaluates them, returning the
last item, *much* like `progn` in common lisp. As stated above, this is be used
in an `if` to place multiple forms in the *if* or *else* conditional branches:

```clojure
user> (do
        (println "Print this line")
        (println "And also this line...")
        "return this line")
=> Print this line
=> And also this line...
=> "return this line"
```

#### when

In some languages, the *else* conditional branch of an `if` function is
mandatory (ex: Haskell), the benefit being that *all* conditions are *defined*.
However, sometimes when using `if`, it might only be desired to do something
*if* the conditional is true. In other words... we don't really care about the
*else* condition, *or* more likely, we intend the `else` to just return `nil`.

In lisp languages, we have `when` to handle this scenario. `When` essentially
combines the functionality of an else-less `if`, with a `do`. It takes a boolean
form, and when "true", it will evaluate the remaining forms wrapped inside the
`when`. Otherwise, it will return `nil`. So for example, the following two
pieces of code are essentially the same:

```clojure
user> (if true
        (do
          (println "If true, run me")
          (println "...don't forget about me")
          "I'm the return value! (in Ralph Wiggum voice...)")
        nil)
        
=> If true, run me
=> ...don't forget about me
=> "I'm the return value! (in Ralph Wiggum voice...)"

user> (if false
        (do
          (println "If true, run me")
          (println "...don't forget about me")
          "I'm the return value! (in Ralph Wiggum voice...)")
        nil)
=> nil
```

```clojure
user> (when true
        (println "If true, run me")
        (println "...don't forget about me")
        "I'm the return value! (in Ralph Wiggum voice...)")
If true, run me
...don't forget about me
"I'm the return value! (in Ralph Wiggum voice...)"

user> (when false
        (println "If true, run me")
        (println "...don't forget about me")
        "I'm the return value! (in Ralph Wiggum voice...)")
nil
```
