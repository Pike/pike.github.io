Localizing Lorentz
##################
:date: 2010-06-24 07:20
:category: L10n
:tags: L10n, Mozilla
:slug: 2010/06/localizing-lorentz

It's been a while, but I'll take a stab at what we did to localize Lorentz, i.e., how did we add strings to a stable branch?

The underlying principle was add-on compatibility, that is, language packs that are out there and compatible with ``3.6.*`` needed to continue to work. The second principle was that while we didn't want to break existing language packs, we did want to offer our localizers to work on the new strings to get the best possible user experience. So we're adding strings without adding strings.

Given that we had a project branch for Lorentz, the work on the Lorentz branch itself was rather simple, just code like you'd always do. We didn't do any special branch mechanics there, and built the Lorentz branch against the regular l10n repositories on 1.9.2. The only caveat here was to not remove strings, only additions were OK. As soon as that work got stable in terms of the strings used, we landed a patch that, for each new string, `adds a hard-coded fallback to the code <http://hg.mozilla.org/projects/firefox-lorentz/rev/30ca0b454785>`__. That way, you pick up the localized string without failing if it doesn't exist. So much for the work on the project branch.

On the stable branch, things are a bit more tricky. Of course we needed to be able to continue shipping security updates from the stable branch, that is, we didn't want to turn builds red for strings that aren't really missing. Yet we wanted to signal that the strings are there and to be localized. Up until then, we only had two stages of strings, missing or not. The latter is what we use for handlers in region.properties, for example. We needed a third stage, "report on this string, but don't fail". So I added a third stage to the logic around filter.py in compare-locales. This logic is now used in `filter.py on the 1.9.2 branch <http://hg.mozilla.org/releases/mozilla-1.9.2/file/ad815619652f/browser/locales/filter.py#l27>`__, but not on central. Another necessary addition was to support filter.py for each module, so that we only had to hack around the toolkit strings once, and ont for all apps on 1.9.2. So there's now a `filter.py file for toolkit on 1.9.2 <http://hg.mozilla.org/releases/mozilla-1.9.2/file/ad815619652f/toolkit/locales/filter.py#l8>`__, making sure we only report on the lorentz strings in toolkit.

Once that logic was in place, we added a "strings-only" patch to 1.9.2, which had the benefit of exposing the en-US strings in the regular repository that our l10n community is working on.

The outcome today is that out of the 74 languages we ship, only 25 still rely on the en-US fallback strings.

In bullet points, that'd be:

-  Do not remove strings, so that newer language packs are compatible with older releases.
-  Add strings with en-US fallbacks, so that they can be localized, but don't error when missing.
-  Make filter.py for the module (browser/mail/toolkit) "report" on the new strings, so that localizers see the strings without hiding real errors from non-fatal ones.
-  Land strings early on the stable branch to get them exposed to l10n (with filter.py, see above).
