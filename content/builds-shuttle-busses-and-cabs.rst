Builds, shuttle busses and cabs
###############################
:date: 2008-02-07 17:52
:category: Mozilla
:slug: builds-shuttle-busses-and-cabs

There have been a few blog posts recently about when to do builds. I'd like to add a few thoughts of mine.

| I'll follow mostly two trains of thought
| \* each check-in raises a bunch of questions, to which we want answers -- quick
| \* the road to these answers has a limited traffic capacity

The current proposals map to two images in my head, the current "build continuously" model is basically a shuttle bus. "Build on check-in" is more like a cab. Now, the interesting artifact in our picture is that both the shuttle bus and the cab have an unlimited capacity for passengers, or check-ins. Do check-ins blend? Yes, they do.

Now, the blending of patches has an upside and a downside. On the upside, it enables us to get around traffic jams. We can just transport as many check-ins as we get. The downside is, the answers that the builds and test runs give can't be associated with individual check-ins anymore. Well, "passes" can, "failures" cannot. I'll postpone perf testing here, 10% win, 9% loss, end up where you were.

There have been previous posts on whether shuttle buses or cabs are the way to go, and my answer is "neither". I guess there is an easy answer if you assume that you have no limits on machines, in that case, just let them run on check-in. That's great -- at least as long as you can actually relate the resulting build, and the tests run on that build, to a source tree. Once we're running out of machines, the story is a little different. Every machine should be continuously building then, and the trick is, 'by then'. That is, each build should adjust the time it's waiting for more check-ins such that, by the time the last idle machine kicks off, all available machine are fairly distributed across the ETA of the next machine. Let's pick some arbitrary number for an initial stabilization time, Tmin. Waiting time for machine n of N could then be

Tmin \* (N-n)/(N-1) + ETA/2 \* (n-1)/(N-1)

if we choose to weight linearly. I did a little `scatterplot game <http://people.mozilla.org/~axel/waitings.html>`__ for you to pick different amounts of slaves, mintimes, etas and such. I bet there is a way to pick better values for Tmin and the power based on bonsai and tinderbox statistics.

Sadly, neither tinderbox nor buildbot offer this, but I could imagine that this would be of more general use to buildbot clients, and would be something to get upstream.

The other part of the picture is "did this particular change impact ???". Now, for questions like "does this compile?", the answer is fairly trivial. I think the same goes for things like unit tests or ref tests. As long as the current state of the tree passes, we're fine. When it fails, that's a more interesting question. Like, it might make sense to then actually refine the built source stamps.

But for questions regarding perfomance, there are worst case scenarios. Like, you see a 1% regression. Is it a 1% regression from patch 2, or is patch 2 actually improving performance, but patch 1 just totally borked it? On top of that, performance data is noisy data. There's likely a good heuristic algorithm to distribute sampling of builds to measure performance on based on total count of tests run per build, age of the build, and current noise on the performance data for that build. So in particular for performance testing, it would be interesting to not just build the latest well-defined source state (thanks cvs), but also to be able to build previously not built source states, and in the performance architecture, to spend the available cycles to further refine the statistics on a range of recent builds, instead of just the latest. And to, of course, relate those data points with the source stamp that correlates to the build that was tested right now.
