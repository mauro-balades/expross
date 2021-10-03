"""
The MIT License (MIT)

Copyright (c) 2021 expross

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import re


class _ContentTypes:
    """A list of Content-Types used for a server response

    Note:
        This class is only a wrapper and its content types can be accessed
        from the class initiation bellow.
    """

    JAVASCRIPT = "application/javascript"
    PDF = "application/pdf"
    JSON = "application/json"
    XML = "application/xml"
    ZIP = "application/zip"
    FORM_ENCODED = "application/x-www-form-urlencoded"

    TEXT = "text/plain"
    CSS = "text/css"
    CSV = "text/csv"
    HTML = "text/html"

    IMAGE_TYPES = (
        "png",
        "jpg",
        "bmp",
        "eps",
        "gif",
        "im",
        "jpeg",
        "msp",
        "pcx",
        "ppm",
        "spider",
        "tiff",
        "webp",
        "xbm",
        "cur",
        "dcx",
        "fli",
        "flc",
        "gbr",
        "gd",
        "ico",
        "icns",
        "imt",
        "iptc",
        "naa",
        "mcidas",
        "mpo",
        "pcd",
        "psd",
        "sgi",
        "tga",
        "wal",
        "xpm",
        "svg",
        "svg+xml",
    )

    VIDEO_TYPES = (
        ("flv", "video/x-flv"),
        ("mp4", "video/mp4"),
        ("m3u8", "application/x-mpegURL"),
        ("ts", "video/MP2T"),
        ("3gp", "video/3gpp"),
        ("mov", "video/quicktime"),
        ("avi", "video/x-msvideo"),
        ("wmv", "video/x-ms-wmv"),
    )

    RE_ACCEPT_QUALITY = re.compile("q=(?P<quality>[^;]+)")


ContentTypes = _ContentTypes()
