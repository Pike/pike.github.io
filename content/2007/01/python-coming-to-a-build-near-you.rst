python coming to a build near you
#################################
:date: 2007-01-11 15:41
:category: L10n
:slug: 2007/01/python-coming-to-a-build-near-you

As a heads-up, I'm making some progress to use a single python process per jar.mn in `bug 361583 <https://bugzilla.mozilla.org/show_bug.cgi?id=361583>`__. AFAICT, I have all the odd ends figured out to merely run one python script per ``jar.mn``, instead of starting a two perl processes per ``jar.mn``, and one per preprocessed entry, plus two calls for zip.

I had to port preprocessor.pl and make-jars.pl over from single scripts to modules. Porting them to python looked like the smaller change at the time, even though I needed to code quite a bit to actually get '!' working in the preprocessor. Damn python for using ``not`` to negate expressions. And I had to subclass zipfile.ZipFile to implement overwriting entries in zip files. That seems to work, now I need to hook it up to the jar maker, which currently only does flat chrome. Oh, and I need to make that code readable for people that don't have direct access to my brain.The good news is, it seems to be blazing fast, my test suite contains a copy browser/base right now, and the current realchrome target takes some 4 seconds on my windows machine, the new one takes less than a second.

Oh, and yes, this is really a step on my path to require python and just python for localizers to create langpacks, and then repackage builds, too.

From a requirements point of view, I'll be testing this at least on python 2.3 and python 2.4, I don't have python 2.5 installed on one of my machines just yet. Which I should, as in particular the zip stuff seems to have changed in the backbone.

The Preprocessor.py is attached to the bug, so if you want to have a look, be my guest.
