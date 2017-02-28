"""
Various dictionary / sequence wrappers 
"""
import collections

class Container(object):
    """A container for objects returned by ....
    """
    def __init__(self, ordereddict=None):
        super(Container, self).__init__()
        self._innerdict = collections.OrderedDict() if ordereddict is None else ordereddict

    @property
    def count(self):
        """Return the number of (unique) objects."""
        return len(self._innerdict)

    def __len__(self):
        return len(self._innerdict)

    @property
    def isempty(self):
        """Return True if there are no objects in the container."""
        return self.count == 0

    # def iterkeys(self):
        # for k in self._innerdict:
            # yield k

    # def keys(self):
        # """ """
        # return self._innerdict.keys()

    # def items(self):
        # """Return a copy of the waves as (key, value) pairs."""
        # return self._innerdict.items()

    def iteritems(self):
        """Return an iterator as (key, value) pairs."""
        return self._innerdict.iteritems()

    def clear(self):
        self._innerdict.clear()

## ----------------------------------------

from __future__ import division
from __future__ import print_function
import numpy as np
import collections
import gc

class ImageStack(object):  # TODO consider deriving from OrderedBunch ?
    """
    """
    def __init__(self, seqoftuples=None):
        super(ImageStack, self).__init__()
        self._innerdict = collections.OrderedDict()
        if seqoftuples is not None:
            self._innerdict.update(seqoftuples)

    @property
    def count(self):
        """ """
        return len(self._innerdict)

    @property
    def isempty(self):
        """ """
        return self.count == 0

    def clear(self):
        """ """
        self._innerdict.clear()
        gc.collect()

    def keys(self):
        """ """
        return self._innerdict.keys()

    def iterkeys(self):
        """ """
        return self._innerdict.iterkeys()

    def items(self):
        """ """
        return self._innerdict.items()

    def iteritems(self):
        """ """
        return self._innerdict.iteritems()

    def __len__(self):
        return len(self._innerdict)

    def __repr__(self):
        return "ImageStack({0})".format(self.items())

    def __str__(self):
        pass


        
        