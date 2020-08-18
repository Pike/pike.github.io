Lazyweb, can I have compilers in js and python?
###############################################
:date: 2010-08-31 08:10
:category: L10n, Mozilla
:tags: l20n
:slug: lazyweb-can-i-have-compilers-in-js-and-python

For our l20n project, we'll want to compile l20n source files into javascript. We want to do that both at compile time, and at runtime.

For runtime, I'll need the compiler written in js by all chances, and for compile time, I'd rather go with python so that I don't have build a HOST_JS or something. Of course, I don't want to maintain two completely independent compiler implementations.

Thus I'm looking for code that can generate compilers in js and python, preferably itself in python or some other language we can use at build time, or at least use for one-off compilations.

Any tips?
