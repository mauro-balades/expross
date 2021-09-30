"""
The MIT License (MIT)

Copyright (c) 2021 pynet

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

from http.server import BaseHTTPRequestHandler
from pynet.response import XMLResponse, HTMLResponse, JSONResponse, CustomResponse
from inspect import signature
from url_parser import parse_url

"""
A request class used for variables like: url args
"""
class Request(dict):

    def __init__(self, *argv, **kwargs):

        _req = kwargs.get('request')

        # get url info
        _parsed_url = parse_url(_req.url)
        # _parsed_url['url']

        self.__dict__['ip'] = _req.address_string()
        self.__dict__['time'] = _req.log_date_time_string()
        self.__dict__['send_header'] = _req.send_header
        self.__dict__['server_version'] = _req.server_version
        self.__dict__['sys_version'] = _req.sys_version
        self.__dict__['location'] = _parsed_url
        self.__dict__['headers'] = _req.headers

        print(self.__dict__)


    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return k in self.__dict__

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def pop(self, *args):
        return self.__dict__.pop(*args)

    def __cmp__(self, dict_):
        return self.__cmp__(self.__dict__, dict_)

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def __unicode__(self):
        return unicode(repr(self.__dict__))

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

            for route in app.routes:
                if self.path == str(route):

                    sig = signature(route.function)
                    args_l = len(sig.parameters)

                    try:

                        self.url = 'http://' + self.server.server_name

                        if self.server.server_port:
                            self.url += ':' + str(self.server.server_port)

                        self.url += self.path

                        if args_l == 0:
                            res = route()
                        elif args_l == 1:
                            res = route(Request(request = self))

                        if type(res) == HTMLResponse or type(res) == str:
                            self.send_response(200)
                            self.send_header("Content-type", "text/html")
                            self.end_headers()
                            self.wfile.write(bytes(str(res), "utf-8"))
                        elif type(res) == JSONResponse or type(res) == dict:
                            self.send_response(200)
                            self.send_header("Content-type", "text/json")
                            self.end_headers()
                            self.wfile.write(bytes(str(res), "utf-8"))
                        elif type(res) == XMLResponse:
                            self.send_response(200)
                            self.send_header("Content-type", "application/xml")
                            self.end_headers()
                            self.wfile.write(bytes(str(res), "utf-8"))

                    except Exception as e:
                        self.send_response(500)
                        self.end_headers()
                        print(e)

                    return

            self.send_response(404)

    return WebServer
