sneak preview
#############
:date: 2006-10-17 13:42
:category: RDF
:slug: sneak-preview

Letting all the overall agenda aside, how does this sound?

::

   js> ds = new RDFSimpleTripleDataStore();
   js> em = new RDF.Vocabulary('urn:x-moz:em#');
   js> ds.assert(RDF.resources[document.location], em.title,
                  RDF.getLiteral("Some English string", null, "en-US"));
   js> c = ''; ds.forEach(function(t) {c += t;}); c

::

      <about:blank> <urn:x-moz:em#title> "Some English string"@en-US.
