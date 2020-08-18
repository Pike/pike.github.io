Coming soon: cross-repository network graphs for hg.m.o
#######################################################
:date: 2011-05-30 08:18
:category: Mozilla
:tags: protovis
:slug: 2011/05/coming-soon-cross-repository-network-graphs-for-hg-m-o

Did you miss the ability to look at our source code and figure out who's working on what where? Thought that only github can do that?

Let me give you a sneak peek at what I've been hacking on over the weekend.

What's the big picture of our mainline code development?

|branched repos of mozilla-central|

You can see the blue line of development along mozilla-central, and then branch points for the release branches, and now for beta (miramar), and aurora. That's pretty broad, and intentionally so. If you're interested in the back and forth on a changeset level, this is how the branch point of fx5 beta looks:

|changesets around the fx5 beta branch point|

Why does it say aurora? Because hg doesn't know what you're looking for. I determine what was branched off of what by looking at pushes, wherever a particular changeset was pushed first, wins. As beta branched off of aurora later, you see that this was the branch of aurora at the time.

Sadly, you don't see the more interesting detail, that after that branch, the developer tools branch merged. If the database in the backend was tracking our project repos, you'd see that.

Of course, there's also an l10n side to this. I get many questions on what to merge and where and so, and it's hard to see what ended up in which repo, and if things are different. Let's follow one of the l10n repos at large:

|branched repositories of Japanese|

There's even more details on the rapid branches for this one, like so:

|changesets around the Japanese fx5 beta branch|

Many of the same landings, but with different hg changesets, and then a merge. That merge didn't make it to miramar, though. Which is OK, that's a one-off anyway.

Now that I wetted your appetite, bad news: Nothing of this is live yet. I'll actually need to make a patch at least for the API in `bug 659260 <https://bugzilla.mozilla.org/show_bug.cgi?id=659260>`__, get review and get it live. Also, this is currently code that's run as part of the l10n dashboard, which isn't really intended to cover all our sources. If we want this at large, it'll need liberation, and the resources that comes with that. The actual code is pretty easy to liberate, though.

And, graphs are made with `protovis <http://vis.stanford.edu/protovis/>`__, including a custom Network-based layout to do DAGs.

.. |branched repos of mozilla-central| image:: http://farm6.static.flickr.com/5266/5775953417_4a916235f7.jpg
   :width: 500px
   :height: 270px
   :target: http://www.flickr.com/photos/axelhecht/5775953417/
.. |changesets around the fx5 beta branch point| image:: http://farm3.static.flickr.com/2402/5775953715_7fcd4bb97f.jpg
   :width: 500px
   :height: 207px
   :target: http://www.flickr.com/photos/axelhecht/5775953715/
.. |branched repositories of Japanese| image:: http://farm6.static.flickr.com/5185/5775953123_28e98e1bea.jpg
   :width: 500px
   :height: 302px
   :target: http://www.flickr.com/photos/axelhecht/5775953123/
.. |changesets around the Japanese fx5 beta branch| image:: http://farm3.static.flickr.com/2745/5776494358_3d4a01c25d.jpg
   :width: 500px
   :height: 308px
   :target: http://www.flickr.com/photos/axelhecht/5776494358/
