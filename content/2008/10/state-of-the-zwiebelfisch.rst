State of the Zwiebelfisch
#########################
:date: 2008-10-02 15:45
:category: L10n, Mozilla
:tags: L10n, Mozilla
:slug: 2008/10/state-of-the-zwiebelfisch

For those that know that I've been somewhat offline lately, good news. I'm back online. I'm not going into the details, but ISPs in Germany and their handling of customers is, errr, let's put it that way: not Firefox.

Other items of progress lately:

`Seth covered Firefox 3.1 Beta 1 <http://blog.mozilla.org/seth/2008/10/01/a-little-on-the-l10n-beta-1-roll-call/>`__. In my words, it went like I expected, our localizers just blew our expectations. That doesn't make me change my expectations. I expect what I think we should expect, and heartly welcome that Firefox gets so much more. 35 localization teams swallowed the even more technical hg compared to CVS. Some localization teams volunteered to help out others. Overall, the current stats are that we have 41 hg l10n repos with localizers commiting, 21 with just me so far, and 6 are plain empty. The last 6 are waiting on good content on cvs to migrate over to hg.

I just landed changes to both hgpoller and hg_templates that add a json output to hg.m.o, once that's pushed live. That json output is designed to allow to clone the pushlog2.db, i.e., with a mere clone of a repository on hg.m.o and a copy of pushlog2.db, you can do all kinds of history magic. I sure hope to use that data to make out opt-in process a lot more appealing and understandable.

The real big thing in the queue is `bug 458014 <https://bugzilla.mozilla.org/show_bug.cgi?id=458014>`__, refactoring browser/locales/Makefile.in. There are a bunch of things I'm doing there. Not wasting time and computing power would be one. Being able to actually tell which build the build is repackaging before it is repacking is the other big thing. The initial comment in the bug has a good analysis.

This is a rather big step for l10n in mozilla land. Being able to actually pick the right source in en-US for the build you're repackaging is something we're talking about for years. It's a prerequisite for doing l10n-merge at build time, too. Which that bug adds, btw. So this bug should really pave the path to reliable l10n nightly builds, good testing infrastructure, and more.

"More" being a new way to start localizing Mozilla applications. No more, no less. Up to now, your localized build was busted if the localized source you used to build wouldn't include all the strings of en-US. With the changes I added in place, you can just make the build insert those at build time. This will not change the output of compare-locales, and will give localizers the ability to, without additional tools, decide on whether to keep a particular string with the same value as en-US or to bother about it later. l10n-merge is really only going to add an intermediate output. Think about it as CPP output.

We talked about this l10n-merge in Whistler, and there are a bunch of loose ends and room of improvement. Nevertheless, the state in bug 458014 is such that I would like to use to figure out how to make a buildbot factory do the right thing at least in the more or less trivial cases.

l10n-merge won't change our policy to only ship complete localizations. I hear folks trying to change it, thus the comment. It'll be tough to convince me to not require complete localizations. "Localizations" doesn't imply translating all strings, though. Localization implies an conscious decision on whether a particular string should be translated or not. Security error messages, of course, those protect our users on the web. XSLT error message much more likely not, there are only a few languages which have a community around XSLT in their native language. Falling back to English without a consious decision is a door wide open to a sucky user experience. Something that at least I don't consider to be Firefox. Maybe something else. Minefield is one possible name for it, there might be others.

PS: I picked Zwiebelfisch for no other reason than "it's late at night, and it starts with Onion"
