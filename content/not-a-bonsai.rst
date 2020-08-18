Not a Bonsai
############
:date: 2009-02-20 11:34
:category: Mozilla
:tags: Mozilla
:slug: not-a-bonsai

News from the tooling sink.

I just brought up what I needed to replace bonsai for hg on `stage/pushes <http://l10n.mozilla.org/stage/pushes/>`__. My request list was as follows

-  Query multiple repositories at once
-  Query for landings to particular directories and files

I would love to get graphs and blame and mark, but I'm still hoping on hgweb on that.

The navigation is a bit rough still, it doesn't have pages, yet, for example. I'm rather happy with the search, though. As it's not discoverable, I'll guide you through a bit. Here's what a sample search would look like:

|Sample search dialog|

You get to this dialog by hitting the search button on the top left. First, you see a limit, this is the maximum number of pushes shown. The button switches that on or off in the query. The next two options are a tad more interesting, they allow you to search in a period of time. I use a date-time-picker for both *from* and *until*. Again, the buttons switch those on and off. The choice button lets you add more queries for paths and repository names, which are the piece after hg.mozilla.org in this setup. But on to the date-time-pickers...

I actually think those are fancy, and yes, I wrote those from scratch. I shamelessly stole the navigation pattern from `Simile's Timeline <http://code.google.com/p/simile-widgets/wiki/Timeline>`__, i.e., I have bands with different resolution in time, which you can scroll. As I don't display any events inside the bands, they're actually empty, but the topmost band is months, then you have a band for days and one for hours. That lets you select a date and a time in a rather untuitive fashion, once you get used to the fact that sliding to the right is decreasing. Which is right for the UI pattern, it just feels awkward.

I find that UI pretty good, in fact, much better than other datetime pickers I found on the net, or the one that Philipp presented at FOSDEM.

The biggest challenge I have is making it accessible, though. Suggestions welcome. I think that a11y on *pushes* sucks in general, patches accepted :-).

A note of warning to end this post. We're adding services at a faster pace than CPUs on the l10n server. Please pound this one with care, i.e., don't pound it. It's gonna enforce limits on searches right now to some extent, be nice. Thanks.

.. |Sample search dialog| image:: https://blog.mozilla.org/axel/files/2009/02/bild-1-300x228.png
   :class: aligncenter
