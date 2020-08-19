Searching l10n
##############
:date: 2009-06-02 07:20
:category: L10n
:tags: dashboard, L10n, Mozilla
:slug: 2009/06/searching-l10n

I'm contemplating adding search in l10n to the dashboard, and I figured I'd put my thoughts out for lazyweb super-review.

Things we might want to search for:

-  Localized strings

   -  in a particular locale
   -  in all locales
   -  going into a particular app

-  entity names

   -  in all of the above

As with the rest of the dashboard, I'd favour a pythonic solution. I've run across `Whoosh <http://whoosh.ca/>`__, which seems to offer me what I'd need. In particular I can mark up searches in just keys or just values of our localized strings with the Schemas it offers.

All sounds pretty neat and contained, I'm just wondering if there's something cool and shiny elsewhere that I'm missing, or if someone came back with "ugh, sucks" from trying Whoosh.

Ad-hoc design for the curious:

For each changeset, we'd parse the old and the new version of the file, getting a list of keys and values, and I'd create two searchable TEXT entries for all changed keys, and added entries. We'd tag that "document" with path, locale, apps, revision, branch. That way, you could search even for strings that aren't currently in the tip, and get a versioned link to where it showed up first, and last, possibly. Given that we have a lot of data and history, I wouldn't be surprised if that corpus would get large pretty quickly. I'd expect to not only index l10n but en-US, too. Thoughts?
