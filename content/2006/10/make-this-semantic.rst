make this semantic
##################
:date: 2006-10-19 16:12
:category: RDF
:slug: 2006/10/make-this-semantic

Brendan's `recent post <http://weblogs.mozillazine.org/roadmap/archives/2006/10/mozilla_2.html>`__ caused a few ripples. Not necessarily in the world, but at least in the pond of planetrdf.com. Out of context, a few statements from my POV.

-  Decisions on RDF in Mozilla are made now.
-  There are folks using RDF. Not necessarily from JS.
-  I'm not creating the RDF implementation for Mozilla 2.
-  Neither `is bsmedberg <https://bugzilla.mozilla.org/show_bug.cgi?id=357276>`__.
-  There is no implementation of an RDF standard in Mozilla. It's closer to, say ``-//Netscape Comm. Corp.//DTD HTML//EN`` than to ``-//W3C//DTD HTML 4.01//EN``.
-  The attack surface of the existing RDF implemention is not in C++, but in it's design decisions.

What I'm doing? I'm still hoping to see a design discussion that is open to participants with other goals than "kill RDF first". And to participate in this discussion, I'm working on at least enough code so that one can seriously evaluate that option.

I'll continue to do snippets posts on particular aspects in the near future, I have drafts in my head talking about attack surface in terms of design decisions, good uses or RDF in Mozilla, pointing at some bad examples of using RDF (/XML), too.
