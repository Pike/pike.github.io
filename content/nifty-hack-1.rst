nifty hack #1
#############
:date: 2006-11-15 19:19
:category: L10n
:slug: nifty-hack-1

During the l10n session today we came up with an request from dynamis for him to be able to not have a string argument show up in a formatted l10n string.

We came up with the idea to specify zero width in the format, but it's actually precision 0.

::

   foo=does "%1$.0S" work?

as foo.properties does actually yield to

::

   js> sb.formatStringFromName('foo',['Firefox'],1)

   does "" work?

So here goes your nifty l10n tip of the day.
