The Ten Hands
#############
:date: 2017-07-11 13:23
:category: Localization, Mozilla L10n team
:slug: the-ten-hands

Gaul is entirely occupied by the Romans. Well, not entirely... One small village of indomitable Gauls still holds out against the invaders.

While most of mozilla `gathered in San Francisco <http://blog.mozilla.org/l10n/2017/06/30/localization-mozilla-sfallhands/>`__, a small group of ten hands gathered in a small village in Slovenia.

|image0|

Matjaz hosted me, Stas, Adrian and Jarek, to work on Pontoon and other aspects of localization infrastructure at Mozilla. Jarek is a volunteer `contributor extraordinaire to Pontoon <https://github.com/mozilla/pontoon/commits/master?author=jotes>`__, and we were finally able to have him join us for his first Mozilla gathering. Adrian is taking a break from his `work on Socorro <https://github.com/mozilla-services/socorro/commits/master?author=adngdb>`__, and will take on work on Pontoon, at least for this quarter.

Adrian, Stas and I hadn't really looked at the Pontoon code base, so this was a great opportunity to get us onboarded. We also had the chance to talk about some of the pros and cons of the basic data models powering Pontoon.

Jarek and Matjaz made great progress on getting `errors and warnings from compare-locales <https://bugzilla.mozilla.org/show_bug.cgi?id=1237667>`__ hooked up to Pontoon. The `PR already has 43 commits <https://github.com/mozilla/pontoon/pull/622>`__, and is shaping up nicely. It's been good to see that we were able to use compare-locales as is, though we might want to optimize one API. I was able to help here a bit verbally myself. It's interesting how efficient such 5 minutes can be, compared to our usual roundtrips of a day between work and not, and continents.

Adrian spent quite some time working on a setup of `Pontoon on docker-compose <https://bugzilla.mozilla.org/show_bug.cgi?id=1376813>`__. Having done that myself for the l10n automation, I was his tester here. The PR is now ready for review, which is also on me. Promise.

Stas started to experiment with graphene-django to expose a GraphQL API for Pontoon. That was surprisingly easy to get started. It was also surprisingly bad in performance. He's written down his notes on the wiki, and we'll reconvene soon on what the next steps should be. And yes, we abused the word "REST" in a lot of different ways during that week.

Stas and I made a lot of progress on support for Fluent in our core infrastructure, adding support for that in compare-locales and elmo. Stas finalized the support for `Fluent in compare-locales <https://hg.mozilla.org/l10n/compare-locales/pushloghtml?changeset=868e29f6439c>`__. I added support for the `diff view in elmo <https://github.com/mozilla/elmo/commit/e40c6b24ec5271dbfde8c6740c67747baaaa836c>`__, which required a `few updates to compare-locales <https://hg.mozilla.org/l10n/compare-locales/log?rev=dd3d1f7841ab%3A%3A5e61f6c95681>`__, too. With the work on `compare-locales 2.0 <https://bugzilla.mozilla.org/show_bug.cgi?id=1372254>`__, I also `updated elmo <https://github.com/mozilla/elmo/compare/e40c6b24ec5271dbfde8c6740c67747baaaa836c...f77445a420144967702be0bfa78b92d185982ef0>`__ to support both the legacy JSON output as well as the new JSON output from 2.0.

|image1|\ The days were just packed, as they say. We did go out and explore the area, mostly to get food. In a place where the cab driver has a day job, you have to. In a place where you can see three different countries from your porch, that also means you might go through passport control to go to dinner. Hello Croatia and croatian kunas, where dinner prices are not in euros. Last but not least a big Thank You to Eva and Robert from the `Cuk Wine House <http://www.hisa-vina-cuk.si/>`__ for their hospitality.

The images are by Adrian Gaudebert and licensed under a `Creative Commons Attribution-NonCommercial 4.0 International License <http://creativecommons.org/licenses/by-nc/4.0/>`__.

.. |image0| image:: https://blog.mozilla.org/l10n/files/2017/07/P1070323-600x142.jpg
   :class: aligncenter size-large wp-image-1137
   :width: 600px
   :height: 142px
.. |image1| image:: https://blog.mozilla.org/l10n/files/2017/07/P1070317-252x336.jpg
   :class: alignright size-medium wp-image-1138
   :width: 252px
   :height: 336px
