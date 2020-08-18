extensions, l10n, and tools
###########################
:date: 2008-11-05 16:15
:category: L10n, Mozilla
:tags: L10n, Mozilla
:slug: extensions-l10n-and-tools

Wladimir Palant has two recent posts on perl scripts he did for helping him in managing localizations for `Adblock Plus <http://adblockplus.org/blog/managing-locales>`__ and `TomTom Home <http://adblockplus.org/blog/managing-locales-now-the-generic-way>`__.

Sadly, Wladimir ignored about a `year of development in the compare-locales work <http://hg.mozilla.org/users/axel_mozilla.com/tooling/log/4f0aed56efbe/mozilla/testing/tests/l10n/lib/Mozilla/Parser.py>`__, and a whole other flock of utilities available as part of the `translation toolkit <http://translate.sourceforge.net/wiki/toolkit/index>`__.

This year of development is the result of testing almost 80 different locales against up to 4 different applications and thousands of localizable strings, trying to catch more and more fatal errors in each update. The development hasn't stopped yet, too. There is more in-depth work going on in Gandalf's Silme project, for example.

While I appreciate that more folks are paying attention to l10n and extensions, it's unfortunate to see such work being invested in steps back in capabilities.

Another approach was recently started by Jean-Bernard "Goofy" on the `babelzilla wiki <http://babelwiki.babelzilla.org/index.php?title=GoofyPlan_for_an_extension_testing_machine>`__ and forum. I'm looking forward to add to and help with that project.
