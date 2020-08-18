compare-locales 0.9.6
#####################
:date: 2012-06-07 04:32
:category: L10n, Mozilla
:tags: compare-locales, L10n, Mozilla
:slug: compare-locales-0-9-6

I've updated compare-locales with two important fixes:

-  License header fix for ini files, `bug 760998 <https://bugzilla.mozilla.org/show_bug.cgi?id=760998>`__
-  l10n-merge now works with multiple errors per file, `bug 756448 <https://bugzilla.mozilla.org/show_bug.cgi?id=756448>`__

I've also updated the license to MPL2.

Update your local installs with the usual commands, like

``pip install -U compare-locales``

The l10n dashboard is already running the new code, I'll file a bug to get the production builds updated probably tomorrow.
