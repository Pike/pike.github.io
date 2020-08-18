Create a localized build locally
################################
:date: 2017-08-04 16:19
:category: Firefox, Firefox Mobile, Localization, Planet
:slug: create-a-localized-build-locally

Yesterday we changed the way that you create localized builds on mozilla-central.

This works for developers doing regular builds, as well as developers or localizers without a compile environment. Sadly, users of artifact builds are `not supported <https://bugzilla.mozilla.org/show_bug.cgi?id=1387485>`__.

For language packs, a mere

``./mach build langpack-de``

will work. If you'd rather wish to build a localized package, you'll want to get the package first. If you're building yourself, that's

``./mach package``

and if you want to get a Nightly build from archive.mozilla.org, just

``./mach build wget-en-US``

If you want to do that for Firefox for Android, you'll need to specify which platform you want. Set ``EN_US_BINARY_URL`` to the `latest-mozilla-central-\* <http://archive.mozilla.org/pub/mobile/nightly/>`__ path for the binary you want to test.

And then you just

``./mach build installers-fr``

That'll take care about getting the french l10n repository, and do all the necessary things to get you a nice little installer/package in ``dist``. Pick your favorite language from `our repositories <https://hg.mozilla.org/l10n-central/?sort=lastchange>`__. Care for a RTL build? ``./mach installers-fa`` will get you a Persian one ;-) .

As with other repositories we clone into ``~/.mozbuild``, you'll want to update those every now and then. They're in ``l10n-central/*``, a repository for each language you tried.

Documentation is on `firefox-source-docs.rtd <https://firefox-source-docs.mozilla.org/build/buildsystem/locales.html>`__, bugs `go here <https://bugzilla.mozilla.org/enter_bug.cgi?product=Core&component=Build%20Config&cc=l10n@mozilla.com>`__. This works for Firefox, Firefox for Android, and Thunderbird.

And now you can safely forget all the things you never wanted to know about localized builds.
