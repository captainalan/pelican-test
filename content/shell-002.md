title: Practical Shell Scripting, Part 2
date: 2020-05-20
category: Linux

In this post I will discuss a relatively straightforward command:
`cat`.  The `cat` command is used to *concatenate* files. So if I had
three files, I could do something like

```bash
cat file1.txt file2.txt file3.txt
```

...and this would display the concatenated content of all these files
to standard output.

A Common Beginner's Mistake
---------------------------

Do not use `cat` with just a single file, piping to another program.
You should instead just use that single file as input to the program
you were piping to.

For example, rather than doing

```bash
# Looking for where I talk about feelings in my_file.txt
cat my_file.txt | grep "feelings"
```

...you should just do,

```bash
# Looking for where I talk about feelings in my_file.txt
grep "feelings" my_file.txt
```

There are efficiency reasons for doing things this way, but most
importantly you don't want to look silly in front of scoffing
neckbeards.

Some better uses of `cat`
-------------------------

There are lots of places where it is good to have `cat` around,
particularly where plain text files are being used&mdash;`cat`
probably won't be too useful manipulating images, dealing with audio
files, etc.

However, dealing with little chunks of human readable text (such as in
log files, short scripts, etc.) `cat` often comes in handy.

### Entering short amounts of text really quickly

If you don't wanna open an editor, you can do

```bash
cat >> foo.txt # Append text fo foo.txt
cat > bar.txt  # Redirect (and replace) text fo bar.txt
```

### Reading a bunch of stuff in `less`

To view/read mixed files on one screen, you can do something like,

```bash
cat file1.txt file2.txt file3.py | less
```

This could be useful for looking at a bunch of mixed/scattered
information in a directory at once, creating an on-the-fly "custom
view".

Organizing with `cat` in mind
-----------------------------

In this post, we looked at `cat` which is not a terribly complicated
command.

If you can remember what `cat` does and also know when it is not so
useful, this is great! One less thing to look up!

Knowing that you have `cat` beside you and that you can likewise
expect it to available in nearly any UNIX environment you may find
yourself working in, you can create files knowing you might use `cat`
with them.

Suppose, for instance, you keep track of groceries to buy on in a
directory on your computer: `shopping/`. You might have a series of files:

- `vegetables.txt`
- `meat.txt`
- `grains.txt`

When you run out of lettuce, you might do `echo "lettuce" >>
vegetables.txt` to quickly add an item to your TODO list.

You can view various combinations of these lists using,

```bash
cat vegetables.txt meat.txt | less
```

You can also use your shell's globbing functions with commands like
[^1]

```bash
cat *.txt # hitting tab will autocomplete filenames
```

What you have with cat is a kind of duct tape to smash files together
in many ways; this allows you to create "dynamic views" of textual
content. Combined with tools like `less` (used for viewing text files
quickly) the possibilities are endless.

[^1]: This worked in `zsh`; didn't try elsewhere yet
