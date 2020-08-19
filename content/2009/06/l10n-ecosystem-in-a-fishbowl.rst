L10n ecosystem in a fishbowl
############################
:date: 2009-06-01 07:02
:category: L10n
:tags: build, buildbot, L10n, Mozilla
:slug: 2009/06/l10n-ecosystem-in-a-fishbowl

Building the infrastructure for our l10n builds is hard, mostly because it's consisting of a ton of things that you don't have control over. We're building 3 and a half applications, Firefox, Thunderbird, Fennec, and Sunbird for calendar. Firefox is built on three versions, one of which is still coming from CVS. Thunderbird is one version on CVS, one on hg. We're touching some 170 hg repos, and a single check-in can do anything between no build, one build, or up to almost 200 builds. Rinse, repeat, yeah, 200 builds for a single landing. Worse than that, you don't have any control over who's landing what when where. Bottom line, you really can't test a change in the l10n build automation reliably in our production setup.

You can create a fake ecosystem, though, and I'll explain a bit how that works. Of course it doesn't end up being trivial, but it's contained. It's not trying to cover the CVS branches, those would require a setup of bonsai, which I chicken away from. Take this post with a grain of salt, I assume there are some errors here as most of it is typed from memory.

As with any recipe, here are the list of ingredients:

-  A set of hg repositories, both for a fake application and some fake l10n repos.
-  An hg server serving those repositories (make that port 8001).
-  Some buildbot infrastructure working on top of these repositories that you're trying to test.
-  Possibly an instance of the l10n dashboard presenting both the build and the l10n data.

The initial chunk is creating the repositories. I created a helper script `create-stage <http://hg.mozilla.org/build/buildbotcustom/file/default/bin/l10n-stage/create-stage>`__ that does that, which is part of `buildbotcustom/bin/l10n-stage <http://hg.mozilla.org/build/buildbotcustom/file/default/bin/l10n-stage/>`__. It's main purpose is to get the templates, hooks etc that are part of our server-side setup on hg.mozilla.org, create some upstream repos for en-US and l10n, and push some initial content from a set of working clones. You call it like

``python l10n-stage -l stagedir``

The ``-l`` keeps the l10n repositories from pushing their initial content, which yields a scenario that is closer to what we have upstream, i.e., a flock of en-US pushes before the l10n repos start. This command creates a bunch of main repositories in the ``repos`` subdir of ``stagedir``, and a bunch of working clones in ``workdir``. It also creates a ``webdir.conf``, that you'll use to run the local hg http server. Let's run that now, in ``stagedir``:

``hg serve -p 8001 --webdir-conf=webdir.conf -t repos/hg_templates``

Now you have a local setup of a application repository called ``mozilla``, and 4 localizations in ``l10n``, ``ab``, ``de``, ``ja-JP-mac``, ``x-testing``. They're all equipped with the same hooks that we run on hg.m.o, in particular, they support pushlog.

Now on to the buildbot infrastructure. There's a sibling script to create-stage, `create-buildbot <http://hg.mozilla.org/build/buildbotcustom/file/default/bin/l10n-stage/create-buildbot>`__, which should create a master setup that is rather close to what we run on releng. It supports various degrees of parallelism for multiple slaves on three platforms, does only dummy builds, though. IIRC. I want to go into more detail on how to set up the new dashboard master, though.

The dashboard master is merely running compare-locales on the actual source repositories. It does come with our bonsai replacement ``pushes``, though. That's basically a pushlog spanning repositories, including file and branch indexing. Here's the basic software components you'll need:

-  django 1.0.x (1.1pre might work, too)
-  buildbot 0.7.10p1, older versions won't work

and from hg.m.o, you'll need `compare-locales <http://hg.mozilla.org/build/compare-locales/>`__, `locale-inspector <http://hg.mozilla.org/users/axel_mozilla.com/locale-inspector/>`__, `l10n-master <http://hg.mozilla.org/users/axel_mozilla.com/l10n-master/>`__, `buildbotcustom <http://hg.mozilla.org/build/buildbotcustom/>`__ and `django-site <http://hg.mozilla.org/users/axel_mozilla.com/django-site/>`__.

Firstly, you set up the db. sqlite and mysql should both work, mysql is actively tested. Edit the various settings.py files to reference your db, with an absolute path if sqlite, and create the schema. The main entry point to the django site is l10n_site, go in there to run ``python manage.py syncdb``. Another edit you want to do is to point ``REPOSITORY_BASE`` to a dir where you can stage another set of clones of your repos. I suggest to not share the hg master repo dir here.

Next, create a buildbot master and a slave. You do that by running the buildbot create-master command on your local clone of ``l10n-master``. You'll need to adapt l10nbuilds.ini to the test set up,

::

   [test]
   app = browser
   type = hg
   locales = all
   mozilla = mozilla
   l10n = l10n
   repo = http://localhost:8001/
   l10n.ini = browser/locales/l10n.ini
   builders = compare

I should put that into the repo somewhere, I guess.

Setting up the slave is trivial, you need to make sure it's on the same machine, though. It will run on the django clones directly.

Before starting master and slave, make sure that all the deps are in your ``PYTHONPATH``.

Last but not least, you need to get all the pushes from your repo setup into your django setup. First, you need to tell the db which repositories it's supposed to get from where. I created sample data for the test app, which you can load by

``python manage.py loaddata localhost``

The repositories I use for the production environment are in ``hg_mozilla_org``, fwiw. You fill the database with the actual push data by running a twisted daemon. Inside django-site, run

``twistd get-pushes -n -t 1 -s l10n_site.settings``

That will ping one repo per second, not update, with data from ``l10n_site.settings``. Now you have everything set up, and you can start to edit en-US and l10n files in your workingdir, and push, and see how that changes your builds and dashboard.

The buildbot waterfall will be on port 8364, and with ``python manage.py runserver``, the dashboard will show up on port 8000. None of this is setup to be on a production server at this point, but it's good for testing.

*Update: Forgot to mention that you need to bootstrap the repo lists.*
