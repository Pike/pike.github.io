Bugzilla dancing for l10n changes
#################################
:date: 2007-03-08 11:25
:category: L10n, Mozilla
:slug: bugzilla-dancing-for-l10n-changes

We're having a `string change on a stable branch <https://bugzilla.mozilla.org/show_bug.cgi?id=372409>`__, and I'd like to give an overview of what I did how to make this less painful. Less is intentionally a relative measure, it's still really very badly painful.

The biggest part of this change was to actually settle on the intended outcome. How should locales behave that make the change, how should locales behave that don't. What should happen to users with language packs, and what with the language pack versioning. In this particular case, language packs aren't loaded yet, so they don't really matter, but in general, it's a question worthwhile answering.

Now, how to get those changes? The (IMHO) best way is to get patches from the localizers that apply easily. The previous step should identify a concrete patch to implement by the localizers. That didn't work out perfectly this time, but we caught the difference in time.

Landing seperate patches in tracking bugs leads to all kinds of messy problems, so I went for one bug per language in CVS, whether built or not, and one central tracking bug.

| Bugzilla magic, part 1: How to file 50 bugs without getting totally frustrated? I created an HTML form which takes an initial comment, the summary, a blocked bug, and then, on the press of a button, creates bug-filing links for all locales. I hard-coded the list of locales for now. It substitutes @AB_CD@ in all fields for the current locale, and picks the right component in the Mozilla Localizations product, which works for all languages but Slovak right now. The goodness of us hunting for bugzilla components now. I can then click on each link, or just use keyboard navigation. Just opening the links via window.open() works, but really stress tests bugzilla (and Firefox), so that's not that good. Anyway, it took me about 50 minutes to file 57 bugs. That includes a bunch of distraction while waiting for bugzilla, I'd wish filing bugs would be a snap. Still, not bad, less than a minute per bug. Released lanuages block the tracking bug, others don't, which was hand-work for now.
| For the non-released languages I made those block the central bug once they had a patch.

Within 24 hours, we had 20 patches, within 48 hours, we had 36 (plus 1 which I still have to find out why it didn't apply). I had to adjust only two patches myself, all others where either fine from the start, or fixed by the localizer on my comments.

YAY on our localization community.

Now, do you want to apply some 36 patches by hand? I don't, so

Bugzilla magic, Part 2: Creating a bad big patch. Create a bug query that gets all bugs that block the tracking bug and have an attachment that is a patch ("Attachment is patch", "is equal to", "1" is the magic trio) . Then click on the XML button, which creates one XML document of all bugs on that query, including all the information. And attachement IDs :-). Now open Jesse's jsshell bookmarklet and get the attachement IDs:

   | res=document.evaluate('bugzilla/bug/attachment[@isobsolete="0"][@ispatch="1"]/attachid',
   | document, null,XPathResult.ANY_TYPE,null);
   | out=[];nd=res.iterateNext();
   | while (nd) {out.push(nd.textContent);nd=res.iterateNext();}
   | out.join(' ')

Now I moved over to bash:

   for att in <insert list of attachement IDs here> ; do wget --no-check-certificate -O- 'https://bugzilla.mozilla.org/attachment.cgi?id='$att > $att;done

``cat`` all those patches together, test the patch and fix the chunks that don't apply, and off you go with 36 fixed locales in 48 hours.
