doing jars, baby
################
:date: 2007-01-12 12:45
:category: Mozilla
:slug: 2007/01/doing-jars-baby

So I successfully hacked my python stuff to create jars, and to do so for python 2.5, too. Testing it in the MozillaBuildRC1, here's time make -C browser chrome for the current code and my new hack:

::

   real    0m21.812s
   user    0m20.731s
   sys     0m11.761s

vs.

::

   real    0m10.375s
   user    0m9.028s
   sys     0m5.158s

from scratch. The numbers don't change significantly if you run them again, which is to be expected, as most files are preprocessed and overwritten anyway.
