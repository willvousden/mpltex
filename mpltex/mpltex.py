__all__ = ['getDpi', 'getContext', 'getPreset']

import matplotlib as mpl
from math import sqrt

def getDpi():
    return 72.27

_goldenRatio = (1 + sqrt(5)) / 2
_presets = {
    'revtex12-single': (468, 10.95, None), # Single-column revtex; 12pt.
    'mnras': (240, 8, _goldenRatio), # Double-column MNRAS; default font size.
    'mnras-2': (504, 8, _goldenRatio * 1.2) # Single-column MNRAS; default font size.
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

def _getParams(preset=None, width=None, fontSize=None, aspectRatio=None, height=None):
    if preset is not None:
        assert preset in _presets, \
            'Preset not found.'
        width0, fontSize0, aspectRatio0 = _presets[preset]
    else:
        width0, fontSize0, aspectRatio0 = None, None, None

    if width is not None:
        if width <= 1:
            assert width0 is not None
            width *= width0
    else:
        width = width0

    width = width if width is not None else width0
    fontSize = fontSize if fontSize is not None else fontSize0
    aspectRatio = aspectRatio if aspectRatio is not None else aspectRatio0

    assert width is not None and fontSize is not None, \
        'Column width or font size missing.'

    dpi = getDpi() # One inch in points (according to TeX).
    if height is None:
        if aspectRatio is None:
            aspectRatio = _goldenRatio
        height = width / aspectRatio
    width /= dpi
    height /= dpi

    return width, height, dpi, fontSize, fontSize * 0.8
