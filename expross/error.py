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

from typing import Callable
from expross.utils import get_response
from expross.errors import CustomBaseException


class ErrorHandler(CustomBaseException):
    """Handles any errors user whants to handle.

    Args:
        error (int): Error code that would be handled. Example: 404 or 500
        function (Callable): Function that would be triggered when error happens
        app (Expross): App's context to change / see its values
    """

    def __init__(self, error: int, function: Callable, app):
        # Initiate class

        self.error = error
        self.func = function
        self.app = app

    def handle(self, ex, req, resp, params):
        """Triggered when we need to handle a specific error

        Args:
            ex (any): error from server
            req (any): request information from the request
            resp (any): response information
            params (any): extra parameters

        Usage:

            @app.error(404):
            def error():
                return "Ups! 404"

        Note:
            Errors can only be registered one, an exception would
            be raised in another function
        """
        data = self.func(req, resp)
        res, type = get_response(data)

        self.app.req = req
        self.app.res = res

        resp.content_type = type
        resp.data = res
        resp.status = int(self._get_code(ex.status))

    def _get_code(self, code: str):
        """Get a code inside a error status

        Args:
            code (str): peace of string in where a code will be taken away

        Example: "404 not found"
                  ^^^

        Returns:
            str: Code extracted from string
        """
        # Get first 3 digits
        return code[:3]
