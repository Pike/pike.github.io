See your django models in SVG
#############################
:date: 2009-03-31 11:20
:category: Mozilla
:tags: django, Mozilla, svg
:slug: see-your-django-models-in-svg

Last week I found `django-command-extensions <http://code.google.com/p/django-command-extensions/>`__, which together with graphviz allow you to create pretty displays of your django models. Sadly not the other way around, but still better than nothing.

The awkward piece is when you like to get SVG output, which I do. Renders fine on my linux VM, but my gecko on OSX is worried (rightfully, I guess). Which can be fixed with sed, at least in those graphs that I have:

   ``sed -e's/8.00/8px/g;s/ Bold;/ ; font-weight: bold;/g'``

Basically, you have to fix the font size and the font weight.

I'll see if I blog about the actual models pre or post April 1st. I don't find them funny, so they're not gonna go live tomorrow ;-).
