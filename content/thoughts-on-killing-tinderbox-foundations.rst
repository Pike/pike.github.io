Thoughts on killing tinderbox, foundations
##########################################
:date: 2009-05-10 21:45
:category: Mozilla
:tags: buildbot, Mozilla
:slug: thoughts-on-killing-tinderbox-foundations

I figured it'd be a good idea to just dump my thinkings on killing tinderbox (as in the the web interface to mozilla's builds). As just the background information grows to a lengthy post, I'll cut them into pieces.

To point you where I'm heading, the executive summary of my thinking is:

*Killing tinderbox is a webdev problem for the most part, with some chunks in IT and build/releng. The latter two should be fine to mostly do what webdev needs to get the job done.*

I won't give my complete rationale for killing tinderbox, for the most part because I've been thinking about that too long and have come up with too many reasons to write them down. But the most important fragments would be in ...

The Rationale:
''''''''''''''

Tinderbox knows relatively little about our builds, and displays even less. The front end is hard to hack, and the back end is tied to a build model that doesn't match that of buildbot. In particular in our move to hg, things have changed considerably in the back.

Listening in to previous discussions, there seems to be a gap between how people talk about our builds, and what our builds really are. Thus I'll bore the few people that actually hack on our build automation for a few, and dive into ...

What buildbot knows:
''''''''''''''''''''

Buildbot, aka the software we're using to control and run our builds, knows plenty about our builds. I'll give a list of things that come up to my mind, with a focus on things that tinderbox wouldn't.

-  Why a build is running.

   -  Which changes went into this build, or if it was a periodic or forced build

-  The steps of each build, with separate description, results, logs

   -  Logs have separate stdout and stderr chunks in order

-  A set of build properties, holding slave name, build number, revision

   -  The set of build properties can be amended, to hold more data. The data can be basically anything that can be pickled in python, and could be constrained to json values, or just natives thereof.

-  Start and end times for both the individual steps and the complete build

There are some shortages in particular when it comes down to our build setup, mostly ...

What even buildbot doesn't know:
''''''''''''''''''''''''''''''''

-  Dependencies between builds. Buildbot has two builtin methods to run builds that depend on prior builds, but it doesn't keep track of that relationship.

For those into schema, one possible version of that is `depicted in this graph <images/2009/05/mbdb.png>`__.

Then, there are things we keep ...

On tinderbox, but not on buildbot:
''''''''''''''''''''''''''''''''''

-  Tree rules

   -  open/closed (used to be on despot for cvs/bonsai)
   -  sheriff

-  Build comments
-  log parsers

So much for the read-only side of life. On top of this, there are a few important things that buildbot enables us to do, which we don't empower our community to use (at least not without a releng-sheriff around).

Buildbot can:
'''''''''''''

-  Trigger builds on arbitrary builders, possibly with particular properties set (the latter requires hackery).
-  Stop most builds while running.

Exposing these should provide a powerful tool to investigate and clear bustages.

You can get a slightly better idea of how things are looking on buildbot itself if you browse around on `Chromium's waterfall <http://build.chromium.org/buildbot/waterfall/waterfall>`__. IMHO, they share the problem of not being able to present the data they have, even though they have less platforms and trees to handle than we do. You can also see the problem of dependent test builds hanging somewhere in the air. You can also nicely see the output per step with the details they have, unconditionally though. Most of the time, you likely don't care.

Going forward, I'll try to wrap my head around which problems our web frontend to our builds actually needs to solve, and which routes I see to getting there.
