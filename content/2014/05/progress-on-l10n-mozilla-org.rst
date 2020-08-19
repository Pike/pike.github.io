Progress on l10n.mozilla.org
############################
:date: 2014-05-22 04:44
:category: L10n
:tags: L10n, Mozilla
:slug: 2014/05/progress-on-l10n-mozilla-org

Today we're launching an update to `l10n.mozilla.org <https://l10n.mozilla.org./>`__ (elmo).

Team pages and the project overview tables now contain sparklines, indicating the progress over the past 50 days.

Want to see how a localization team is doing? Now with 100% more self-serve.

If the sparklines go up like so

|good progress|

the localization is making good progress. Each spark is an update (either en-US or the locale), so sparks going up frequently show that the team is actively working on this one.

If the sparklines are more like

|not so much|

then, well, not so much.

The sparklines always link to an interactive page, where you can get more details, and look at smaller or larger time windows for that project and that locale.

You should also look at the bugzilla section. A couple of bugs with recent activity is good. More bugs with no activity for a long time, not so much.

Known issues: We still have localizations showing status for ``central/nightly``, even though those teams don't work on central. Some teams do, but not all. Also, the sparklines start at some point in the past 50 days, that's because we don't figure out the status before. `We could <https://bugzilla.mozilla.org/show_bug.cgi?id=1014497>`__.

.. |good progress| image:: /images/2014/05/Screen-Shot-2014-05-22-at-12.44.15-PM.png
   :class: aligncenter size-full wp-image-563
   :width: 220px
   :height: 64px
   :target: /images/2014/05/Screen-Shot-2014-05-22-at-12.44.15-PM.png
.. |not so much| image:: /images/2014/05/Screen-Shot-2014-05-22-at-12.47.58-PM.png
   :class: aligncenter size-full wp-image-564
   :width: 228px
   :height: 74px
   :target: /images/2014/05/Screen-Shot-2014-05-22-at-12.47.58-PM.png
