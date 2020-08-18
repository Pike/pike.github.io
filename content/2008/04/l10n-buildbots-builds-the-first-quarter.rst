L10n buildbots builds, the first quarter
########################################
:date: 2008-04-14 09:37
:category: L10n, Mozilla
:slug: 2008/04/l10n-buildbots-builds-the-first-quarter

The current setup of my l10n buildbot is running for 3 months now, or a quarter. I figured that'd be a good time to do some stats.

In these three months, the l10n server ran about 10600 builds, 10416 of those on trunk. Of the latter, 2330 builds succeeded, 8086 failed (fun number pun). The total amount of build time during these three months was merely 3 days, the rest of the day it was just pounding bonsai-l10n and slacking.

The mean response time, that is, the time between the change that bonsai shows and the end of the build is 3-4 minutes, with the following distribution

|Histogram of build lags|

The lags go as high up as almost 2 hours, the really big jumps seem to be problems on bonsai-l10n, there are a few builds taking 20-30 minutes due to slowness in cvs check-outs. I'm not showing some 36 builds in the diagram above. But the histogram shows nicely, you should in general be done within 10 minutes, and even if the build didn't do langpacks on linux but full repacks on windows, I would expect a similar reponsiveness on comparable hardware to the l10n server.

The bad news is, the code is mostly non-reviewed, and should use a pending feature for buildbot, custom build properties. Otherwise, reconfig will never work.

.. |Histogram of build lags| image:: /images/2008/04/lag-histogram.png
   :target: http://blog.mozilla.org/axel/2008/04/14/l10n-buildbots-builds-the-first-quarter/histogram-of-build-lags/
