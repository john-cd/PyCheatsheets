"""
Utilities to inspect classes, properties, modules.

Created on June 23.
@author: Sylvain
"""
import sys
import inspect
import collections


def interrogate(item):
    """Print useful information about item."""
    if hasattr(item, "__name__"):
        print("NAME:    ", item.__name__)
    if hasattr(item, "__class__"):
        print("CLASS:   ", item.__class__.__name__)
    print("ID:      ", id(item))
    print("TYPE:    ", type(item))
    print("VALUE:   ", repr(item))
    print("CALLABLE: ")
    if isinstance(item, collections.Callable):
        print("Yes")
    else:
        print("No")
    if hasattr(item, "__doc__"):
        doc = getattr(item, "__doc__")
        if doc is not None:
            doc = doc.strip()  # Remove leading/trailing whitespace.
            firstline = doc.split("\n")[0]
            print("DOC:     ", firstline)


# -----------------------------------------------------------------------------


def inspectpublicmethods(inst):
    """Inspects the public and non-magic methods on the instance of a class."""

    def ispublicmethod(m):
        return inspect.ismethod(m) and not m.__name__.startswith("_")

    for name, meth in inspect.getmembers(inst, predicate=ispublicmethod):
        # meth is a bound method.
        # explanation:
        # http://metapython.blogspot.com/2010/11/python-instance-methods-how-are-they.html
        print(name, meth)
        # Returns a named tuple: ArgSpec(args, varargs, keywords, defaults).
        # See also inspect.formatargspec()
        print("\tArgs: ", inspect.getfullargspec(meth))
        print("\tDoc: ", inspect.getdoc(meth))  # or: meth.__doc__
        # meth is a descriptor object:
        # print "\tAttributes:", dir(meth)
        # meth.__func__ or im_func is the inner function wrapped by the bound
        # method.
        func = meth.__func__
        print("\t__func__: ", func.__name__, repr(func), func.__doc__)


def inspectproperties(klass):
    """Inspects the properties of a class (does not work for an instance)."""
    for name, value in inspect.getmembers(klass, predicate=inspect.isdatadescriptor):
        print(name, value)
        print("\tDoc:", inspect.getdoc(value))


def inspectmodule(mod=sys.modules[__name__]):
    """Inspects the methods and functions of a module."""

    def isfuncormethod(m):
        return inspect.ismethod(m) or inspect.isfunction(m)

    print("Module:")
    for name, func in inspect.getmembers(mod, predicate=isfuncormethod):
        print(name, repr(func))
        print("\tDoc: ", inspect.getdoc(func))


# -----------------------------------------------------------------------------

# code borrowed from the rlcompleter module
# tested under Python 2.6 ( sys.version = '2.6.5 (r265:79063, Apr 16 2010,
# 13:09:56) \n[GCC 4.4.3]' )

# or: from rlcompleter import get_class_members


def get_class_members(klass):
    ret = dir(klass)
    if hasattr(klass, "__bases__"):
        for base in klass.__bases__:
            ret = ret + get_class_members(base)
    return ret


def uniq(seq):
    """ the 'set()' way ( use dict when there's no set ) """
    return list(set(seq))


def get_object_attrs(obj):
    # code borrowed from the rlcompleter module ( see the code for
    # Completer::attr_matches() )
    ret = dir(obj)
    # if "__builtins__" in ret:
    #   ret.remove("__builtins__")
    if hasattr(obj, "__class__"):
        ret.append("__class__")
        ret.extend(get_class_members(obj.__class__))
        ret = uniq(ret)
    return ret


## Test ##############################################################
def _test():
    class A(object):
        def method1(self):
            pass

        @property
        def x(self):
            return "x"

    a = A()
    print("a.method1")
    interrogate(a.method1)
    print("a.x")
    interrogate(a.x)
    print("inspectpublicmethods")
    inspectpublicmethods(a)
    print("inspectproperties")
    inspectproperties(A)
    print("inspectmodule")
    inspectmodule()


if __name__ == "__main__":
    _test()
