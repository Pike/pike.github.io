On the process to code
######################
:date: 2015-01-19 09:00
:category: Mozilla
:tags: Mozilla
:slug: on-the-process-to-code

gps blogs a bunch about his vision on how coding on Firefox should evolve. Sadly there's a bunch of process debt in commenting, so I'll put my comments in a medium where I already have an account.

A lot of his thinking is based on `Code First <http://gregoryszorc.com/blog/2015/01/16/bugzilla-and-the-future-of-firefox-development>`__. There's an `earlier post <http://gregoryszorc.com/blog/2015/01/10/code-first-and-the-rise-of-the-dvcs-and-github>`__ with that title, but with less content on it, IMHO.

   In summary, **code first capitalizes on the fact that any change to software involves code and therefore puts code front and center in the change process.**

I strongly disagree.

Code is really just one artifact of many of creating and maintaining a software product.

Or, as `Shane blogged <https://shanetomlinson.com/2015/hackers-need-process-too/>`__,

   First rate hackers need process too

Bugzilla is much more than a review tool, it's a store of good and bad ideas. It's where we document which of our ideas are bad, or just not good enough. It's where we build out our shared understanding of where we are, and where we want to be.

I understand how gps might come to his conclusions. Mostly because I find myself in a bucket that might be like his. Where your process is really just documenting that you agree with yourself, and that you're going forward with it. And then that you did. Yeah, that's tedious and boring. Which is why I took my hat as module owner more often lately, and landed changes without a bug, and with ``rs=foopy``. Old guard.

Without applying my basic disagreement to several paragraphs over several posts, some random notes on a few of gps' thinking and posts:

I agree that we need to do something about reviews. splinter's better than plain text, but not quite there. Github PRs feel pretty horrible at least in the way we use them for gaia. As soon as things get slightly interesting, no status in either the PR nor bugzilla makes any sense anymore. I'm curious on MozReview/reviewboard, though the process to get things hooked up there is steep. I'll give it a few more tries for the few things I do on Firefox, and improvements on code and docs. The one time I used it, I felt very new.

Much of the list gps has on `process debt <http://gregoryszorc.com/blog/2015/01/09/firefox-contribution-process-debt>`__ are things he cares about, and very few other people. In particular newcomers won't even know to bother, unless they happen to across that post by accident. The other questions are not process debt, but good things to learn, and to learn early.
