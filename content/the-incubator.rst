The incubator
#############
:date: 2007-04-30 15:21
:category: L10n, Mozilla
:slug: the-incubator

When working on new localizations of Firefox and Thunderbird, it's pretty tricky to get all the tooling right and to distribute your work for testing. In addition, there's no real build environment that tells me how far particular localizations are. That changed, enter the `incubator <http://l10n.mozilla.org/buildbot/>`__. Incubator runs in buildbot for the most part, and calls into the Mozilla build system for the real work. I don't repack builds, as these are really for early testing, I do generate language packs against the last stable release, though. I'm looking forward to the app-agnostic branching for 2.0.0.4, here, too, then the language packs should have a real chance to work against Thunderbird, too. For now, check out the `language packs <http://l10n.mozilla.org/~buildmaster/langpacks/>`__. I'm repackaging the l10n trunk against en-US branch, so we can get lively engineering work on the side of the localizers against a stable and popular target. Thus *incubator*.

The whole thing runs on the l10n server, that is, master, slave and download location. Thanks to Reed Loden for helping me with the set up there.

This is still work in progress, I hope to see our new localizations pound that thing with check-ins to get some testing and experience.

**What works:**

-  Bonsai poller. I whacked that poor creature into oblivion, I need it to support multiple subsets of repositories on different bonsai servers and branches.
-  CVS checkout of that same data.
-  Did I say same data? Yep, I actually have one data structure to create both the change source and the source build steps

**What works not:**

-  Any kind of load balancing or fail over does not work. I do want to stick to the plan to only have the source once per slave, but the concept of "get the source on all my slaves, and then distribute the repacks on them as they come" doesn't seem to exist in buildbot. Partially, you could get there with scheduler.Dependent, but I guess that would stall the complete build if a slave dies.
-  Adding a download link to the waterfall display.
-  Fast update, only check-out what bonsai poller found.
-  Dependency checking in repackaging. In the real world, one should repackage all locales only for changes to en-US, and for changes in l10n only repackage affected localizations. This is somewhat mid-hanging fruit, I guess I could add a .fileIsImportant check to scheduler.Dependent.

As for the Waterfall display, I'm less sure than before that there is a nice way to display all of our locales. Not sure how bad that is, there seem to be ways to select subsets of the waterfall, for example just the `Albanian browser repack <http://l10n.mozilla.org/buildbot/?show=language-pack_browser_sq>`__.

If you happen to be one of the localizers on there, give bonsai 10-20 minutes to pick up your changes. If you'd like to be on there, and you're not, poke me.
