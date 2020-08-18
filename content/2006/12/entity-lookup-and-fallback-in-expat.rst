entity lookup and fallback in expat
###################################
:date: 2006-12-08 10:14
:category: L10n, Mozilla
:slug: 2006/12/entity-lookup-and-fallback-in-expat

As there were more people talking about this than I recall, here's the public correction on what I though would be true:

#. I see no way to hook into expat to make it resolve an entity. See the XML_TOK_ENTITY_REF handling in `xmlparse.c <http://lxr.mozilla.org/mozilla/source/parser/expat/lib/xmlparse.c#2296>`__.
#. We can redefine entities. I'm not exactly sure on how the brand.dtd-inclusion in the `neterror overrides <http://lxr.mozilla.org/mozilla/source/browser/locales/en-US/chrome/overrides/netError.dtd>`__ will like this, yet.

Does hacking the chrome protocol to concat the DTD files for all available locales sound like a good idea?

And I wonder if we can revisit the XML_ERROR_UNDEFINED_ENTITY in xmlparse.c to just notify us, so that we could whine in the error console without busting.
