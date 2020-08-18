working demo, waterfall and more
################################
:date: 2008-12-19 16:50
:category: L10n, Mozilla
:tags: build, buildbot, Mozilla
:slug: 2008/12/working-demo-waterfall-and-more

Thanks to Reed, I just put up my latest pet project up on the l10n server.

It's offering a new web interface for buildbot builds. It does so by feeding the status data that buildbot has into a database on the one end, and on the other end is a django app displaying that data.

The nice thing about this is that writing features (or fixing bugs) is "just webdev". Compared to whatever you want to call tinderbox hacking.

There are already a few concepts demoed on the site. All urls are in flux, note the "stage" in them. But the principle should be obvious.

Firstly, you can get to a regular waterfall on `waterfall <http://l10n.mozilla.org/stage/builds/waterfall>`__. Yes, there are some time-sorting issues there. But it's quick, which is cool. Compare it to the `regular buildbot waterfall <http://l10n.mozilla.org/buildbot/waterfall>`__ (didn't bother checking which timerange that shows). And it offers a nice compromise (IMHO) for displaying detail or not. For finished builds, it shows one box per build. For builds in progress, it shows a box per step (it doesn't show a box for the build for those steps, which is confusing). It has a blame column, too. Whenever you see a change number, that links to a new page, which lists all builds for that particular change. `This one <http://l10n.mozilla.org/stage/builds/builds_for?change=23071>`__ shows an en-US check-in with all locales turning red, for example. `Another one <http://l10n.mozilla.org/stage/builds/builds_for?change=23080>`__ just shows how things go green for Arabic again, as that localizer checked in.

For the l10n builds, that's peanuts, but if you're landing on a tree with real compiles, being able to follow all builds for your landing, and no others sounds cool.

And django comes with helpers for generating feeds, so creating a meaningful live bookmark to follow your own landing doesn't seem like an unsolvable RFE.

There's more. You can restrict the waterfall to only show builds for a particular slave. You can restrict the shown builds to only show builds with a particular property, say, the `Macedonian builds <http://l10n.mozilla.org/stage/builds/waterfall?locale=mk&endtime=1229726521>`__, compared to `all builds <http://l10n.mozilla.org/stage/builds/waterfall?endtime=1229726521>`__.

There's obviously lots of room for improvement, the code is in the tinder app in my `hg repo <http://hg.mozilla.org/users/axel_mozilla.com/django-site/>`__. Volunteers welcome.
