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

from expross.errors import NoRouteName, NoMethodSpecified, NoFunctionSpecified

"""
A class to contain all of the information a router should have
"""
class Route(object):

    """
    create a new route
    """
    def __init__(self, *argv, **kwargs):

        self.route = kwargs.get('route', None)
        self.methods = kwargs.get('methods', None)
        self.function = kwargs.get('func', None)

        if self.route is None:
            raise NoRouteName("Route should be specified")
        if self.methods is None:
            raise NoMethodSpecified("methods should be specified")
        if self.function is None or type(self.function) == object:
            raise NoFunctionSpecified("a functio should be specified")

    def __repr__(self):
        return ("<Route route=\"%s\" function=%s methods=%s>" % (self.route, self.function, self.methods))

    def __str__(self):
        return self.route

    def __call__(self, *argv, **kwargs):
        return self.function(*argv, **kwargs)
