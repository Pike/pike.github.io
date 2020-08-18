Not just incubating
###################
:date: 2007-06-06 03:46
:category: L10n, Mozilla
:slug: 2007/06/not-just-incubating

I have written about the incubator `before <http://blog.mozilla.org/axel/2007/04/30/the-incubator/>`__, it's a tool that should help localizations newly in CVS to work towards release. It's based on buildbot, and I whacked it pretty hard recently.

The `result <http://l10n.mozilla.org/buildbot/>`__ can be seen on the l10n server again. What's new?

-  Incubator is now L10n Trunk, I'm running my tools on all localizations working on the trunk now. That's both localizations moving towards fx3 and new ones.
-  It's using the python implementation of CompareLocales. It does check more, and it's output could potentially suck less. Red again means items missing, orange is obsolete items, green is good.
-  I'm exposing stats on localizations. You'll find a *90% translated* in the output box of the comparison step. More below.
-  There's one column for trunk, and one for incubators. You can tell which build is yours by looking at the description of the comparison step.
-  Technically, it doesn't sink the l10n server anymore on incubator check-ins.
-  Only incubator builds do langpacks right now, and only if the comparison ain't red. There's a download link labeled [D] on the upload step that takes you there.

**So what's the stats?** First of all, I know that "*translated*" isn't the right term, but it's as wrong as anything else, so wth. What I'm doing is, I'm counting all entries in DTDs and properties files which key does not match [kK]ey. Then I'm comparing those values to the en-US values and then do a 100*changed/(changed + unchanged). There are still a bunch of values that don't need to be changed to be localized, so I'm not worried that we're not at 100% anywhere. I do think that the differences between the high 70s and the 90 are real, though. I'm confident that removing the keys made those stats comparable mostly, as it did fix Japanese.

**Why the redo?** As indicated above, the first implementation didn't scale, so I needed a bit more buildbot-ism. I didn't feel good about adding new languages to the incubator just for load reasons. That's solved. The amount of languages leading to numbers of columns turned out to be bad, too.

**What the redo?** I'll make follow-up post on that, this one is long enough.
