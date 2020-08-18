Why RDF?
########
:date: 2006-10-20 11:04
:category: RDF
:slug: why-rdf

| As `brendan has asked <http://www.xulplanet.com/ndeakin/article/358?show=c#comments>`__, here goes my reasoning why Firefox should have RDF, independent of what other browsers do. Or at least the part that I didn't forget.
| The main difference is the extensions ecosystem that makes Firefox such a great browser. Extensions come and go, they change, and they interact with the user and the browser. Spot the missing arc? I haven't seen a whole lot extensions out there making use of each other. But they should. They shouldn't have to depend on each other, they should just be a tad happier and snappier when the buddy they know about is there.

Why would that be a reason to use RDF? Because the strong point of RDF is the ability to gather assertions from independent sources and to through them together independent of whether they belong together or not. RDF doesn't require the data to be connected, essentially, which enables you to mumble stuff about stuff that don't necessarily make sense in that context, but are way cool if you add a few arcs that somebody else knew.

I'm convinced that we will see a new stage of development in our ecosystem if we enable this loose communication. Yes, because despite the fact that we have an RDF implementation, and that we're using an RDF/XML file to describe extension metadata (``install.rdf``, which really has more information in it than just install stuff already), we're not permitting information not targetted at the extension manager itself to survive. For reasons that make a great other post, tentatively titled "a bunch of nonos". But hey, ``install.rdf`` is there, and we should use it. Dictionaries used to fall back to install.js, before we actually hacked dictionary support into extensions. Or say, an there is an extension that does a whole bunch of stuff to make a particular site even better. And if it could install a greasemonkey script, it could even .... . Why would anyone have to check if greasemonkey is installed and if it knows about your script, and whatnot, when just adding an arc to install.rdf would be good enough to enable greasemonkey to just grab those when it's there? Microsummaries are similar. Anything that is "small helper text file for big cool feature."

So much for the extensions itself, another good use I see are community building extensions, we all know `Matthew <http://www.allpeers.com/blog/>`__ is going to jump up and down here. Anything that wants to work on relations of stuff could choose to use an RDF backend.

I personally don't see any good model for communicating information between microformats parsers and microformats consumers than something that will at least looks and smells like RDF.

That said, I'm not of the opinion that Everything should be done in RDF. I don't want to solve sparse systems of linear equations by using SPARQL queries on a world-spanning assertions store. Use the right tools and concepts at the right place.

We're lucky to have a dynamic and agile ecosystem, with players going in and out, and RDF is made to model that. That's why we want it, and others may not. IMHO.
