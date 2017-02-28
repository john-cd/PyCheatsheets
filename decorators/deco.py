"""
Decorator Examples.
"""
import os
import functools
import itertools
from decorator import decorator

### Tagging -------------------------------------------------------------------
        
def tag(**tags):
    """A simple decorator that attaches tags (metadata) to a function. 
    
    >>> @tag(somekey=somevalue, somekey2=somevalue2)
    ... def f():
    ...    pass
    """
    @decorator
    def dec(func, *args, **kw):
        func.__dict__.update(tags)
        return func(*args, **kw)   
    return dec 
    ## equivalent to directly writing:
    # def func():
    #   pass
    # func.somekey = somevalue
    # func.somekey2=somevalue2
    ## Example:        
    # tags = func.__dict__ # __dict__ is always defined
    # if name in tags: 
        # val = tags[name]
    # else:
        # pass 
    ##or: hasattr(func, "somekey")    
    
### Catching exceptions -------------------------------------------------------

@decorator
def catch(func, *args, **kw):
    """Catch most exceptions in 'func' and prints them.
    Use to decorate top-level functions and commands only.  
    """
    #d: print "calling %s with args %s, %s" % (func.__name__, args, kw)   
    try:
        return func(*args, **kw)
    except StandardError as e:
        print e            
        ## TODO consider:
        # if e.message:
            # print e.message
        # else:
            # print e 

### Argument checking ---------------------------------------------------------            
            
# def no_arg(func):
    # """Require that the 'line' argument is an empty string."""
    # def wrapper(self, line):
        # if not line:
            # return catch(func)(self, line)    
        # else:
            # print "This command takes no argument."
    # #~~~
    # return functools.update_wrapper(wrapper, func)
    # ##or simply: 
    # ## wrapper.__name__ = f.__name__
    # ## wrapper.__doc__ = f.__doc__   
  
class line_arg(object):  
    """Decorator that checks the 'line' argument is present / absent (empty string) as required."""
    ## decorator class. see http://www.artima.com/weblogs/viewpost.jsp?thread=240845
    def __init__(self, must_have_argument=True, msg=None):
        super(line_arg, self).__init__()
        self._must_have_argument = must_have_argument # True if a non-empty 'line' argument must be provided."""
        if msg is None:
            self._msg = "This command requires an argument." if self._must_have_argument else "This command takes no argument." 
        else:    
            self._msg = msg  
    
    def __call__(self, func):
        def wrapper(self2, line):
            if bool(line) == self._must_have_argument: 
                return catch(func)(self2, line)    
            else:
                print self._msg  
        #~~~        
        return functools.update_wrapper(wrapper, func)

## Alternative implementation using decorator package:  
## see http://micheles.googlecode.com/hg/decorator/documentation.html
## http://stackoverflow.com/questions/147816/preserving-signatures-of-decorated-functions    
def line_arg2(must_have_argument=True, msg=None):
    if msg is None:
        msg = "This command requires an argument." if must_have_argument else "This command takes no argument."  
    @decorator    
    def dec(func, *args, **kw):
        itr = itertools.ifilter(lambda x: x != "", itertools.chain(args, kw.values())) # ignore any empty string 
        argument_present = bool([ arg for arg in itr ][1:]) # skip first argument (i.e. "self")
        if argument_present == must_have_argument: 
            return catch(func)(*args, **kw)    
        else:
            print msg 
    return dec      


# from utils import _topath
    
# class file_arg(object):  
    # """Decorator that checks whether the 'line' argument is a file name or path."""
    # def __init__(self, existence=True, default_ext=".txt", msg_no_arg=None, msg_existence=None):
        # super(file_arg, self).__init__()
        # self._existence = existence # True if the file must exist, False if it must not exist, None if we don't care
        # self._msg_no_arg = "No file name or path was specified." if msg_no_arg is None else msg_no_arg
        # default_msg_existence = "The file {0} does not exist." if self._existence else "The file {0} already exists." 
        # self._msg_existence = default_msg_existence if msg_existence is None else msg_existence
        # self._default_ext = default_ext # default extension of the file, if not provided
    
    # def __call__(self, func):
        # @functools.wraps(func)
        # def wrapper(self2, filename):
            # if not filename:  
                # print self._msg_no_arg
                # return
            # file_path = _topath(filename, default_ext=self._default_ext)
            # if (self._existence is not None) and (self._existence != os.path.exists(file_path)): 
                # print self._msg_existence.format(file_path)
                # return 
            # return catch(func)(self2, file_path)
        # ##~~~            
        # return wrapper     

                
# def validate_index_or_name(f): 
    # """"""
    # @functools.wraps(f)  
    # def wrapper(index_or_key):
        # try:    
            # w = fromindexorname(index_or_key)
        # except IndexError as e:
            # print "Index out of range (check with 'list')."
            # return
        # except KeyError as e:
            # print "File name or path not found (check with 'list')."
            # return
        # else:
            # try:
                # return f(w)
            # except StandardError as e:
                # print "Error:"
                # print e    
                # return   


 
        

        