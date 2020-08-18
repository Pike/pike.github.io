l10n merge
##########
:date: 2008-07-03 10:10
:category: L10n, Mozilla
:tags: L10n
:slug: l10n-merge

I've just pushed an implementation of l10n-merge to my `tooling repository <http://hg.mozilla.org/users/axel_mozilla.com/tooling/>`__. It's now actually just an option to compare-locales, and will do the weakest heuristic for now.

Whenever compare-locales finds missing entries in an existing file, it will create a copy of that file in a staging directory for the merge, and append the missing entries. For the bulk of our files, that should work fine. Bookmarks.html is an exception, as are the netError files, I think order of entities and dtd inclusions matters there. In the end, you get a staging directory with files that got fixed up, a localization directory with both good files and files with missing entries, and the original en-US source. Making jar.mn actually pick localized files up from three different places in a particular order is in my `build-patches repository <http://hg.mozilla.org/users/axel_mozilla.com/index.cgi/build-patches/>`__.

Here's why, in case you wonder: First and foremost, it leaves the original source alone. I like it like that. Secondly, it does as few file manipulations as possible in the best case, a complete localization doesn't do a single copy or something. It's not all that invasive into the build system as one might think, too. At least as soon as you want to look at the code to see where you're looking for files, checking a bunch of source base dirs is rather trivial.
