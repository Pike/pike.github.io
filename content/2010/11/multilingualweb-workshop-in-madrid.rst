MultilingualWeb: Workshop in Madrid
###################################
:date: 2010-11-05 08:24
:category: L10n, Mozilla
:tags: L10n, mlw, Mozilla
:slug: 2010/11/multilingualweb-workshop-in-madrid

So I've been at the W3 MultilingualWeb `Workshop in Madrid <http://www.w3.org/International/multilingualweb/madrid/madrid-results.html>`__ last week, and I guess there are a few things worth reporting.

`MultilingualWeb <http://www.multilingualweb.eu/>`__ is a project bound to host 4 workshops to bring people from different fields together to see how standards and best practices (existing and not) can help the web. Being mozilla, we don't really need to add that it's beyond just one language, right? The effort is strongly supported by the European Union, so there's a bias towards participants in these workshops being from Europe, though the folks by themselves certainly talk beyond that.

The crowd in Madrid was really diverse, standards people, government (EU and India), researchers, content, and, well, browsers. The browsers people were Charles McCathieNevile (Opera), Jan Nelson and Peter Constable (Microsoft), and me (Mozilla). There we no folks from webkit-based browsers.

Interesting bits and pieces:

I guess other people made that experience lately, too, but I welcome the way that MSFT is positioning themselves lately. Now they just need to compare beta builds to beta builds, and, (insider joke) while we hack on canvas, you learn JS:

   ``- ctx = canvas1.getContext("2d"); + ctx = document.getElementById('canvas1').getContext("2d");``

Still need to actually look at the results in competing browsers, and not on my font-broken OSX, but we're not doing too bad.

Gecko should really start using `CLDR <http://cldr.unicode.org/>`__ data for stuff like plurals, dates, calendars, lists. I should also really read up on `ES' i18n_api <http://wiki.ecmascript.org/doku.php?id=strawman:i18n_api>`__.

It was interesting to see common questions on what's a language from Denis Gikunda, who's working on l10n for google in sub-saharan Africa. Now that Anloc is coming in with their localizations, we're getting more exposed to how the history of those languages is so different from European ones.

Facebook's Ghassan Haddad reported on a few interesting things. Like Zuckerman coming into his interview with "you can't slow our development down". Interesting about this is that the resulting infrastructure is far from zero-impact on the development. There are quite some restrictions on what content you can put up, and you have to add syntactic sugar all over, too. Go check `their docs <http://developers.facebook.com/docs/internationalization>`__ for details. Also, they're not slowing down the publishing of localizations.

We got a bit of detail in the discussion about vandalism in fb l10n. They initially relied on community there, but when they got hit, they took down the localized sites until they had tooling support. Ghassan didn't come forward with details on what they do, though.

They are doing something conceptually similar to l20n to localize their social messages like "A is now friend with B, C", to make those depend on all the genders. IIRC, they call it string or entity *explosion*. Didn't get to ask any questions about this one, sadly.

Most of the science people talked about processes that all sound very good for the data we get from feedback in Firefox 4 betas. Natural language processing with trends detection, "translation" of SMS Spanish into Spanish, and much more. Sadly, there's nothing shrink wrapped that we could just use, but there's interest in creating a project to find out, maybe for Firefox Next?

One thing that felt slightly odd was the Semantic Web. I thought that was dead, but there's still optimism around that. Maybe semantics that help machine translation make a case for it, I'm not sure. Also, there seems to be more structured data coming to the "public web", and the algorithms that transform the "hidden web" into the "public web" could more easily add markup than human authors would. Still, there wasn't much hope in the browser people. Luckily, the browser doesn't really need to do anything but creating a DOM, and passing markup around for machine translation engines taking benefit from additional semantics.

Last but not least, I did finally get to spend some quality time with our Madrid community, thanks to the folks for taking me out twice. I had a great time, and sorry that my English speaking tempo aligned with your Spanish speaking tempo way too often :-).
