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

from expross.errors import MethodNotAvailable
from expross.utils import get_response
from expross.context import Context

from falcon import Request, Response


class Resource:
    """This used every request the server recieves

    Note:
        This is a wrapper for <Route> class, if you whant to see arguments,
        methods, raises and functions, there is the place to find it
        (expross/routes.py)
    """

    def _check_for_method(self, method: str):
        """check if a method is valid

        Args:
            method (str): This is the method to be evaluated

        Raises:
            MethodNotAvailable: this is triggered when a method is not avaiable for a route

        Note:
            There is a diference between this function and the one on (expross/routes.py).
            If a method is not valid here, we raise an exception <MethodNotAvailable>. and in
            the one the route is, it just returns True if it is valid.
        """
        if not method in self.methods:
            raise MethodNotAvailable(f"Method {method} is not avaiable for this route")

    def _get_packed_result(self, req, res):
        """Get a complete version of the function's response

        Args:
            context (str): extra context used in uri's templates

        Returns:
            any: The result the response will have as body
            int: status code for the response

            Note:
                If code is a string, we are assuming that it is the
                content-type response. So code will be defaulted to
                200 and content_type will now be code

            str: Content-type of the response
        """
        # TODO: add arguments if the have a templated url
        data = self.function(req, res)

        # TODO: clean a bit this code.
        try:
            res, code, content_type = data
        except ValueError:
            try:
                content_type = None
                res, code = data

                # If code is a string, we assume
                # it is the content-type.
                if type(code) == str:
                    content_type = code
                    code = 200

            except ValueError:
                res = data
                code = 200

        return res, code, content_type

    def on_get(self, req: Request, resp: Response, **context):
        """Triggered when a GET request has been requested

        Args:
            req (Request): This information from the request
            resp (Response, optional): Response information
        """
        self._check_for_method("GET")

        self.app.context = Context(context)
        res, code, content_type = self._get_packed_result(req, resp)

        # Get response's data in bytes
        data, type = get_response(res)

        resp.status = code
        resp.data = data
        resp.content_type = type if content_type is None else content_type

    def on_post(self, req: Request, resp: Response, **context):
        """Triggered when a POST request has been requested

        Args:
            req (Request): This information from the request
            resp (Response, optional): Response information
        """
        self._check_for_method("POST")

        self.app.context = Context(context)
        res, code, content_type = self._get_packed_result(req, resp)

        # Get response's data in bytes
        data, type = get_response(res)

        resp.status = code
        resp.data = data
        resp.content_type = type if content_type is None else content_type
