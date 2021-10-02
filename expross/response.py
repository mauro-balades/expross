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

from expross.types import ContentTypes


class html(object):
    def __init__(self, content: str, *argv, **kwargs):

        self.content = content
        self.code = int(kwargs.get("code", 200))
        self.type = ContentTypes.HTML

    def __str__(self):
        return self.content


class json(object):
    def __init__(self, content: str, *argv, **kwargs):

        self.content = content
        self.code = int(kwargs.get("code", 200))
        self.type = ContentTypes.JSON

    def __str__(self):
        return self.content


class xml(object):
    def __init__(self, content: dict, *argv, **kwargs):

        self.content = content
        self.code = int(kwargs.get("code", 200))
        self.type = ContentTypes.XML

    def __str__(self):
        return self.content


class text(object):
    def __init__(self, content: dict, *argv, **kwargs):

        self.content = content
        self.code = int(kwargs.get("code", 200))
        self.type = ContentTypes.TEXT

    def __str__(self):
        return self.content


class csv(object):
    def __init__(self, content: dict, *argv, **kwargs):

        self.content = content
        self.code = int(kwargs.get("code", 200))
        self.type = ContentTypes.CSV

    def __str__(self):
        return self.content


class zip(object):
    def __init__(self, content: dict, *argv, **kwargs):

        self.content = content
        self.code = int(kwargs.get("code", 200))
        self.type = ContentTypes.ZIP

    def __str__(self):
        return self.content


class pdf(object):
    def __init__(self, content: dict, *argv, **kwargs):

        self.content = content
        self.code = int(kwargs.get("code", 200))
        self.type = ContentTypes.PDF

    def __str__(self):
        return self.content
