Looking at the internals of our builds
######################################
:date: 2010-11-10 09:34
:category: Mozilla
:tags: build, buildbot, Mozilla
:slug: 2010/11/looking-at-the-internals-of-our-builds

Chris Atlee has put up database dumps of both the `scheduler and the status databases <https://wiki.mozilla.org/ReleaseEngineering/BuildAPI>`__. These databases are the most detailed and (almost, status db is not) first class information on what our builds are really doing. The current code on top of that is all pylons-based, and I am, as many other mozillians, part of the django shop. So for one I figured "let's see if I can make django read this".

I can. It's a bit rough, though, as some of the tables for many-to-many relationships don't contain a primary key column. Django really doesn't like that, and thus there are some things that you cannot do without those columns. Most of it works just fine, though. This holds at least for the status db, which I looked at in more detail, but the scheduler db ain't much different. Filed `bug 611014 <https://bugzilla.mozilla.org/show_bug.cgi?id=611014>`__.

The code for this is up at `django_moz_status on github <https://github.com/Pike/django_moz_status>`__.

Of course, me being able to talk to the db with a python shell won't help you much, right? So I've spent a few more hours to actually create a really rough website on top of it, which I want to share with you.

Coconut. Hard to open, and once you get there, you may not like it. I have a thing with project names.

`Coconut <https://github.com/Pike/coconut>`__ is a bunch of django views on top of django_moz_status, held together by `site_demo <https://github.com/Pike/site_demo>`__. You can see it in action (for now) on the `l10n community server <http://l10n.mozilla-community.org/coconut/sources?count=50&offset=1362437&exclude_empty&branch=mozilla-central>`__. This view is exposing three concepts of buildbot, and how they play together:

Sourcestamps (first column): Every build in buildbot has a sourcestamp, and a sourcestamp can have multiple builds. The sourcestamp knows a branch, a revision, and a list of changes going into the builds associated with it.

Changes (second column): Changes are the external "real life" events that may or may not trigger builds. In this view, you see a few list of changes that look like a push to hg (and are just that), as well as a plethora of changes by Mr. sendchange, and Mr. sendchange-unittest. If you remove some query params on the above URL, you can also see a `bunch of sourcestamps without changes <http://l10n.mozilla-community.org/coconut/sources?count=50&offset=1362437>`__. Those are nightlies.

Builds (last column): Each sourcestamp can have multiple builds, I'm just showing the builder name (a symbolic short name), the buildnumber, and the result as color. The third column is actually a guess on the platform of the build, based on the ``platform`` build property. If that's not set, ``unknown`` is used.

Which brings me nicely to another two pieces of our build infrastructure that has been hard to look at so far. Build steps and build properties. Surf along? Let's look at `a build <http://l10n.mozilla-community.org/coconut/build/1894077>`__.

The first section of the build pages shows some general information, builder, buildnumber, status. The start and end time, how long the build took. Also it lists the buildbot master, and the category of the builder. Categories allow to filter for builds, sadly, a builder can only be in one category.

Next up is build steps. Each step in a build is an item of work, and an entity of failure. Different steps can handle failures differently, too. You can see that the build starts with a flock of steps that do administrative tasks on the slave. You can see which fragment of time of the build that step took by looking at the bar in the second column. You'll see that the majority of that build went into the compile step. And that that passed. And after that compile, there's a bunch of adminstrative stuff again.

There are two things that you do not see. One is, each of those steps has build logs attached to them. Commonly one, but possibly more. I'll talk more about logs in a different post. The other thing is, steps can change the build properties. Which is to say, the build properties which are shown at the end of the build page are not static, but change during the build run.

Build properties? Right, within buildbot, several objects can have properties, among them, builds. You'll find things like the buildnumber, the slavename, the branch, buildername (pretty). You'll also find a host of things around the packaging of the build. Quite generally, our build try to put things that are needed for the build itself or for logic around into build properties.

The end of the page is reiterating which changes are associated with the sourcestamp for this build.

Let me stress your patience once more and invite you to visit a `build with a failed step <http://l10n.mozilla-community.org/coconut/build/1893242>`__. In this build page you can see how the clobber step worked fine, and took quite some time, and the actual status of the build is due to the actual test step failing with a warning.

Now this post is already pretty lengthy, so I'll take a break here and invite you to go in and click back and forth a bit, and to do some url hacking. If you think this is rough and you're having a hard time figuring out what's why, I'll do a follow up post on how to add chocolate to coconut.

PS: the database this instance is working on is a snapshot that ends in August, details may be different today. I shrunk the database, too, only the last 10k builds still have the buildsteps.

Update: Changed the links to the l10n community server.
