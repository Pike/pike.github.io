Firefox Nightlies
#################
:date: 2018-03-01 18:21
:category: Firefox, Localization, Planet
:slug: firefox-nightlies

We've run into a problem with localized Firefox Nightlies in some languages today. We'd like to apologize for that, and also help you getting unstuck.

The Nightly builds of Firefox from February 28 in some localizations listed below start with an XML parsing error, the infamous YSOD - the yellow screen of death. To fix your local installation, either go to the `Nightly Download Page <https://www.mozilla.org/firefox/nightly/all/>`__ and reinstall Firefox Nightly, or run the following in your Firefox install location:

``firefox.exe -chrome chrome://browser/content/aboutDialog.xul``

The latter should just launch the about window, and download an update for Firefox Nightly. You might need to adjust the executable name, depending on your platform. The example above is for Windows.

The affected localizations are: as, bn-BD, bn-IN, en-GB, en-ZA, es-ES, gn, gu-IN, hi-IN, ia, ja, kn, ko, mai, mr, my, ne-NP, or, pa-IN, si, te, zh-CN, and zh-TW.

Please don't blame the localizers for this, whether a localization was affected or not depended on technical details.

Check out `bug 1442145 <https://bugzilla.mozilla.org/show_bug.cgi?id=1442145>`__ for those technical details and more, and `bug 1442181 <https://bugzilla.mozilla.org/show_bug.cgi?id=1442181>`__ on how we intend to avoid this problem in the future.
