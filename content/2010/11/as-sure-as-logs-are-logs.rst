As sure as logs are logs
########################
:date: 2010-11-15 12:04
:category: Mozilla
:tags: build, buildbot, Mozilla
:slug: 2010/11/as-sure-as-logs-are-logs

... or not.

As promised, I'll write a bit about build logs today. You'll see what our logs are, and, to begin with, I'll take you on a tour through ``buildMessage`` to explain how the logs we have end up being what you see served off of tinderbox.

First off, buildbot is basically the same thing as any regular gecko app, one main thread and loads of callbacks. So when reading on, all your spontanous reactions are good.

The ``buildMessage`` code does:

#. synchronous IO to load all logs of a build into memory, basically up to some 70M
#. synchronous string handling to paste all that data together, with some extra padding
#. synchronous compression of the resulting string
#. synchronous base64 encoding of the compressed string

All on the main thread, all in one go, blocking. All of that to give you a single lengthy unformatted blob of text. Why?

Because our build logs are actually not a single lengthy unformatted blob of text, which is what tinderbox wants.

Let's have a peek into what our build logs are, really. In my previous posts, I introduced you to the concept of build steps. They're really the basic entity of work to be done for a build. Now, the logs are stored in buildbot pretty much in how the data comes, that is, each log is associated with a step, and the storage is happening as the chunks arrive. Commonly, that'd be stdout and stderr data coming from shell commands run on the slave. The information about which stream the data is on is persisted, too, as is the order, so any log looks like this, basically:

.. raw:: html

   <table cellspacing="0" cellpadding="5" border="1">

.. raw:: html

   <tr>

.. raw:: html

   <td rowspan="6" style="vertical-align: top;">

Step reference

.. raw:: html

   </td>

.. raw:: html

   <td>

*header*

.. raw:: html

   </td>

.. raw:: html

   <td>

length

.. raw:: html

   </td>

.. raw:: html

   <td>

data

.. raw:: html

   </tr>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

*stdout*

.. raw:: html

   </td>

.. raw:: html

   <td>

length

.. raw:: html

   </td>

.. raw:: html

   <td>

data

.. raw:: html

   </tr>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

*stdout*

.. raw:: html

   </td>

.. raw:: html

   <td>

length

.. raw:: html

   </td>

.. raw:: html

   <td>

data

.. raw:: html

   </tr>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

*stdout*

.. raw:: html

   </td>

.. raw:: html

   <td>

length

.. raw:: html

   </td>

.. raw:: html

   <td>

data

.. raw:: html

   </tr>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

*stderr*

.. raw:: html

   </td>

.. raw:: html

   <td>

length

.. raw:: html

   </td>

.. raw:: html

   <td>

data

.. raw:: html

   </tr>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

*stdout*

.. raw:: html

   </td>

.. raw:: html

   <td>

length

.. raw:: html

   </td>

.. raw:: html

   <td>

data

.. raw:: html

   </tr>

.. raw:: html

   </tr>

.. raw:: html

   </table>

As most of you aren't among the few priviledged ones to actually look at the real logs, I've set up a fake log page for you to take a look. It's an l10n repack, mostly because they're somewhat small in both step count and log size, and because I'm used to them. Here's the `actual make step <http://people.mozilla.org/~axel/logs-example/#repack_installers>`__ highlighted. You can see the introduction being shown in blue, which is the common color for *header* chunks. Buildbot just uses that channel to show setup and shutdown information on the step. Then there's the actual make output in black. If there was something on stderr, it'd be styled in red. Sorry, I didn't quickly come up with something that has stderr.

The first take-away is that you can get to just the build output of the step you're interested in.

If you're nostalgic, you can check the checkbox for tinderbox, the css style sheet changes to show you what you'd get from tinderbox. Try to find the information again?

One further detail, there can be more than one log per step. Buildsteps that set build properties quite commonly have two logs, one that keeps track of the command that got run, and another that keeps track of the actually changed build properties. You can look at an example in the `builddir step <http://people.mozilla.org/~axel/logs-example/#set_builddir>`__. The boring last line is the second log.

Log files are really not all that complicated, and much more useful than what we get back from tinderbox. Let's look at some of the pros:

Log files come in as the build goes. This enables buildbot to publish build logs in almost realtime. There's little-to-no cost for that, too, a simple node.js proxy can ensure that only one log is read at any time. Another benefit is, one can archive logs incrementally, removing the current stress on the masters to publish more data than they want to chew in one go.

Log files are per task. As the logs are associated with a step, which has a name and a builder, there's pretty rich information available on what the data in question is actually about. Think about hg-specific error parsers for one step, ftp-specific ones for the next, and mochitest-specific ones for the one after that. All in one build. If we'd archive the raw data, we can easily improve our parsers and be compatible with old logs. Or add new steps to the build process without fear to break existing log parsers.

Tinderbox can still be fed. Even if we're not sending out tinderbox log mails from the masters, we can still do the processing out of band in an external process or even external machine, offload the masters, and not enforce us to change all infrastructure in one go.

There is a hard piece, too, storage. Build logs are plenty, and they're anywhere from a dozen bytes to 70M. Within the same build, even. There a hundreds of thousands small files, and thousands of really large ones. I hope that adding some information on what our build logs really are helps to spike a design discussion on this. If to compress, on which level. Retention, per step type, even? Store as single files, in one dir, or in a hierarchy, or as tar balls? Or all of the above as part of retention? Is hbase a fit?
