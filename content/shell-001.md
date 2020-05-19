title: Practical Shell Scripting, Part 1
date: 2019-05-19
category: Linux

In this series of articles, I will document how I do various things
using shell scripts[^1].  My basic approach is to use `bash` to
automate stuff by documenting and replicating steps that I take on the
**Command Line Interface** (CLI) [^2].

Preliminary things
------------------

It is assumed the reader has basic working knowledge of doing things
like navigating around directories, deleting files, using some editor,
etc. No knowledge is assumed of using specific tools like `find`,
`xargs`, `curl`, etc. Much of the content here will be treating how to
do useful things using those tools.

### Additional Setup

There is a utility called [ShellCheck](https://www.shellcheck.net/)
which may be helpful to set up with your favorite editor/development
environment. This tool can help you find common mistakes in your shell
script code *before* you even try to run it.

### Methodology

When there is something that I want to do (on Linux), I'll try to do
it all via the command line. Anything non-trivial that I might have to
do again I'll want to document somewhere so I don't have to bother
figuring out the annoying aspects again. Comments can be written to
explain non-obvious choices.

Shell Scripts as Duct Tape
--------------------------

First, my "User Philosophy"!

On your computer, you have many programs that can individually do
useful things. Shell scripting is the *de facto* way to smash a bunch
of programs together to do more complex tasks for you.

Shell scripting is different from "programing" in the sense that you
are often dealing with relatively high-level structures, understanding
*what* programs do without needing to concern yourself with *how* they
do it. In this way, you leave it up to the "real programers" to take
care of things like optimizing their programs to be efficient. Your
job is to just make sure that things hold together "good enough" with
duct tape.

Over time you can refine your programs to be better. What is most
important is to get the job done and not get to hung up on what is
best. It is better to write more shell scripts, gradually learning
what is "best" among the many options to do things than to get hung up
on some esoteric problem too long.

Careful engineering is the realm of using more full-featured,
complexity-friendly programing languages. You can write programs in
other languages and call them from shell-scripts if you have to do
something particularly complicated that your default tools cannot
handle so well (e.g. write a parser for a new custom file format you
created).

Where's my Search Bar?
----------------------

MacOS has a fancy search feature you can use by pressing COMMAND+SPACE
by default. When you do this, you can type words, and MacOS will scan
your computer in who-knows-what-way for the text you are entering and
stuff the OS guesses might be related. Windows Explorer has similar
search features too, I think. How do you do something similar on
Linux? [^3]

Suppose, we want to list all the Markdown files in a directory (`.md`
extension). Using `find` this can be done in
one line.

```bash
# Find all markdown files in my blog directory
find my-blog-directory -type f -name "*.md"
```

We can extend this command to do something else, for example, find all
instances in these files of the word "foo". Below, we build off our
previous command which found all markdown files in a directory by
adding the `-exec` flag and specifying a command to run on each of the
files that `find` finds.

```bash
# Search markdown files for text "foo"
find my-blog-directory -type f -name "*.md" -exec grep "foo" {} +
```

One kinda annoying thing about working with (UNIX) shell scripts is
that each (utility) program will have its own idiosyncratic syntax.
In the case of `find`, you're going to specify options using `-thing`
(in this example we specified the *type* of thing we wanted to find
and a pattern for the *name* to match).

There is some additional special syntax here. When we run the `-exec
grep "foo" {} +`, the `-exec {} +` syntax tells `find` to run the
given command (in this case `grep ...` for each file found, where `{}`
will be where the filename is inserted.

As with natural language, fluent speakers don't spend all day thinking
about how grammar works while they are talking [^4]. Instead, they
remember common patterns that they use frequently. Stuff like the
`find` syntax above is confusing at first, but is something you will
get used to pretty quickly if you use it frequently.

Smashing Together More Things
-----------------------------

The previous command we built up can be used to do all sorts of stuff
since `-exec +` allows us to call *any program*.

For example, let's suppose we wanted to get a whole bunch of YouTube
links to download and watch later. How do I get all the YouTube links
from my the markdown files in my blog directory?

```bash
# Search markdown files for links to YouTube
find my-blog-directory -type f -name "*.md" -exec \
grep -h -o "youtube\.com\/watch?v=[[:alnum:]]*" {} +
```

With `grep` I used the `-h` option to *hide* the file name of the file
I'm currently searching and used the `-o` option to *only* show the
matched text, not the whole line of the regular expression I used.

The output of this command can be saved into some file for further
processing.  For example, you can use `youtube-dl` to help you
automatically download all the links you just collected while
you go do something else.

General Lessons from `find`
---------------------------

You may find that after using shell scripts to do stuff for some time
you begin to think about how you can do things like naming files
consistently to make things like pattern matching via globbing easy.

In the examples I gave above, I relied on file extensions (`.md`) to
do my file finding. However I might want to process a bunch of files
starting with `my-diary-`, for instance.

Naming files and organizing directories in a way that makes sense for
easy processing is akin to setting up an SQL database with
well-planned tables; it may take more effort to start doing this
initially, but your efforts may be rewarded later down the road.


More links and resources
------------------------

Relating to content discussed in this article:

- [35 Practical Examples of Linux Find
  Command](https://www.tecmint.com/35-practical-examples-of-linux-find-command/) (Ravi Saive 2012)
- [Bash Globbing Tutorial](https://linuxhint.com/bash_globbing_tutorial/) (Fahmida Yesmin 2018)


[^1]: For the most part, I'll be using `zsh` and doing `bash`
    compatible things. The stuff I'm doing should all work on a pretty
    default set-up with a major distribution (e.g. Debian, Arch) where
    you can easily install common programs.
[^2]: See Luke Smith's video ["Terminal vs. Bash vs. Command Line
    vs. Prompt"](https://www.youtube.com/watch?v=hMSByvFHOro) (Dec. 2, 
    2019) for clarification on terminology.
[^3]: I'm just going to use the word "Linux" here to describe a UNIX
    computing environment where you can easily install certain common
    programs. There is no time for me to quibble over GNU/Linux vs BSD
    vs whatever!! Life is too short!!
[^4]: After-hours linguistics discussions are OK.
