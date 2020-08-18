How is ab-CD doing?
###################
:date: 2008-01-28 15:52
:category: L10n, Mozilla
:slug: 2008/01/how-is-ab-cd-doing

Just wanted to plot a brief update. I'm currently mostly working on improving our understanding of how localizations are doing for Firefox 3. The plan is to come up with a dashboard, gathering at least the quantifiable machine-readable information. The work there is improving nicely, you can see it at http://l10n.mozilla.org/dashboard/. There is still stuff to come, like, I'm likely going to make the Builds tab the default one, and I'm going to move away from red and green.

Now, moving away from red and green made a good jump right now, as I have made live an output that actually visualizes the status of the product localization over time. Right now, it's aiming to do 30 days, but it doesn't have enough stats for that just yet. I'm using Simile's timeplot here, and exhibit for the index. To explain the graph (I suck at markup, so it's a crufty legend right now), the red lines are missing entities, black is obsolete. Those two have their y-axis on the left. The grey beast is the unchanged entries, with the y-axis on the right. The blue ticks are actually changes by the localizer (not in en-US, the graph updates though), click on those to get the check-in messages, the committer is a link to a bonsai query for +/- half an hour. You can browse through the active l10n stats on http://l10n.mozilla.org/buildbot/statistics, which points to, for example, the `Polish stats <http://l10n.mozilla.org/buildbot/statistics?buildername=linux-langpack&tree=trunk&app=browser&locale=pl>`__.

`Code in hg <http://hg.mozilla.org/users/axel_mozilla.com/tooling/>`__.
