Try'ing talos on node.js
########################
:date: 2010-06-07 07:37
:category: Mozilla
:tags: trysite
:slug: 2010/06/trying-talos-on-node-js

I wasn't all happy with how django helped me in coding the `try-talos visualization <{filename}/2010/05/trying-to-look-at-talos.rst>`__, so I recreated this based on `node.js <http://nodejs.org/>`__. The result is a single project on github, `talos-node <http://github.com/Pike/talos-node>`__, that just requires you to get a local install of node.js. It will actually incrementally render the pages as it does server side loads, so it doesn't look completely dead throughout. Outcome at the side is a much better interaction to figure out which test is performing how, you can now mouse-ever one result, and you see all tests, both for your try-revision and the references. I also moved away from showing the range and mean value to showing all values, so you see how your red spot is doing in the flock of blues. There's an `updated screenshot on flickr <http://www.flickr.com/photos/axelhecht/4678970196/>`__.

A few comments on hacking on node.js. The nice thing about it is, there are tons of helper modules out there. The bad thing is, most of them are not compatible with a current version of node.js. Is the buzz over?

I ended up hacking my own simple asynchronous templating engine, the guts are shown in the readme.

I hope that being just ``node server.js`` once you have node.js up, it's gonna make people more willing to actually run it locally.
