.. _quasar-api:

package_name API
================

Importing from package_name
---------------------------

In Python, the distinction between what is the public API of a library and what
are private implementation details is not always clear.  Unlike in other
languages like Java, it is possible in Python to access "private" functions or
objects.  Occasionally this may be convenient, but be aware that if you do so
your code may break without warning in future releases.  Some widely understood
rules for what is and isn't public in Python are:

- Methods / functions / classes and module attributes whose names begin with a
  leading underscore are private.

- If a class name begins with a leading underscore, none of its members are
  public, whether or not they begin with a leading underscore.

- If a module name in a package begins with a leading underscore none of
  its members are public, whether or not they begin with a leading underscore.

- If a module or package defines ``__all__``, that authoritatively defines the
  public interface.

- If a module or package doesn't define ``__all__``, then all names that don't
  start with a leading underscore are public.

.. note:: Reading the above guidelines one could draw the conclusion that every
          private module or object starts with an underscore.  This is not the
          case; the presence of underscores do mark something as private, but
          the absence of underscores do not mark something as public.


API definition
--------------

Every submodule listed below is public. That means that these submodules are
unlikely to be renamed or changed in an incompatible way, and if that is
necessary, a deprecation warning will be raised for one SciPy release before the
change is made.

* `package_name`

* `package_name.module1`


.. toctree::
   :maxdepth: 1
   :hidden:
   :titlesonly:

   quasar <main_namespace>
   quasar.module1 <module1>
