Being a localizer in the rapid release cycle
############################################
:date: 2011-04-11 18:15
:category: L10n, Mozilla
:tags: L10n, Mozilla
:slug: 2011/04/being-a-localizer-in-the-rapid-release-cycle

We're changing to a `6-week release train model <http://mozilla.github.com/process-releases/>`__, and this is going to impact how localizers do their contributions. The following scheme has been cycled in .planning for a bit, so this is what we'll be doing. We'll adapt that if needed, of course, but based on experience with the next cycle or two.

Recap on the rapid release cycle: en-US developers work on *mozilla-central*, as they used to, and every 6 weeks, we'll pull their contributions to another repository, called `mozilla-aurora <http://hg.mozilla.org/releases/mozilla-aurora/>`__. That repository is string frozen. String changes only land in this repository as part of the merge from *central* to *aurora*. After another 6 weeks, the content goes to yet another repository, *mozilla-beta*. Corresponding to those, there's *l10n/mozilla-aurora* and *l10n/mozilla-beta*. And now you know. Find a glossary at the end of this post.

There are two different localizer schemes: Early birds and friends of string freeze. Read the following descriptions and pick one for your individual localization team.

**Early Birds** are those localization teams that are happy to follow the *mozilla-central* content quickly and make sure that all issues relating to localizing that code are found and fixed. We already have a few of those that have built their reputation among our hackers to have good input to follow. We don't need a lot of those, but the ones we have are crucial to make the plan work, and have code that is properly localizable at any time on *aurora*. You'll be following the fx_central tree on the l10n dashboard to catch up on changes.

**Friends of String Freeze** are those teams that prefer to have stable content to localize with a decent time window to act on it. Many of our localization teams are in this group. If you're in this group, you'll set your calendar alarm to the next window, hg pull -u on your *mozilla-aurora* clone, your *l10n/mozilla-aurora* clone, localize, push, test, fix, push, sign-off. Then you set your calendar to the next 6-week cycle, and you're all set. The expectation here is that the amount of strings will be rather low, so a day of l10n plus testing and fixing is fine. Usually, you should be able to deliver a great localization for the next version of Firefox in some 3 days. Firefox 5 right now is some 30 strings, other releases will be a good deal bigger. But nowhere close the 1.2k strings of Firefox 4. You'll be watching the fx_aurora tree on the l10n dashboard to see the status of your localization.

Sign-offs will happen on *aurora*, in rare cases on *beta*. The setup where we work towards release is *aurora*.

What about the *beta* repositories? Well, I hope to not see a necessity to land on *l10n/mozilla-beta* for the most part. You should expect that changes you make on *l10n/mozilla-beta* will be dropped once we do the next update from *aurora*, so you want to have the fixes on both *aurora* and *beta*, if applicable. But really, you want to be good on *aurora*. Then *beta* will be fine and no hassle.

**How that maps to mercurial work:**

For the **Friends of String Freeze**, you'll not need to worry about anything other than pulling on both repos every cycle. We'll take your content from *l10n/mozilla-aurora* to *l10n/mozilla-beta*, and may very well at some point stop doing *l10n-central* builds at all for you. Just keep things simple here.

For the **Early Birds**, we'll rely on you self-identifying and doing a tad of extra work. You'll be in best shape to merge your contributions from *l10n-central* to *l10n/mozilla-aurora*, making sure that the result has all your fixes from both *central* and *aurora*, where you want them. You're techy-geeky-savvy anyways, so that's allright. If at some point, we learn that there's a pattern that benefits from automation, we'll check in on that when we get there, too. You shouldn't have to worry about getting content on *l10n/mozilla-beta* anymore than the rest, though.

| **Glossary**:
| `mozilla-central <http://hg.mozilla.org/mozilla-central/>`__ is the mercurial repository that en-US code is landed to as development makes progress.
| `l10n-central <http://hg.mozilla.org/l10n-central/>`__ is the tree of mercurial repositories that the early-bird localizers use as development makes progress.
| *central* is short for either, or both, of mozilla-central and l10n-central, depending on context.

The terms around `mozilla-aurora <http://hg.mozilla.org/releases/mozilla-aurora/>`__, `l10n/mozilla-aurora <http://hg.mozilla.org/releases/l10n/mozilla-aurora/>`__, and *aurora* map to their corresponding terms for *central*, same for `mozilla-beta <http://hg.mozilla.org/releases/mozilla-beta/>`__, `l10n/mozilla-beta <http://hg.mozilla.org/releases/l10n/mozilla-beta/>`__, and *beta*.

**Update**: Fixed the links to map to the new and stable repository locations.
