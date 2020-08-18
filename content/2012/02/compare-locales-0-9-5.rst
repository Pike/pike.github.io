compare-locales 0.9.5
#####################
:date: 2012-02-15 08:05
:category: L10n, Mozilla
:tags: compare-locales, L10n, Mozilla
:slug: 2012/02/compare-locales-0-9-5

Busy times for compare-locales, there's another release out the door.

| New in this release are a significant rewrite of the Properties parser. A lot less regular expressions, a lot more performance in bad situations. Thanks to glandium for poking me hard with a patch. That patch didn't work, but at least it got my butt to it. Comparing ``bn-IN`` is now down to 23 secs for 3 minutes+.
| The next big thing is that I now run checks on entities that are keys, too. That doesn't seem to have caused any regressions, but look out for new false positives. On the plus side, if you use '&' as accesskey, you'll get an error report instead of a ysod.
| Finally, I added support for mpl2 license headers, so we're all set there.

As usual, update with ``pip install -U compare-locales``.
