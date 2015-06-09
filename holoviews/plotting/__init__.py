
from ..core.options import Cycle
from .plot import Plot

# Tags used when matplotlib output is to be embedded in HTML
IMAGE_TAG = "<img src='{src}' style='max-width:100%; margin: auto; display: block; {css}'/>"
VIDEO_TAG = """
<video controls style='max-width:100%; margin: auto; display: block; {css}'>
<source src='{src}' type='{mime_type}'>
Your browser does not support the video tag.
</video>"""
PDF_TAG = "<iframe src='{src}' style='width:100%; margin: auto; display: block; {css}'></iframe>"


HTML_TAGS = {
    'base64': 'data:{mime_type};base64,{b64}', # Use to embed data
    'svg':  IMAGE_TAG,
    'png':  IMAGE_TAG,
    'gif':  IMAGE_TAG,
    'webm': VIDEO_TAG,
    'mp4':  VIDEO_TAG,
    'pdf':  PDF_TAG
}

MIME_TYPES = {
    'svg':  'image/svg+xml',
    'png':  'image/png',
    'gif':  'image/gif',
    'webm': 'video/webm',
    'mp4':  'video/mp4',
    'pdf':  'application/pdf'
}


def public(obj):
    if not isinstance(obj, type): return False
    baseclasses = [Plot, Cycle]
    return any([issubclass(obj, bc) for bc in baseclasses])

from .mpl import GrayNearest
from .mpl import GrayNearest

_public = ["MPLPlotRenderer", "GrayNearest"] + list(set([_k for _k, _v in locals().items() if public(_v)]))
__all__ = _public
