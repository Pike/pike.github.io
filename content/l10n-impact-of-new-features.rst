l10n impact of new features
###########################
:date: 2007-03-27 04:59
:category: L10n, Mozilla
:slug: l10n-impact-of-new-features

We had our first l10n impact meeting for Firefox 3, `places <http://wiki.mozilla.org/Places>`__ was on. The meeting minutes are on the `wiki <http://wiki.mozilla.org/Places:L10n_impact_meeting/2007-03-19>`__, but there are few key points that are of more general interest.

| Firstly, the l10n impact meetings are held for the first time for Firefox 3, so we're going forward with open eyes, ready to continue with what works, and change what doesn't or could work better. The places meeting worked out good, so we're going forward in this direction. The general idea behind these meetings is, if the PRD lists one P1 item for you, you're stuck with 7. Your feature is supposed to be in an up-to-par quality not only in English (US), but in another 6 languages, too. And that number may grow, even. As you as a feature developer can't make that yourself, the key is to jointly develop features. It's the "help us to help you" dance.
| Secondly, we have loads of documents on how to write localizable software, most of which are old. `Writing localizable code <http://developer.mozilla.org/en/docs/Writing_localizable_code>`__ on MDC is the newest and the only currently maintained one. I'm happy to see comments on that document, as always, the discussion page is a good place for that in general. Bigger discussions are best held in .l10n.

There are two areas where we don't have a good set of documentation,

-  how to design localization of features
-  how to develop features in an l10n-friendly way

The first area is something we just need to learn about, and doing meetings on that topic is likely the only way to really understand what needs to be done, and to carry experience from one area to the other. I guess we're just too creative in our features to have ready-built recipes for this. To clarify, this is not about whether you use a DTD or a properties file for something, or if an RDF file is cool.

This is about answering the question what a German speaking user in Rwanda would expect Firefox to do. What is supposed to happen if some user decides to install an, say, Khmer version of Firefox 3.0.0.3 over an English (US) one, just because we started supporting that language with that release? If you look at your `Feature Plan Template <http://wiki.mozilla.org/Firefox3/Feature_Plan_Template#Upgrade.2FDowngrade.2FSidegrade>`__, this is what sidegrading is supposed to be. Installing a partner build or non-partner build over an existing install goes by the same name.

Let me give you an example, in the `Firefox 2 default bookmarks <http://mxr.mozilla.org/mozilla1.8/source/browser/locales/en-US/profile/bookmarks.html?force=1>`__. There are links to Getting Started, customization, about etc. Those generally go by the name of in-product pages, and are really just extensions of Firefox on the web. If you decide to use a French build, you'd expect to get help and extensions in French, so actually, these links should probably follow the currently installed language. It's an interesting question whether the titles should do, too. On the other hand, there is one link in there to demo the live bookmarks, a news feed. In that case, my personal expectation would be to not change that. All of this of course only if the user hasn't changed the default. Whatever that means for a link collection. As you can see, even something as old as bookmarks has interesting stories to tell when it comes down to localization design.

Once these questions are properly answered, the technical implementation of those is a lot less cumbersome and surprising, too. At least that's my expectation.

| These questions get more involved as soon as you touch services and web properties of third parties. We have quite a bit of experience in that, and even more rules, but as they involve 3rd parties, it's tricky to put them on public paper. So you want to check in with Mic and me on that. Rules of thumb, we can't do anything without permission; not everything good in Amercia is good in Germany; permissions can be revoked. Mic and I can help create good public guidelines for localizing whatever you need, too.
| Next step, assuming we know what a feature is actually supposed to do, how do you go about and code it such that localizers can make your feature rock in the localized versions? The first and foremost step is the quality of the en-US code. It needs to be understandable by users, of course, but on a code level, it needs to be understandable by localizers, too, even more than that, it should be understandable by looking at tests (**) and localizable files only, even. One way to tackle this, and I'm suggesting that you go this route until we have contradicting evidence, is to separate writing localizable code from exposing the localizable content to localizers.

Writing localizable code
   This is the technical process of putting UI strings into DTD files or properties files. You shoud rethink your architecture if you need something else, please ask me for comments then, too. More on MDC, as linked above.
Exposing localizable content to localizers
   Now you're actually putting the DTD and properties files into the ``locales/en-US``, exposing them to localized builds.

Why the difference? Whenever you change (see MDC doc) a UI string in your feature, you're going to break all localized builds. That's a bug, it can be fixed, it's not trivial to do so, though. Break as in, there won't be anything uploaded to ftp, localizers can't test the trunk. This is the technical reason. The software engineering reason, and that's more important and likely to stick even if we get the technical one fixed, is that unless you know what your UI is supposed to look like and what the UE is supposed to be like, localizers are going to play a guessing game. They'll guess stuff, and it's much harder to fix the guesses later on than to just not start guessing. Before you start to expose your code to localizers, you want to go through the following check-list:

-  Is the functionality of the feature specified and documented?
-  Are the policies published, if necessary, in particular for 3rd party hooks? Were those policies published early enough for localizers to comply today?
-  Are the localizable files proper? No unused strings, good key names, good comments etc? Is the content in there sufficiently stable, or would I be wasting the time of localizers? (*)
-  Can this work in RTL languages? Don't forget accessibility, too.
-  Are the tests up? (**)

If you can run through this check list and be fine, it's time to get your code out there in the wild. Be prepared for some half-a-dozen reviews of your code instantly. You want to write an announcement for the l10n newsgroup, too.

As far as I'm concerned, it's fine to ship UI strings in content for alphas, as long as you keep an eye on landing them in ``locales/en-US`` in time.

| (*) Finding out when your code is stable is not exactly science. As long as you follow the `guidelines <http://developer.mozilla.org/en/docs/Writing_localizable_code>`__, you want to work and improve on your code. You need to find a balance between releasing early and just adding noise.
| (**) Tests? Yes, tests. Please provide tests for exposing all strings you have to end users, so that localizers know how to test their work in action. Litmus tests are probably fine, you should explain how to open all dialogs and panes etc. Writing tests for error messages is harder, yet more important, too.
