Notes on SemWiki
################
:date: 2012-07-20 09:01
:category: Mozilla
:slug: 2012/07/notes-on-semwiki

Semantic Wiki is nice, but it's hard to wrap one's head around. Thus, writing down some notes-to-non-self.

Most importantly, start with paper. SemWiki isn't very forgiving if you reconsider. Once you've made some headway with paper, set up mediawiki locally. I've thrown my db away three times so far because I did do reconsider. FYI, that's a tad tricky, here's what works for me:

-  kill the db and recreate it
-  move ``LocalSettings.php`` away
-  load ``index.php``, follow the configuration 'til you have a db, ignore the download
-  ``php maintainance/update.php`` to get the semwiki tables
-  ``Special:SMWAdmin`` to do tables and data update (log in again)
-  ``php maintainance/runJobs.php`` to speed up the data update

Using ``Special:CreateClass`` is nice, as it's doing a whole lot of things for you. There is one thing it doesn't, for Properties linking to Pages, it won't ask you for the Form to create/edit those pages. ``Special:CreateProperty`` does, but that's of little help. You can add that later by editing the Property page, and adding a ``Has default form`` like

``This is a property of type [[Has type::Page]]. It links to pages that use the form [[Has default form::Aisle Milestone]].``

Property name is the wiki page name of a property, Field name is the human readable name used in the forms created, btw. If you loose the mapping between field and property name, edit the form, and explicitly specify the property with ``{{{field|Summary|property=Has summary}}}`` or the like. Though, more likely, you dropped ``[[Has summary::{{{Summary|}}}]]`` in the template, I replaced that with just ``{{{Summary|}}}``, which breaks stuff.

Also, you don't want to use '/' in your form names, that breaks editing URLs from your referring pages.

Oh, and yes, you don't need to add the namespaces like ``Template:`` etc when entering the names in the semwiki forms, those are prepended automagically.

Another drawback of ``Special:CreateClass`` is, it'll do all its work asynchonously, so you'll need to wait a while 'til things are up for you to actually enter your data. Locally, you can speed things up with ``php maintainance/runJobs.php``.

I'm still torn on how much I'd really like to use the free text, right now I'm using a Text property to create a summary that I can put in a prominent part of the template.

One more trick, if you're using largely prefixed pages, like we do on wikimo, you can get pretty descent sorting if you edit the Template to have a category hook like

``[[Category:Aisle/Use Case|{{#titleparts: {{PAGENAME}} | | -1 }}]]``

This is for `Aisle <https://wiki.mozilla.org/Aisle/Project>`__, for which I ended up creating my own semweb instead of using our standard feature pages. They have a ton of stuff I don't need, and don't have a few things I hope to use.
