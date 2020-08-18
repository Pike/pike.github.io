hg annotate and "did we ship that?"
###################################
:date: 2009-11-27 09:56
:category: Mozilla
:tags: jetpack, Mozilla
:slug: 2009/11/hg-annotate-and-did-we-ship-that

I came across the question on whether a particular piece of code was in a particular release, and if so, which. Say, you're going through old bugs like me and you want to know if something's fixed b2 or fixed b4. So you head over to hg annotate and then...

I wrote a jetpack feature to the rescue. It's as rude as it's icon, but it's getting the tags and the revisions from hg.m.o, and replaces the not-so-useful author@rev integers with the latest release tag. Currently I hacked this up for Firefox and Thunderbird, and it relies on FIREFOX_version_RELEASE being a proper version. It's doing two background http requests, so it takes a while, no UI feedback on that. How'd a jetpack do that right?

HTH, and I wish jetpacks were even more simple. Docs, please. And it took me a while to figure out that using the included "Develop" tab isn't as fancy, editing outside and refresh felt quicker.

Anyway, if you have jetpack installed, head over to the install page of the `annotate jetpack feature <http://people.mozilla.com/~axel/jetpacks/annotate.html>`__.
