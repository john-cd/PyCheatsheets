# -*- coding: utf-8 -*-
"""
Created on Wed May 21 18:33:40 2014

Example - projecting an image into a 3D box

@author: Sylvain
"""
import pylab
from matplotlib.cbook import get_sample_data
from matplotlib._png import read_png


fn = get_sample_data("lena.png", asfileobj=False)
# or:  fn = open('milkyway.png','r')

# fn is a file object
img = read_png(fn)
x, y = pylab.ogrid[0 : img.shape[0], 0 : img.shape[1]]
ax = pylab.gca(projection="3d")
ax.plot_surface(x, y, 10, rstride=5, cstride=5, facecolors=img)
pylab.show()
