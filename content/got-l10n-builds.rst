got l10n builds
###############
:date: 2009-06-05 03:22
:category: L10n, Mozilla
:tags: build, L10n, Mozilla
:slug: got-l10n-builds

'nuff said? Not even remotely.

We've had l10n builds as long as I'm working on l10n, actually, I got involved around the time when we started to do them upstream. They always were considerably better than each localizer doing their build at home on whatever (virus-infected) hardware they found, with help from other community members for the platforms they didn't have. But at the light of day, it was more

   That? Yeah, I know. That's crap.

And I know you can hear my voice in your head right now :-).

Those days are gone. We're running Firefox and Fennec builds on the releng infrastructure now for a few days that are actually sound builds made to service our l10n community. Some highlights:

-  Builds are finished some 10 minutes after a localizer landing, on all three platforms.
-  There's no deadlock between different locales, thanks to all l10n builds running on a pool of slaves.
-  Builds are "l10n-merged", against the actual build that's repackaged. Independent of missing strings or files, you have a build that can be tested.
-  No more race conditions between nightly and trunk source status.

The impact of this shouldn't be under-estimated. We are, for the first time in years, producing builds that allow a localizer to actually immediately test. Localizers can work incrementally, translate one feature, check-in, test. No worries if something landed in en-US in the meantime, or whatnot. With the new builds, I have seen various localizers coming from hundreds of missing strings to a tested build on two or three platforms in a matter of a few hours. Back in the days, that was the waiting time for the first build. The new locales all pull all-nighters to get their final bits in. They want to, and now they actually can.

I want to thank coop and armenzg for their great help in making this happen, aki for porting it over to fennec. Of course thanks go to joduinn and sethb, too, for bearing with the ongoing meetings we have, trying to battle the crap down. To dynamis for the initial work on l10n-merge. Also thanks to bsmedberg and Chase for the initial works on both automation and build process, and ted for the various reviews on making our build system catch up.

Finally, we're not going to stop here. Armen is working on creating the necessary files to get l10n builds on a nightly update channel. Yep, you heard right, that's where we are right now. I know that KaiRo is working on getting the goodness over to the comm-central apps. And yours truly is hacking on the dashboard together with gandalf, more on that in a different post.
