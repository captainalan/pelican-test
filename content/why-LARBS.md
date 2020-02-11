title: Why LARBS?
date: 2019-12-27
category: Linux

In my [Arch Linux Install for n00bs](https://captainalan.github.io/pelican-test/arch-linux-install-for-n00bs.html) I gave details on how to install Arch linux and then suggested [LARBS](https://larbs.xyz) as a way to get up and running with your new installation. In this article I detail *why* I find LARBS particularly useful and address some points brought up by haters.


Sensible Defaults
=================

The number one reason to use LARBS is to experience with **sensible defaults
for a keyboard centered workflow**. LARBS offers an out-of-the-box setup of
many nice things that can take a long time to set up manually: a **tiling
window manager**, vi-like **line editing** (via zsh), a PDF reader (Zathura).

Furthermore, LARBS comes bundled with software you probably want: e.g. a
privacy-respecting browser (Brave), git, some programming languages and
compilers. The `yay` tool is already setup to help you grab even more software
from Arch Linux's AUR repositories.

### But *real* Linux users set these things up themselves

Practical people want good tools readily available to them. If you begin
learning guitar on a really poorly made instrument you are more likely to
become discouraged and give up. On the other hand, if you have a more
experienced friend (or shop) set up your instrument when you are getting
started, you may make a lot more progress, more quickly in *actually learning
how to play*.

Furthermore, many aspects of installing things randomly often are annoying and
don't involve much learning. The arcane details of how to run some program you
are probably going to run only very rarely are perhaps better offloaded to
automation (e.g. the shell scripts LARBS uses).

### But using someone else's setup is lame!

LARBS does not constrain how you set things up later---it's just a shell script
to get you started.

For instance, I use emacs a lot, and Luke Smith (who made LARBS) doesn't. Many
tools in LARBS I don't care about or use (e.g. `vifm`, vim-like file manager)
because I just use `dired` in emacs.

Pros and Cons
=============

What LARBS is *not* good for
--------------------------

Obviously, if you require applications that require Windows or some other OS, you are out of luck.

If you are doing complicated things with sound, hardware, etc. LARBS only gives a basic desktop setup. It may be much harder to adjust these settings in LARBS compared with a well-established Linux distribution, such as Lubuntu or Manjaro (two others I have tried with older hardware).

It is hard to set up typing in CJK; I'm still figuring out how to get this well
integrated and will upload a guide when I am able to do so nicely.

What LARBS *is* good for
-------------------------

LARBS is good for getting a decent general computing and programming
environment set up quickly.

For a user coming from a more traditional desktop setup, LARBS allows you to
explore ideas like...

- Tiling windows for more efficient screen space usage
- Remapping CAPS LOCK for happier keyboarding
- Editing config files to change settings

...without the trouble that might come from tweaking another installation (e.g.
modifying default Ubuntu) or doing everything from scratch.

While on the one hand, there is definitely learning to be done in *doing*
things yourself from the start, why shouldn't we reuse good defaults and stable
software set up by more knowledgable people? Studying the LARBS config files is
a good way to start writing your own configs.

Summary
=============

If you wanna try out a tilling window manager, just install Arch and LARBS. It
is not even that bad and you can customize it more later as you find out more
about what you want.
