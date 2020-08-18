Why l10n tools should be editors instead of serializers
#######################################################
:date: 2012-07-20 09:18
:category: L10n, Mozilla
:tags: L10n, Mozilla
:slug: 2012/07/why-l10n-tools-should-be-editors-instead-of-serializers

If your tool serializes internal state instead of editing files, it'll do surprising things if it encounters surprising content. Like, turn

``errNotSemicolonTerminated=Named character reference was not terminated by a semicolon. (Or “&” should have been escaped as “&amp;”.)``

into

``errNotSemicolonTerminated=Named character reference was not terminated by a semicolon. (Or “” should have been escaped as “amp;”.)``

And that's for a string the localizer never touched.

(likely `narro issue 316 <http://code.google.com/p/narro/issues/detail?id=316>`__)
