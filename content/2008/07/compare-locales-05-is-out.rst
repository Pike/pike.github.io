compare-locales 0.5 is out
##########################
:date: 2008-07-25 07:35
:category: L10n
:tags: L10n, compare-locales
:slug: 2008/07/compare-locales-05-is-out

I just uploaded compare-locales 0.5 on pypi. To update your current install, use

easy_install -U compare-locales

This is the new version that can handle mozilla-central. There are two main features that were required to do so:

-  Not get the directories to compare from client.mk.
-  Drop the default path for l10n directories.

The latter was already an optional parameter to compare-locales, and is now mandatory. This is mostly because with hg, you'll more likely end up with several local repos representing branches or items of work. You just point which source to compare to which tree, and you're done.

The first change is a bit more drastic. I created new files to hold the information about which directories actually contribute to the localization of an app, for Firefox on mozilla-central, cvs trunk, and the 1.8 branch, and for Thunderbird on cvs trunk and 1.8 branch. Now that cvs trunk is dead for shredder, we'll need a new one on comm-central. I suggest to put those files into $(APP)/locales/l10n.ini, you can take a peek at `the browser one on mxr <http://mxr.mozilla.org/mozilla-central/source/browser/locales/l10n.ini>`__. As you can see, it pulls the toolkit information in from a seperate ini file. If you're creating an l10n.ini file for your app, feel free to CC me on the bug and request my review.

The main change for localizers is that you call it differently. It doesn't really matter anymore from where you call it, just make sure that the first argument is the path to the l10n.ini, the second argument is the base dir for the localizations, and then list the locales that you want to compare. There is a remaining constraint in that the l10n base dir needs to have the localization in a subdir with the same name as the locale code.

compare-locales browser/locales/l10n.ini ../l10n de fr hi-IN

would compare German, French and Hindi Firefox localizations.
