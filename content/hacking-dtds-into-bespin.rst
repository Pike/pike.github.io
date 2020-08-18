Hacking DTDs into Bespin
########################
:date: 2009-08-20 08:40
:category: Mozilla
:tags: Bespin, Mozilla
:slug: hacking-dtds-into-bespin

Just a quick side note, I'm hacking on a DTD mode for `Bespin <https://bespin.mozilla.com/>`__. The code is pretty ughly still, but the output is getting OK.

|screenshot of editing a DTD in Bespin|

It already supports marking up errors, to a similar extent that they're found in compare-locales these days. Better parsing for the actual values is a bigger task, in particular one that should improve Bespin's XML mode at the same time. 'Cause that didn't impress me yet.

Code will come in `bug 510579 <https://bugzilla.mozilla.org/show_bug.cgi?id=510579>`__.

.. |screenshot of editing a DTD in Bespin| image:: http://farm4.static.flickr.com/3433/3839873768_32b8e2b6ec.jpg
   :target: http://www.flickr.com/photos/axelhecht/3839873768/
