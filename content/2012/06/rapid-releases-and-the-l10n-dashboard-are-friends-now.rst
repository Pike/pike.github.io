Rapid releases and the l10n dashboard are friends now
#####################################################
:date: 2012-06-09 12:07
:category: L10n
:tags: elmo, L10n, Mozilla
:slug: 2012/06/rapid-releases-and-the-l10n-dashboard-are-friends-now

Wait a second, we're on the rapid release schedule for almost a year now, and 9 releases. How can the l10n dashboard be friends with the trees only now?

Well, I've hacked and lied and tweaked and spoofed the data for a year. No more.

The obvious changes are:

-  Localizers as well as drivers can now see how far behind their work is, in release cycles
-  channel migration code is actually not a lie, and can be taken over by release management

On the team page, you'll now see something like

|image0|

You'll notice the difference between the **Current** sign-off with the green check-mark, and the **fx14** one with the looking glass. In the past, we've shown the green check-mark for both, now we're actually showing the version that we're using instead of the current one, and the looking glass is there to indicate that the localizer should actually look into this. There's been a good deal of confusion about this, and I sure hope that this will resolve it a good deal.

There's a ton of follow-up work, `for one on elmo <https://bugzilla.mozilla.org/showdependencytree.cgi?id=650816&hide_resolved=0>`__. This bug has been blocking a lot of other patches and work, both for the localizer-facing parts as well as the release infrastructure-facing parts.

More so, the state of localizations changes from "n missing strings, probably in this bucket" to "didn't update since fx12". That's changing how we guide our work as l10n drivers a good deal. The impact between what we do and what localizers do becomes less anecdotal, and more science.

And there's quite a few things we need to do, in particular for desktop.

.. |image0| image:: /images/2012/06/Bildschirmfoto-2012-06-09-um-19.01.16.png
   :class: alignnone size-full wp-image-471
   :width: 991px
   :height: 257px
   :target: /images/2012/06/Bildschirmfoto-2012-06-09-um-19.01.16.png
