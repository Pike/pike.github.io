compare-locales 0.9.1 is out
############################
:date: 2010-11-24 07:30
:category: L10n, Mozilla
:tags: L10n, Mozilla
:slug: 2010/11/compare-locales-0-9-1-is-out

I released compare-locales 0.9.1 yesterday on pypi. Do the regular

   ``easy_install -U compare-locales``

to update your local copy.

This update includes two bug-fixes compared to `0.9 <http://blog.mozilla.org/axel/2010/10/04/cl09/>`__,

-  Don't warn about XML-defined entities like &amp;, `bug 604404 <https://bugzilla.mozilla.org/show_bug.cgi?id=604404>`__
-  Ensure that merged entities have a trailing newline, `bug 612619 <https://bugzilla.mozilla.org/show_bug.cgi?id=612619>`__

In particular the latter will make our l10n-merge code more stable. Sadly, we actually need to fix all the newly-reported errors in all stable branches and apps before we can update the production tag. Errors make compare-locales fail, and rightfully so. And fail is bad for release builds that don't merge, also rightfully so.
