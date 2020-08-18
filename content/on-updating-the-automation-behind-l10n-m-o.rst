On updating the automation behind l10n.m.o
##########################################
:date: 2017-03-03 13:01
:category: L10n, Mozilla
:tags: buildbot, compare-locales, L10n, Mozilla
:slug: on-updating-the-automation-behind-l10n-m-o

Or, how to change everything and nobody sees a difference.

*Heads up: All I'm writing about here is running on non-web-facing VMs behind VPN.*

**tl;dr:** I changed 5 VMs, landed 76 changesets in 7 repositories, `resolving 12 bugs <https://bugzilla.mozilla.org/buglist.cgi?bug_id=1137667%2C1341886%2C1342649%2C1138550%2C1138553%2C1137666%2C1336138%2C1330707%2C1137668%2C1333398%2C1290906%2C1343233&bug_id_type=anyexact&list_id=13470378&query_format=advanced#>`__, got `two issues in docker <https://github.com/issues?utf8=%E2%9C%93&q=user%3Adocker+is%3Aissue+author%3APike+>`__ fixed, and took a couple of days of downtime. If automation is your cup of tea, I have some open questions at the end, too.

To set the stage: Behind the scenes of the `elmo website <https://l10n.mozilla.org/>`__, there's a system that generates the data that it shows. That system consists of two additional VMs, which help with the automation.

One is nick-named *a10n*, and is responsible for polling all those mercurial repositories that we use for l10n, and to update the elmo database with information about these repositories as it comes in. elmo basically keeps a copy of the mercurial metadata for quicker access.

The other is running ``buildbot`` to do the actual data collection jobs about the l10n status in our source repositories. This machine runs both a master and one slave (the actual workhorse, not my naming).

This latter machine is an old VM, on old OS, old Python (2.6), never had real IT support, and is all around historic. And needed to go.

With the help of IT, I had a new VM, with a new shiny python 2.7.x, and a new storage. Something that can actually run current versions of compare-locales, too. So I had to create an update for

+-----------------------------------+---+---------------------------------------------------------------------------------------------------------------------+
| Python 2.6                        | → | Python 2.7.x                                                                                                        |
+-----------------------------------+---+---------------------------------------------------------------------------------------------------------------------+
| globally installed python modules | → | virtualenv                                                                                                          |
+-----------------------------------+---+---------------------------------------------------------------------------------------------------------------------+
| Django 1.4.18                     | → | Django 1.8.x                                                                                                        |
+-----------------------------------+---+---------------------------------------------------------------------------------------------------------------------+
| Ubuntu                            | → | CentOS                                                                                                              |
+-----------------------------------+---+---------------------------------------------------------------------------------------------------------------------+
| Mercurial 3.7.3                   | → | Mercurial 4.0.1 and hglib                                                                                           |
+-----------------------------------+---+---------------------------------------------------------------------------------------------------------------------+
| individual local clones           | → | `unified <http://mozilla-version-control-tools.readthedocs.io/en/latest/hgmozilla/unifiedrepo.html>`__ local clones |
+-----------------------------------+---+---------------------------------------------------------------------------------------------------------------------+
| No working stage                  | → | docker-compose up                                                                                                   |
+-----------------------------------+---+---------------------------------------------------------------------------------------------------------------------+

At the same time, we also changed hg.m.o from http to https all over the place, which also required a handful of code changes.

One thing that I did not change is buildbot. I'm using a heavily customized version of buildbot 0.7.12, which is incompatible with later buildbot changes. So I'm tied to my branch of 0.7.12 for now, and with that to Twisted 8.2.0. That will change, but in a different blog post.

Unified Repositories
~~~~~~~~~~~~~~~~~~~~

One thing I wanted and needed for a long time was to use *unified* clones of our mercurial repositories. Aside from the obvious win in terms of disk usage, it allows to use mercurial directly to create a diff from a revision that's only on aurora against a revision that's only on beta. Sadly, I did think otherwise when I wrote the first parts of elmo and the automation behind it, often falling back to ``default`` instead of an actual hash revision, if I didn't know anything ad-hoc. So that had to go, and required a surprising amount of changes. I also changed the way that comparisons are triggered, making them fully reproducible. They also got more robust. I used to run ``hg id -ir .`` to get the revision, which worked OK, unless you had extension errors in stdout/stderr. Meh. Good that that's gone.

As I noted, the unified repositories also benefit doing diffs, which is one of the features of elmo for reviewing localizations. Now that we can just use plain mercurial to get those diffs, I could remove a bunch of code that created diffs between aurora and beta by creating diffs between each head and some ancestor, and then sticking those diffs back together. Good that that's gone.

Testing
~~~~~~~

Testing an automation with that many moving parts is hard. Some things can be tested via unit tests, but more often, you just need integration tests. I still have to find a way to write automated integration tests, but even manual integration tests require a ton of set-up:

-  elmo
-  MySQL
-  ElasticSearch
-  RabbitMQ
-  Mercurial upstream repositories
-  Mercurial web server
-  a10n get-pushes poller
-  a10n data ingestion worker
-  Buildbot master
-  Buildbot slave

Doing this manually is evil, and on Macs, it's not even possible, because Twisted 8.2.0 doesn't build anymore. I used to have a script that did many of these things, but that's .... you guessed it. Good that that's gone. Now I have a ``docker-compose`` `test setup <https://github.com/Pike/test-l10n>`__, that has most things running with just a ``docker-compose up``. I'm still running elmo and MySQL on my host machine, fixing that is for another day. Also, I haven't found a good way to do initial project setup like database creations. Anyway, after finding a couple of bugs in docker, this system now fires up quickly and let's me do various changes and see how they pass through the system. One particularly nice artifact is that the output of docker-compose is actually all the logs together in one stream. So as you're pushing things through the system, you just have one log to watch.

As part of this work, I also greatly simplified the code structure, and moved the buildbot integration from three repositories into one. Good that those are gone.

snafus
~~~~~~

Sadly there were a few bits and pieces where my local testing didn't help:

Changing the URL schemes for hg.m.o to https alongside this change triggered a couple of problems where Twisted 8.2 and modern Python/OpenSSL can't get a connection up. Had to replace the requests to websites with synchronous ``urllib2.urlopen`` calls.

Installing mercurial in a virtualenv to be used via hglib is good, but WSGI doesn't activate the virtualenv, and thus ``PATH`` isn't set. My `fix <https://github.com/mozilla/elmo/commit/737a1328285a89d595bfabb29b2b900762fbdb37>`__ still needs `some server-side changes <https://bugzilla.mozilla.org/show_bug.cgi?id=1343898>`__ to work.

I didn't have enough local testing for the things that Thunderbird needs. That left that setup burning for longer than I anticipated. The fix wasn't hard, just badly timed.

Every now and then, Django 1.8.x and MySQL decide that it's a good idea to throw away the connection, and die badly. In the case of long-running automation jobs, that's really hard to prevent, in particular because I still haven't fully understood what change actually made that happen, and what the right fix is. I just plaster ``connection.close()`` into every other function, and see if it stops dying.

On Saturday morning I woke up, and the automation didn't process Firefox for a locale on aurora. I freaked out, and added tons of logging. Good logging that is. Best logging. Found a different bug. Also found out that the locale was Belarus, and that wasn't part of the build on Saturday. Hit my head against a wall or two.

Said logging made uncaught exceptions in some parts of the code actually show up in logs, and discovered that I hadn't tested my work against bad configurations. And we have that, Thunderbird just builds everything on central, regardless of whether the repositories it should use for that exist or not. I'm not really happy yet with the way I fixed this.

Open Questions
~~~~~~~~~~~~~~

-  Anyone got taskcluster running on something resembling docker-compose for local testing and development? You know, to get off of buildbot.
-  Initial setup steps for the docker-compose staging environment are best done ... ?
-  Test https connections in docker-compose? Can I? Which error cases would that cover?
