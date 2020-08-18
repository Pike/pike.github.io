white russian
#############
:date: 2008-07-22 15:38
:category: L10n, Mozilla
:tags: buildbot, L10n, Mozilla
:slug: white-russian

Where do we go, sings Marillion. In this context, rather, where do my thoughts go.

l10n builds it is again. I'm currently working on porting my buildbot work over to buildbot 0.7.8, and prep it for mozilla-central. There are a few interesting points:

-  0.7.8 is not released yet. Finding bugs, fixing bugs, `reporting back upstream <http://thread.gmane.org/gmane.comp.python.buildbot.devel/3226/focus=3260>`__.
-  0.7.8 has scheduler properties. Drop all the fuzzyness about queues in schedulers etc. Just set up properties right away. Smoooooothness. Lost merging builds for now.
-  mozilla-central doesn't have l10n configuration in client.mk. That's `bug 445217 <https://bugzilla.mozilla.org/show_bug.cgi?id=445217>`__, landed on hg and various cvs branches. This change goes along with various changes to compare-locales, which I haven't released yet.
-  As I don't have to call into client.mk anymore and read the config data from plain files instead, I can do that asynchronously (more easily). My master just starts up now.

All in all, interactions inside the l10n build scheduling are much easier to grok thanks to scheduler properties.

To add some cream to the milk, here's how I picture l10n builds to go one day:

-  pull central (and friends for Thunderbird, SeaMonkey)
-  pull and update to tip for locale to build
-  for the most performant platform:

   -  update central and en-US to tip
   -  compare-locales with rich reporting to dashboard and siblings
   -  possibly other source verification and test code

-  update en-US to nightly changeset
-  compare-locales with merge, fail on error
-  repack, fail on error
-  upload binaries

The source analysis step is going to be the important one to be used for the dashboard, as that needs to have the most current information.

The actual builds on the other hand will be generated against the changesource for the last nightly, i.e., they will merge in en-US content based on the right data, and will only fail on rare occasions where the merge is harder than necessary, or when there are plain bustages in the localization.

In case you really want to know, the patches I'm currently working on are in a `public hg queue repo <http://hg.mozilla.org/users/axel_mozilla.com/tooling-patches/>`__.
