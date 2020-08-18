Thoughts on APIs
################
:date: 2006-10-21 11:10
:category: Mozilla
:slug: 2006/10/thoughts-on-apis

I guess it would be a good idea to share a few general baseline concepts I think I have learned while thinking about an RDF API.

Query results should be queryable (does that word exist?). E4X does a great job here. ``.foo`` returns a ``XMLList``, which you can query again with a ``.bar``.

The funny trick is to actually

-  do that somewhat performant,
-  get really usable individual results.

The first item may be done by doing the actual queries as soon as you start using real results. The second item can be done by using ``WANT_CONVERT`` on ``nsIXPCScriptable`` cleverly.

One challenge in doing a "nice" API is that

::

   foo.bar.baz

is the same thing as

::

   var tmp = foo.bar;
   tmp.baz

Doing late queries helps here, too.

There is no good query API described in XPIDL. Design your interface to "just work" for C++ and to deliver the right data for the scriptable helper to provide the actual API to js clients.
