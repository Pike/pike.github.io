Running into builds, just testing
#################################
:date: 2009-06-10 10:29
:category: L10n, Mozilla
:tags: build, buildbot, L10n, Mozilla
:slug: running-into-builds-just-testing

I've blogged previously on how to `set up a staging environment <http://blog.mozilla.org/axel/2009/06/01/l10n-ecosystem-in-a-fishbowl/>`__ to test the l10n build system, but I didn't go into any detail on how to actually do builds in that set up. That shall be fixed.

I'm picking you up at the point where

``twistd get-pushes -n -t 1 -s l10n_site.settings``

is running stable. You probably want to ``tail -f twistd.log`` to follow what it's doing. This piece is going to watch the hg repositories in ``stage/repos`` and feed all the pushes to those into the db. Next is to make sure that you actually get builds.

The first thing you need to do is to configure the ``l10n-master`` to access the same database as the ``django-site``. Just make sure that ``DATABASE_*`` settings in ``l10n-master/settings.py`` and ``django-site/l10n_site/settings.py`` match. The other setting to sync is ``REPOSITORY_BASE``, which needs to match in both ``settings.py``\ s. I suggest setting that to an empy dir next to the l10n-master. I wouldn't use the ``stage/repos`` dir, mostly because I didn't test that. Now you set up the master for buildbot, by running

``buildbot create-master .``

inside the l10n-master clone. Next thing is to create a ``slave`` dir, which is well put next to the ``l10n-master``. Despite what buildbot usually likes, this slave should be on the same machine that the rest is running on.

``mkdir slave buildbot create-slave slave localhost:9021 cs pwd``

So much for the general setup. With the twistd daemon running to get the pushes, you can now switch on the master and the slave, by doing a ``buildbot start .`` in both dirs. I suggest that you keep a ``tail -f twistd.log`` running on the master. If you decide to set things up to track the upstream repositories, I start the master, then the slave, and if both are up fine, I start the twistd daemon for get-pushes.

Now let's trigger some builds:

Open ``stage/workdir/mozilla/browser/locales/en-US/file.properties`` in your favorite editor, and do a modification. I suggest to just do a whitespace edit, or to change the value of the existing entity, as that is going to keep your localizations green. Check the change in to the working clone, and then push. The get-pushes output should show that it got a new push, and then on the next cycle, feed the push into the database. You'll notice by the output of a hg pull showing up in the log. On the next poll on the l10n-master, builds for all 4 locales should trigger. You should see an update of four builds on `the waterfall <http://localhost:8000/builds/waterfall>`__, and 4 locales on the ``test`` tree on the `local dashboard <http://localhost:8000/dashboard/>`__.
