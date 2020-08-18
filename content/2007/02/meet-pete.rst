Meet Pete
#########
:date: 2007-02-01 06:28
:category: L10n, Mozilla
:slug: 2007/02/meet-pete

I've been doing some investigation on localization architectures in the last two months or so, triggered by parts of the 50-2-100 thread in .l10n and .planning. In particular, I've been reading the archives of `translate-i18n <http://sourceforge.net/mailarchive/forum.php?forum_id=7939>`__, which happens to be the (main?) gettext mailing list. Looking at the problem reports there and following the links out to stuff like `XLIFF <http://www.oasis-open.org/committees/tc_home.php?wg_abbrev=xliff>`__, I looked for solutions to the following tasks:

-  attractive for coders
-  attractive for localizers
-  support for both XML (XUL) and js (C++)
-  support for plurals
-  ... and genders
-  fix problems with labels and accesskeys, too
-  play nice with version control systems (and not necessarily with mail)

and found ... nothing.

Thus, I have been spending the good half of my time recently to actually work on a solution that can match all of the points above. The code name for that project is L20n, as it takes L10n a significant step further. And we're all heading 2.0 anyways.

| I invite you to spend some time looking at the details on the `wiki <http://wiki.mozilla.org/L20n>`__, as well as to look at some of the `examples <http://people.mozilla.com/~axel/l20n/js-l20n/>`__ I have so far, targetting HTML and JS. That's a bazaar rep, too.
| The scope of the project is not limited to Mozilla, if we care for acceptance in our localization community, we should care about other projects, too. And the problems we tackle here are not our very own problems, everybody is hitting them, so our chances are not too bad. I already have some limited feedback from folks outside of Mozilla, and I'll send further pings if all goes well. The timeline as far as it impacts Mozilla is Mozilla 2.

If you can help, I'm looking for feedback in general, either here, on the wiki or in .i18n. I need some tips on writing specs in general, too. If you have experience in code generation based on grammars, I'd love to see some pleasant surprises, using antlr hasn't been one so far. If you want to join working on the spec, I'd be happy to add some editors. And of course, I need help in showing this off in other languages, both spoken and programming. If you have a sample you'd like to see done, let's get it on. Some of the `open issues <http://wiki.mozilla.org/L20n:Issues>`__ are on the wiki, too.

I intend to have a discussion on this proposal at FOSDEM, too, leveraging the gathering of all kinds of Open Source projects there, hopefully.

Oh, and I get to choose the code names, so `Meet Pete <http://sluggy.com/daily.php?date=070126>`__ ;-).
