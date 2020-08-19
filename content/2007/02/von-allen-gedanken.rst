Von allen Gedanken ...
######################
:date: 2007-02-19 09:15
:category: L10n
:slug: 2007/02/von-allen-gedanken

Welcome to another round of `l20n <http://wiki.mozilla.org/L20n>`__. I finally added expressions and macros. Expressions are closely following the C grammar, I ripped out the bitwise operators and some C-isms. Macros are a new grammar struct to implement things like plural forms, with the additional benefit that I didn't limit this to one form, but actually embedded this into the grammar. That is, if a localizer feels like having to use a different implementation for plurals, (s)he can. This should be useful in particular when it comes down to limiting the plural forms on integers, non-negative numbers, general floats, if you want to handle NaN etc. An example for such a macro would be

   <plural: (n) -> {n != 1}>

which happens to be the gettext plural macro for English and German. You can see that in action on my new `plurals example <http://people.mozilla.com/~axel/l20n/js-l20n/sample-04.html>`__.

I'm looking forward to see folks submitting patches to add locales here. If someone feels like improving the web pages a bit, I wouldn't be offended either, I know that most of this feels really as hacky as it is.

If you are like me and would like to see the grammar and more spec work online, I'd appreciate your opinions on the licensing of that, just asked today in .legal.

*... schätze ich doch am meisten ... die interessanten.*
