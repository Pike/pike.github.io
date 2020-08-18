New version of compare-locales released, please update
######################################################
:date: 2010-04-08 16:29
:category: L10n, Mozilla
:tags: L10n, Mozilla
:slug: new-version-of-compare-locales-released-please-update

I've released a new version of compare-locales, and you should **really** update.

The new version of compare-locales adds:

-  support for more than one filter.py
-  support for filter.py returning more than just bools, but "error", "report", or "ignore".

**Why?**

| Lorentz strings. They are missing, but them missing isn't fatal. So we needed a third state.
| And some of them are in toolkit, so we're moving parts of the filter.py logic from all over the place into
| ``releases/mozilla-1.9.2/toolkit/locales/filter.py``. That means that we can remove the hacks in comm-central and mobile-browser, making our life so much more reliable and predictable.

The changes to 1.9.2 will land shortly, so versions of compare-locales prior to 0.7 will stop working.

**Update paths:**

| ``easy_install -U compare-locales``
| is the easiest way to do it. Depending on OS and local settings, you might want to
| ``sudo easy_install -U compare-locales``

| Or,
| ``hg clone http://hg.mozilla.org/build/compare-locales/``
| and do whatever you did last time, setting paths or python setup.py install.

**How does it look? Where's beef? Or veggies?**

Here's what 0.8 spits out for German on 1.9.2 with patched filter.py:

::

   de
      browser/chrome/browser
        browser.properties
            +crashedpluginsMessage.learnMore
            +crashedpluginsMessage.reloadButton.accesskey
            +crashedpluginsMessage.reloadButton.label
            +crashedpluginsMessage.submitButton.accesskey
            +crashedpluginsMessage.submitButton.label
            +crashedpluginsMessage.title
        preferences/advanced.dtd
            +submitCrashes.accesskey
            +submitCrashes.label
      toolkit/chrome/mozapps/plugins/plugins.dtd
          +reloadPlugin.middle
          +reloadPlugin.post
          +reloadPlugin.pre
          +report.disabled
          +report.failed
          +report.please
          +report.submitted
          +report.submitting
          +report.unavailable
   de:
   keys: 940
   report: 17
   unchanged: 634
   changed: 4561
   87% of entries changed

You can see the regular output of missing strings, and you'll recognize all of lorentz. New here are three things:

| The strings in the long display are not counted as missing, but are in a new summary item called "report". Those strings are not fatal, but should get localized.
| The return value of compare-locales is only dependent on \*missing\* strings, i.e., code checking the return value will see a successful run of compare-locales if there are reported strings, as long as there are none missing.
| If you switch l10n-merge on, it won't merge the reported strings, but rely on the real code falling back as intended.

Not-so-important feature update, compare-dirs is now supporting l10n-merge, too. That's sweet for the upcoming weave stuff.

Questions are welcome here, bug reports are welcome in `"Mozilla
Localizations", "Infrastructure" component <https://bugzilla.mozilla.org/enter_bug.cgi?product=Mozilla%20Localizations&component=Infrastructure&rep_platform=All&op_sys=All&short_desc=%5Bcompare-locales%5D>`__.
