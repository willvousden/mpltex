__all__ = ['getDpi', 'getContext']

import matplotlib as mpl
from math import sqrt

def getDpi():
    return 72.27

def getContext(columnWidth, fontSize, aspectRatio=None, height=None):
    dpi = getDpi() # One inch in points (according to TeX).
    width = columnWidth / dpi
    if height is None:
        if aspectRatio is None:
            aspectRatio = (1 + sqrt(5)) / 2
        height = width / aspectRatio

    rc = {}
    rc['text.latex.unicode'] = True
    rc['text.usetex'] = True
    rc['font.family'] = 'serif'
    rc['font.serif'] = ['Computer Modern']

    rc['font.size'] = fontSize
    rc['axes.labelsize'] = fontSize
    rc['legend.fontsize']= fontSize
    rc['xtick.labelsize'] = fontSize * 0.8
    rc['ytick.labelsize'] = fontSize * 0.8

    rc['axes.labelcolor'] = 'black'
    rc['xtick.color'] = 'black'
    rc['ytick.color'] = 'black'

    rc['figure.figsize'] = width, height
    rc['figure.dpi'] = dpi

    return mpl.rc_context(rc)
