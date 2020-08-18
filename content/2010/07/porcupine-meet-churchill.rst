Porcupine, meet Churchill
#########################
:date: 2010-07-27 12:16
:category: L10n, Mozilla
:tags: L10n, Mozilla
:slug: 2010/07/porcupine-meet-churchill

I've been talking with Seth today on how we can answer questions about the status of l10n. My grumpy argument was that I wouldn't know how to make graphs over time actually show progress, instead of just "failure". I had two naive graphs, one is showing all missing strings summed up over all locales. That graph would be dominated by the long tail of several dozen locales with a few hundred strings each, and you wouldn't see a dozen fighting over a few strings each.

The other is what I nick-name "porcupine graph", show how many locales have no missing strings, vs those that have some missing strings. This is what's actually implemented on the l10n dashboard as tree progress graphs. But how ever small a string change would be, it goes to all red. And it doesn't help that one can't mix green and red color gradients, so the graph usually shows spikes of red and a little black.

|porcupine|

Who'd want that as their progress stats, huh?

Now, during the chat with Seth I came up with the idea to just give a little bit of leeway, and accept some missing strings to be OK, at least for some time. I filed `bug 582280 <https://bugzilla.mozilla.org/show_bug.cgi?id=582280>`__ on that, and made a rough initial implementation of it. Nothing fancy, just a constant ignored bound of missing strings. Let's see how the past two weeks of Firefox 4 look now, with just a total of 5 missing strings being OK, ``?bound=5``:

|two weeks good and bad|

Now Churchill won over the porcupine, but it's still pretty red. Which is OK, we haven't even branched yet, right? So I went ahead and figured I'd add an option ``hideBad``:

|two weeks good|

Wow, progress. This graph actually looks like our community rocks as much as it does. Gets me grumpy, because this was really just about half an hour of work, plus a few years of thinking.

Now, how do we look on the long run, say, well over half a year? Bumping the bound up to 15, we're doing like

|half year progress|

Pretty good, heh? You can `play with it on the dashboard <https://l10n-stage-sj.mozilla.org/dashboard/tree-status/fx40x?starttime=1255682183&bound=15&hideBad>`__, too. The overall take aways would be:

We have about 20 locales that really track trunk.

We didn't have that many landings with a high amount of added strings.

I like both :-).

.. |porcupine| image:: http://farm5.static.flickr.com/4090/4834738435_c1dac145a2_z.jpg
   :width: 640px
   :height: 378px
   :target: http://www.flickr.com/photos/axelhecht/4834738435/
.. |two weeks good and bad| image:: http://farm5.static.flickr.com/4106/4834738689_45d9cb4219_z.jpg
   :width: 640px
   :height: 378px
   :target: http://www.flickr.com/photos/axelhecht/4834738689/
.. |two weeks good| image:: http://farm5.static.flickr.com/4085/4834738881_2b3beba630_z.jpg
   :width: 640px
   :height: 383px
   :target: http://www.flickr.com/photos/axelhecht/4834738881/
.. |half year progress| image:: http://farm5.static.flickr.com/4105/4834746465_c9cd423d83_z.jpg
   :width: 640px
   :height: 382px
   :target: http://www.flickr.com/photos/axelhecht/4834746465/
