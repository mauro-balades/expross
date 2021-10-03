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

from falcon import Request, Response
from falcon import HTTPFound

import falcon
import os

class Expross(object):
    """Expross is a lightweight web server to introduce JavaScript developers familiar with Express to Python.

    Args:
        host_name (str, optional): host name for the server. Defaults to localhost.
        port (int, optional): port for the server to run in. Defaults to 8000.
        templates (str, optional): Templates folder. Defaults to "templates".

        Note:
            host_name and port can be also changed when puting them as parameters
            for the listen() function. Templates argument can also be changed by
            using the set_templates(name: str) function

    """

    default_host_name = "localhost"
    default_port = 8000
    default_templates = "templates"
    default_static = "public"

    def __init__(self, *argv, **kwargs):
        # Initiate class

        super(object, self).__init__()

        self.default_port: int = kwargs.get("port", self.default_port)
        self.default_host_name: str = kwargs.get("host_name", self.default_port)

        self.routes = []
        self.errors = []
        self.req: Request = None
        self.res: Response = None

        self.app: falcon.App = falcon.App()

        # Jinja2 initialitaion
        _templates: str = kwargs.get("templates", self.default_templates)
        file_loader: FileSystemLoader = FileSystemLoader(_templates)
        self.jinja_env: Environment = Environment(loader=file_loader)

        # Default config
        self.jinja_env.trim_blocks = True
        self.jinja_env.lstrip_blocks = True
        self.jinja_env.rstrip_blocks = True

    def serve_static(
        self, route: str = "/" + default_static, folder: str = "./" + default_static
    ):
        """Serves static files

        Usage:
            app.serve_static('/static', './static')

        Args:
            route (str, optional): route's name. Defaults to "/public".
            folder (str, optional): folder's name. Defaults to "./public".
        """
        current = os.getcwd()
        folder = os.path.join(current, folder)
        self.app.add_static_route(route, folder)

    def set_templates(self, name: str = "templates"):
        """overrides the templates folder's name in the configuration

        Args:
            name (str, optional): folder's name. Defaults to "templates".
        """
        file_loader: FileSystemLoader = FileSystemLoader(name)
        self.jinja_env: Environment = Environment(loader=file_loader)

    def error(self, error):
        """add an error handler to your app

        Usage:

            @app.error(404):
            def error():
                return "Ups! 404"

        Args:
            error (int | ErrorLike): error to be handled
        """

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

    def get(self, _route: str = None):
        """add a route to the server with the GET method

        Args:
            route (str): route to be added to the router's list
        """

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

    def post(self, _route: str = None):
        """add a route to the server with the POST method

        Args:
            route (str): route to be added to the router's list
        """

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

    def listen(self, hostName: str = default_host_name, serverPort: int = default_port):
        """Start a web server

        Args:
            hostName (str, optional): host name for the server. Defaults to localhost.
            serverPort (int, optional): port for the server to run in. Defaults to 8000.

        Note:
            This function is intended to be at the bottom of the script, when
            all routes and error handlers has been loaded
        """
        self.default_port = serverPort
        self.default_host_name = hostName

        with make_server(hostName, serverPort, self.app) as httpd:
            print("Server started http://%s:%s" % (hostName, serverPort))

            # Serve until process is killed
            httpd.serve_forever()

    def url_for(self, name: str):
        """Returns a route depending on the function's name

        Args:
            name (str): name for the function

        Usage:

            @app.get("/")
            def main():
                pass

            url_for('main')
            >> /

        Returns:
            str: If a function has been found
            None: If no function has been found
        """
        for route in self.routes:
            if route.function.__name__ == name:
                return str(route)

        return None

    def redirect(self, location: str):
        """Redirects to the specified location

        Args:
            location (str): Location to be redirected

        Raises:
            HTTPFound (depends on code): A Exception used to redirect user

            Note:
                Please do not do any error handling for this. This is an intentionally
                error to redirect user.
        """
        # TODO: create more options based on status codes
        raise HTTPFound(location)

    def render(self, data: str, **context: any):
        """render a jinja2 string with some context

        Args:
            data (str): string template to be parsed
            context (any, optional): additional context to give to the template. Defaults to None.

        Returns:
            str: a rendered version of the string
        """
        tm = Template(data)
        return tm.render(**context)

    def render_template(self, name: str, **context: any):
        """render a jinja2 template file with some context

        Args:
            name (str): template file to be parsed
            context (any, optional): additional context to give to the template. Defaults to None.

        Returns:
            str: a rendered version of the template
        """
        template = self.jinja_env.get_template(name)
        rendered = template.render(**context)
        return rendered

    def _set_request(self, req: Request):
        """Set a request to the app

        Args: req (Request): request to be set
        """
        self.req = req

    def _set_response(self, res: Response):
        """Set a response to the app

        Args: res (Response): request to be set
        """
        self.req = req

    def __repr__(self):
        # default_port and default_host_name are being overieded
        # in the start() function
        return '<Expross port=%i host_name="%s">' % (
            self.default_port,
            self.default_host_name,
        )
