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

from expross.errors import NoRouteName, NoFunctionSpecified
from expross.resource import Resource
from typing import Callable

"""
A class to contain all of the information a router should have
"""


class Route(Resource):

    """
    create a new route
    """

    def __init__(self, *argv, **kwargs):

        self.route: str = kwargs.get("route", None)
        self.methods: list = kwargs.get("methods", ["GET"])
        self.function: Callable = kwargs.get("func", None)
        self.app: __import__("expross").Expross = kwargs.get("app")

        if self.route is None:
            raise NoRouteName("Route should be specified")
        if self.function is None or type(self.function) == object:
            raise NoFunctionSpecified("a function should be specified")

    """
    checks if a methos is balid

    :param method: method to be questioned
    """

    def is_valid_method(self, method: str):
        return method in self.methods

    def __repr__(self):
        return '<Route route="%s" function=%s methods=[%s]>' % (
            self.route,
            self.function,
            self.methods,
        )

    def __str__(self):
        return self.route

    def __call__(self, *argv, **kwargs):
        return self.function(*argv, **kwargs)
