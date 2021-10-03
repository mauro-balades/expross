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

from expross.response import *
from expross.types import ContentTypes

import inspect


def get_response(data):
    """Create a response that will be directly used for a server response

    Args:
        data (any): Data to be processed to server

    Returns:
        bytes: Bytes converted from string to be ooutputed to server
        str: Conte-Type of the output
    """

    _type = type(data)

    # Defaults to text/plain
    content = ContentTypes.TEXT

    # We assume it is html
    if _type == str:
        content = ContentTypes.HTML
    elif _type == dict:
        content = ContentTypes.JSON
    elif inspect.isclass(data):
        content = data.type

    return bytes(str(data), "utf-8"), content
