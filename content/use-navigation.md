title: Use Browser Navigation
date: 2020-02-26
category: Interwebs

Built into all browsers these days are buttons like FORWARD, BACK, and
REFRESH. However, many web developers choose to build navigation
components into their sites which ignore this built in functionality.
The result is UI **bloat**. There are multiple back buttons displayed
for most users, both those on screen and those on the browser
itself. Rather than having content quickly and cleanly delivered, we
are faced with all-looking-the-same websites, which are supposedly
user-friendly.

Individual users can do things to get rid of browser clutter. However,
most people aren't nerds who tweak their browser settings to hide
things they don't want (or who set up stuff like `vim` keybindings for
their browser).

Content First
-------------

Making use of browser buttons instead of cluttering a UI with your own
buttons puts your *content first*. Navigating your web pages should be
non-annoying, but is not the main reason people (should) visit your
website. Hopefully you have something useful to offer that pretty
menus and spinners.

### Peripheral friendliness

One other advantage of making use of normal BACK/FORWARD functionality
is that many keyboards and mice (as well as other things, like game
controllers) can be set up to access these functions on convenient
thumb-buttons and other more ergonomic fixtures. Save your ass
expensive medical bills from <b>RSI</b> and stuff and build for the
future.

### Action plan

I'm going to write many web pages that you have to use your browser
navigation to get away from. No need to write another "back" button if
you can just press back. No layers of abstraction above normal browser
navigation.

Other technical notes
---------------------

Modern web tech like **React** piles on some layers of abstraction
through things like **dynamic routing** with tools like **React
router** to implement forward-back functionality in **Single Page
Applications** (SPA). This is understandable for making snappy web
pages that feel "modern".

However, if you don't load too many images and other media, keep
things clean and simple, etc., web pages don't even take that long to
load. This blog, for instance.
