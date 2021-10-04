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


class Route(Resource):
    """This is a router service used for every individual route

    Args:
        route (str): Route to be checked every request
        methods (list, optional): A list of avaiable methods a route can have. Defaults to ["GET"]

            Note:
                Each route can have diferent methods but the route can't be the same if a route with
                same method has already been registered. (Something like what happens with the function)
                Only HTTP methods will be avaiable:

                * The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.
                * The HEAD method asks for a response identical to that of a GET request, but without the response body.
                * The POST method is used to submit an entity to the specified resource, often causing a change in state or side effects on the server.
                * The PUT method replaces all current representations of the target resource with the request payload.
                * The DELETE method deletes the specified resource.
                * The CONNECT method establishes a tunnel to the server identified by the target resource.
                * The OPTIONS method is used to describe the communication options for the target resource.
                * The TRACE method performs a message loop-back test along the path to the target resource.
                * The PATCH method is used to apply partial modifications to a resource.

                you can see more information here: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

        function (Callable): This function will be used every request if the route and methods are the same.

            Note:
                The function parameter will only be called if route is correct and method is correct, you can
                have the same function for more than one method, what you can't have is a function with same name
                or same method.

            Example:

                @app.get("/")
                def func1():
                    pass

                @app.get("/")
                def func2():
                    pass

        app (Expross): This is an app context used to manipulate Expros's variables

    Raises:
        NoRouteName: when a router's name has not been specified
        NoFunctionSpecified: when a router's function has not been specified

    Note:
        Raises should not appear but, just in case something fails, it is recomended
        to raise an error.
    """

    def __init__(self, *argv, **kwargs):
        """Initiate the class

        Note: You can see arguments and raises in the clas's stringdoc
        """

        self.route: str = kwargs.get("route", None)
        self.methods: list = kwargs.get("methods", ["GET"])
        self.function: Callable = kwargs.get("func", None)
        self.app: __import__("expross").Expross = kwargs.get("app")

        if self.route is None:
            raise NoRouteName("Route should be specified")
        if self.function is None or type(self.function) == object:
            raise NoFunctionSpecified("a function should be specified")

    def is_valid_method(self, method: str):
        """This function is to check if a router has a valid method

        Args:
            method (str): This method is used to check if it is valid

        Returns:
            bool: True if it is valid False if it is not
        """
        return method in self.methods

    def __repr__(self):
        return '<Route route="%s" function=%s methods=%s>' % (
            self.route,
            self.function,
            self.methods,
        )

    def __str__(self):
        return self.route

    def __call__(self, *argv, **kwargs):
        return self.function(*argv, **kwargs)
