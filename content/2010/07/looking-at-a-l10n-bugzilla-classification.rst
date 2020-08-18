Looking at a l10n bugzilla classification
#########################################
:date: 2010-07-26 13:44
:category: L10n, Mozilla
:tags: L10n, Mozilla
:slug: 2010/07/looking-at-a-l10n-bugzilla-classification

We intend to move from components per locale in the "Mozilla Localizations" product to a matrix of products per locale, and components for each of Firefox, Thunderbird, et al. I've created an add-on to set up the products and components and laid out in the `newsgroup thread <http://groups.google.com/group/mozilla.governance/msg/011a024c7fb39360>`__. I wanted to share some screen shots on how things look locally now.

``enter_bug.cgi?classification=Mozilla in Your Language`` looks like this:

|enter_bug.cgi|

Localizers can edit the descriptions on `localize.m.o <https://localize.mozilla.org/projects/bugzilla_components/>`__. I'm not totally convinced that the current formatting of the products are great. The double () braces disturb me, both here and on the actual bug form (see below). I might prefer "l10n:ab-CD Language (Region)".

|Enter bug|

This is the actual bug entry form, and shows the localized component description. It also shows a rather confusing line wrapping of the product name.

Another aspect that we were concerned about was how it'd look if you changed the product of a bug. Locally, this looks like this now:

|Re-productize bug|

Got comments? Please leave them in the `original newsgroup thread <http://groups.google.com/group/mozilla.governance/browse_frm/thread/5983760ed8357cfc#>`__, or here.

.. |enter_bug.cgi| image:: http://farm5.static.flickr.com/4122/4831080567_ef7019129b_b.jpg
   :width: 540px
   :height: 1024px
   :target: http://www.flickr.com/photos/axelhecht/4831080567/
.. |Enter bug| image:: http://farm5.static.flickr.com/4132/4831739790_1f525c5582.jpg
   :width: 500px
   :height: 170px
   :target: http://www.flickr.com/photos/axelhecht/4831739790/
.. |Re-productize bug| image:: http://farm5.static.flickr.com/4102/4831739950_47e0b37a3c.jpg
   :width: 500px
   :height: 375px
   :target: http://www.flickr.com/photos/axelhecht/4831739950/
