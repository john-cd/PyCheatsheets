import collections as _coll
import repr as reprlib

## Python 2.x implementation of a data transport class
## that keeps track of the attributes' insertion order
## and optionally display order.
## For the proper way to do in Python 3.x, see
## http://legacy.python.org/dev/peps/pep-3115/ 

class OrderedBunch: # must be an old-style class !!

    def __init__(self, seqoftuples=None, displayorder=None):
            # print "INIT: self.__dict__: {0}.".format(self.__dict__)
            self._innerdict = _coll.OrderedDict()
            # print "INIT: self._innerdict: {0}.".format(self._innerdict)
            if seqoftuples is not None:
                self._innerdict.update(seqoftuples)
            self._displayorder = displayorder
    
    # called instead of normal mechanism (i.e. store the value in the instance dictionary)
    def __setattr__(self, name, value):
        # print "<__setattr__: {0} {1}>".format(name, value)
        # do not simply execute self.name = value - this would cause a recursive call.
        if name.startswith("_"):
            self.__dict__[name] = value     # "internal" attribute - store in __dict__ as usual
        else:        
            self._innerdict[name] = value
    
    # # Called only when an attribute lookup has not found the attribute in the usual places
    # # (i.e. it is not an instance attribute nor is it found in the class tree for self).
    def __getattr__(self, name):
        # print "<__getattr__: {0}>".format(name)  
        if name in self._innerdict:
            return self._innerdict[name]
        else:    
            raise AttributeError("{0} not found.".format(name))
    
    # TODO low pri: consider __delattr__(self, name) if needed.   
    
    def keys(self):
        return self._innerdict.keys()
    
    def iterkeys(self):
        return self._innerdict.iterkeys()
    
    def items(self):
        return self._innerdict.items()
    
    def iteritems(self):
        return self._innerdict.iteritems()
        
    def __len__(self):
        return len(self._innerdict) 
    
    def __repr__(self):
        tuplelist = self.items() 
        optional = ", displayorder={}".format(self._displayorder) \
                   if self._displayorder is not None else "" 
        return "OrderedBunch({0}{1})".format(tuplelist, optional)   
        
        ## alternative:  pprint.pformat(tuplelist) or  reprlib.aRepr.repr(tuplelist)
        # then you can modify representation with repr.aRepr./someattribute/ as needed 
        
    def __str__(self):
        if self._displayorder is not None:
            tuplelist = sorted([(k, v) for k, v in self.iteritems() \
                                if k in self._displayorder],
                                key=lambda e: self._displayorder.index(e[0]))
        else:
            tuplelist = self.iteritems()
        return "\n".join(["{0}: {1}".format(k,v) for k, v in tuplelist])

    def copy_in_order(self, *displayorder):
        """Returns another instance containing the attributes which names (strings)
        are passed in argument, in the order specified.
        If no arguments are passed, the order is the instance's default displayorder 
        passed to the instance's constructor or, if none, the insertion order.  
        - Attributes' values are shallow copied. 
        - Duplicated names, names not corresponding to attributes of the instance,
        or attributes not listed in the arguments are ignored.  
        """
        defaultdisplayorder = self._displayorder if self._displayorder is not None else self.keys()
        todisplay = displayorder if len(displayorder) > 0 else defaultdisplayorder   
        itr = ( (k, v) for k, v in self.iteritems() if k in todisplay )
        return OrderedBunch(sorted(itr, key=lambda e: todisplay.index(e[0]))) 
    
    def get_attribute_names_alpha_order(self):
        """Returns an alphabetically sorted list of the names of all public attributes.
        Use with copy_in_order()."""
        return sorted(self.keys()) # or: vars(self).keys() or inspect.getmembers(self)
  

        