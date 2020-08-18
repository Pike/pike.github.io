git-merge 2013
##############
:date: 2013-05-13 05:36
:category: Mozilla
:tags: git, GitMerge, Mozilla
:slug: git-merge-2013

I spent Friday and Saturday on `git-merge <http://git-merge.com/>`__, an unconference on git. Thursday was developer day, for core contributors to git itself, and libgit2/jgit. I didn't go there. Friday was "user" day, and Saturday was hackday. I figured it might be useful to go to the userday, and turned out, it was. It wasn't all that much about users at all. It was strictly unconference, so people would take the stage and give a quick lightening talk, and later in the day we had a few breakout sessions. The most user-like people were folks migrating to git just now, and they had a good deal of folks to talk to in the breakout session.

The rest of Friday was actually library and tool hackers talking about what they're doing. There are notes on `github.com/git-merge/user-day <https://github.com/git-merge/user-day/blob/master/docs/01-index.md>`__, but I do want to hightlight a few.

`imerge <https://github.com/mhagger/git-imerge>`__ is probably the most interesting to gecko hackers. It allows you to merge or rebase intensive histories with conflicts incrementally, with tons of automation. It even allows to do test runs on the merges it does automatically. If you ever resolved the same conflict 10 times in one rebase, this is for you.

libgit2 was under the hood of many, with core contributors of the library itself being there, plus the maintainers of at least the C# and the python bindings. There was also a good deal of tooling based on jgit, a pure-java implementation of git.

Much debate on java vs not, actually. And Cmd-F1. Little conflict between git and hg.

I also got to enjoy the github backend talk by `vmg <https://github.com/vmg>`__, with Ernie, Bert, and smoke through chimneys. I had seen a recording of it before, but it was well worth it seeing it live.

I joined the breakout session about teaching git, and had the pleasure to be in a group that tought git in various parts of the globe. Yes, that might be relevant to me, so that was good exercise. I talked with `Scott Schacon <https://github.com/schacon>`__ about localized version of the git book, and localized github docs, too.

Given that I had the chance to talk and co-hack with all those tooling guys, I decided to drop by on Saturday for the hack day. I wanted to take the opportunity to talk about my weird repository rewrite questions, and so I did.

Saturday was great. I only got 20 lines of code written, but I finally understood what git is about in the back-end. There's loads of hackery that you can do, and funny enough, both I and `Ben <https://github.com/ben>`__ ended up hacking on a repository rewrite algorithm, which helped me a lot, both talking about the structure of the code, as well as vetting the approach. His code in C# is actually in a `PR <https://github.com/libgit2/libgit2sharp/pull/429>`__. Worth a look for people that want to see how to hack tooling on top of that binding. I tried the same in python, and succeeded to some extent. David Ibáñez helped me a great deal. But it also showed me the difference between the C# API and the python bindings. If only mono was easy to get up on the mac.

On the conference itself, it was set up at the Radisson Blu next to the Berliner Dom, which is a nice venue for that size. Wifi worked, food and beer were there. It's sad that many people claimed tickets and didn't show up. Now you know what you missed, and what you made other people miss. Bad bunny, no chocolates! Thanks again for Jen for setting things up great.

Thanks to all the folks at git-merge for making it a great event. See you in Berlin…
