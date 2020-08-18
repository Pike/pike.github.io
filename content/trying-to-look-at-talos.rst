'Try'ing to look at Talos
#########################
:date: 2010-05-20 03:15
:category: Mozilla
:tags: Mozilla, trysite
:slug: trying-to-look-at-talos

I've started to hack on the bcp47 patch, and as I add complexity to the chrome registry code path, I'll actually need to look at performance results. Being a good citizen, I'll start with try-server builds. TBH, the prospect of having to do that kept me from starting on this patch for a while, and it didn't come far yet, too. Now, enough rant, I've created a hack. Open the book of e-ville.

When looking at talos results, I've got two problems: An overwhelming amount of numbers, and, in particular for the try server, finding something OK to compare with. All tools we have so far compare runs that are close in time, but in terms of try, that's not necessarily close in code, nor anything else good. So here's what I did:

#. Open the try pushlog, and select a push to investigate.
#. Load ``/try/json-info?node=`` until the reference repo has a parent of that changeset pushed, checked via ``/mozilla-central/json-pushes?changeset=``.
#. Load up to five later pushes than the one found.
#. Load a total of ten pushes including the ones above going back in time.
#. Ask graphs-stage api for the perf results.
#. Average per test and platform, and create a scatter plot for each, with 1 being the mean, displaying min and max of the mozilla-central reference numbers, plus the try result.
#. Show missing perf results in the try run and the base results.

On to the caveats: None of the json apis above support cross-site XHR requests, AFAICT, so I had to create a full blown web app to do this. I picked django just because that's what I'm used to. The app is tested on 1.1.1, but should work on 1.2 as well. So far, there's no db requirements.

Even worse, ``json-info`` is really slow, so the app as it is right now doesn't even remotely scale. Mostly the reason why I don't intend to host it anywhere as is.

I don't understand why there is pretty much noise in which test results actually come up. Nor if graph-stage is the right graph server to use to begin with.

It looks like ripped out of the book of e-ville.

Here's the two screens for your sneak-preview pleasure:

The start screen, where you can select your push:

|First screen of my ughful try talos compare app|

After clicking Go, and waiting a while, you'd end up with

|second screen of my ughful try talos compare app|

You can get to the alert showing test name and platform by clicking on the dots.

If you're interested, the code is triple-licensed and on `hg.mozilla.org <http://hg.mozilla.org/users/axel_mozilla.com/trysite/>`__. Patches welcome.

I could in theory see solving the perf problems with integrating the pushes app we have for the l10n dashboard, but that's more involved than I feel like spending time on right now. Mostly because I don't exactly know how good refreshing the try clone would perform.

.. |First screen of my ughful try talos compare app| image:: http://farm4.static.flickr.com/3385/4623422407_82e9264042_o.png
   :width: 498px
   :height: 504px
   :target: http://www.flickr.com/photos/axelhecht/4623422407/
.. |second screen of my ughful try talos compare app| image:: http://farm5.static.flickr.com/4038/4624027250_4e7a5f2210_b.jpg
   :width: 1024px
   :height: 453px
   :target: http://www.flickr.com/photos/axelhecht/4624027250/
