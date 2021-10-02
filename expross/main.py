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
from __future__ import absolute_import

from expross.routes import Route
from expross.errors import ErrorHandlerExists, ErrorCodeExists
from expross.error import ErrorHandler

from wsgiref.simple_server import make_server

from jinja2 import Template
from jinja2 import Environment, FileSystemLoader

import falcon
from falcon import Request
from falcon import HTTPFound

"""
Expross is a web server for litle web projects
"""


class Expross(object):

    default_host_name = "localhost"
    default_port = 8000
    default_templates = "templates"

    """
    Init Expross

    :param port: Optional port to the server be runned on (3000)
    :param host_name: Optional name of server (localhost)
    """

    def __init__(self, *argv, **kwargs):

        super(object, self).__init__()

        self.default_port: int = kwargs.get("port", self.default_port)
        self.default_host_name: str = kwargs.get("host_name", self.default_port)

        self.routes = []
        self.errors = []
        self.req: Request = None

        self.app: falcon.App = falcon.App()

        # Jinja2 initialitaion
        _templates: str = kwargs.get("templates", self.default_templates)
        file_loader: FileSystemLoader = FileSystemLoader(_templates)
        self.jinja_env: Environment = Environment(loader=file_loader)

        # Default config
        self.jinja_env.trim_blocks = True
        self.jinja_env.lstrip_blocks = True
        self.jinja_env.rstrip_blocks = True

    """
    add a route to the server with GET method

    :param route: route to apply
    :type route: str
    """

    def get(self, _route: str = None):
        def decorator(func):
            self._check_for_repeated_route(_route, "GET", func)
            _repeated = self._check_for_mentioned_route(_route)

            if _repeated:
                _repeated.methods.append("GET")
            else:
                route = Route(route=_route, methods=["GET"], func=func, app=self)
                self.app.add_route(_route, route)
                self.routes.append(route)

        return decorator

    """
    add a error handler to the server

    :param error: error to handle
    :type error: int
    """

    def error(self, error):
        def decorator(func):

            for err in self.errors:
                if err.func.__name__ == func.__name__:
                    raise ErrorHandlerExists("Same error function exists")
                elif err.error == error:
                    raise ErrorCodeExists(f"Code for {error} is already being handled")

            handler = ErrorHandler(error, func, self)
            self.app.add_error_handler(error, handler.handle)
            self.errors.append(handler)

        return decorator

    """
    add a route to the server with the POST method

    :param route: route to apply
    :type route: str
    """

    def post(self, _route: str = None):
        def decorator(func):
            self._check_for_repeated_route(_route, "POST", func)
            _repeated = self._check_for_mentioned_route(_route)

            if _repeated:
                _repeated.methods.append("POST")
            else:
                route = Route(route=_route, methods=["POST"], func=func, app=self)
                self.app.add_route(_route, route)
                self.routes.append(route)

        return decorator

    def _check_for_mentioned_route(self, name):
        for route in self.routes:
            if str(route) == name:
                return route

        return None

    def _check_for_repeated_route(self, name, method, function):
        for route in self.routes:
            if (
                name == str(route)
                and method in route.methods
                or route.function.__name__ == function.__name__
            ):
                raise RouteAlreadyExists(
                    f"Router with name {name} ({method}) already exists"
                )

    """
    Start the web server

    :param hostName: Name of the server (defaults to localhost)
    :param serverPort: Port of the server (defaults to 3000)
    :type port: int
    """

    def listen(self, hostName: str = default_host_name, serverPort: int = default_port):

        self.default_port = serverPort
        self.default_host_name = hostName

        with make_server(hostName, serverPort, self.app) as httpd:
            print("Server started http://%s:%s" % (hostName, serverPort))

            # Serve until process is killed
            httpd.serve_forever()

    def url_for(self, name: str):
        for route in self.routes:
            if route.function.__name__ == name:
                return str(route)

        return None

    """
    Redirects to the specified location using the provided http_code (defaults to HTTP_302 FOUND)
    """

    def redirect(self, location: str):
        raise HTTPFound(location)

    """
    render a jinja2 string with some context

    :param data: string to be parsed
    :param context: additional context to give to the template
    """

    def render(self, data: str, **context: any):
        tm = Template(data)
        return tm.render(**context)

    """
    render a jinja2 string with some context

    :param name: template file to be parsed
    :param context: additional context to give to the template
    """

    def render_template(self, name: str, **context: any):
        template = self.jinja_env.get_template(name)
        rendered = template.render(**context)
        return rendered

    """
    set a request so that user can use it

    :param req: the request class
    :type req: Request
    """

    def _set_request(self, req: Request):
        self.req = req

    def __repr__(self):
        # default_port and default_host_name are being overieded
        # in the start() function
        return '<Expross port=%i host_name="%s">' % (
            self.default_port,
            self.default_host_name,
        )
