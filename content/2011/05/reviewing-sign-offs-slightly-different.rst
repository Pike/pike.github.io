Reviewing sign-offs, slightly different
#######################################
:date: 2011-05-10 03:39
:category: L10n
:tags: L10n, Mozilla
:slug: 2011/05/reviewing-sign-offs-slightly-different

Opening the magic box of l10n admin stuff:

We're doing sign-offs, y'know? Localizers hit the l10n dashboard and click a button to say "this revision is good to ship". Which is cool, because then they don't need approval for every patch for release branch fixes.

And I'm reviewing the signoffs. Sounds all good, and well proven.

Enter the new release cycle. What's new? This is a small update, on a quick turnaround. So I can't do what I did for previous releases, and just not review the first sign-off. That was just an early beta (for most locales) and had a 1000 new strings. Sounded fair. Anyway, now we're just doing 30 strings, so doing an incremental review against what's on 4.0.1 is in order. So what does that mean?

#. I need to get the revision that we're shipping on 4.0.1. For sign-offs that update one branch, that's all hooked up in the UI, but not for 4.0.x to 5. That's `bug 655943 <https://bugzilla.mozilla.org/show_bug.cgi?id=655943>`__.
#. The revision on 4.0.1 is on l10n-mozilla-2.0, the signoff on 5 is on a revision of l10n/mozilla-aurora. Neither need to exist in the other repo, so you can't just use plain hg commands on a repo. That's `bug 655942 <https://bugzilla.mozilla.org/show_bug.cgi?id=655942>`__.

Now, I wouldn't be me if I wouldn't script myself out of it, here's the `gist of it <https://gist.github.com/964230>`__. And yes, this blog post is as much code comments as there are for that one.
