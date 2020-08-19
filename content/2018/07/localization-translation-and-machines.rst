Localization, Translation, and Machines
#######################################
:date: 2018-07-12 06:25
:category: L10n
:tags: L10n, Mozilla
:slug: 2018/07/localization-translation-and-machines

TL;DR: Is there research bringing together Software Analysis and Machine Translation to yield Machine Localization of Software?

   I’m Telling You, There Is No Word For ‘Yes’ Or ‘No’ In Irish

from `Brendan Caldwell <https://brendycaldwell.com/2013/03/19/on-craic-im-telling-you-there-is-no-word-for-yes-or-no-in-irish/>`__\ 

The art of localizing a piece of software with a *Yes* button is to know what that button will do. This is an example of software UI that makes assumptions on language that hold for English, but might not for other languages. A more frequent example in both UI and languages that are affecting is piecing together text and UI controls:

|image0|

In the localization tool, you'll find each of those entries as individual strings. The localizer will recognize that they're part of one flow, and will move fragments from the shared string to the drop-down as they need. Merely translating the individual segments is not going to be a proper localization of that piece of UI.

If we were to build a `rule-based <https://en.wikipedia.org/wiki/Rule-based_machine_translation>`__ machine localization system, we'd find rules like

-  ``gaelic-yes``:
   If the title of your dialog contains a verb, localize *Yes* by translating the found verb.

   .. raw:: html

      </p>

-  | ``pieced-ui``:
   | For each variant,

   .. raw:: html

      </p>

   -  Piece together the fragments of English to a single sentence
   -  Translate the sentences into the target language
   -  Find shared content in matching positions to the original layout
   -  Split each translated fragment, and adjust the casing and spacing
   -  Map the subfragments to the localization of the English individual fragments

   Map the shared fragment to the localization of the English shared fragment

Now that's rule-based, and it'd be tedious to maintain these rules. `Neural Machine Translation <https://en.wikipedia.org/wiki/Neural_machine_translation>`__ (NMT) has all the buzz now, and Machine Learning in general. There is `plenty of research <https://slator.com/academia/here-machine-translation-researchers-are-geeking-out-on/>`__ that improves how NMT systems learn about the context of the sentence they're translating. But that's all text.

It'd be awesome if we could bring Software Analysis into the mix, and train NMT to localize software instead of translating fragments.

For Firefox, could one train on English and localized DOM? For Android's XML layout, a similar approach could work? For projects with automated screenshots, could one train on those? Is there enough software out there to successfully train a neural network?

Do you know of existing research in this direction?

.. |image0| image:: /images/2018/07/Pieced-together-UI-300x94.png
   :class: aligncenter size-medium wp-image-600
   :width: 300px
   :height: 94px
   :target: /images/2018/07/Pieced-together-UI.png
