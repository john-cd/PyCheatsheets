"""
Various dictionary / sequence wrappers
"""
import gc
import collections


class Container(object):
    """A container for objects returned by ....
    """

    def __init__(self, ordereddict=None):
        super(Container, self).__init__()
        self._innerdict = (
            collections.OrderedDict() if ordereddict is None else ordereddict
        )

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
        return iter(list(self._innerdict.items()))

    def clear(self):
        self._innerdict.clear()


# ----------------------------------------


class ImageStack(object):
    def __init__(self, seqoftuples=None):
        super().__init__()
        self._innerdict = collections.OrderedDict()
        if seqoftuples is not None:
            self._innerdict.update(seqoftuples)

    @property
    def count(self):
        return len(self._innerdict)

    @property
    def isempty(self):
        return self.count == 0

    def clear(self):
        self._innerdict.clear()
        gc.collect()

    def keys(self):
        return list(self._innerdict.keys())

    def iterkeys(self):
        return iter(list(self._innerdict.keys()))

    def items(self):
        return list(self._innerdict.items())

    def iteritems(self):
        return iter(list(self._innerdict.items()))

    def __len__(self):
        return len(self._innerdict)

    def __repr__(self):
        return "ImageStack({0})".format(list(self.items()))

    def __str__(self):
        pass
