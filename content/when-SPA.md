title: Uses and Misuses of Single Page Web Applications
date: 2020-11-05
category: Interwebs

Today, there are a handful of popular **Web Frameworks** including
React, Angular, and Vue. What these things do is allow you to use more
*programatic* ways to spit out websites made of HTML, CSS, and
JavaScript rather than writing the HTML, CSS, and JavaScript directly.
The things these web frameworks make are often called **single page
applications** (SPA) because they involve going to one URL with
**dynamic data** as opposed to having you click links to navigate
through *multiple* pages. A popular example of a very complex SPA is
Facebook (also the company that creates the React library mentioned
above).

The Dynamic Web App
===================

Web Frameworks offer ways to automate tasks such as, repeating
elements. These are the bread and butter of SPAs&mdash;relatively
homogenous data presented in pretty UIs.

For instance, on a "newsfeed", you may have a bunch of posts
structured like,

```html
<user-post>
    <author>Alan</author>
    <message>
        Don't believe everything you see and hear on TV!
    </message>
</user-post>

<user-post>
    <author>Joe</author>
    <message>
        Do I hear MALARKEY rising?
    </message>
</user-post>

<user-post>
    <author>Donald</author>
    <message>
        Coofefe through a mask. what a day.
    </message>
</user-post>
```

A user that visits your dynamic web app sees this data rendered to
their web browser, whether on a laptop, phone, or tablet.

Data like that above will typically *not* be "hardcoded" as it is in
the example above. Instead, you will likely have some external site (API)
that gives some data like,

```json
[
    {"author": "Alan", "message": "Don't believe everything you see and hear on TV!"},
    {"author": "Joe", "message": "Do I hear MALARKEY rising?"},
    {"author": "Donald", "message": "Coofefe through a mask. what a day."}
]
```

...and then that data will be "digested" by a web app "frontend".

```jsx
posts.map(post =>
    <user-post>
        <author>{post.author}</author>
        <message>{post.message}</message>
    </user-post>
);
```

An analogy I often give for this is that... the "web framework" makes
a nice looking bathroom: sink, shower, etc. The backend is the
delivery of the water to the proper places. Web developers are
"Internet Plumbers".

The Web "App" versus the Web Site
---------------------------------

Looking for a job in "coding", you'll probably get most people telling
you to go and learn one of the web frameworks mentioned here because
they are a popular way for large companies to make websites. Social
media sites like Facebook, Twitter, and the like make use of these
sorts of things. For these sites, it makes sense to have fancy ways
for generating *dynamic content* because they are constantly updating
their databases with things people (and robots) produce and displaying
these things to users as they come in.

It makes sense why companies like Facebook, Google, and Twitter have
been at the forefront of making many of the modern technologies we use
today when you think about the sort of content they deal with and at
the massive sacale they strive for. These sites value things like,

- Interactivity (users clicking buttons, typing stuff)
- Huge quantities of data
- Ease of integrating advertisements, third party components, and
  other avenues of monetization

In contrast, on a "traditional" website, you cannot get data in "real
time". It is necessary to refresh webpages to *ask the server* for new
information. "Traditional" webpages are more like books, pamphlets, or
brochures that don't frequently update but nonetheless may contain
lots of valuable information presented (hopefully) in an accessible
way. It is more common for "traditional" websites to have many
custom-made, unique pages as opposed to homogenous "posts" or "tweets"
which restrict what kind of content users can post.


Choose the tools for the job
----------------------------

The modern web framework is built for making **web applications**
(apps) that deal with dynamic data. Implied with *dynamic data* is
interfacing with some kind of database, which often means using a
cloud provider like Amazon's AWS or Microsoft's Azure. Creating a web
app often means committing to working with certain big companies,
using technology you may need to update, and learning more complex
tooling.

As the attractive high paying sort of web jobs will often mean working
with big clients in government, NGOs, and big corporations who collect
lots and lots of data, specializing in making dynamic web apps is a
popular career path for technophilic individuals who want nice things.

On the other hand, making a traditional website can be relatively
straight forward. There are many very smart people who have their own
websites, but but care less about fancy styling. For example, a
college professor may just want to link some publications, give a
contact address, and post one photo. This is not hard to do and
doesn't require hiring a full-time developer.

It isn't really fair to compare an individual's homepage with
Facebook&mdash;asking which is *better* is kind of non-sensical
because they are really two different things. One is a fancy kitchen
sink hooked up to straight to the US government and another may just
be a weekend project for sharing family recipes.
