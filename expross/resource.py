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

from falcon import Request, Response

"""
A request handler for expross
"""


class Resource:
    def _check_for_method(self, method):
        if not method in self.methods:
            raise MethodNotAvailable(f"Method {method} is not avaiable for this route")

    def _get_res_and_code(self):
        data = self.function()

        try:
            res, code, content_type = data
        except ValueError:
            try:
                content_type = None
                res, code = data
            except ValueError:
                res = data
                code = 200

        return res, code, content_type

    def on_get(self, req: Request, resp: Response):
        self._check_for_method("GET")

        self.app.req: Request = req
        res, code, content_type = self._get_res_and_code()
        data, type = get_response(res)

        resp.status = code
        resp.data = data
        resp.content_type = type if content_type is None else content_type

    def on_post(self, req: Request, resp: Response):
        self._check_for_method("POST")
