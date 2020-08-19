compare-locales 0.9.2 released
##############################
:date: 2011-12-07 05:38
:category: L10n
:tags: compare-locales, L10n, Mozilla, tools
:slug: 2011/12/compare-locales-0-9-2-released

I just uploaded a new release of compare-locales to `pypi <http://pypi.python.org/pypi/compare-locales>`__, `hg.m.o <http://hg.mozilla.org/l10n/compare-locales/>`__ and `github <https://github.com/Pike/compare-locales/tree/afdc6a6e1ef1d2d9c851688ca116bb83e02625d6>`__.

Changes since the last released version:

-  Support for nested ``l10n.ini``\ s, notably, ``browser/branding``.
-  Errors on CSS specs, notably, if en-US is a length or min-width etc, the translation also needs to be one.
-  Warn if CSS specs don't match in property or unit. Say, en-US gives min-width:14ex and the localization has width:120px, warn. Thanks to Rimas for the request.
-  Warn if en-US is just a number, and the localization is not.

See also the `pushes on hg.m.o <http://hg.mozilla.org/l10n/compare-locales/pushloghtml?fromchange=RELEASE_0_9_1&tochange=RELEASE_0_9_2>`__.

You can install/update with

::

   pip install -U compare-locales

Next up is to use the new version on the dashboard.

It's not part of our release automation, though. `Bug 650465 <https://bugzilla.mozilla.org/show_bug.cgi?id=650465>`__ met some resistance in release-drivers, IIRC, as we'd need to change what we're shipping in 3.6. More errors means failure unless l10n-merge is on on existing builds, which effectively changes `all 20 locales that have errors on 3.6 <https://l10n-stage-sj.mozilla.org/shipping/dashboard?tree=fx36x>`__.
