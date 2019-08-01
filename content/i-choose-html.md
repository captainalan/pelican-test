title: I choose HTML
date: 2019-07-20
category: Interwebs

Before, I built [my website in
React](https://captainalan.github.io/me). Now, it is being rebuilt in
plain HTML/CSS (with some help from Bootstrap and jQuery to make
things like mobile responsiveness less tedious). After spending a
considerable amount of time with fancy frameworks, why take a step
"backwards"?

## I got blocked?!

I was trying out some different Linux distributions, and decided to
give the fully-free distro [Trisquel](https://trisquel.info) a spin.
To my dismay, I found that [*my own
site*](http://captainalan.github.io/me) was blocked blocked for some
JavaScript-y reasons. It turns out that all sites that make use of
React (or at least `create-react-app`, the tool I used to bootstrap my
site) are *blocked* when [certain sorts of
JavaScript](https://www.gnu.org/software/librejs/) are blocked.

## Next steps

It is my goal to produce informative, unobtrusive websites
that are easily indexed, linked, downloaded, etc.

I am becoming more interested in **static site generators** (such as
[Pelican](https://blog.getpelican.com), which was used to make this
site) because the HTML/CSS they spit out is compatible in most places
and they also make things like RSS feeds easy to do.
