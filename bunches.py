import pprint
import collections as _coll
import repr as reprlib

class Bunch(object):
    """
    A helper class that serves as a C#-style struct / property bag.
    
    Usage:
    >>> mystruct = Bunch(field1=value1, field2=value2)
    >>> mystruct.field3=value3
    """
    # Status: tested
    # History: added _repr__ June 29, 2014.
    
    def __init__(self, **kwds):
        super(Bunch, self).__init__()
        self.__dict__.update(kwds) 

    ### the following methods are attributes of the class, not the class instance 
    ### meaning they show up in Bunch.__dict__ not Bunch().__dict__    
    
    def __str__(self): # used by print - use with partialcopy() to reduce clutter  
        return pprint.pformat(self.__dict__, depth=1)
        #or:
        #state = ["%s = %r" % (attribute, value) for (attribute, value) in self.__dict__.items()]
        #return '\n'.join(state)
     
    def __repr__(self):
        return "Bunch(**{0})".format(reprlib.aRepr.repr(self.__dict__))
        # note: you can modify representation with repr.aRepr./someattribute/ as needed 
     
    def partialcopy(self, *attributenames):
        """Returns a partial shallow copy of the current instance
        with only the attributes which names are passed in argument.
        Duplicated attribute names or missing attributes are ignored.
        """
        d = { k : v for k,v in self.__dict__.iteritems() if k in attributenames }
        return Bunch(**d)           
    
    def asOrderedDict(self, *attributenames):
        """Returns an ordered dictionary containing the attributes which names 
        are passed in argument, in the order specified.
        - Attributes' values are shallow copied. 
        - Duplicated names, names not corresponding to attributes the instance,
        or attributes not listed in the arguments are ignored.  
        """
        ol = [ (k, v) for k, v in self.__dict__.iteritems() if k in attributenames ]
        return _coll.OrderedDict(sorted(ol, key=lambda e: attributenames.index(e[0]))) 
    
    def getnames(self):
        """Returns a sorted list of the names of the public attributes."""
        return sorted( name for name in self.__dict__ if not name.startswith("_") ) # or: vars(self).keys() or inspect.getmembers(self)
    
# # Alternatives:

# # Use namedtuple: 
# NT = collections.namedtuple("MyObj", ["file_path", "...", "..."])

# # or:  
# X = type('X', (object,), dict(a=1, b=2))

# # or:
# class Bunch(dict):
    # __getattr__ = dict.__getitem__
    # # or
    # # def __getattr__(self, name):
    # #   return self[name]

# # or:
# class Bunch2:  # old-style class
    # def __init__(self, **kwds):
        # self.__dict__.update(kwds)

    # def __setattr__(self, name, value):
        # # do your verification stuff here
        # self.__dict__[name] = value

# # Do the following to avoid infinite recursion in __getattribute__, __setattr__ ...
        
# class Bunch3(object):  # new-style class 
# def __init__(self, **kwds):
    # super(Bunch3, self).__init__()
    # self.__dict__.update(kwds)

# def __getattribute__(self, attr):
    # return super(Bunch3, self).__getattribute__(attr)
    
# # def __setattr__(self, name, value):
    # # super(Bunch3, self).__setattr__(name, value) 

    
    
def _example_Bunch():
    b = Bunch(c=3, b=2)
    b.a = 1
    print "b ", b # {'a':1, 'b':2, 'c':3} # insertion order not kept
    print "b.c ", b.c # 3
    print "b.a ", b.a # 1
    b2 = b.partialcopy("c", "a", "do not exist")    
    print "b2 ", b2 # {'a':1, 'c':3} # insertion order not kept
    od = b.asOrderedDict("c", "b", "do not exist")
    print od # [("c", 3), ("b", 2) ]
    print "names", b.getnames()
    print "repr(b)", repr(b)
    ## testing limit on display length
    bb = Bunch(**{ chr(90 + i % (123-90)) + str(i): i for i in xrange(1000) })
    print "repr(b)", repr(bb)
    #note: should not work:
    # b3 = Bunch(**{ 1: "zz"})
    # b4=Bunch(a=1, 1="s")
    
 
if __name__ == '__main__':
    print "Testing Bunch"
    _example_Bunch()  
    
    