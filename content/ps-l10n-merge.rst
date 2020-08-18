PS: l10n-merge
##############
:date: 2009-11-06 08:02
:category: L10n, Mozilla
:tags: build, L10n, Mozilla
:slug: ps-l10n-merge

`Armen just blogged about this <http://armenzg.blogspot.com/2009/11/firefox-release-engineering.html>`__, and as it's constantly mentioned around l10n, I wanted to add a bit more detail to l10n-merge.

l10n-merge is originally an idea by our Japanese localizer dynamis. The current implementation used in the builds is by me, integrated as an option to compare-locales. There are spin-offs of that algorithm in the silme library, too.

l10n-merge attempts to solve one reason for "yellow screens of death", i.e., XML parsing errors triggered by incomplete localizations. This is really crucial as localizations don't just pop up by swinging magic wands, they're incremental work, and a huge chunk of that. So in order to test your work, you need to see the strings you have in, say, Firefox, without having the other 4000 strings done yet. Other l10n-infrastructures handle this by falling back to the original language at runtime (gettext), but doing that at runtime of course has perf impact, and size. l10n-merge does the same thing at compile (repackaging) time.

Design goals for l10n-merge were:

-  not mess with any source repositories
-  not do any file-io that's not really needed

Thus, in order to not mess with the source repos, l10n-merge doesn't modify the sources inline, but creates copies of the files it touches in a separate dir. Commonly, we're using '``merged``' in the build dir. Now, creating a full copy of everything would be tons of file io, so l10n-merge only creates copies for those files which actually need to get entities added to existing localized content. This plays together with code in JarMaker.py which is able to pick up locale chrome content from several source dirs.

A Firefox localization contains some 450 files, and say for the current 9 B1-to-B2 missing strings in two files, it would copy over those two files from l10n, and add the missing entities to the end. Then JarMaker is called with the right options, and for those two files, will pick them up from ``merged``, the rest of the localization is gotten from l10n. For missing files, it actually looks into the en-US sources, too, so we don't have to do anything for those. To give an example, for ``chrome/browser/foo`` in the ``browser`` 'module', it searches:

#. ``.../merged/browser/chrome/foo``
#. ``l10n/ab-CD/browser/chrome/foo``
#. ``mozilla/browser/locales/en-US/chrome/foo``

Now it's time to list some pitfalls that come with l10n-merge:

-  If you're passing the wrong dir for mergedir, nothing breaks. All build logic breakage would come from missing files, and due to the fallback to en-US, there are no missing files.
-  l10n-merge, as compare-locales, doesn't cover XML parsing errors inside entity values yet. `Bug 504339 <https://bugzilla.mozilla.org/show_bug.cgi?id=504339>`__ is filed, there are some tricky questions on reporting, as well as having to write an XML parser from scratch.
-  l10n-merge only appends entities, but that's fine 95% of the time. Only counter-examples are DTDs including other DTDs.
-  People using l10n-merge need to manually maintain the merge dir. Pruning it via compare-locales is risky business if you specify the wrong path by accident, so I consider this a feature. But if you're seeing Spanish in a French build, clobber the mergedir and build again :-)
