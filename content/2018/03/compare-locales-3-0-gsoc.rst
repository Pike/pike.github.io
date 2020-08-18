compare-locales 3.0 - GSOC
##########################
:date: 2018-03-20 18:54
:category: Planet, Tools
:slug: 2018/03/compare-locales-3-0-gsoc

There's something magic about `compare-locales 3.0 <https://pypi.python.org/pypi/compare-locales/3.0.0>`__. It comes with Python 3 support.

It took me quite a while to get to it, but the `writing is on the wall <https://docs.djangoproject.com/en/2.0/releases/2.0/#python-compatibility>`__ that I had to add support for Python 3. That's just been out for `10 years <https://docs.python.org/release/3.0/whatsnew/3.0.html>`__, too. Well, more like 9ish.

We're testing against Python 2.7, 3.5, and 3.6 now.

Thanks to `Emin Mastizada <https://mozillians.org/u/mastizada/>`__ for the reviews of this patch.

Slightly related, we're having `two l10n-tooling related proposals <https://wiki.mozilla.org/Community:SummerOfCode18>`__ out for this year's `Google Summer of Code <https://summerofcode.withgoogle.com/>`__. Check out Google's student guide for `how to pick a project <https://google.github.io/gsocguides/student/finding-the-right-project>`__. Adrian is mentoring a project to improve the experience of first-time users of Pontoon. I'm mentoring a project to support Android's localization platform as a first-class citizen. You'd write translation quality checks for compare-locales and add support for the XML dialect to Pontoon.
