Language packs are restartless now
##################################
:date: 2012-09-27 04:04
:category: L10n, Mozilla
:tags: L10n, Mozilla
:slug: language-packs-are-restartless-now

*Language packs are add-ons that you can install to add additional localizations to our desktop applications.*

Starting with tomorrow's nightly, and thus following the Firefox 18 train, language packs will be restartless. That was `bug 677092 <https://bugzilla.mozilla.org/show_bug.cgi?id=677092>`__, landed as `812d0ba83175 <https://hg.mozilla.org/mozilla-central/rev/812d0ba83175>`__.

To change your UI language, you just need to install a language pack, set your language (*), and open a new window. This also works for updates to an installed language pack. Opening a new window is the workaround for not having a reload button on the chrome window.

The actual patch turned out to be one line to make language packs restartless, and one line so that they don't try to call in to ``bootstrap.js``. I was optimistic that the chrome registry was already working, and rightfully so. There are no changes to the language packs themselves.

Tests were tricky, but Blair talked me through most of it, thanks for that.

(*) Language switching UI is `bug 377881 <https://bugzilla.mozilla.org/show_bug.cgi?id=377881>`__, which has a mock-up for those interested. Do not be scared, it only shows if you have language packs installed.
