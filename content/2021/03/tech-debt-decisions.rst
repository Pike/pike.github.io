Technical Debt as Decisions
###########################
:date: 2021-03-09 18:00:00
:category: Tech
:tags: techdebt
:slug: 2021/03/tech-debt-decisions

I've got thinking about technical debt a lot lately, and how to manage it. This post will be about decisions as a definition of technical debt.

In a second post I'll talk about investments, risk management and insurances as a model on how to live with technical debt. I also want to talk about how to make conscious decisions within that framework, in particular with Open Source tech in mind. That's probably going into a third post.

To set the context, why would you care? Technical debt is not going to kill your project or product. But it can slow down and weaken your response. If you're out of luck, any other seemingly harmless challenge can kill your project. It's like one of those diseases you die with, not of.

Let's talk about decisions. Good decisions. Bad decisions. I'm going with loaded words here, mostly because they're short. The difference between a good and a bad decision is the number of people that regret a given decision. At a given point in time.

Let's do a hypothetical and constructed example of how that ties into technical debt. Your organization has a service that runs as is, you don't have feature requests or planned work for it. It's running on Python 2, and none of the other parts that create that service have dropped support for Python 2. You call a meeting to decide on adding Python 3 support. You decide not to, and everyone is excited to work on stuff that pushes your organization forward.

You wake up one morning, and someone's taking money out of your bank account. You investigate, and it turns out there's a known vulnerability in one of the external parts of said service. Not too bad, though, there's already a new version with a fix. They've also dropped Python 2 support.

We made a perfectly fine decision, we have a somewhat urgent problem and a seemingly easy fix. The elephant in the room is that the easy fix isn't easy for **us**. The decision to not add support for Python 3 is a bad decision **now**. We have technical debt. Now we have three possible ways forward.

* We stick to our original decision. We can do that in two ways.

  * We shut the project down. Maybe there's an alternative today? Or maybe can't access or afford any of the alternative routes and shut down anything related. [#elmo]_
  * We get a backport of the security fix. Either by paying an upstream vendor, or by forking and doing it ourselves.

* We make a change decision, and add Python 3 support. And then we fix the problem at hand.

The significant aspect of technical debt is the "backport" alternative. Decisions that just turned bad usually offer an affordable option. Those are a mild amount of work with clear deliverables, which makes them attractive. On the downside, they keep the bad decision around, and frequently add another bad decision on top. In our example, you know right away that you regret maintaining a Python 2 fork.

The example I'm using is luckily and awkwardly constructed, but we've all heard these before, right?

* It's OK, it's just an experiment.
* The experiment was a great success, let's ship the code we have.

I think of technical debt as the legacy of our past decisions. And that there are no good or bad decisions. There are the decisions that are good for us right now, and the ones that aren't. The quality of a decision is always bound to our particular current context. The people that make up *we* is changing over time, competing priorities change over time, as do external factors.

As much as this is a cliffhanger, this is also all that I want to put into the first post. In the next post, I'm going to talk about how to live with technical debt, and when to make good decisions.

If you have comments, feel free to contact me on `Twitter`_ and `LinkedIn`_.

.. [#elmo] I've done that not too long ago. The details are not all that relevant as is this: Shut down things you can't keep up.

.. _Twitter: https://twitter.com/axelhecht
.. _LinkedIn: https://www.linkedin.com/in/draxelhecht
