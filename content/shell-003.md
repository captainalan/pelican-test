title: Practical Shell Scripting, Part 3
date: 2020-05-21
category: Linux

In this post, we will introduce `xargs`, which allows you to pass in
arguments to a command via standard input.

For example, to do

```bash
echo "$HOME" | xargs ls -la
```

is like doing

```bash
ls "$HOME" -la
```

We can think of `xargs` as a kind of "keyword" or "syntactic feature"
of shell scripting since it gives us a general mechanism for combining
the inputs and outputs of various commands.

Use with `find`
---------------

The `-exec` option of `find` can be cumbersome to work with as your
commands get more complex. In this example, `find` is used to get text
files in the current directory, and then these files are passed to
`cat` (and then printed to standard output) using `xargs`.

```bash
find . -maxdepth 1 -type f -name "*.txt" | xargs cat
```

Using various options of `find` we can pass different stuff to
`xargs`. Below, we find directories with names beginning with "Foo"
and use the `tree` command to print textual tree representations of
these. This might be useful for copy/pasting a directory
representation to quickly show a collaborator how some project is laid
out.

```bash
find . -maxdepth 1 -type d -name "Foo*" | xargs tree 
```

Using `find` together with `xargs` can be a useful pattern when you
have to repeat some action against on some files/directories that can
be found using parameters `find`.


Storing Arguments in Text Files
-------------------------------

Using `xargs` we can run commands based on data stored in text
files. This can be very convenient for separating data from the logic
of some script.

Let's suppose you have some directory `media_to_consoom_later/`. Here,
you queue up YouTube links like,

```
youtube.com/video1
youtube.com/video2
youtube.com/video3
```

...in a file called `youtube-videos.txt`. You have another video
called `youtube-music.txt` that follows the same format:

```
youtube.com/track1
youtube.com/track2
youtube.com/track3
```

Using `xargs` you can quickly execute two commands to download all the
videos with one set of options and then all the music files with
another. Here is an example usage with the program `youtube-dl`, used
for downloading media off YouTube:


```bash
# No special options needed for video
cat youtube-videos-day1.txt youtube-videos-day2.txt | xargs youtube-dl

# Use -x for 'extract audio'
cat youtube-music.txt | xargs youtube-dl -x
```

Storing lines like the ones above in a shell script file, you don't
have to remember all the flags/ettings for `youtube-dl`, and you can
just drop in text links in an intuitive way into the appropriate text
files.

This example too could be done with `find`, matching `-name` or some
other option as in,

```bash
# No special options needed for video
find . -name "youtube-videos*" -type f | xargs youtube-dl
```

What is cool here is that you can separate the more complicated part
of what you're doing (e.g. setting up some options with `find`;
reading some stuff from a file that may be created through a
complicated procedure) from a relatively simple command you want to
run (e.g. `youtube-dl`). Editing the `...| xargs <COMMAND>` is not so
bad even if the stuff that comes before it is difficult to figure out
the first time.
