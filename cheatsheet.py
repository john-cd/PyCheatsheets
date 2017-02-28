#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 15:37:59 2014

@author: Sylvain
"""
sys.exit("Do not try to execute or import this cheat sheet!")

### Python =============================================================

# http://www.python.org/
# http://en.wikipedia.org/wiki/Python_(programming_language)

# https://docs.python.org/2/index.html

### Cheatsheets Books & Recipes ------------------------------------------------

# http://www.astro.ufl.edu/~warner/prog/python.html
# http://overapi.com/python/
# http://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf

## Extensive summary / reference (40 pages) : Richard Gruet's Python page:

# http://rgruet.free.fr/#QuickRef

## Recipes

# http://code.activestate.com/recipes/
# https://wiki.python.org/moin/SimplePrograms

## On-line Books

# http://www.itmaybeahack.com/book/python-2.6/html/index.html
# http://en.wikibooks.org/wiki/Python_Programming
# https://github.com/gregmalcolm/python_koans

### Python distributions ------------------------------------------------------

# Python(x,y)
# Scientific and engineering development software for numerical computations, data analysis and data visualization
# https://code.google.com/p/pythonxy/

# Winpython
# http://winpython.sourceforge.net/
#-- portable scientific python for windows
#-- philosophy: http://sourceforge.net/p/winpython/wiki/Roadmap/
# - portable / isolated: does not register for .py by default
# - less packages than python(x, y)

# Anaconda
# Free enterprise-ready Python distribution for large-scale data processing, predictive analytics, and scientific computing
# including Python, NumPy, SciPy, Pandas, IPython, Matplotlib, Numba, Blaze, Bokeh,
# review: similar to Winpython - can be made portable. simpler than python(x,y)
# https://store.continuum.io/cshop/anaconda/
# https://store.continuum.io/static/img/Anaconda-Quickstart.pdf

# ActivePython
# http://www.activestate.com/activepython

# DAWN
# http://www.dawnsci.org/

# Canopy
# https://www.enthought.com/products/canopy/
# - commercial distribution , slow startup, package manager limited in community edition, basic editor
# - problems during uninstall
# - review: http://xcorr.net/2013/04/30/canopy-scientific-python-editor-for-windows/
# - The package manager offers a graphical interface to perform much the same tasks as easy_install and pip.
# - The documentation browser offers shortcuts for the online docs for Scipy, matplotlib, and more

# Sage
# http://www.sagemath.org/index.html

### Python-aware Text Editors -------------------------------------------------

# Notepad++  http://notepad-plus-plus.org/
# http://www.sublimetext.com/

### Python IDEs----------------------------------------------------------------

# http://en.wikipedia.org/wiki/Comparison_of_integrated_development_environments#Python
# https://wiki.python.org/moin/PythonEditors
# http://blogs.esri.com/esri/arcgis/2013/06/24/choosing-the-right-python-integrated-development-environment/

# Spyder
# - the IDE provided by Python(x,y)

# IDLE The standard Python environment
# http://www.python.org/idle
# - not great but usable

# Python tools for Visual Studio
# https://pytools.codeplex.com/
# - great if using VS for other purposes

# NINJA IDE
# http://ninja-ide.org/

# ActivePython
# http://www.activestate.com
# - feature-packed; contains Pythonwin IDE

# Eric Free IDE using Qt http://eric-ide.sf.net
# http://eric-ide.python-projects.org/
# http://eric-ide.python-projects.org/eric-screenshots.html

# Komodo Commercial IDE http://www.activestate.com

# Wingware Commercial IDE http://www.wingware.com

# BlackAdder Commercial IDE and (Qt) GUI builder
# http://www.thekompany.com

# Boa Constructor Free IDE and GUI builder http://boa-constructor.sf.net

# Anjuta Versatile IDE for Linux/UNIX http://anjuta.sf.net

# ArachnoPython Commercial IDE http://www.python-ide.com

# Code Crusader Commercial IDE http://www.newplanetsoftware.com

# Code Forge Commercial IDE http://www.codeforge.com

# Eclipse Popular, flexible, open source IDE
# http://www.eclipse.org

# KDevelop Cross-language IDE for KDE http://www.kdevelop.org

# VisualWx Free GUI builder http://visualwx.altervista.org

# wxDesigner Commercial GUI builder http://www.roebling.de

# wxGlade Free GUI builder http://wxglade.sf.net

# PyCharm
# http://www.jetbrains.com/pycharm/

# Pyscripter
# https://code.google.com/p/pyscripter/

# IEP: interactive editor for Python
# http://www.iep-project.org/

### IPython -------------------------------------------------------------------
# http://ipython.org/

# Using IPython makes interactive work easy. Data processing, exploration of numerical models,
# trying out operations on-the-fly allows to go quickly from an idea to a result.
# - better shell
# - notebook interface
# - embeddable kernel
# - parallel python

### IPython shell shortcuts:
## a- TAB expansion to complete python names and file paths
## b- ~ and * directory / file expansion
## c- many "magic" methods:
    %lsmagic  # list of all magic methods
    %quickref # cheatsheet
    %magic

## Help:
?       # overall help
help    # python help system
?someobj or someobj?   # help
??someobj or someobj?? # detailed help
## also %pdoc %pdef %psource  for docstring, function definition, source code only.

## To run a program directly from the IPython console:
%run somescript.py  # instead of execfile("somescript.py") at the python prompt
# %run has special flags for timing the execution of your scripts (-t),
# or for running them under the control of either Python’s pdb debugger (-d) or profiler (-p).
%run -d myscript.py

%edit %ed # edit then execute
%save
%load example.py # load local (example) file (or url) allowing modification
%load http://matplotlib.org/plot_directive/mpl_examples/mplot3d/contour3d_demo.py
%macro # define macro with range of history lines, filenames or string objects
%recall

%whos           # list identifiers you have defined interactively
%reset  -f -s   # remove objects -f for force -s for soft (leaves history).
# %reset is not a kernel restart
# - restart with Ctrl+. in "qtconsole").
# - import module ; reload(module) to reload a module from disk

%debug  # jump into the Python debugger (pdb)
%pdb    # start the debugger on any uncaught exception.

%cd     # change directory
%pwd    # print working directory
%env    # OS environment variables

!OScommand
!ping www.bbc.co.uk
%alias # system command alias

## _ __ ___ etc... for previous outputs.
## _i _ii _i4  etc.. for previous input. _ih for list of previous inputs

### GUI integration:
## start with ipython --gui=qt or at the IPython prompt:
%gui wx
## arguments can be wx, qt, gtk and tk.

### Matplotlib / pylab graphics in an iPython shell:
## - start with: ipython --matplotlib ( or --matplotlib=qt etc...)
## - at the IPython prompt:
%matplotlib             # set matplotlib to work interactively; does not import anythig
%matplotlib  inline
%matplotlib qt          # request a specific GUI backend
%pylab inline
# %pylab makes the following imports:
    # import numpy
    # import matplotlib
    # from matplotlib import pylab, mlab, pyplot
    # np = numpy
    # plt = pyplot
    # from IPython.display import display
    # from IPython.core.pylabtools import figsize, getfigs
    # from pylab import *
    # from numpy import *

### Qtconsole - an improved console
## http://ipython.org/ipython-doc/stable/interactive/qtconsole.html
## at the command prompt:
ipython.exe qtconsole --pylab=inline --ConsoleWidget.font_size=10
## alternative: --matplotlib inline
## or within IPython:
%matplotlib  inline
%pylab inline
## To embed plots, SVG or HTML in qtconsole, call display:
from IPython.core.display import display, display_html
from IPython.core.display import display_png, display_svg
display(plt.gcf()) # embeds the current figure in the qtconsole
display(*getfigs()) # embeds all active figures in the qtconsole
#or:
f = plt.figure()
plt.plot(np.rand(100))
display(f)

# http://xcorr.net/2013/04/19/ipython-and-ipython-notebook-for-matlab-users/

### IPython Notebook web-based interface:
## - start with: ipython notebook and switch to browser
## - keyboard shortcuts:
## Enter to edit a cell
## Shift + Enter to evaluate
## Ctrl + m or Esc for the "command mode":
## In command mode:
##      h list of keyboard shortcuts
##      1-6 to convert to heading cell
##      m to convert to markdown cell
##      y to convert to code
##      c copy / v paste
##      d d delete cell
##      s save notebook
##      . to restart kernel
##

### Wakari (online IPython notebooks):
# - free 512MB RAM 10GB disk 100 MB data upload space plan
# https://www.wakari.io/
# https://www.wakari.io/gallery

## Notebook viewer:
# http://nbviewer.ipython.org/

### Other Tools ---------------------------------------------------------------

# Pip - A tool for installing and managing Python packages.
# http://www.pip-installer.org/en/latest/#

# Cython: C code integration: http://en.wikipedia.org/wiki/Cython

# PyPy, Stackless Python: other implementations of Python

### Language ==================================================================

# Python supports the following data types:
# boolean
# integer
# long  # use L suffix; dropped since Python 3.0
# float
# complex # 5 + 2j
# str(ing)
# list
# object
# None

# Some immutable types:
# int, float, long, complex
# str
# bytes
# tuple
# frozen set

# Some mutable types:
# byte array
# list
# set
# dict

# These reserved words cannot be used as variable
# names:and, as, assert, break, class, continue, def, del, elif, else,
# except, False, finally, for, from, global, if, import, in, is, lambda,
# None, nonlocal, not, or, pass, raise, return, True, try, with, while,
# yield

# In Python, everything is an object. A variable is like a nametag attached to an object, not a box that stores a value.
# Assignment statements modify namespaces, not objects.
# In other words,

name = 10
# means that you’re adding the name “name” to your local namespace, and making it refer to an integer object containing the value 10.

## Basic ----------------------------------------------------------------------

# pound sign to start a comment
help()
help(anobject)
import math
print math.__doc__
id(math.__doc__)    # unique ID (address) of an object

# inspect object: dir(), vars(), str(), repr()
str(someobject)
repr(someobject)    # printable representation of an object
type(someobject) # type of an object
vars(someobject)        # vars(x) returns x.__dict__ the dictionary where Python objects store their instance variables
vars(someobject).keys() # just the attribute names
dir()
dir(someobject)  # dir(x) returns a dictionary of x's "attributes, its class's attributes, and recursively the attributes of its class's base classes."

import inspect
inspect.getmembers(someobject)

# http://stackoverflow.com/questions/980249/difference-between-dir-and-vars-keys-in-python

# The str() function is meant to return representations of values which are
# fairly human-readable, while repr() is meant to generate representations which
# can be read by the interpreter

# len(): returns the length of a string (number of characters)

## Code Blocks

# - Python uses whitespace indentation
# - The line before the start of a code block always ends in a colon:
# for i in range(10):
# if x > y:
# while x < 100:
# - The Python standard is 4 spaces, and that’s what you should use

### Naming Conventions / Style ------------------------------------------------

# http://legacy.python.org/dev/peps/pep-0008/
# http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html

# Name your classes and functions consistently; the convention is to use
# CamelCase for classes and lower_case_with_underscores for functions and methods. Always use self as the name for the first method argument

# joined_lower for functions, methods, attributes
# joined_lower or ALL_CAPS for constants
# StudlyCaps for classes
# camelCase only to conform to pre-existing conventions

# Attributes: interface, _internal, __private (uses name mangling)

# Keep lines below 80 characters in length.
# Use implied line continuation inside parentheses/brackets/braces

# Docstrings = How to use code
# Comments = Why (rationale) & how code works


## Module Structure

"""module docstring"""

# imports
# constants
# exception classes
# interface functions
# classes
# internal functions & classes

def main(...):
    ...

if __name__ == '__main__':
    status = main()
    sys.exit(status)

## Booleans -------------------------------------------------------------------

# considered False: False, but also 0, 0.0, "", [], {}, (), set(), None
# considered True: True, non-zero numbers, non-empty strings / sequences, any object not explicitly False

if list:  # test if not empty
    pass  # do something here

## Strings --------------------------------------------------------------------

# Three ways to declare a string in Python: single quotes ('), double quotes ("), and triple quotes (""").

print "There are", cars, "cars available."
print ("Hello, " + "world!") # concatenate
print ('bouncy, ' * 3)
# answer = raw_input() # You should use "input()" in python 3.x
var = 10
print ("If we add 10 to your number, we get ", var)
print ("If we add 10 to your number, we get %s" % var) # old style format
# Use the %r for debugging, since it displays the "raw" data of the variable
t = 0.6
y = 1.0
print 'At t=%g s, the height of the ball is %.2f m.' % (t, y)
# join:
seq = ['1', '2', '3', '4', '5']
' '.join(seq)

seq = [1,2,3,4,5]
' '.join(map(str, seq))

print "abc".upper()


## format()
print ("If we add 10 to your number, we get {0}".format(var))
for x in range(1,11):
     print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)

print 'This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible')


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print ('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
        'Dcab: {0[Dcab]:d}'.format(table))


## Sequences ------------------------------------------------------------------

# Five major kinds of sequences in Python:
# strings, lists, tuples, dictionaries, and sets

string = "Hello, world!"
string[2]
string[-2] # Negative indexes are counted from the end of the string
string[3:9] # slicing
string[:5]
string[-6:-1]
string[:] # shallow copy !

for c in string: print(c)  # in Python, a string is just a sequence, so we can iterate over it!
l1=[c for c in string]

## Lists are mutable and ordered ----------------------------------------------
range(4)

spam = []  # empty list
spam = ["bacon", "eggs", 42]
# Python is zero-based
spam[0]
spam[2]
len(spam)
type(spam)
spam.append(2.5)
spam.insert(1, 'and')
del spam[1]
spam.pop(0)  # Remove the first item , which is the item at index 0
spam.remove(42)

zeros = [0] * 5  # beware: when building a new list by multiplying, Python copies each item by reference
[1,2] + [3,4]  # combine lists
# extend
a = [1,2,3]
b = [4,5,6]
a.extend(b)

list1 = [1, 2, 3, 4]
for item in list1:
    print (item)

list2 = list1[:]  # Shallow copy using "[:]"
list2[0] = 2  # Only affects list2, not list1
list2 = copy.deepcopy(list1) # A deep copy

del list1[:] # Clear a list
list1 = []   # Not really clear but rather assign to a new empty list

##  List comprehensions

#result = [expression for item1 in sequence1  [if condition1]
#  [for item2 in sequence2 [if condition2] ... for itemN in sequenceN [if conditionN]]
#  ]

animals = ['dog', 'cat', 'bird']
plurals = [animal + 's' for animal in animals]
doubles = [2 * x for x in range(8)]

listOfWords = ["this","is","a","list","of","words"]
items = [word[0] for word in listOfWords]
items = [x+y for x in 'cat' for y in 'pot']  # strings are sequences of characters

list = [1, 2, 3, 4]
newlist = [item for item in list if item >2]

# Flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print [num for elem in vec for num in elem]


### Tuples are similar to lists, except they are immutable --------------------
(10, 'Mary had a little lamb')
('one-element tuple',)
var = ("me", "you", ("us", "them")) # nested
foo, bar = "rocks", (0, "the universe") # multiple assignment; outer tuple created from items separated by commas
( [1, 2], [3, 4] ) # tuple made of mutable objects
# conversion
l = [4, 5, 6]
tuple(l)
t = (4, 5, 6)
list(t)

# Create a named tuple class 'person':
person = collections.namedtuple('person', 'name firstName age') # field names separated by space or comma
assert issubclass(person, tuple)
assert person._fields == ('name', 'firstName', 'age')

# Create an instance of person:
jdoe = person('Doe', 'John', 30)
assert  str(jdoe) == "person(name='Doe', firstName='John', age=30)"
assert jdoe[0] == jdoe.name == 'Doe' # access by index or name is equivalent
assert jdoe[2] == jdoe.age == 30

# Convert instance to dict:
assert jdoe._asdict() == {'age': 30, 'name': 'Doe', 'firstName': 'John'}

# Although tuples are normally immutable, one can change field values via _replace():
jdoe._replace(age=25, firstName='Jane')
assert str(jdoe) == "person(name='Doe', firstName='Jane', age=25)"


### Dictionaries are mutable and unordered ------------------------------------
definitions = {"guava": "a tropical fruit", "python": "a programming language", "the answer": 42}
definitions["guava"]
definitions["new key"] = "new value"

dict1 = {}                     # Create an empty dictionary
dict2 = dict()                 # Create an empty dictionary 2
dict2 = {"r": 34, "i": 56}     # Initialize to non-empty value
dict3 = dict([("r", 34), ("i", 56)]) # Init from a list of tuples
dict4 = dict(r=34, i=56)       # Initialize to non-empty value 3
dict1["temperature"] = 32      # Assign value to a key
if "temperature" in dict1:     # Membership test of a key AKA key exists
  del dict1["temperature"]     # Delete AKA remove
equalbyvalue = dict2 == dict3
itemcount2 = len(dict2)        # Length AKA size AKA item count
isempty2 = len(dict2) == 0     # Emptiness test
dict2.keys()
for key in dict2:              # Iterate via keys
  print key, dict2[key]        # Print key and the associated value
  dict2[key] += 10             # Modify-access to the key-value pair
for value in dict2.values():   # Iterate via values
  print value
dict5 = {x: dict2[x] + 1 for x in dict2 } # Dictionary comprehension in Python 2.7 or later
dict6 = dict2.copy()             # A shallow copy
dict6.update({"i": 60, "j": 30}) # Add or overwrite
dict7 = dict2.copy()
dict7.clear()                  # Clear AKA empty AKA erase
print dict1, dict2, dict3, dict4, dict5, dict6, dict7, equalbyvalue, itemcount2

## Dictionary comprehension
{x: x*x for x in range(6)}
{('a'*x) for x in range(6)}

## Zipping two sequences to build a dictionary
seq1 = ('a','b','c','d')
seq2 = [1,2,3,4]
d = dict(zip(seq1,seq2))

## dict.get(key, default)
navs = {}
for (portfolio, equity, position) in data:
    navs[portfolio] = (navs.get(portfolio, 0) + position * prices[equity])

## dict.setdefault()
navs = {}
for (portfolio, equity, position) in data:
    navs.setdefault(portfolio, 0)                # set if necessary, then return default
    navs[portfolio] += position * prices[equity]

## mutating the dict - use .keys() to create static copy
for key in d.keys():
    d[str(key)] = d[key]



## Sets are mutable, unordered and do not allow duplicate values --------------
mind = set([42, 'a string', 40, 41])
frozen=frozenset(['life','universe','everything']) # Frozenset is an immutable, hashable version of set.

set1 = set()                   # A new empty set
set1.add("cat")                # Add a single member
set1.update(["dog", "mouse"])  # Add several members
if "cat" in set1:              # Membership test
  set1.remove("cat")
#set1.remove("elephant") - throws an error
print set1
for item in set1:              # Iteration AKA for each element
  print item
print "Item count:", len(set1) # Length AKA size AKA item count
isempty = len(set1) == 0       # Test for emptiness
set1 = set(["cat", "dog"])     # Initialize set from a list
set2 = set(["dog", "mouse"])
set3 = set1 & set2             # Intersection
set4 = set1 | set2             # Union
set5 = set1 - set3             # Set difference
set6 = set1 ^ set2             # Symmetric difference
issubset = set1 <= set2        # Subset test
issuperset = set1 >= set2      # Superset test
set7 = set1.copy()             # A shallow copy
set7.remove("cat")
set8 = set1.copy()
set8.clear()                   # Clear AKA empty AKA erase
print set1, set2, set3, set4, set5, set6, set7, set8, issubset, issuperset

# set comprehesion
a = {x for x in 'abracadabra' if x not in 'abc'}

### Files ---------------------------------------------------------------------

f = open('workfile', 'w') # modes: r w r+ rb wb r+b
f.read(size)  # return strings only
f.readline()  # a newline character (\n) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline
for line in f:
        print line,
value = ('the answer', 42)
    s = str(value)
    f.write(s)
f.close()
with open('workfile', 'r') as f:
     read_data = f.read()
f.closed

## Serialization as JSON

json.dumps([1, 'simple', 'list'])
json.dump(x, afile)
x = json.load(fromfile)

## Other sequences ------------------------------------------------------------

# array: a typed-list, an array may only contain homogeneous values.
# collections.defaultdict: a dictionary that, when an element is not found, returns a default value instead of error.
# collections.deque: A double ended queue, allows fast manipulation on both sides of the queue.
# heapq: A priority queue.
# Queue: A thread-safe multi-producer, multi-consumer queue for use with
# multi-threaded programs. Note that a list can also be used as queue in a single-threaded code.


## Control flow ---------------------------------------------------------------

x = -6                              # Branching
if x > 0:                           # If
  print "Positive"
elif x == 0:                        # Else if AKA elseif
  print "Zero"
else:                               # Else
  print "Negative"

## Conditional Expressions
result = (whenTrue if condition else whenFalse)
s = 'negative' if x < 0 else 'nonnegative'


## for loops
list1 = [100, 200, 300]
for i in list1: print i             # A for loop
for i in range(0, 5): print i       # A for loop from 0 to 4
for i in range(5, 0, -1): print i   # A for loop from 5 to 1
for i in range(0, 5, 2): print i    # A for loop from 0 to 4, step 2
list2 = [(1, 1), (2, 4), (3, 9)]
for x, xsq in list2: print x, xsq   # A for loop with a two-tuple as its iterator
l1 = [1, 2]; l2 = ['a', 'b']
for i1, i2 in zip(l1, l2): print i1, i2 # A for loop iterating two lists at once.
for i, x in enumerate(l):  # keep track of iteration cycles over an iterable
      print i, x

# loop in reverse
for i in reversed(xrange(1,10,2)):  print i


# "for" statement accepts "else", which runs if no "break"
for n in range(2, 10):
     for x in range(2, n):
         if n % x == 0:
             print n, 'equals', x, '*', n/x
             break
     else:
         # loop fell through without finding a factor
         print n, 'is a prime number'


## while loops
i = 5
while i > 0:                        # A while loop
  i -= 1
list1 = ["cat", "dog", "mouse"]
i = -1 # -1 if not found
for item in list1:
  i += 1
  if item=="dog":
    break                           # Break; also usable with while loop
print "Index of dog:",i
for i in range(1,6):
  if i <= 4:
    continue                        # Continue; also usable with while loop
  print "Greater than 4:", i

# # Iterators / Generators ----------------------------------------------------

# https://docs.python.org/2/howto/functional.html

### Get iterator with: iter(obj)
L = [1,2,3]
it = iter(L)
it.next() # next number or raise StopIteration
# etc...

# iterators are the underlying mechanism for loops:
for i in [1,2,3]:
    print i

# # # Iterator class definition
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):         # returns an object with a next() method.
        return self
    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

## Generator expressions

line_list = ['  line 1\n', 'line 2  \n', ...]

# Generator expression -- returns iterator
stripped_iter = (line.strip() for line in line_list)  # always have to be written inside parentheses
obj_total = sum(obj.count for obj in list_all_objects())  # function parens count

# Compare to list comprehension -- returns list
stripped_list = [line.strip() for line in line_list]

# Generator expressions ("genexps") are just like list comprehensions, except
# that where listcomps are greedy, generator expressions are lazy [use iterators]. Listcomps compute the entire result list all at once, as a list. Generator expressions compute one value at a time, when needed, as individual values. This is especially useful for long sequences where the computed list is just an intermediate step and not the final result.


## Generators - shortcut for iterators

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

# another example
def genID(initialValue=0):
  v = initialValue
  while v < initialValue + 1000:
    yield "ID_%05d" % v
    v += 1
  return    # or: raise StopIteration()

generator = genID() # Create a generator
for i in range(10): # Generates 10 values
  print generator.next()

# sending value to generator (advanced)
def counter (maximum):
    i = 0
    while i < maximum:
        val = (yield i)
        # If value provided, change counter
        if val is not None:
            i = val
        else:
            i += 1
it = counter(10)
print it.next()
it.send(8) # sends value to generators
print it.next()

## Important functions that accept iterables
# map(f, iterA, iterB, ...)
# filter(predicate, iter)
# reduce(func, iter, [initial_value])
# sorted(iterable, [cmp=None], [key=None], [reverse=False])
# any(iter) and all(iter)

## "itertools" package

# itertools.count(n) returns an infinite stream of integers, increasing by 1 each time. You can optionally supply the starting number, which defaults to 0:
# itertools.cycle([1,2,3,4,5])
# itertools.repeat('abc', 5)
# itertools.chain(['a', 'b', 'c'], (1, 2, 3))
# itertools.izip(['a', 'b', 'c'], (1, 2, 3)) # equivalent to zip()
# itertools.islice(iter, [start], stop, [step])
# itertools.tee(iter, [n]) replicates an iterator
# itertools.imap(operator.add, [5, 6, 5], [1, 2, 3]) # equivalent to map()
# itertools.starmap(func, iter) assumes that the iterable will return a stream of tuples, and calls f() using these tuples as the arguments
# itertools.ifilter(predicate, iter) returns all the elements for which the predicate returns true

# itertools can handle infinite sequences



### Sorting ---

# Decorate a list with the keys to sort
to_sort = [(item[1], item[3], item)
           for item in a_list]
# Sort:
to_sort.sort()
# Undecorate:
a_list = [item[-1] for item in to_sort]

## or better:
def my_key(item):
    return (item[1], item[3])

to_sort.sort(key=my_key)


## Functions ------------------------------------------------------------------

# Objects passed as arguments to functions are passed by REFERENCE; they are not being copied around.
# Passed objects of mutable types such as lists and dictionaries can be changed by the called function

def first2items(list1 = ["a", "b"]):   # default argument values
  return list1[0], list1[1]            # return multiple values as a tuple
a, b = first2items(["Hello", "world", "hi", "universe"])
print a + " " + b

# The default value of a function argument is evaluated at the point of function definition in the defining scope:

i = 5
def f(arg=i):
    print arg

i = 6
f() #prints 5


# The default value is evaluated only once.This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes.

def f(a, L=[]):
    L.append(a)
    return L

print f(1)
print f(2)
print f(3) # prints [1,2,3]

# Use instead:

def f(a, L=None):
    L = L or []  # None is considered boolean false
    L.append(a)
    return L

## Variable-Length Argument Lists: *args, **kwargs

def print_tail(first,*tail):
    print tail

def make_dictionary(max_length=10, **entries):
    return dict([(key, entries[key]) for i, key in enumerate(entries.keys()) if i < max_length])

make_dictionary(max_length=2, key1=5, key2=7, key3=9)

## Unpacking arguments
args = [3, 6]
range(*args) # == range(3, 6)

d = {"start": 1, "end": 2}
f(**d)


# # Closures:  functions are first-class objects.

def adder(outer_argument): # outer function
  def adder_inner(inner_argument): # inner function, nested function
    return outer_argument + inner_argument # Notice outer_argument
  return adder_inner
add5 = adder(5) # a function that adds 5 to its argument
add7 = adder(7) # a function that adds 7 to its argument
print add5(3) # prints 8
print add7(3) # prints 10

## Lambdas
print (lambda a, b: a + b)(4, 3)


### Functional programming
# (see iterator section above)

# filter(function, sequence) returns a sequence consisting of those items from the sequence for which function(item) is true. If sequence is a string or tuple, the result will be of the same type; otherwise, it is always a list.

filter(lambda x: x % 2 != 0 and x % 3 != 0, range(2, 25))


def cube(x): return x*x*x

map(cube, range(1, 11))


seq = range(8)
map(lambda x, y: x+y, seq, seq) # iterate over multiple sequences


reduce(add, range(1, 11))  # returns a single value constructed by calling the binary function function on the first two items of the sequence, then on the result and the next item, and so on

## Decorator syntactic sugar
def attrs(**kwds):
    def decorate(f):
        for k in kwds:
            setattr(f, k, kwds[k])
        return f
    return decorate  # returns a function !

@attrs(versionadded="2.2", author="Guido van Rossum")
def mymethod(f):
    pass

## functools

# The functools module in Python 2.5 contains some higher-order functions.
# A higher-order function takes one or more functions as input and returns a new
# function. The most useful tool in this module is the functools.partial() function.

## using functools.wraps to make a decorator mimic the underlying function
from functools import wraps
def my_decorator(f):
     @wraps(f)
     def wrapper(*args, **kwds):
         print 'Calling decorated function'
        return f(*args, **kwds)
    return wrapper
@my_decorator
def example():
     """Docstring"""
     print 'Called example function'

example()
#Calling decorated function
#Called example function
example.__name__
#'example'
example.__doc__
#'Docstring'
##  Without the use of this decorator factory, the name of the example function would have been 'wrapper', and the docstring of the original example() would have been lost.


## Modules --------------------------------------------------------------------

# A module is just an ordinary file in the form <filename>.py.
# A module called mymodule.py can be imported into main.py by inserting import
# mymodule.py at the top of main.py. After importing mymodule.py, you can
# modify and use the module's functions and variables in main.py.
# To access them, use the form mymodule.myfunction().
# To access any documentation, use the form pydoc mymodule.

# imports the math standard module.
import math
# All of the functions in that module are namespaced by the module name
print math.sqrt(10)

# alias
import time as t
print t.localtime()

# import an object only
from time import localtime
current_time = localtime()

# import method wih alias
from math import sin as SIN
print SIN(3)

# import multiples
from subprocess import Popen, PIPE

# import all
from math import *
print sqrt(10)

# For efficiency reasons, each module is only imported once per interpreter # session. Therefore, if you change your modules, you must restart the # interpreter – or, if it’s just one module you want to test interactively, use # reload(), e.g. reload(modulename).


# Modules can be three different kinds of things:
#
# Python files
# Shared Objects (under Unix and Linux) with the .so suffix
# DLL's (under Windows) with the .pyd suffix
# directories
# Modules are loaded in the order they're found, which is controlled by sys.path.
# The current directory is always on the path.
#
# Directories should include a file in them called __init__.py, which should probably include the other files in the directory.

### Packages

# The __init__.py files are required to make Python treat the directories as
# containing packages; this is done to prevent directories with a common name,
# such as string, from unintentionally hiding valid modules that occur later on
# the module search path. In the simplest case, __init__.py can just be an empty
# file, but it can also execute initialization code for the package or set the
# __all__ variable (for "from pkg import *" statements)

## Directory Structure
# see "skeleton" folder
# http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/

## Relative Imports ...........................................................

# http://stackoverflow.com/questions/14132789/python-relative-imports-for-the-billionth-time
# http://legacy.python.org/dev/peps/pep-0328/

# package/
    # __init__.py
    # subpackage1/
        # __init__.py
        # moduleX.py
        # moduleY.py
    # subpackage2/
        # __init__.py
        # moduleZ.py
    # moduleA.py

# Assuming that the current file is either moduleX.py or subpackage1/__init__.py,
# following are correct usages of the new syntax:

from .moduleY import spam
from .moduleY import spam as ham
from . import moduleY
from ..subpackage1 import moduleY
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo
from ...package import bar
from ...sys import path # insane

# BEWARE: Relative imports must always use from <> import; import <> is always absolute.
# Of course, absolute imports can use from <> import by omitting the leading dots.

# BEWARE: cannot use if __name__ == '__main__': when using relative imports.
# otherwise get "Attempted relative import in non-package"
# use "python -m" or write a script in the root of the package

### sys.path tricks for package loading

def import_path(fullpath):
    """
    Import a file with full path specification. Allows one to
    import from anywhere, something __import__ does not do.
    """
    path, filename = os.path.split(fullpath)
    filename, ext = os.path.splitext(filename)
    sys.path.append(path)
    module = __import__(filename)
    reload(module) # Might be out of date
    del sys.path[-1]
    return module

# Another example:
# if __name__ == '__main__' and __package__ is None:
    # from os import sys, path
    # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


## Classes --------------------------------------------------------------------

class Rectangle:
    # Optionally define variable width
    width = 0
    # Constructor with default arguments
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
    # Functions
    def setWidth(self, width):
        self.width = width
    def setHeight(self, height):
        self.height = height
    def getArea(self):
        return self.width * self.height

arect = Rectangle()  # create a new Rectangle with dimensions 0x0.
arect.setWidth(4)
arect.setHeight(6)
print arect.getArea()  # returns 24
rect2 = Rectangle(7,3)  # new Rectangle with dimensions 7x3.

# Inheritance
class RectWithPerimeter(Rectangle):
    #add new functions
    def getPerimeter(self):
        return 2*self.height + 2*self.width
    def setDims(self, width, height):
    #call base class methods from Rectangle
        Rectangle.setWidth(self, width)
        Rectangle.setHeight(self, height)


arect = RectWithPerimeter(6,5)  # Uses the constructor from Rectangle because no new constructor is provided to override it.
print arect.getArea()  # Uses the getArea function from Rectangle and prints 30.
print arect.getPerimeter()  # Uses getPerimeter from RectWithPerimeter and prints 22.
arect.setDims(4,9)  # Use setDims to change the dimensions.

# Special Methods
# __str__ is a special method, like __init__, that is supposed to return a string representation of an object.
class Time(object):
      def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
      def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
# operator overloading
      def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

time = Time()
print time

## Multiple inheritance
class DerivedClassName(Base1, Base2, Base3):
    pass

## Static / class methods
class C(object):
    @classmethod
    def f(cls, arg1, arg2, ...): pass

class C(object):
    @staticmethod
    def f(arg1, arg2, ...): pass

C.f()
C().f()
# Unlike static methods, class methods prepend the class reference to the argument list before calling the function.
# One use for class methods is to create alternate class constructors. Example: Dict.fromkeys('abracadabra')

## Properties -----------------------------------------------------------------

## Properties (new style class only)
class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x
    def setx(self, value):
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")

# Using decorators
class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self._x = value

    @x.deleter
    def x(self):
        del self._x

c = C()
try:
	c.x = -1
except ValueError:
    print "Woops. Not allowed"

## Descriptors ----------------------------------------------------------------

# http://users.rcn.com/python/download/Descriptor.htm

## Descriptor example - generalization of properties
# https://docs.python.org/2/howto/descriptor.html
# A class that defines one or more of the special methods __get__(self,instance,owner), __set__(self,instance,value), __delete__(self,instance) can be used as a descriptor. Creating an instance of a descriptor as a class member of a second class makes the instance a property of the second class.
# http://nbviewer.ipython.org/urls/gist.github.com/ChrisBeaumont/5758381/raw/descriptor_writeup.ipynb

from weakref import WeakKeyDictionary

class NonNegative(object):
    """A descriptor that forbids negative values"""
    def __init__(self, default):
        self.default = default
        self.data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        # we get here when someone calls x.d, and d is a NonNegative instance
        # instance = x
        # owner = type(x)
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):
        # we get here when someone calls x.d = val, and d is a NonNegative instance
        # instance = x
        # value = val
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self.data[instance] = value


class Movie(object):

    #always put descriptors at the class-level !!!!
    rating = NonNegative(0)
    runtime = NonNegative(0)
    budget = NonNegative(0)
    gross = NonNegative(0)
    # Because they live at the class level, every instance shares the same descriptor.

    def __init__(self, title, rating, runtime, budget, gross):
        self.title = title
        self.rating = rating
        self.runtime = runtime
        self.budget = budget
        self.gross = gross

    def profit(self):
        return self.gross - self.budget


m = Movie('Casablanca', 97, 102, 964000, 1300000)
print m.budget  # calls Movie.budget.__get__(m, Movie)
m.rating = 100  # calls Movie.budget.__set__(m, 100)
try:
    m.rating = -1   # calls Movie.budget.__set__(m, -100)
except ValueError:
    print "Woops, negative value"


## Metaclasses ----------------------------------------------------------------
# http://en.wikipedia.org/wiki/Metaclass

# In Python,
# - Everything is an object
# - Everything has a type
# - No real difference between 'class' and 'type'
# - Classes (not just class instances) are objects
# - Their type is 'type'

class Something(object):
     pass

type(Something)

# Metaclasses allow replacement of a class' type.
# Then, just as an object is an instance of its class, a class is an instance
# of its metaclass.

# example: a simple class without metaclass
class Car(object):
    __slots__ = ['make', 'model', 'year', 'color']

    def __init__(self, make, model, year, color): # note the constructor
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    @property
    def description(self):
        """ Return a description of this car. """
        return "%s %s %s %s" % (self.color, self.year, self.make, self.model)

# Metaclass that eliminates the need for __init__
class AttributeInitType(type):
     def __call__(self, *args, **kwargs):
         """ Create a new instance. """

         # First, create the object in the normal default way.
         obj = type.__call__(self, *args)

         # Additionally, set attributes on the new object.
         for name, value in kwargs.items():
             setattr(obj, name, value)

         # Return the new object.
         return obj

class Car(object):
     __metaclass__ = AttributeInitType
     __slots__ = ['make', 'model', 'year', 'color']

     @property
     def description(self):
         """ Return a description of this car. """
         return "%s %s %s %s" % (self.color, self.year, self.make, self.model)

type(C) is AttributeInitType

# In Python 3.x, use class Car(object, metaclass=AttributeInitType): instead

## Exceptions -----------------------------------------------------------------

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    ## to raise exception: raise Exception('spam', 'eggs')
except IOError as e:    # alias
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except (RuntimeError, TypeError, NameError):  # multiple exceptions. parentheses are required
     pass
except Exception as inst:# generic exception processing
    print "Unexpected error:", sys.exc_info()[0]
    print type(inst)     # the exception instance
    print inst.args      # arguments stored in .args
    print inst           # __str__ allows args to printed directly
    raise
#except:  # avoid. bare except is equivalent to except BaseException: -- catches all exceptions, including SystemExit and KeyboardInterrupt
else:
    print "excuted if no exception"
    i = int(s.strip()) # no exception
finally:
    print "always executed before leaving the try statement"


## with statement

with open("myfile.txt") as f:
    for line in f:
        print line,

## Argument checking
def g(x):
    if x < 0: raise ValueError, "g(x) - negative number not allowed"

# Useful snippets / methods:
# assert expr[, message]
# isinstance(x, int)
# callable(2) # False
# callable([1,2].pop) # True
# issubclass(class, classinfo)
# getattr(3, "imag") # return value of an attribute of an object, given the attribute name passed as a string

## Attribute checking
if hasattr(spam, 'eggs'):
    ham = spam.eggs
else:
    handle_error()

# EAFP paradigm
try:
    ham = spam.eggs
except AttributeError:
    handle_error()


## Built-in Exceptions

# https://docs.python.org/2/library/exceptions.html

## Custom exceptions

class CustomException(Exception):
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)

try:
    raise CustomException("My Useful Error Message")
except CustomException, (instance):
    print "Caught: " + instance.parameter


## Custom exception hierarchy

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        prev -- state at beginning of transition
        next -- attempted new state
        msg  -- explanation of why the specific transition is not allowed
    """

    def __init__(self, prev, next, msg):
        self.prev = prev
        self.next = next
        self.msg = msg

## Magic Methods --------------------------------------------------------------

#   http://www.rafekettler.com/magicmethods.html

# # Custom collections --------------------------------------------------------
# # https://docs.python.org/2/reference/datamodel.html?highlight=__setitem__#emulating-container-types

# # Basic skeleton for custom dictionary:
import collections

class MyDict(collections.MutableMapping):
    def __init__(self, *args, **kwargs):
        super(MyDict, self).__init__()
        self._data = {4: "four", 8: "eight"}

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        for elem in self._data:
            yield elem

    def __getitem__(self, key):
        raise KeyError

    def __setitem__(self, key, value):
        raise KeyError

    def __delitem__(self, key):
        raise KeyError

# # Inspection ----------------------------------------------------------------
import inspect

class A:
    def a(self):
        "some doc"
        pass

# # Inspect unbound methods of a class
_type = A
for func_name, value in inspect.getmembers(_type, predicate=inspect.ismethod):
    print func_name, value
    print inspect.getargspec(value)
    print value.__doc__

# # Inspect bound methods of an instance
inst = A()

for name, value in inspect.getmembers(inst, predicate=inspect.ismethod):
    ##public methods only
    if not name.startswith('_'):
        print name, value
        print inspect.getargspec(value) # Returns a named tuple ArgSpec(args, varargs, keywords, defaults).
        print inspect.getdoc(value)

# # Methods are stored in the attribute dictionary of a class as functions: klass.__dict__[func_name]
# # calling instance.func_name returns a bound method via the descriptor protocol
for k, v in A.__dict__.items():
        print k, v


# # Dynamic method redefinition -----------------------------------------------

# http://igorsobreira.com/2011/02/06/adding-methods-dynamically-in-python.html
# http://stackoverflow.com/questions/3803517/convert-partial-function-to-method-in-python

# # Example: redefinition of a function's globals
def namespaced_function(function, global_dict, defaults=None):
    '''
    Redefine(clone) a function under a different globals() namespace scope
    '''
    if defaults is None:
        defaults = function.__defaults__

    new_namespaced_function = types.FunctionType(
        function.__code__,
        global_dict,
        name=function.__name__,
        argdefs=defaults
    )
    new_namespaced_function.__dict__.update(function.__dict__)
    return new_namespaced_function

# # # Standard library ========================================================

# argparse
# copy  Generic shallow and deep copying operations.
# csv
# doctest
# glob
# inspect
# itertools
# math, cmath
# os, os.path
# pickle
# pprint
# profile, cProfile
# pydoc
# re
# shutil
# unittest
# shlex

import os
os.chdir(r"C:\Documents and Settings\me\My Documents\some\")

## Documentation --------------------------------------------------------------

## PyDoc
from pydoc import help

## Docutils is an open-source text processing system for processing plaintext documentation into useful formats, such as HTML, LaTeX, man-pages, open-document or XML.
# http://docutils.sourceforge.net/
# http://docutils.sourceforge.net/rst.html

## Sphinx
# http://sphinx-doc.org/

## reStructuredText

# QUICK REFERENCE:
# http://docutils.sourceforge.net/docs/user/rst/quickref.html
# http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt

## Use of reStructuredText in docstrings
# see http://infinitemonkeycorps.net/docs/pph/
"""
    # Typical function documentation:

    :param volume_id: The ID of the EBS volume to be attached.
    :type volume_id: str

    :param instance_id: The ID of the EC2 instance
    :type instance_id: str

    :return: `Reverse geocoder return value`_ dictionary giving closest
        address(es) to `(lat, lng)`
    :rtype: dict
    :raises GoogleMapsError: If the coordinates could not be reverse geocoded.

    Keyword arguments and return value are identical to those of :meth:`geocode()`.

    .. _`Reverse geocoder return value`:
        http://code.google.com/apis/maps/documentation/geocoding/index.html#ReverseGeocoding
"""
# Take-home points:

# Normal docstring formatting conventions apply: see PEP 257
# Identifier references go in `backticks`.
# :param lat: latutide documents parameters
# :type lat: float documents parameter types
# :return: dictionary giving closest addresses... documents return values
# :rtype: dict documents return type
# :raises GoogleMapsError: If coordinates could not... documents exceptions raised
# >>> starts a doctest and is automatically formatted as code;
# Code can also be indicated by indenting four spaces or preceding with :: and a blank line
# Link to other methods, functions, classes, modules with :meth:`mymethod`,
# :func:`myfunc`, :class:`myclass`, and :mod:`mymodule`
# Hyperlink names go in backticks with a trailing underscore: `Google`_
# and targets can be defined anywhere with .. _Google: http://www.google.com/

## reST format details ........................................................

"""All reST files use an indentation of 3 spaces; no tabs are allowed.
The maximum line length is 80 characters for normal text, but tables,
deeply indented code samples and long links may extend beyond that.
Code example bodies should use normal Python 4-space indentation.
Paragraphs are simply chunks of text separated by one or more blank lines.
As in Python, indentation is significant in reST, so all lines of the same
paragraph must be left-aligned to the same level of indentation.

Section headers are created by underlining (and optionally overlining)
the section title with a punctuation character, at least as long as the text:

=================
This is a heading
=================
# with overline, for parts
* with overline, for chapters
=, for sections
-, for subsections
^, for subsubsections
", for paragraphs

one asterisk: *text* for emphasis (italics),
two asterisks: **text** for strong emphasis (boldface), and
backquotes: ``text`` for code samples.
escape with a backslash \

* This is a bulleted list.
* It has two items, the second
  item uses two lines.

1. This is a numbered list.
2. It has two items too.

. This is a numbered list.
. It has two items too.

Nested lists are possible, but be aware that they must be separated from the
parent list items by blank lines

## Definitions

term (up to a line of text)
   Definition of the term, which must be indented

   and can even consist of multiple paragraphs

next term
   Description.

## Source Code double colon

This is a normal text paragraph. The next paragraph is a code sample::

   It is not processed in any way, except
   that the indentation is removed.

   It can span multiple lines.

This is a normal text paragraph again.

## Links

`Link text <http://target>`_ for inline web links.

## Explicit Markup

An explicit markup block begins with a line starting with .. followed by
whitespace and is terminated by the next paragraph at the same level of
indentation. (There needs to be a blank line between explicit markup
and normal paragraphs.

.. sectionauthor:: Guido van Rossum <guido@python.org>


## 1. Footnotes

Lorem ipsum [#]_ dolor sit amet ... [#]_

.. rubric:: Footnotes

.. [#] Text of the first footnote.
.. [#] Text of the second footnote.


:mod:`parrot` -- Dead parrot access
===================================

.. module:: parrot
   :platform: Unix, Windows
   :synopsis: Analyze and reanimate dead parrots.
.. moduleauthor:: Eric Cleese <eric@python.invalid>
.. moduleauthor:: John Idle <john@python.invalid>

.. function:: repeat([repeat=3[, number=1000000]])
              repeat(y, z)
   :bar: no

   Return a line of text input from the user.


.. class:: Spam

      Description of the class.

      .. data:: ham

         Description of the attribute.

## Inline markup

:rolename:`content`  or  :role:`title <target>`

:meth:`~Queue.Queue.get` will refer to Queue.Queue.get but only display get as the link text.

The following roles refer to objects in modules and are possibly hyperlinked
if a matching identifier is found:

mod
The name of a module; a dotted name may be used. This should also be used for package names.

func
The name of a Python function; dotted names may be used. The role text should not include trailing parentheses to enhance readability. The parentheses are stripped when searching for identifiers.

data
The name of a module-level variable or constant.

const
The name of a “defined” constant. This may be a C-language #define or a Python variable that is not intended to be changed.

class
A class name; a dotted name may be used.

meth
The name of a method of an object. The role text should include the type name and the method name. A dotted name may be used.

attr
The name of a data attribute of an object.

exc
The name of an exception. A dotted name may be used.

"""

# # # Debugging ---------------------------------------------------------------

# http://stackoverflow.com/questions/1623039/python-debugging-tips
# http://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/

# # Useful functions for debugging:
def print_attributes(obj):
    for attr in obj.__dict__:
        print attr, getattr(obj, attr)

## pdb:
# https://docs.python.org/2/library/pdb.html
# http://web.archive.org/web/20120819135307/http://aymanh.com/python-debugging-techniques

## commands:
# help
# p pp # print, pretty print
# list args
# continue step next
# run restart
# where down up # print stack trace and move frame
# quit
# ;; (separator)
# [!]statement
# Commands that the debugger doesn’t recognize are assumed to be Python statements
# and are executed in the context of the program being debugged.
# Python statements can also be prefixed with an exclamation point (!).

## 1- in IPython, use %debug or %pdb

## 2- at the console prompt:
import pdb
import mymodule
pdb.run('mymodule.test()')

## 3- use debugger as a script: python -m pdb myscript.py

## 4- break into the debugger from a running program by inserting:
import pdb; pdb.set_trace()

## 5- console-based visual debugger for Python
## https://pypi.python.org/pypi/pudb



### generates an object diagram with Lumpy
from swampy.Lumpy import Lumpy

lumpy = Lumpy()
lumpy.make_reference()

# do something here

# draw the current state (relative to the last ref)
lumpy.object_diagram()


### Logging -------------------------------------------------------------------

# https://docs.python.org/2/howto/logging.html
#
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG) # format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.warning('%s before you %s', 'Look', 'leap!')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')


### Unit testing --------------------------------------------------------------

## Three methods: doctest (easy/limited), unittest(requires API), nose(adaptable)
## To generate unit tests automatically, see: http://pythoscope.org/

## Location of the tests in the project:
# http://guide.python-distribute.org/example.html
# http://stackoverflow.com/questions/61151/where-do-the-python-unit-tests-go
# while using relative imports: http://legacy.python.org/dev/peps/pep-0328/

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print average([20, 30, 70])
    40.0
    """
    return sum(values, 0.0) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests

# or:
def _test():
  import doctest, example
  return doctest.testmod(example)

if __name__ == "__main__":
    _test()


### unittest ..................................................................
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

def _test():
    unittest.main() # Calling from the command line invokes all tests

if __name__ == '__main__':
    _test()

### nose ......................................................................

# https://pypi.python.org/pypi/nose/1.3.3
# http://nose.readthedocs.org/en/latest/
# http://pythontesting.net/framework/nose/nose-introduction/

## at the command prompt:
nosetests
nosetests -v    # verbose
nosetests -s    # disable output capture
nosetests --with-coverage # code coverage

## or from a script:
import nose
result = nose.run(defaultTest=__name__)
#or even: nose.main()

# # Use decorator to run set-up / teardown functions
# # before test.
# # @with_setup(setup_func, teardown_func)
# # requires: from nose import with_setup
# def setup_func():
    # "set up test fixtures"

# def teardown_func():
    # "tear down test fixtures"

# @with_setup(setup_func, teardown_func)
# def test():
    # "test ..."

# test.setup = setup_func
# test.teardown = teardown_func

## test generator
# def test_evens():
    # for i in range(0, 5):
        # yield check_even, i, i*3

# def check_even(n, nn):
    # assert n % 2 == 0 or nn % 2 == 0

## Test Class

# class TestA:

    # def setup(self):
        # print ("TestA:setup() before each test method")

    # def teardown(self):
        # print ("TestA:teardown() after each test method")

    # @classmethod
    # def setup_class(cls):
        # print ("setup_class() before any methods in this class")

    # @classmethod
    # def teardown_class(cls):
        # print ("teardown_class() after any methods in this class")

    # def test_numbers_5_6(self):
        # print 'test_numbers_5_6()'
        # assert 5 * 6 == 30

    # def test_strings_b_2(self):
        # print 'test_strings_b_2()'
        # assert 'b' * 2 == 'bb'

## Optional API for cleaner output:

# from nose.tools import assert_equal
# from nose.tools import assert_not_equal
# from nose.tools import assert_raises
# from nose.tools import raises

# Nose finds and runs unittests with no problem, and with no extra steps.
# Nose can run doctests


### Multithreading ------------------------------------------------------------

import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print 'Finished background zip of: ', self.infile

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print 'The main program continues to run in foreground.'

background.join()    # Wait for the background task to finish
print 'Main program waited until background was done.'


## Python 2.x versus 3.x ------------------------------------------------------

# In Python 2.x, using the / operator on two integers will return another integer,
# using floor division
# avoid with:
from __future__ import division
1/2

## Print
from __future__ import print_function

print( "335/113=", end="" )
print( 335.0/113.0 )
print( "Hi, Mom", "Isn't it lovely?", end="" )
print( 'I said, "Hi".', 42, 91056 )

import sys
print( "This is an error message", file=sys.stderr )
print( "This is stdout" )
print( "This is also stdout", file=sys.stdout )



## Scientific libraries =======================================================

# List of packages in WinPython:
# http://sourceforge.net/p/winpython/wiki/PackageIndex_27/

# Python for scientific computing: Where to start
# http://sjbyrnes.com/?page_id=67
# http://datacommunitydc.org/blog/2013/03/getting-started-with-python-for-data-scientists/
# http://quant-econ.net/getting_started.html

# SciPy - Python-based ecosystem of open-source software for mathematics, science, and engineering.
# include NumPy, SciPy library, Matplotlib, IPython, SymPy, Pandas
# http://www.scipy.org/
# http://www.scipy.org/install.html

# https://wiki.python.org/moin/NumericAndScientific
# https://wiki.python.org/moin/NumericAndScientific/Plotting
# https://wiki.python.org/moin/NumericAndScientific/Formats


import numpy as np  # NumPy (multidimensional arrays, linear algebra, ...)
import scipy as sp  # SciPy (signal and image processing library)
import matplotlib as mpl         # Matplotlib (2D/3D plotting library)
import matplotlib.pyplot as plt  # Matplotlib's pyplot: MATLAB-like syntax
#or: from pylab import *              # Matplotlib's pylab interface: imports matplotlib + numpy (very MATLAB-like)
import guidata  # GUI generation for easy dataset editing and display
import guiqwt                 # Efficient 2D data-plotting features
import guiqwt.pyplot as plt_  # guiqwt's pyplot: MATLAB-like syntax

## SciPy ----------------------------------------------------------------------

# http://www.scipy.org/
# http://scipy-lectures.github.io/index.html
# http://scipy-lectures.github.io/advanced/image_processing/

## NumPy ----------------------------------------------------------------------
# NumPy - a powerful N-dimensional array object
# http://www.numpy.org/

 import numpy as np

### Data types: np.bool_, np.int_, int8 .. int64, uint8 .. uint64, float_,
## float16 .. float64, complex_, complex64, complex128
## _int = C long (int64 or int32); float_ = float64; complex_ = complex128

## NumPy knows that Python int refers to np.int_, bool means np.bool_,
## that float is np.float_ and complex is np.complex_.

t = np.float_           # type
d = np.dtype(t)         # or dtype('float64'). a dtype object with info about the type
d.byteorder
np.issubdtype(d, int)   # False

## Numpy generally returns elements of arrays as array scalars
## (a scalar with an associated dtype). Array scalars differ from Python scalars,
## but for the most part they can be used interchangeably.
## Generally, problems are easily fixed by explicitly converting array scalars
## to Python scalars, using the corresponding Python type function (e.g., int, float, complex, str, unicode).

## Data-types can be used as functions to convert python numbers to array scalars
## python sequences of numbers to arrays of that type, or as arguments to the
## dtype keyword that many numpy functions or methods accept.

x = np.float32(1.0)     # convert to array scalar: type(x) = numpy.float32, x.dtype = dtype('float32')
y = np.int_([1,2,4])    # convert to array([1, 2, 4]): type(y) = numpy.ndarray, y.dtype = int32


### Array creation ............................................................
x = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
x.shape # (2, 3)
x.dtype # dtype('int32')

y = np.array([[1,2.0],[0,0],(1+1j,3.)]) # note mix of tuple and lists, and types

## Conversion
z = x.astype(float)     # type(y) = numpy.ndarray, z.dtype = float64
# or z = np.float64(x)

## Built-in functions for creating standard arrays:
np.zeros((2, 3))                        # see also ones(), eye()
np.arange(2, 3, 0.1, dtype=np.float)    # arrays with regularly incrementing values.
np.linspace(1., 4., 6) # arrays with a specified number of elements, and spaced equally between the specified beginning and end values.
np.indices((3,3)) # set of arrays (stacked as a one-higher dimensioned array), one per dimension with each representing variation in that dimension.

## Import
# http://docs.scipy.org/doc/numpy/user/basics.io.genfromtxt.html
from StringIO import StringIO
data = "1, 2, 3\n4, 5, 6"
np.genfromtxt(StringIO(data), delimiter=",") # delimiter=(4, 3, 2) for fixed-width file
# options: autostrip=True, comments='#', skip_header=3, skip_footer=5
# usecols=(0, -1), dtype=(int, float, int), names="A, B, C" \or\ names=True (from the file)

## Also can import from: csv, pytables, pyFITS...

### Indexing using Python container-like syntax ...............................
# http://docs.scipy.org/doc/numpy/user/basics.indexing.html
x = np.arange(10)
x.shape = (2,5) # now x is 2-dimensional
x[1,2]  # zero-based - the element of x in the *second* row, *third*column, namely, 6.
x[1,-1] # indexing from the end of the array
x[0]    # subdimensional array
x[0][2] # == x[0, 2]
y = x[:,1] # slicing
y[0] = 9 # changes the corresponding element in x
z = np.arange(35).reshape(5,7)
z[1:5:2,::3] # slicing and striding

### Indexing with other arrays ................................................
#(or any other sequence-like object that can be converted to an array,
# such as lists, with the exception of tuples !!
x = np.arange(10, 1, -1)
x[np.array([3, 3, 1, 8])]
# What is returned when index arrays are used is an array with the same shape as
# the index array, but with the type and values of the array being indexed.
x[np.array([[1,1],[2,3]])]

y = np.arange(35).reshape(5,7)
y[np.array([0,2,4]), np.array([0,1,2])] # returns y[0,0], y[2,1], y[4,2].
y[np.array([0,2,4]), 1]  # If the index arrays do not have the same shape, there is an attempt to broadcast them to the same shape.

# Boolean or “mask” index arrays
y[ y>20 ]

# new axis
y.shape #(5, 7)
y[:,np.newaxis,:].shape # (5, 1, 7)

# ellipsis
z = np.arange(81).reshape(3,3,3,3)
z[1,...,2]  # == z[1,:,:,2] - selecting in full any remaining unspecified dimensions.

### Variable numbers of indices with tuples:

# If one supplies to the index a tuple, the tuple will be interpreted as a list of indices, not as an array.
z = np.arange(81).reshape(3,3,3,3)
indices = (1,1,1,1)
z[indices] # == z[1,1,1,1] - single value
z[[1,1,1,1]] # == z[ np.array([1,1,1,1]) ] - produces an array of dimension n-1 since only one array index is given
z[ (1,1,1,slice(0,2)) ]  # same as z[1,1,1,0:2]
z[ (1, Ellipsis, 1) ] # same as z[1,...,1]

### Broadcasting ..............................................................

## element-by-element operation:
a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 2.0, 2.0])
a * b  # array([ 2.,  4.,  6.])

# broadcasting: the scalar is duplicated
a = np.array([1.0, 2.0, 3.0])
b = 2.0
a * b  # array([ 2.,  4.,  6.])

# When operating on two arrays, NumPy compares their shapes element-wise. It starts with the trailing dimensions, and works its way forward. Two dimensions are compatible when
# - they are equal, or
# - one of them is 1

### Structured arrays (aka “Record arrays”) ...................................
# http://docs.scipy.org/doc/numpy/user/basics.rec.html

## Create a one-dimensional array of length 2. Each element of this array is a record
# that contains three items, a 32-bit integer, a 32-bit float, and a string of length 10 or less:
x = np.zeros((2,),dtype=('i4,f4,a10'))
x[:] = [ (1,2.,'Hello'), (2,3.,"World") ]

## Indexing by field name.
# In this case the fields have received the default names ‘f0’, ‘f1’ and ‘f2’.
y = x['f1'] # x['f1']
# Rather than being a copy of the data in the structured array, y is a view, i.e., it shares exactly the same memory locations.

## 1) "dtype" can contain a string, a comma-separated list of type specifiers:
# - b1, i1, i2, i4, i8, u1, u2, u4, u8, f2, f4, f8, c8, c16, a<n>
#(representing bytes, ints, unsigned ints, floats, complex and fixed length strings of specified byte lengths)
# - int8,...,uint8,...,float16, float32, float64, complex64, complex128

# Each type specifier can be prefixed with a repetition number, or a shape. In these cases an array element is created, i.e., an array within a record. That array is still referred to as a single field.
x = np.zeros(3, dtype='3int8, float32, (2,3)float64') # array of 3 records containing a 1D array of 3 int8, a float and 2x3 flot64 matrix.
x

## 2) "dtype" can contain a List of tuples:
# Each tuple has 2 or 3 elements specifying:
# a) The name of the field (‘’ is permitted),
# b) the type of the field, and
# c) the shape (optional).
x = np.zeros(3, dtype=[('x','f4'), ('y',np.float32), ('value','f4',(2,2))])

# 3) "dtype" can contain a Tuple argument:
# The only relevant tuple case that applies to record structures is when a
# structure is mapped to an existing data type.
# This is done by pairing in a tuple, the existing data type with a matching
# dtype definition (using any of the variants being described here).
x = np.zeros(3, dtype=('i4',[('r','u1'), ('g','u1'), ('b','u1'), ('a','u1')]))
x       # array of 3 int32 values
x['r']  # array of the 3 unsigned bytes, each the first byte in the 3 int32

# 4) "dtype" can contain a Dictionary argument:
x = np.zeros(3, dtype={'names':['col1', 'col2'], 'formats':['i4','f4']})
# optional keys: ‘offsets’ and ‘titles’.
# offsets contain integer offsets for each field, and
# titles are objects containing metadata for each field (these do not have to be strings), where the value of None is permitted.

# The other dictionary form permitted is a dictionary of name keys with tuple values specifying type, offset, and an optional title.
x = np.zeros(3, dtype={'col1':('i1',0,'title 1'), 'col2':('f4',1,'title 2')})

## Accessing and modifying field names
x.dtype.names
x.dtype.names = ('x', 'y')


### Matplotlib ----------------------------------------------------------------

# Matplotlib offers the best set of 2D tools for visualization and preparing graphics
# of high quality (together with latex it offers the ability to write latex code and rendering it within the graph).
# With it you can turn your data or your models into figures for presentations or articles.
# http://www.matplotlib.org
# image gallery: http://matplotlib.org/gallery.html
# pyplot command summary: http://matplotlib.org/api/pyplot_summary.html
# examples http://matplotlib.org/examples/index.html
# tutorial: http://www.loria.fr/~rougier/teaching/matplotlib/
# see also: https://www.wakari.io/nb/url///wakari.io/static/notebooks/Lecture_4_Matplotlib.ipynb

# Recommended module abbrevs:
import matplotlib.pyplot as plt
import numpy as np
# sometimes: import numpy.ma as ma
# sometimes: import matplotlib as mpl

### Matplotlib, pylab, and pyplot: how are they related?

# http://matplotlib.org/faq/usage_faq.html

# - matplotlib is the whole package.
# - pylab and matplotlib.pyplot are modules in matplotlib.
# - matplotlib.pyplot is a collection of command style functions that works like MATLAB.
# - The matplotlib namespace (import matplotlib as mpl) is the object-oriented plotting API.
# - matplotlib.pyplot provides the state-machine interface to the underlying plotting library.
# - matplotlib.pyplot is _stateful_, in that it keeps track of the current figure
# and plotting area, and the plotting functions are directed to the current axes.
# - Each matplotlib.pyplot function makes some change to a figure: eg, create a figure,
# create a plotting area in a figure, plot some lines in a plotting area,
# decorate the plot with labels, etc....
# - pylab combines pyplot with numpy (for mathematics and arrays) into a single namespace,
# making that environment even more MATLAB-like.
#  Summary:
# - The matplotlib.pyplot interface is generally preferred for non-interactive
# plotting (i.e., scripting).
# - The pylab interface is convenient for interactive calculations and plotting, as it minimizes typing.

# a- pylab style:
from pylab import *
x = arange(0, 10, 0.2)
y = sin(x)
plot(x, y, linewidth=2.0)
show()
# try with ipython: pylab?

# second pylab example:
from pylab import *
from random import normalvariate
ts_length = 100
epsilon_values = []   # An empty list
for i in range(ts_length):
    e = normalvariate(0, 1)
    epsilon_values.append(e)
plot(epsilon_values, 'b-')
show()

# b- pyplot style:
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 10, 0.2)
y = np.sin(x)
plt.plot(x, y, 'ro') # ro = plot as red dots; default b- = solid blue line
plt.axis([-2, 12, -2, 2]) # [xmin, xmax, ymin, ymax]
plt.show()
# Note that this example used pyplot’s state-machine to automatically and
# implicitly create a figure and an axes.

# c- matplotlib API style:
# The matplotlib frontend or matplotlib API is the set of classes that do the
# heavy lifting, creating and managing figures, text, lines, plots and so on (Artist tutorial).
# For full control of your plots and more advanced usage, use the pyplot interface
# for creating figures, and then use the object methods for the rest:
import matplotlib.pyplot as plt
import numpy as np
# if needed, make low-levels symbols from matplotlib available under the mpl alias.
x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig = plt.figure()
# Return a subplot axes positioned by the given grid definition.
ax = fig.add_subplot(111) # or fig.add_subplot(1,1,1) nrows, ncols, plot_number
ax.plot(x, y)
plt.show()

### Interactive mode ..........................................................

# http://matplotlib.org/faq/usage_faq.html
# matplotlib.interactive(boolean)
# or turned on via matplotlib.pyplot.ion(),
# and turned off via matplotlib.pyplot.ioff().
# queried via matplotlib.is_interactive().

# - In interactive mode, pyplot functions (but not lower functions) automatically
# (re)draw to the screen. Typing at the Python prompt:
import matplotlib.pyplot as plt
plt.ion()
plt.plot([1.6, 2.7])
plt.title("interactive test") #redraws automatically
plt.xlabel("index")#redraws automatically
# - When plotting interactively, if using lower object method calls in addition to pyplot
# functions, call plt.draw() whenever you want to refresh the plot.
ax = plt.gca()
ax.plot([3.1, 2.2])
plt.draw()
# - Use non-interactive mode in scripts in which you want to generate one or
# more figures and display them before ending or generating a new set of figures.
# In that case, use plt.show() to display the figure(s) and to block execution.
import matplotlib.pyplot as plt
plt.ioff()
plt.plot([1.6, 2.7])
plt.show()
# the show() command blocks the input of additional commands until you manually kill the plot window.

### Examples...................................................................
# [Tutorial](http://matplotlib.org/1.3.1/users/pyplot_tutorial.html)

t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^') # red dashes, blue squares and green triangles
plt.show()

## 1- Controlling line properties
plt.plot(x, y, linewidth=2.0)
# or:
line, = plt.plot(x, y, '-')
line.set_antialiased(False) # turn off antialising

# or with setp() - set properties
lines = plt.plot(x1, y1, x2, y2)
plt.setp(lines, color='r', linewidth=2.0)
# use keyword args as above or MATLAB style string value pairs plt.setp(lines, 'color', 'r', 'linewidth', 2.0)

# Key Line2D properties:
# alpha	float
# animated	[True | False]
# label	any string
# linestyle or ls	[ ‘-‘ | ‘–’ | ‘-.’ | ‘:’ | ‘steps’ | ...]
# linewidth or lw	float value in points

## 2- Working with multiple figures and axes

# The function gca() returns the current axes (a matplotlib.axes.Axes instance),
# and gcf() returns the current figure (matplotlib.figure.Figure instance).
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

## - place the plot explicitly in the figure canvas
x = np.linspace(0, 5, 10)
y = x ** 2
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # lower, bottom, width, height (range 0 to 1)
axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title');

## - create an insert
fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # inset axes
# main figure
axes1.plot(x, y, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('title')
# insert
axes2.plot(y, x, 'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('insert title');

## - create subplots automatically
fig, axes = plt.subplots(nrows=1, ncols=2)
for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title');
fig.tight_layout()

## - figure size
fig = plt.figure(figsize=(8,4), dpi=100)
# create a figure with size 800 by 400 pixels.
# figsize is a tuple with width and height of the figure in inches,
# and dpi is the dot-per-inch (pixel per inch).
# save figure
fig.savefig("filename.png")
fig.savefig("filename.png", dpi=200) # overrides dpi
fig.savefig("filename.svg")

## - legends
ax.plot(x, x**2, label="y = x**2") # or: r"$y = \alpha^2$" in latex
ax.plot(x, x**3, label="curve2", color="red", alpha=0.5)
ax.legend();
ax.legend(loc=0) # let matplotlib decide the optimal location
ax.legend(loc=1) # upper right corner
ax.legend(loc=2) # upper left corner
ax.legend(loc=3) # lower left corner
ax.legend(loc=4) # lower right corner
# .. many more options are available
##

## - Update the matplotlib configuration parameters:
matplotlib.rcParams.update({'font.size': 18, 'font.family': 'serif'})
# restore
matplotlib.rcParams.update({'font.size': 12, 'font.family': 'sans'})


## 2D contour plot:
## http://physics.nmt.edu/~raymond/software/python_notes/paper004.html
x = linspace(0,10,51)   # 1D array
y = linspace(0,8,41)
(X,Y) = meshgrid(x,y)   # X and Y are 2D arrays repeating x and y respectively
a = exp(-((X-2.5)**2 + (Y-4)**2)/4) - exp(-((X-7.5)**2 + (Y-4)**2)/4) # shape of X, Y, a: (41, 51)
c = plt.contour(x,y,a)
l = plt.clabel(c)       # countour labels
lx = plt.xlabel("x")
ly = plt.ylabel("y")
plt.show()


## Colormaps and contour figures
alpha = 0.7
phi_ext = 2 * pi * 0.5

def flux_qubit_potential(phi_m, phi_p):
    return 2 + alpha - 2 * cos(phi_p)*cos(phi_m) - alpha * cos(phi_ext - 2*phi_p)

phi_m = linspace(0, 2*pi, 100)
phi_p = linspace(0, 2*pi, 100)
X,Y = meshgrid(phi_p, phi_m)
Z = flux_qubit_potential(X, Y).T

fig, ax = subplots()
p = ax.pcolor(X/(2*pi), Y/(2*pi), Z, cmap=cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max())
cb = fig.colorbar(p)

fig, ax = subplots()
im = imshow(Z, cmap=cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max(), extent=[0, 1, 0, 1])
im.set_interpolation('bilinear')
cb = fig.colorbar(im)

fig, ax = subplots()
cnt = contour(Z, cmap=cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max(), extent=[0, 1, 0, 1])

### matplot3D: 3D plots .......................................................

# http://matplotlib.org/mpl_toolkits/mplot3d/index.html
# http://matplotlib.org/mpl_toolkits/mplot3d/api.html#module-mpl_toolkits.mplot3d.axes3d
# http://matplotlib.org/mpl_toolkits/mplot3d/api.html#module-mpl_toolkits.mplot3d.axis3d

from mpl_toolkits.mplot3d.axes3d import Axes3D

fig = plt.figure(figsize=(14,6))

# `ax` is a 3D-aware axis instance, because of the projection='3d' keyword argument to add_subplot
ax = fig.add_subplot(1, 2, 1, projection='3d')

p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)

# surface_plot with color grading and color bar
ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, antialiased=False)
cb = fig.colorbar(p, shrink=0.5)
##
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1, 1, 1, projection='3d')
p = ax.plot_wireframe(X, Y, Z, rstride=4, cstride=4)

##
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1, projection='3d')
ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
cset = ax.contour(X, Y, Z, zdir='z', offset=-pi, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='x', offset=-pi, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='y', offset=3*pi, cmap=cm.coolwarm)

ax.set_xlim3d(-pi, 2*pi);
ax.set_ylim3d(0, 3*pi);
ax.set_zlim3d(-pi, 2*pi);

## pyformex --------------------------------------------------------------------

# http://www.nongnu.org/pyformex/
# pyFormex is a program for generating, transforming and manipulating large
# geometrical models of 3D structures by sequences of mathematical operations.
# Unlike traditional CAD systems, pyFormex uses a powerful (Python based)
# scripting language as the basic user input method, making it very well suited
# for automated and repeated (parametric) design procedures. It provides a wide
# range of operations on surface meshes, like STL type triangulated surfaces,
# and FEA meshes or CFD grids. There is also support for Nurbs curves and surfaces.
# pyFormex is often used to create 3D models from medical scan images,
# or as a pre- and post-processor for FEA programs. But it can just as well be
# used to create some nice 3D renderings.

## Mayavi ---------------------------------------------------------------------

# mayavi offers a complete set of openGL bindings for rendering 3D graphics and images.

# http://code.enthought.com/projects/mayavi/

# http://docs.enthought.com/mayavi/mayavi/

# mlab
# http://docs.enthought.com/mayavi/mayavi/mlab.html

# http://scipy-lectures.github.io/packages/3d_plotting/index.html

# Cookbook
# http://wiki.scipy.org/Cookbook/MayaVi
# http://wiki.scipy.org/Cookbook/MayaVi/Examples

# version 1?
# http://mayavi.sourceforge.net/docs/guide/index.html
# http://mayavi.sourceforge.net/docs/guide/ch04.html

## Pandas ---------------------------------------------------------------------

# Python Data Analysis Library: http://pandas.pydata.org/

#pandas is well suited for many different kinds of data:
#
#* Tabular data, as in an SQL table or Excel spreadsheet
#* Ordered and unordered (not necessarily fixed-frequency) time series data
#* Matrix data, potentially with row and column labels
#* Any other form of common structured data

# All pandas data structures are value-mutable (the values they contain can be
# altered) but not always size-mutable. The length of a Series cannot be changed,
# but, for example, columns can be inserted into a DataFrame. However, the vast
# majority of methods produce new objects and leave the input data untouched.
# In general, though, we like to favor immutability where sensible.

# http://pandas.pydata.org/pandas-docs/stable/10min.html

import pandas as pd

s = pd.Series([1,3,5,np.nan,6,8]) # create series
dates = pd.date_range('20130101',periods=6)
# Creating a DataFrame by passing a numpy array, with a datetime index and labeled columns
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
# Creating a DataFrame by passing a dict of objects that can be converted to series-like.
df2 = pd.DataFrame({ 'A' : 1.,
                        'B' : pd.Timestamp('20130102'),
                         'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                         'D' : np.array([3] * 4,dtype='int32'),
                         'E' : 'foo' })
df2.dtypes
df.head()
df.tail(3)
df.index
df.columns
df.values
df.describe()
df.T # transpose
df.sort_index(axis=1, ascending=False)
df.sort(columns='B')
df['A']
df.A
df[0:3]
df['20130102':'20130104']
df[df.A > 0]
df[df > 0]

## PyTables - managing hierarchical datasets (HDF files) -----------------------

# - Manage large hierarchical datasets
# - Read and write data to files in the HDF5 format.

# Main site: http://pytables.github.io/
# Hint for SQL users: http://www.pytables.org/moin/HintsForSQLUsers
# See many example scripts in ..\pytables folder.
# and scripts in <python Lib dir>\tables\scripts\ such as ptdump.

# Other software using HDF5: http://www.hdfgroup.org/tools5app.html

from tables import *
# or:
from tables.file import open_file
from tables.group import Group
from tables.leaf import Leaf
from tables.table import Table, Column
from tables.unimplemented import UnImplemented

## Basic Structure

# - File is the in-memory representation of a PyTables (.hdf) file.
# Most interesting operations occur there: http://pytables.github.io/usersguide/libref/file_class.html
# - All nodes in a PyTables tree are instances of the Node class.
# - The Group and Leaf classes are descendants of Node.
# - Group instances (referred to as groups from now on) are a grouping structure
# containing instances of zero or more groups or leaves, together with
# supplementary metadata.
# - Leaf instances (referred to as leaves) are containers for actual data
# and cannot contain further groups or leaves.
# - The Table, Array, CArray, EArray, VLArray and UnImplemented classes
# are descendants of Leaf, and inherit all its properties.
# - Array stores homogeneous elements (called atoms).
# - Accepted types are NumPy arrays and scalars, as well as native Python
# sequences and scalars, provided that values are regular (i.e. they are not like
# [[1,2],2]) and homogeneous (i.e. all the elements are of the same type).
# - CArray is a chunked Array: use when compressing homogeneous data.
# - EArray is for extendable, homogeneous datasets. The main difference between
# an EArray and a CArray, from which it inherits, is that the former can be
# enlarged along one of its dimensions, the enlargeable dimension.
# - VLArray represent array with rows that can have a variable number of homogeneous elements.
# - Table stores heterogeneous data in rows and columns. The contents are defined
# by a description (see examples below).
# - The description parameter can be None(default) if obj is provided. In that case
# the structure of the table is deduced by obj. Accepted obj types are NumPy
# record arrays, as well as native Python sequences convertible to numpy record arrays.
# - Supported pytables types: http://pytables.github.io/usersguide/datatypes.html
# - The type of the objects saved in an array / table is stored as an HDF5 attribute
# (named FLAVOR). This attribute is then read as Array meta-information
#(accessible through in the Array.attrs.FLAVOR variable), enabling the read objects
# to be converted into the original type. This provides a means to save a large
# variety of objects as arrays with the guarantee that you will be able to later
# recover them in their original form.

## Templates to define a table (container of heterogeneous columns):
## - can be a class derived from IsDescription:
# class Record(IsDescription):
    # name      = StringCol(16)   # or StringCol(itemsize=16) - 16-character String
    # idnumber  = Int64Col()      # Signed 64-bit integer
    # ADCcount  = UInt16Col()     # Unsigned short integer
    # TDCcount  = UInt8Col()      # unsigned byte
    # grid_i    = Int32Col()      # integer
    # grid_j    = Int32Col()      # integer
    # pressure  = Float32Col()    # float  (single-precision)
    # energy    = FloatCol()      # double (double-precision)
# -- the table cells can contain an array (or even more complicated data):
    # pressure2    = Float32Col(shape=(2,3)) # array of floats (single-precision)
    # temperature2 = Float64Col(shape=(2,3)) # array of doubles (double-precision)

## - Native NumPy dtype instances are also accepted:
# Event = dtype([
    # ("name"     , "S16"),
    # ("TDCcount" , uint8),
    # ("ADCcount" , uint16),
    # ("xcoord"   , float32),
    # ("ycoord"   , float32)
    # ])

## - The template can be a dictionary as well:
# Event = {
#     "name"     : StringCol(itemsize=16),
#     "TDCcount" : UInt8Col(),
#     "ADCcount" : UInt16Col(),
#     "xcoord"   : Float32Col(),
#     "ycoord"   : Float32Col(),
#     }

# - You can also use any of the atom factories, i.e. the one which
# accepts a PyTables type.
# Particle2 = {
    # "ADCcount": tables.Col.from_type("int16"),          # signed short integer
    # "TDCcount": tables.Col.from_type("uint8"),          # unsigned byte
    # "grid_i": tables.Col.from_type("int32"),            # integer
    # "grid_j": tables.Col.from_type("int32"),            # integer
    # "idnumber": tables.Col.from_type("int64"),          # signed long long
    # "name": tables.Col.from_kind("string", 16),         # 16-character String
    # "pressure": tables.Col.from_type("float32", (2,)),  # float
    #                                                    (single-precision)
    # "temperature": tables.Col.from_type("float64"),     # double
    #                                                    (double-precision)
#}

## Storing a dictionary in pytables:
# - break it up into its individual components and then store them as
# individual pieces using test_dict.iteritems
# - use recarrays, that allows you to load them into tables in a clean and
# effective way:

import tables as T
import numpy as N
ra = N.array([(3.14159,'some string',[1,2,3,4,5],N.arange(0,10,0.1))],
             dtype = "f8,S20,(5,)i4,(100,)f8")
f = T.open_file("test.h5", "w")
t = f.create_table(f.root, 'table', ra)  # creates appropriate columns automatically !!
print "table metadata-->", repr(t)
print "table data-->", t[:]
f.close()


## Scikit-image ---------------------------------------------------------------

## http://scikit-image.org/




## Scikit-learn ---------------------------------------------------------------

## http://scikit-learn.org/stable/#
## Machine Learning in Python
## Simple and efficient tools for data mining and data analysis
## Built on NumPy, SciPy, and matplotlib
## http://ogrisel.com/  contributor to the scikit-learn library

## Great skilearn tutorial!!
## http://www.astroml.org/sklearn_tutorial/index.html

## http://machinelearningmastery.com/a-gentle-introduction-to-scikit-learn-a-python-machine-learning-library/

## Example: Decision Tree Classifier
from sklearn import datasets
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

## load the iris datasets
dataset = datasets.load_iris()
## fit a CART model to the data
model = DecisionTreeClassifier()
model.fit(dataset.data, dataset.target)
print(model)
## make predictions
expected = dataset.target
predicted = model.predict(dataset.data)
## summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))


## Joblib - lightweight pipelining in Python ----------------------------------
# http://pythonhosted.org/joblib/
	# 1. transparent disk-caching of the output values and lazy re-evaluation (memoize pattern)
	# 2. easy simple parallel computing
	# 3. logging and tracing of the execution


from tempfile import mkdtemp
cachedir = mkdtemp()

import numpy as np
from joblib import Memory
mem = Memory(cachedir=cachedir)
a = np.vander(np.arange(3)).astype(np.float)
square = mem.cache(np.square)
b = square(a)

# Easy to write readable parallel code
from joblib import Parallel, delayed
from math import sqrt
Parallel(n_jobs=1)(delayed(sqrt)(i**2) for i in range(10))

# Replacement for pickle (serialization)

# Memoize
joblib.memory

## GUI design -----------------------------------------------------------------

# TRAITS
# http://scipy-lectures.github.io/packages/traits/index.html

# formlayout is a tiny Python module for creating form dialogs/widgets to edit various type of parameters with having to write any GUI code (it requires Python 2.5+ and PyQt4 4.3+ or PySide 1.1+).
# https://code.google.com/p/formlayout/

# guidata
# Based on the Qt Python binding module PyQt4, guidata is a Python library generating graphical user interfaces for easy dataset editing and display.
# https://pythonhosted.org/guidata/


## Other ----------------------------------------------------------------------

# PyChem - Chemometrics
# http://pychem.sourceforge.net/

# http://numfocus.org/

# D3.js

## -----------------------------------------------------------------------------

# Note from January Meetup: Visualizing Multivariate Data & ML in Python for Largish Data in San Diego
# Kevin davenport, Packetsled

# Data reduction
# Gaussian random projection
# PCA using random SVD
# Kmeans using minibatch

# San Diego supercomputer center
# Python plus C++ library

# Extratreeclassifier

# Pytables
# Numfocus.org

