l10n-merged linux builds on the l10n server
###########################################
:date: 2008-10-21 14:43
:category: L10n
:tags: build, buildbot, L10n, Mozilla
:slug: 2008/10/l10n-merged-linux-builds-on-the-l10n-server

I reached another milestone on the l10n builds on the l10n server - reliable l10n depend builds.

A short recap on why they could not be reliable. Details are in `Armen's and John's presentation in Whistler <http://docs.google.com/Present?docid=dnkkbhp_95dkvbbzgt&pli=1>`__. First and foremost, l10n builds with missing strings break. They might start, or not, maybe even crash. Or just display the yellow screen of xml parsing death. Now, l10n builds are not really builds, but repackages of an en-US build. Between the time that the en-US build started, or, in hg, the revision it used, and the tip at the time when the en-US binary is finished and available, there can be further l10n-impact landings. We are using the nightly builds for the repackages throughout the whole day even, so the chance that the current en-US source doesn't correspond to the nightly increases. So even if you know that a localization is good tip vs tip, you can't say if it's breaking the previous nightly or not. Huh? Look at the graphs in Armen's and John's presentation for more arrows going back and forth in time. ;-)

Enter bugs `452426 <https://bugzilla.mozilla.org/show_bug.cgi?id=452426>`__ and `458014 <https://bugzilla.mozilla.org/show_bug.cgi?id=458014>`__. 452426 added the changeset id to application.ini (thanks Ted), and 458014 refactored browser/locales/Makefile.in with additional logic to extract that info for the build system. I got that one landed yesterday, so we can now get the source stamp of mozilla-central for a firefox build.

Right, good catch, this doesn't work for comm-central builds. I'll leave it up to them to figure out how to reproduce the plethora of repos they have.

So far, so good. You download the nightly, unpack, ident (the rule to extract the changeset id). Now you back to your source tree and hg update to that revision, and run compare-locales against that. We'd be able to reliably say "works" or "better don't touch".

We promised more, and more pieces came together today.

With reliable compare-locales code, one can not only detect missing strings, but also add missing strings to files. Think about a CPP step, nothing permanent, nothing gets landed upstream. But just for the needs of this particular build, you'd have something that has all strings. Not all translated, some padded from en-US. That works. compare-locales is already able to do merges for a while now, storing the changed files into a separate location. Mostly because I consider changing the source to be evil. So what about missing files? Nothing. Good files? Nothing. How does the build pick up files from merges, l10n, **and** en-US then?

By rewriting make-jars.pl, enter JarMaker.py. Among overall readibility improvements and removing XPFE hacks, JarMaker.py offers to pick up l10n files from a list of top-level source dirs.  It offers another cute feature, by writing both chrome and extension manifests at once. Now, with bug 458014, we don't have to run the libs phase for installers and langpack separately. (I never got why we do that until I rewrote make-jars.pl, actually.) The rewrite of JarMaker.py was preceeded by rewriting Preprocessor.py, so that all of the jar generation can happen in a single python process.

Starting from today, all of this came together with my installation of buildbot on the l10n server.

This gives us

-  builds on push, i.e., feedback within 5-10 minutes (real stats pending)
-  comparisons of the l10n tip against both

   -  the en-US tip (for the upcoming nightly)
   -  changeset of the previous (for the existing nightly, with l10n-merge)

-  html-ified output for both of those
-  updates for the dashboard

and last, but not at all least, a

-  working build, even for partial translations.

Find 60 3.1b2pre linux builds on the `l10n server <http://l10n.mozilla.org/~buildslave/fx31x/>`__.

Thanks to Armen, I used a few of his new makefile targets for download and upload, he did a bunch of work for the sourcestamps-in-application.ini on cvs, too. Thanks to Ted, the poor fellow had to review all my rewrites and Makefile dependencies foo, and did some patches, too. hgpoller stuff not to forget.

TODO:

-  silme will offer even more reliable merges
-  nightly scheduler for all locales (currently I only build on l10n and en-US l10n-impact changes) (*)
-  mar's
-  comm-central
-  more Makefile foo to pick up more missing files from en-US in doubt... (*)
-  ... or at least document the core set of required files (*)

I won't take most of those, fwiw. Possibly only the (*) ones.

Sources are in my `tooling repository <http://hg.mozilla.org/users/axel_mozilla.com/tooling/>`__, and there's an updated version of compare-locales, 0.6, on pypi. No drastic changes here, just some paths fixes, mostly for Windows.
