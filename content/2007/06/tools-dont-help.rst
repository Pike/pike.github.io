tools don't help
################
:date: 2007-06-26 04:03
:category: L10n, Mozilla
:slug: 2007/06/tools-dont-help

Localization tools are a pity. The Hebrew localizers switched from one tool to the other, and attached a patch to bug `373436 <https://bugzilla.mozilla.org/show_bug.cgi?id=373436>`__, +1190/-818 lines for toolkit alone. Given that toolkit 'only' has some 2000 strings, that's a pretty big diff.

I wrote a diff tool that ignores all the formatting and ordering, and oops. The actual changes boil down to +6/-6. Even worse, I can hardly a- that patch, if I want that localization to go forward.

To anyone pondering to write l10n tools, would you please consider writing them with Openess in your mind? Tool lock-in is not an option, even if it spares you half a day of work to write a decent serialization architecture.

Oh, and don't ask me to endorse your tool until bugs like this are fixed.

</rant>
