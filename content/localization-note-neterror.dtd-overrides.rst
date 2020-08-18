# Localization note (netError.dtd): overrides
#############################################
:date: 2008-04-08 05:33
:category: L10n, Mozilla
:slug: localization-note-neterror.dtd-overrides

I thought I knew what we did for netError.xhtml and netError.dtd, but I didn't, so here's a little thing I learned today:

`netError.xhtml <http://mxr.mozilla.org/mozilla/source/docshell/resources/content/netError.xhtml>`__ loads 3 DTDs, one for xhtml, one is `netError.dtd <http://mxr.mozilla.org/mozilla/source/dom/locales/en-US/chrome/netError.dtd>`__ (global) and one is global.dtd (for RTLishness). Two boring ones, one interesting. Now, what we used to do is that browser would override the global `netError.dtd <http://mxr.mozilla.org/mozilla/source/dom/locales/en-US/chrome/netError.dtd>`__ (which is in the dom module) with its own version. Not anymore, global netError.dtd now imports global's `netErrorApp.dtd <http://mxr.mozilla.org/mozilla/source/dom/locales/en-US/chrome/netErrorApp.dtd>`__ and that is then overriden, by, guess, right, `netError.dtd <http://mxr.mozilla.org/mozilla/source/browser/locales/en-US/chrome/overrides/netError.dtd>`__ in browser.

Lesson learned: if you're hunting parsing errors in Firefox net error pages, you have to check both netError.dtd files for syntax errors, but not netErrorApp.dtd.
