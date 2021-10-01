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

from expross.response import XMLResponse, HTMLResponse, JSONResponse, CustomResponse
from expross.request import Request
from expross.errors import RedirectPlease

from http.server import BaseHTTPRequestHandler
from hiurlparser import parse_url

from http import HTTPStatus

"""
made so that we can access other variables like routers
"""


def web_server_wrapper(app: object):

    """
    Web server handler
    """

    class WebServer(BaseHTTPRequestHandler):

        """
        when user does a GET request,
        """

        def do_GET(self):

            self.get_url()
            _path = parse_url(self.url)["path"]

            for route in app.routes:

                if _path == str(route) and route.is_valid_method("GET"):

                    try:

                        app._set_request(Request(request=self))

                        try:
                            res, code = route()
                        except ValueError:
                            res = route()
                            code = HTTPStatus.OK
                        except RedirectPlease as redi:
                            redi_args = redi.args
                            self._redirect(redi_args[0], redi_args[1])
                            self.wfile.write(
                                bytes(str(f"Redirecting to {redi_args[0]}"), "utf-8")
                            )
                            return

                        if not code or type(code) != int:
                            code = HTTPStatus.OK

                        if type(res) == HTMLResponse or type(res) == str:
                            self._set_response(res, code, "text/html")
                        elif type(res) == JSONResponse or type(res) == dict:
                            self._set_response(res, code, "text/json")
                        elif type(res) == XMLResponse:
                            self._set_response(res, code, "application/xml")
                        else:
                            # Do same thing as it was html
                            self._set_response(res, code, "text/html")

                    except Exception as e:
                        self.send_response(500)
                        self.end_headers()
                        print(e)

                    return

            self.send_response(404)

        def do_POST(self):

            self.get_url()
            _path = parse_url(self.url)["path"]

            content_length = int(self.headers["Content-Length"])

            for route in app.routes:

                if _path == str(route) and route.is_valid_method("POST"):

                    try:

                        app._set_request(
                            Request(
                                request=self,
                                content_length=content_length,
                                post_data=self.rfile.read(content_length),
                            )
                        )

                        try:
                            res, code = route()
                        except ValueError:
                            res = route()
                            code = HTTPStatus.OK
                        except RedirectPlease as redi:
                            redi_args = redi.args
                            self._redirect(redi_args[0], redi_args[1])
                            return

                        if not code or type(code) != int:
                            code = HTTPStatus.OK

                        if type(res) == HTMLResponse or type(res) == str:
                            self._set_response(res, code, "text/html")
                        elif type(res) == JSONResponse or type(res) == dict:
                            self._set_response(res, code, "text/json")
                        elif type(res) == XMLResponse:
                            self._set_response(res, code, "application/xml")
                        else:
                            # Do same thing as it was html
                            self._set_response(res, code, "text/html")

                    except Exception as e:
                        self.send_response(HTTPStatus.OK)
                        self.end_headers()
                        print(e)

                    return

            self.send_response(404)

        """
        redirect user to any location with any http_code

        :param location: location to be redirected
        :param code: code of the response (302)
        :type location: str
        :type code: int
        """

        def _redirect(self, location: str, code: int = 302):
            self.send_response(int(code))
            self.send_header("Location", location)
            self.end_headers()

        """
        set the response to client

        :param res: The response, it can be a dictionary, text, etc...
        :param code: code to return (defaults to 200)
        :param type: content-type of the result
        :type code: 200
        :type type: str1
        """

        def _set_response(self, res, code: int, type: str):
            self.send_response(code)
            self.send_header("Content-type", type)
            self.end_headers()
            self.wfile.write(bytes(str(res), "utf-8"))

        """
        make a response to the client

        :param res: The response, it can be a dictionary, text, etc...
        :param code: code to return (defaults to 200)
        :type code: 200
        """

        def response(self, res, code: int == HTTPStatus.OK):
            if type(res) == HTMLResponse or type(res) == str:
                _set_response(res, code, "text/html")
            elif type(res) == JSONResponse or type(res) == dict:
                _set_response(res, code, "text/json")
            elif type(res) == XMLResponse:
                _set_response(res, code, "application/xml")
            else:
                # Do same thing as it was html
                _set_response(res, code, "text/html")

        """
        add a new url value to self.url
        """

        def get_url(self):
            self.url = "http://" + self.server.server_name

            if self.server.server_port:
                self.url += ":" + str(self.server.server_port)

            self.url += self.path

    return WebServer
