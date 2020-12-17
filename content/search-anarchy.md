title: Modern UIs and the Rejection of Hierarchy
date: 12-16-2020
category: Linux

I've been doing some listening/watching of Jonathan Pageau's [Symbolic
World](https://thesymbolicworld.com/) content which has got me
thinking about symbols and meanings of lots of things around me. In
this post I want to share a brief analysis of *ways to interact with a
computer* and how even in this area we see a *leveling of hierarchy*.

File Hierarchies
----------------

Those familiar with Linux or any UNIX based operating system will know
that the typical organization of a systems's files is hierarchical.
Typically there is soom *root* denoted `/`. Below that there is often
a directory `/home/` under which users will have their personal files.
My user files are under `/home/alan/`, for instance. Users can then
organize their files further with directories like
`/home/alan/Documents/`, `/home/alan/Downloads/` and so on and so
forth.

Like a tree where each branch becomes a "mini tree" in a kind of
recursive process, we can see that individual projects/programs often
employ a similar structure. Using the `tree` utility, for instance, I
can view the hierarchical structure this very file is found in.

```
├── content
│   ├── [...]
│   ├── corona-virus-001.md
│   ├── corona-virus-002.md
│   ├── corona-virus-003.md
│   ├── [...] 
│   ├── qwerty-theory.md
│   ├── search-anarchy.md
├── Makefile
├── [...]
├── README.md
└── tasks.py

```

Each file has its place. To use a **static site generator** you must
put files in their correct place&mdash;alongside other similar
files&mdash;otherwise you probably won't get the result you're going
for [^1]

To become familiar with a system or software project, you will need to
learn *where to find everything*. That is, *what are the positions in
the hierarchy* and which files to go to in order to change the
program's behavior. A skilled developer or administrator will know
many quirks or tricks of some particular system.

Skilled developers of course aim to make systems that are easy to
learn about and scale readily.

The Flattened Search-based Model
--------------------------------

The MacBook tries to get rid of the need to understand file
hierarchies and become familiar with projects like in the examples
above. Using the Finder application, users simply *search* and the
computer (rather than the user) is tasked with finding the relevant
files.

You have probably met someone with a very messy (computer) desktop.
Today's powerpoint, last week's powerpoint, and e-mail attachments
from some party you probably don't need to know about all litter the
same (digital) space of the disordered desktop. For this sort of user,
the Finder approach provides much help&mdash;nowdays, you might not
even need to choose meaningful *names* for files because the Finder
application might search *within* files and make up keywords based on
their contents. So `Unnamed document.docx` might contain the words
"biology homework" and a search for "Biology" might be able to point
to this file even though the user didn't even bother to give it a
meaningful name.

The Finder approach thus allows (or even *encourages*) a sort of
"organizational bankruptcy"&mdash;giving up on keeping stuff
well-ordered. You might as well dump everything into a folder called
"Stuff" and let Finder retrieve the appropriate file(s).

Smartphone App Prison
---------------------

The smartphone app model involves making a kind of "jail" for each
thing you do&mdash;an e-mail app, a music streaming app, a fitness
tracking app&mdash;whereby *integrating* data between the many things
you do is not easily done on a phone. Unlike on a desktop PC where you
might pull up a spreadsheet alongside a word processor and write up an
analysis or a report on last week's sales, the smartphone shafts most
things into one small self-contained video-game-like interface.

There are some security and marketing advantages to this&mdash;of
course you don't want your app getting compromised because of a
security flaw in someone else's app&mdash;likewise you want to be able
to monetize *your* product.

But these advantages are more important for the *makers* of the apps
rather than the *users*. It shouldn't matter much where a good tool
comes from as long as it works well, and you shouldn't have to
constantly think about its special features&mdash;it should seamlessly
facilitate your work as a kind of extension of your body.

Apps invert this relationship whereby tools are an extension of your
body. Instead, *you* become a *data point* in an app's network. Rather
than you exercising agency over a tool, popular apps to gather usage
statistics on *you* and charge *you* for how you use the app. The tool
profits from you using it. You are the eyes, ears, and mouth of the
app&mdash;the app makes you accept all liability for using it and can
be taken from you at any time.

Choosing tech, configuring for success
--------------------------------------

If you're not going to spend much time with technology, it probably
doesn't matter very much what you do. Most people I know, however, are
stuck using computers and phones for many hours a day&mdash;especially
during all this COVID stuff. So we might as well get comfy with how to
best channel these devices to *work for us*.

PCs are often preferable to smart phones. A well-ordered desktop is
preferable to an indifferntiated pile of files and tools. Similar to
how you might choose to furnish a room for particular
purposes&mdash;e.g. as a work room or as a dining room, we can also
set up your computing environments to encourage *time well spent*.

While many aspects of using computers can be annoying, simple
principles that would be applicable for organizing any workspace,
whether online or offline, can help you be more productive and focused
when using digital technology.


[^1]: Here, all the files I wrote are in the **Markdown** format
    denoted by the `.md` extension. To make a new blog entry, I simply
    make a new markdown file, specify information like the title of my
    blog post and the date, and then run scripts in the `Makefile` to
    *make* my website.
