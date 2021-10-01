"""
The MIT License (MIT)

Copyright (c) 2021 expross

Permission is hereby granted, free of charge, to any person obtaining a copy
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
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

from hiurlparser import parse_url

"""
A request class used for variables like: url args
"""


class Request:
    def __init__(self, *argv, **kwargs):
        self._req = kwargs.get("request")

        self.url = parse_url(self._req.url)
        self.args: dict = self.url.get("query", {})

        # For POST methods
        _content_length = kwargs.get("content_length", None)
        if _content_length:
            self.content_length = _content_length

        _post_data = kwargs.get("post_data", None)
        if _post_data:
            self.post_data = _post_data

    """
    return request's ip
    """

    def ip(self):
        return self._req.address_string()

    """
    return request's time
    """

    def time(self):
        return self._req.log_date_time_string()

    """
    return request's ip
    """

    def send_header(self, *argv, **kwargs):
        return self._req.send_header(*argv, **kwargs)

    """
    return request's server version
    """

    def server_version(self):
        return self._req.server_version

    """
    return request's system version
    """

    def sys_version(self):
        return self._req.sys_version

    """
    return request's headers
    """

    def headers(self):
        return self._req.headers
