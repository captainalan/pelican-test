title: Create React App: An Entry Point into "Modern" Web Development
date: 2020-05-18
category: Interwebs

Introducing React
-----------------

A popular way to build websites these days is to use
[React](https://reactjs.org/), which is officially described as "A
JavaScript library for building user interfaces".  With React, you
write JavaScript which does stuff in a "virtual DOM" rather than the
(browser's) DOM directly. In this way, you can work with some nice
abstractions that get "compiled" down to stuff a browser understands
natively.

To use React, you only need one web page&mdash;we'll call this
`index.html`. You use JavaScript to "inject" everything into some
root. Using React, you will assume your users have JavaScript enabled
in their browser.

```html
<noscript>u need javascript</noscript>
<div id="root"></div>
```

Using JavaScript to simulate different pages (by rendering different
"components"), you can provide users with a very fast-feeling
experience. This is because instead of requesting new pages form a
server when you click around your web app, you are just shuffling
around stuff in the aforementioned "Virtual DOM" using React's
(JavaScript) library. The result is near-zero "loading time" switching
between complex views which need not be organized in static "pages".


Using Create React App to skip the setup
----------------------------------------

Beginners with React typically start building apps using a tool called
[`create-react-app`](https://github.com/facebook/create-react-app).
This tool gives a basic working app ("website") with a bunch of fancy
features ready to be used. For example,
[webpack](https://webpack.js.org/)&mdash;a "modular
bundler"&mdash;already comes set up and ready to use. You can write
your JavaScript app in a bunch of files, use `imports` and stuff and
rely on the default setup to package up everything together to be
deployed to the web. You can get a flying start trying out things like
JSX (HTML-looking JavaScript syntax used with React). Since
`create-react-app` is a pretty popular tool, it is convenient to
search stuff like how to deploy an app created with this tool to
places like [GitHub pages](https://pages.github.com/) or
[Netlify](https://www.netlify.com/).

Using `create-react-app` is how I personally got started with my
programing career [^1]. I heard React was the hottest, latest and
greatest technology so I went and learned the basics using
`create-react-app` so I could go find work.

Assuming you have `npm` installed, you can start using
`create-react-app` by calling [^2],

```bash
npx create-react-app name-of-my-new-app
cd name-of-my-new-app # Navigate into the directory of your new app
npm start # Start the development server
```

The newly created app will contain a `README.md` file that includes
instructions on how to do some basic stuff.

Typically where people go from here is to open up their new app
directory in VS Code, which has big bucks (Microsoft) behind it as
well as armies of people making extensions and stuff.

What is nice
------------

The set-up described above is not so difficult to do. You can start
using fancy features like cutting-edge new JavaScript syntax right
away.  You can create a production build with `npm run build`. You can
expand what `create-react-app` gives you by installing new packages.
The already-bundled script allow you to think less about setup and
config and focus your energies on doing things like making stuff
pretty with CSS and following the official docs on ["Thinking in
React"](https://reactjs.org/docs/thinking-in-react.html).
You are well-equipped to enter the "React cult".

Where trouble begins
--------------------

Overally, as a tool for getting started and trying out some new
technology, `create-react-app` is very nice. It can be dangerous to
use, however.

The more complex of a job you are trying to do, you will find that you
will butt heads with `create-react-app`. You are given many
pre-configured *layers of abstraction*, set up for getting to work
quickly. When something goes wrong or when you need a new specific
functionality, it may be necessary to "look under the hood" and find
out "how the sausage is made".

In this way, the "flying start" granted by `create-react-app` may
cause more trouble for you than it helps because it encourages you to
use all sorts of things you are not familiar with.

More experienced developers than me tell me that they more often than
not *do not* use `create-react-app` because if they are trying to do
something specific, it is easier to start from smaller building blocks
and build up a nice configuration. This is not too unlike the attitude
of many Linux "power users" that that prefer to start with something
like Debian or Arch Linux (relatively few default packages to start
with) rather than installing a more "user-friendly" distribution like
Ubuntu.

For smaller, more isolated problems or reproducing examples of
specific issues, there are tools like
[codepen.io](https://codepen.io/) which require no installation on
your part. Other setups, such as
[GatsbyJS](https://www.gatsbyjs.org/)&mdash;a static site
generator&mdash;will use React with a different configuration than
`create-react-app`.

More general issues
-------------------

Oftentimes, reaching for a popular "modern" solution like React is the
gut reaction for developers. Personally, I began learning React
because there were lots of job listings that mentioned it.

The conveniences given by tools like `create-react-app` encourage
(new) developers to jump into complicated technology "stacks" because
it is easy to introduce a huge lump of technology with minimal effort
at the beginning.

There are many costs, however, to pay after enjoying this initial
convenience. A big one for beginning developers is having a big pile
of technology of which you understand little to nothing of many of its
parts.

The pain of working through setting up a new project with a complex
tech stack is instructive in that it encourages you to think about why
it is(n't) worth it to introduce XYZ new and fancy
feature.

It is for this reason that many more experienced developers than me
recommend focusing on fundamentals such as (vanilla) JavaScript, HTML,
and CSS on the front end plus some knowledge of how HTTP works, what
good structures in databases look like, and common practices for doing
things like authentication and handling file uploads in backend code.


[^1]: I was in graduate school in the social sciences; I decided to
    start looking for work in web development. *Note:* "programing" is
    not a typo; this is the preferred spelling of Great Web Historian
    [Xah Lee](http://xahlee.info/).
[^2]: Consult the [official
    documentation](https://reactjs.org/docs/create-a-new-react-app.html#create-react-app)
    for the latest instructions.
