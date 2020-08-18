l10n buildbot update
####################
:date: 2008-07-24 15:31
:category: L10n, Mozilla
:tags: buildbot, L10n
:slug: 2008/07/l10n-buildbot-update

I've updated the buildbot master and slaves running on the l10n server in the last few days.

There have been a few reasons to do so:

-  for Firefox 3.1 localization, I will need an updated compare-locales
-  ... and support on the dashboard
-  there's a new buildbot 0.7.8 around the corner
-  ... which offers scheduler properties, which make l10n buildbots sooooo much nicer
-  and, hrm, I had bugs to fix in the history view

For a while now it was obvious that the code running the buildbot on l10n.mozilla.org would be much nicer and easier to grok, if it used the new features upcoming in buildbot, namely, scheduler properties. I've been doing some weird hacks to get around the lack of those on buildbot 0.7.7, and nobody liked those, including me.

Luckily, it wasn't hard at all to drop all the weird code I used in favour of scheduler properties, for the most part, it was removing code. For the curious ones among you, have a look at the `crucial diff <http://hg.mozilla.org/users/axel_mozilla.com/tooling/index.cgi/diff/27cafbe24f0d/mozilla/tools/buildbotcustom/buildbotcustom/l10n.py>`__.

The downside of that change is that I needed to update my custom code at a few places that used build properties in the 0.7.7 style. Once I learned the tricks, the patch was rather systematic, though, no real surprises. Again, `there's a patch <http://hg.mozilla.org/users/axel_mozilla.com/tooling/index.cgi/rev/cb6f1833f935>`__ in the original queue for curious folks.

I've followed the buildbot trunk darcs repository since the announcement of the imminent release last week on my local setup, and found a few issues. Which is cool, as those issues are fixed now, and I have a unpatched buildbot 0.7.8pre running on l10n.m.o. This is actually a real treat, as we (the release team as well as I) have been running slightly patched releases of buildbot to fix bustages in the past. And those bustage fixes tended to be slightly different upstream than in our repo, making upgrading to a new version of buildbot a pita.

On top of that work on the backbone, I've `fixed a few timezone issues <http://hg.mozilla.org/users/axel_mozilla.com/tooling/index.cgi/rev/348dbbaa1332>`__ all around, which most apparently broke the statistics pages. They're linked to from the `dashboard <http://l10n.mozilla.org/dashboard/>`__ as history (H). Those most apparently showed when trying to click on the bonsai links. There are blue vertical marker lines for l10n check-ins, and if you click on those, a lens opens with the commiter, the files and the check-in comment. The commiter email is actually a link to bonsai-l10n. UE guidance welcome.

While I was at it, I fixed both the start and end times of the timelines, as well as their display. Now they're actually piecewise constant, as they should be. Ok, they're not. They're still P1, because timline likes that, but they look really close to P0.

Part of the preparations for fx3.1 was the renaming of "trunk" into "fx30x". That should not only enable us to have fx3.1 on the dashboard, but other projects, too. Those required some changes to the existing data archive, in particular the database that I have locally. Those changes weren't too bad, though.

Known regressions:

-  I check out from scratch now on each build. Should be less of an issue on hg. And CVS is stable, and I only check out the locale that I build. Thus resolved WHATEVER.
-  If anybody has links referring to "trunk", those are broken now. "fx30x" is the new name for "trunk".
-  If you find more, `file a bug <https://bugzilla.mozilla.org/enter_bug.cgi?product=Mozilla%20Localizations&component=Infrastructure>`__, comment, or drop me a mail.
