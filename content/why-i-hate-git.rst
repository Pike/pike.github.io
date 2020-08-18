Why I hate git
##############
:date: 2011-08-07 10:20
:category: Mozilla
:slug: why-i-hate-git

::

   wokbok:django-durationRel axelhecht$ git push -f
   Counting objects: 7, done.
   Delta compression using up to 4 threads.
   Compressing objects: 100% (4/4), done.
   Writing objects: 100% (4/4), 560 bytes, done.
   Total 4 (delta 2), reused 0 (delta 0)
   Unpacking objects: 100% (4/4), done.
   remote: error: refusing to update checked out branch: refs/heads/master
   remote: error: By default, updating the current branch in a non-bare repository
   remote: error: is denied, because it will make the index and work tree inconsistent
   remote: error: with what you pushed, and will require 'git reset --hard' to match
   remote: error: the work tree to HEAD.
   remote: error: 
   remote: error: You can set 'receive.denyCurrentBranch' configuration variable to
   remote: error: 'ignore' or 'warn' in the remote repository to allow pushing into
   remote: error: its current branch; however, this is not recommended unless you
   remote: error: arranged to update its work tree to match what you pushed in some
   remote: error: other way.
   remote: error: 
   remote: error: To squelch this message and still keep the default behaviour, set
   remote: error: 'receive.denyCurrentBranch' configuration variable to 'refuse'.
   To /Users/axelhecht/src/django-durationRel
    ! [remote rejected] master -> master (branch is currently checked out)
   error: failed to push some refs to '/Users/axelhecht/src/django-durationRel'

Also known as ``ux-jargon`` and completely useless.
