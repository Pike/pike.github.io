What's a Firefox localization?
##############################
:date: 2007-02-14 09:15
:category: L10n, Mozilla
:slug: whats-a-firefox-localization

One of the untold stories of Firefox is that localizing Firefox is something different. Inside our localization community, it is an often heard complaint that we're doing *this* while every other project in its sane mind does *that*. I have been thinking about that often, but we haven't actually made a story out of it, so here is my take.

When thinking about Firefox, I see four major distinguishing features.

-  Firefox is not just a piece of software.
-  Firefox has users. A few dozen million users a week, even.
-  On top of that, a good deal of those users never installed Firefox themselves, or would have. Our strong community with USB sticks did that for them, and for us.
-  Mozilla keeps those users safe. The internet is a rough place to hang out, and we're updating the Firefox installations of our users to our best knowledge.

In particular the first and the fourth point make an essential difference to our localization story. We want our users to be using the safest version of our software. Not doing so puts our users at a real life risk, and thus we're compromising on the language. We don't offer downloads of Firefox 1.0 versions on our website, just because that happens to be the last version of Firefox in a particular language. The amount of users we have and the variety of their technical skills make us do automatic updates to keep our users safe.

What does that mean for a localization? It means, Mozilla can't use a localization of any particular version of our software. We're making a long term commitment to our users, and we need our localization teams to join us in that commitment. We want and need the localization teams to join our community.

Which brings me to the first point from above, Firefox is not just a piece of software. Firefox is a community of users, contributors, and developers forming around a piece of software, including moms, dads, and neighbors just as well as xptcall ports haxxors. And localizers. That's why users of Firefox in a particular language expect to see more than "just" the software. The website is one part (yay to mozilla.com localization), AMO (yay) is another. MDC (yay) is another level in which local communities can engage and help. Most locales have already organized forums and other community-building sites in their own regime, which is a great thing. We're trying to be conservative in what we require localization teams to do, but the variety in opportunities in our ecosystem should give you a good idea why localizing Firefox is much more successful when it's a team effort. I'm excited to see how many of the items in this paragraph moved from yikes to yay, btw.

Of course, being a joint development community is a two way road. We made some good progress on that on the MOZILLA_1_8_0_BRANCH and Firefox 1.5.0.x, freezing that for changes that would require localization changes. That way, we can, and do, ship the currently most secure version for all our languages, and serve automatic updates for those. Same of course holds for our newer stable branches.

Looking forward, the next big step will be the major update from Firefox 2 to Firefox 3. Optimistically, we want to offer Firefox 3.0 to all existing Firefox 2 users, in their language of choice. If that won't work due to resource constraints, we should be able to take all the 2.0.0.x locales on Fx3 by the time we offer an automatic major update. We will remain to rely on our contributors for localization, but there is a clear commitment to not break this by BD, QA, or build/release, let alone engineering.

That makes us different, and good. IMHO.
