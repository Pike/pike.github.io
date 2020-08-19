Fennec added to l10n dashboard
##############################
:date: 2009-02-27 10:45
:category: L10n
:tags: Fennec, L10n, Mozilla
:slug: 2009/02/fennec-added-to-l10n-dashboard

I just added Fennec localization stati to the `l10n dashboard <http://l10n.mozilla.org/dashboard/?tree=fennec10x>`__. It's only pretending to do arm linux tgz's right now, and it's not uploading them anywhere. I expect that will happen soon on the main build machines.

There were a few funky edges to make fennec build similar to what we have in Firefox now. Most notably, Fennec uses a completely different directory structure, which looks really familiar once on disk. The main difference is that when Fennec developers check in to a file in ``mobile/locales/en-US/chrome``, that file is actually in ``locales/en-US/chrome`` in the repository. When a localizer catches up with that change, they're really landing to ``ab-CD/mobile/chrome``. That requires some special hooks in the code that watches for l10n changes on the build master. The biggest hurdle was surprisingly the all-locales file in the end. That just blew the logic I had. I'm now loading the all-locales file by assuming that it's right next to l10n.ini, while I'm still using the path to all-locales in l10n.ini to control what the AllLocalesWatcher pays attention to, to update the list of all-locales in the master when that's changing in the repo.

What I really like is that we're adding this product to our localization story in good shape. In my little universe, the big winner is that we're starting with l10n-merge working. Thanks to mfinkle's timely reviews, I added logic to the build to export both the gecko and the fennec revisions of the en-US build that's repackaged, so one can run compare-locales (with or without l10n-merge) against the sources that actually went into the build. This is really important to get the missing strings right, and to ensure that the build is working as good as it can.

So, localizers, now is the time to land. Please make sure to touch base with Stas on any questions regarding web services. Using what we have for Firefox is a good base, though. Gandalf can help with general technical issues, as can I. If you're not part of the fun, and want to join, please `file a bug <https://bugzilla.mozilla.org/enter_bug.cgi?product=Fennec&cc=l10n@mozilla.com>`__.

We're well aware that you'll need a descent infrastructure to test with. What is most important to you guys? Leave a comment on this post?
