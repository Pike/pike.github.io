Migrate to Fluent
#################
:date: 2019-05-02 01:24
:category: L10n
:tags: Fluent
:slug: 2019/05/migrate-to-fluent

Introduction
============

A couple of weeks ago the Localization Team at Mozilla `released the Fluent Syntax specification <https://hacks.mozilla.org/2019/04/fluent-1-0-a-localization-system-for-natural-sounding-translations/>`__. As mentioned in our announcement, we already have over 3000 Fluent strings in Firefox. You might wonder how we introduced Fluent to a running project. In this post I'll detail on how the design of Fluent plays into that effort, and how we pulled it off.

|image0|

Fluent's Design for Simplicity
==============================

Fluent abstracts away the complexities of human languages from programmers. At the same time, Fluent makes easy things easy for localizers, while making complex things possible.

When you migrate a project to Fluent, you build on both of those design principles. You will simplify your code, and move the string choices from your program into the Fluent files. Only then you'll expose Fluent to localizers to actually take advantage of the capabilities of Fluent, and to perfect the localizations of your project.

Fluent's Layered Design
=======================

When building runtime implementations, we created several layers to tightly own particular tasks.

#. Fluent source files are parsed into Resources.
#. Multiple resources are aggregated in Bundles, which expose APIs to resolve single strings. Message and Term references resolve inside Bundles, but not necessarily inside Resources. A Bundle is associated with a single language, as well as fallback languages for i18n libraries.
#. Language negotiation and language fallback happen in the Localization level. Here you'd implement that someone looking for Frisian would get a Frisian string. If that's missing or has a runtime problem, you might want to try Dutch, and then English.
#. Bindings use the Localization API, and integrate it into the development stack. They marshal data models from the programming language into Fluent data models like strings, numbers, and dates. Declarative bindings also apply the localizations to the rendered UI.

Invest in Bindings
------------------

Bindings integrate Fluent into your development workflow. For Firefox, we focused on `bindings to generate localized DOM <https://firefox-source-docs.mozilla.org/intl/l10n/l10n/fluent_tutorial.html#markup-localization>`__. We also have `bindings for React <https://github.com/projectfluent/fluent.js/wiki/React-Bindings>`__. These bindings determine how fluent Fluent feels to developers, but also how much Fluent can help with handling the localized return values. To give an example, integrating Fluent into Android app development would probably focus on a `LayoutInflator <https://developer.android.com/reference/android/view/LayoutInflater>`__. In the bindings we use at Mozilla, we decided to localize as close to the actual display of the strings as possible.

If you have declarative UI generation, you want to look into a declarative binding for Fluent. If your UI is generated programmatically, you want a programmatic binding.

The Localization classes also integrate IO into your application runtime, and making the right choices here has strong impact on performance characteristics. Not just on speed, but also the question of showing untranslated strings shortly.

Migrate your Code
=================

Migrating your code will often be a trivial change from one API to another. Most of your code will get a string and show it, after all. You might convert several different APIs into just one in Fluent, in particular dedicated plural APIs will go away.

You will also move platform-specific terminology into the localization side, removing conditional code. You should also be able to stop stitching several localized strings together in your application logic.

As we'll go through the process here, I'll show an example of a sentence with a link. The project wants to be really sure the link isn't broken, so it's not exposed to localizers at all. This is shortened from an actual example in Firefox, where we link to our privacy policy. We'll convert to `DOM overlays <https://github.com/projectfluent/fluent.js/wiki/DOM-Overlays#functional-elements>`__, to separate localizable and non-localizable aspects of the DOM in Fluent. Let's just look at the HTML code snippet now, and look at the localizations later.

Before:

::

   <li>&msg-start;<a href="https://example.com">&msg-middle;</a>&msg-end;</li>

After:

::

   <li data-l10n-id="msg"><a href="https://example.com" data-l10n-name="msg-link"></a></li>

Migrate your Localizations
==========================

Last but not least, we'll want to migrate the localizations. While migrating code is work, losing all your existing localizations is just outright a bad idea.

For our work on Firefox, we use a Python package named ``fluent.migrations``. It's building on top of the ``fluent.syntax`` package, and programmatically creates Fluent files from existing localizations.

It allows you to copy and paste existing localizations into a Fluent string for the most simple cases. It also concats several strings into a single result, which you used to do in your code. For these very simple cases, it even uses Fluent syntax, with specialized global functions to copy strings.

Example:

::

   msg = {COPY(from_path,"msg-start")}<a data-l10n-name="msg-link">{COPY(from_path,"msg-middle")}</a>{COPY(from_path,"msg-end")}

Then there are a bit more complicated tasks, notably involving variable references. Fluent only supports its built-in variable placement, so you need to migrate away from ``printf`` and friends. That involves firstly normalizing the various ways that a printf parameter can be formatted and placed, and then the code can do a simple replacement of the text like ``%2$S`` with a Fluent variable reference like ``{user-name}``.

We also have logic to read our Mozilla-specific plural logic from legacy files, and to write them out as `select-expressions <https://projectfluent.org/fluent/guide/selectors.html>`__ in Fluent, with a variant for each plural form.

These transforms are implemented as pseudo nodes in a template AST, which is then evaluated against the legacy translations and creates an actual AST, which can then be serialized.

Concluding our example, before:

::

   <ENTITY msg-start "This is a link to an ">
   <ENTITY msg-middle "example">
   <ENTITY msg-end ".">

After:

::

   msg = This is a link to an <a data-l10n-name="msg-link">example</a> site.

Find out more about this package and its capabilities in the `documentation <https://firefox-source-docs.mozilla.org/intl/l10n/l10n/fluent_migrations.html>`__.

Given that we're OpenSource, we also want to carry over attribution. Thus our code not only migrates all the data, but also splits the migration into individual commits, one for each author of the migrated translations.

Once the baseline is migrated, localizers can dive in and improve. They can then start using parameterized Terms to adjust grammar, for example. Or add a plural form where English didn't need one. Or introduce a platform-specific terminology that only exists in their language.

.. |image0| image:: /images/2019/04/arewefluentyet.png
   :class: aligncenter size-full wp-image-603
   :width: 600px
   :height: 367px
   :target: https://arewefluentyet.com
