__all__ = ['getDpi', 'getContext', 'getPreset', 'getScreenContext']

import matplotlib as mpl
from math import sqrt

def getDpi():
    return 72.27

_screenDpi = 96
_screenFontSize = 12
_goldenRatio = (1 + sqrt(5)) / 2
_presets = {
    'revtex12-single': (468, 10.95, None), # Single-column revtex; 12pt.
    'mnras': (240, 8, _goldenRatio), # Double-column MNRAS; default font size.
    'mnras-2': (504, 8, _goldenRatio * 1.2), # Single-column MNRAS; default font size.
    'thesis': (300, 8, _goldenRatio),
    'thesis-wide': (426, 8, _goldenRatio)
}

def getPreset(preset):
    return _presets[preset]

def getContext(returnParams=False, *args, **kwargs):
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

    if returnParams:
        return rc
    else:
        return mpl.rc_context(rc)

def getScreenContext(pixelWidth=None, fontSize=None, aspectRatio=None, returnParams=False):
    if aspectRatio is None:
        aspectRatio = _goldenRatio

    if fontSize is None:
        fontSize = _screenFontSize

    params = {
        'figure.dpi': _screenDpi,
        'text.usetex': False,
        'mathtext.fontset': 'stixsans',
        'font.family': 'Bitstream Vera Sans',
        'font.size': fontSize,
        'axes.labelsize': fontSize,
        'legend.fontsize': fontSize,
        'xtick.labelsize': fontSize * 0.8,
        'ytick.labelsize': fontSize * 0.8,
        }
    if pixelWidth is not None:
        pixelHeight = pixelWidth / aspectRatio
        params['figure.figsize'] = (pixelWidth / _screenDpi, pixelHeight / _screenDpi)

    if returnParams:
        return params
    else:
        return mpl.rc_context(params)

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
