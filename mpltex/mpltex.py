__all__ = ['getDpi', 'getContext', 'getPreset']

import matplotlib as mpl
from math import sqrt

def getDpi():
    return 72.27

_goldenRatio = (1 + sqrt(5)) / 2
_presets = {
    'revtex12-single': (468, 10.95, None), # Single-column revtex; 12pt.
    'mnras': (240, 8, _goldenRatio * 0.8), # Double-column MNRAS; default font size.
    'mnras-2': (504, 8, _goldenRatio) # Single-column MNRAS; default font size.
}

def getPreset(preset):
    return _presets[preset]

def getContext(*args, **kwargs):
    width, height, dpi, fontSize, tickFontSize = _getParams(*args, **kwargs)

    rc = {}
    rc['text.latex.unicode'] = True
    rc['text.usetex'] = True
    rc['font.family'] = 'serif'
    rc['font.serif'] = ['Computer Modern']

    rc['font.size'] = fontSize
    rc['axes.labelsize'] = fontSize
    rc['legend.fontsize']= fontSize
    rc['xtick.labelsize'] = tickFontSize
    rc['ytick.labelsize'] = tickFontSize

    rc['axes.labelcolor'] = 'black'
    rc['xtick.color'] = 'black'
    rc['ytick.color'] = 'black'

    rc['figure.figsize'] = width, height
    rc['figure.dpi'] = dpi

    return mpl.rc_context(rc)

#def updateFigure(figure, *args, **kwargs):
    #width, height, dpi, fontSize, tickFontSize = _getParams(*args, **kwargs)

    #figure.set_size_inches(width, height)
    #figure.set_dpi(dpi)
    #figure.

    #for a in figure.as_list():
        #for item in a.get_xticklabels() + a.get_yticklabels():
            #item.set_fontsize(tickFontSize)

        #for item in [a.title, a.xaxis.label, a.yaxis.label]:
            #item.set_fontsize(fontSize)

        #a.

def _getParams(preset=None, columnWidth=None, fontSize=None, aspectRatio=None, height=None):
    if preset is not None:
        assert preset in _presets, \
            'Preset not found.'
        columnWidth, fontSize, aspectRatio = _presets[preset]
    assert columnWidth is not None and fontSize is not None, \
        'Column width or font size missing.'

    dpi = getDpi() # One inch in points (according to TeX).
    width = columnWidth / dpi
    if height is None:
        if aspectRatio is None:
            aspectRatio = _goldenRatio
        height = width / aspectRatio

    return width, height, dpi, fontSize, fontSize * 0.8
