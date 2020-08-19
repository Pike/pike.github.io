bug comment of the week
#######################
:date: 2007-03-27 10:09
:category: L10n
:slug: 2007/03/bug-comment-of-the-week

I'd like to award Phil Ringnalda with the **L10n cookie of the week**-award for hunting down the unused strings on the trunk. Not just that, but also the bug comment of the week, as far as I'm concerned, goes to the initial comment of `bug 375485 <https://bugzilla.mozilla.org/show_bug.cgi?id=375485#c0>`__. If you ever wondered if there are low-hanging fruit to make our applications easier to localize, and to improve the quality of our localizations, removing dead strings by the time you kill them in one of them. Phil not only tracked down which strings are not used anymore, but also why, finding strings which death dates back to 2000. Strings which our localizers worked on, or, `56 <http://mxr.mozilla.org/l10n-mozilla1.8/search?string=findField.tooltip>`__ `ways to lose your lover <http://www.allmusic.com/cg/amg.dll?p=amg&token=&sql=33:9aq7ggjctvnz>`__. It's a nice demo of our font rendering caps, though.

Lesson to take away is, if you kill a localizable string, kill it, if you add one, use it.
