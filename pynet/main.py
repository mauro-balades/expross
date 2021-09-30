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

from pynet.server import web_server_wrapper
from http.server import BaseHTTPRequestHandler, HTTPServer

methods = [
    'GET'
]

"""
PyNet is a web server for litle web projects
"""
class PyNet(object):

    default_host_name  = "localhost"
    default_port = 8000

    """
    Init PyNet

    :param port: Optional port to the server be runned on (3000)
    :param host_name: Optional name of server (localhost)
    """
    def __init__(self, *argv, **kwargs):

        self.default_port = kwargs.get('port', self.default_port)
        self.default_host_name = kwargs.get('host_name', self.default_port)
        self.routes = []

    """
    add a route to the server

    :param route: route to apply
    :param methods: Methods available (default: GET)
    :type route: str
    :type methods: <Method>(GET, POST, PUT, DELETE)
    """
    def request(self, route: str, methods: list = ['GET']):

        def decorator(func):
            self.routes.append({
                'route': route,
                'func': func,
                'methods': methods
            })

        return decorator

    """
    Start the web server

    :param hostName: Name of the server (defaults to localhost)
    :param serverPort: Port of the server (defaults to 3000)
    :type port: int
    """
    def start(self, hostName: str = default_host_name, serverPort: int = default_port):
        webServer = HTTPServer((hostName, serverPort), web_server_wrapper(self))
        print("Server started http://%s:%s" % (hostName, serverPort))

        try:
            webServer.serve_forever()
        except KeyboardInterrupt:
            pass

        webServer.server_close()
        print("Server stopped.")
