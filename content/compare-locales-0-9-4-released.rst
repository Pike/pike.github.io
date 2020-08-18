compare-locales 0.9.4 released
##############################
:date: 2012-01-20 04:37
:category: L10n, Mozilla
:tags: L10n, Mozilla
:slug: compare-locales-0-9-4-released

There's yet another update to compare-locales, we're now at 0.9.4. Please update your local installs with

``pip install -U compare-locales``

Changes since 0.9.3 are:

-  Catch ``%`` as error. Sadly, there's not much more the parser reports than ``Invalid Token``, but at least it says something. You need to escape that as ``&#037;``.
-  Stability fix, there was a crash on ``<!ENTITY "reference to  &ƞǿŧ;-known entity">``. Unicode is hard.
