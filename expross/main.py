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
from typing import Callable

from expross.routes import Route
from expross.errors import ErrorCodeExists, RouteAlreadyExists, VariableIsConstant
from expross.error import ErrorHandler

from wsgiref.simple_server import make_server

from jinja2 import Template
from jinja2 import Environment, FileSystemLoader

from falcon import Request, Response
from falcon import HTTPFound

import minify_html
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

    Note:
        Default values can be changed in diferent ways. You can change it by
        adding parameters, define them in other functions. For example, you can
        change host name and port number in the listen() function. Also, you can
        directly change clas's attributes.

    Warning:
        All examples in the documentation, all references in code and in the tests.
        This class will be placed into a variable in where it's name is "app".

    """

    # | Default values, they can be overrided
    default_host_name = "localhost"
    default_port = 8000
    default_templates = "templates"
    default_static = "public"

    def __init__(self, *argv, **kwargs):
        # | Initiate class

        super(object, self).__init__()

        self.default_port: int = kwargs.get("port", self.default_port)
        self.default_host_name: str = kwargs.get("host_name", self.default_port)

        self.routes: list = []
        self.errors: list = []
        self.middlewares: list = kwargs.get("middlewares", [])

        self.context = None

        self.app: falcon.App = falcon.App(middleware=self.middlewares)

        # Jinja2 initialitaion
        _templates: str = kwargs.get("templates", self.default_templates)
        file_loader: FileSystemLoader = FileSystemLoader(_templates)
        self.jinja_env: Environment = Environment(loader=file_loader)

        # Add a default enpoint
        self.default_enpoint: str = kwargs.get("endpoint", None)

        # Default config
        self.jinja_env.trim_blocks = True
        self.jinja_env.lstrip_blocks = True
        self.jinja_env.rstrip_blocks = True

        self.vars = []

        # Add all middlewares
        for i in self.middlewares:
            self.use(i)

    def serve_static(
        self, route: str = "/" + default_static, folder: str = "./" + default_static
    ):
        """Serves static files

        Usage:
            app.serve_static('/static', './static')

        Args:
            route (str, optional): route's name. Defaults to "/public".
            folder (str, optional): folder's name. Defaults to "./public".

        Warning:
            imagine you have a server in (http://localhost:8000). Once you have
            called serve_static('/static', './static') function, all files inside
            the folder param will be visible to other users. For example, if you go to
            http://localhost:8000/static/secrete_file, user will be able to
            see that file. So if you whant to hide secrete files, better todo
            use a middleware or add a custom route to that file, allowing what files
            can be visible and private.
        """
        # | Get static folder.
        # | falcon requires an abstract
        # | path, in order to serve static files
        current = os.getcwd()
        folder = os.path.join(current, folder)

        # | add route, abstract folder to falcon
        # | in order to serve static.
        self.app.add_static_route(route, folder)

    def set_templates(self, name: str = "templates"):
        """overrides the templates folder's name in the configuration

        Args:
            name (str, optional): folder's name. Defaults to "templates".
        """
        file_loader: FileSystemLoader = FileSystemLoader(name)
        self.jinja_env: Environment = Environment(loader=file_loader)

    def use(self, middleware):

        if type(middleware) == type(self):
            for r in middleware.routes:
                nr = Route(route=str(r), methods=r.methods, func=r.function, app=self)
                self.app.add_route(str(r), nr)
                self.routes.append(nr)

            for e in middleware.errors:
                handler = ErrorHandler(e.error, e.func, self)
                self.app.add_error_handler(e.error, handler.handle)
                self.errors.append(handler)

            for v in middleware.vars:
                self.set_var(v["name"], v["value"], v["const"])

            return

        self.app.add_middleware(middleware)
        self.middlewares.append(middleware)

    def set_var(self, name: str, val: str, constant: bool = False):
        """Set a variable to the app's contenxt

        Args:
            name (str): Name of the variable
            val (str): Value for the variable
            constant (bool, optional): Declare if the value can be changed or not. Defaults to False.

        Raises:
            VariableIsConstant: If trying to change a variable's value but variable is constant

        Returns:
            dict: Variable object
        """

        exists = False
        for var in self.vars:
            if var["name"] == name:
                exists = True

        if not exists:
            self.vars.append(
                {
                    "name": str(name),
                    "value": str(val),
                    "const": constant,
                }
            )

            return True

        for i, var in enumerate(self.vars):
            if var["name"] == name:

                if var["const"]:
                    raise VariableIsConstant(f"Variable {name} is a constant")

                self.vars[i]["value"] = str(val)
                self.vars[i]["const"] = constant

        return True

    def get_var(self, name: str):
        """Get an object from an app's variable

        Args:
            name (str): Name of the variable

        Returns:
            dict: Object of the variable
        """
        ret = None

        for var in self.vars:
            if var["name"] == name:
                ret = var

        return ret

    def error(self, error, func: Callable):
        """add an error handler to your app

        Usage:

            def my_error():
                return "Ups! 404"

            app.error(HTTPNotFound, my_error)

        Args:
            error (int | ErrorLike): error to be handled
        """

        for err in self.errors:
            if err.error == error:
                raise ErrorCodeExists(f"Code for {error} is already being handled")

        handler = ErrorHandler(error, func, self)
        self.app.add_error_handler(error, handler.handle)
        self.errors.append(handler)

    def all(self, _route: str, func: Callable):
        """add a route to the server with the all methods available

        Args:
            route (str): route to be added to the router's list
            func (Callable): Function to be called when endpoint is being called
        """
        for method in ["GET", "POST"]:
            self._add_route(_route, func, method)

    def get(self, _route: str, func: Callable):
        """add a route to the server with the GET method

        Args:
            route (str): route to be added to the router's list
            func (Callable): Function to be called when endpoint is being called
        """
        self._add_route(_route, func, "GET")

    def post(self, _route: str, func: Callable):
        """add a route to the server with the POST method

        Args:
            route (str): route to be added to the router's list
            func (Callable): Function to be called when endpoint is being called
        """
        self._add_route(_route, func, "POST")

    def listen(
        self,
        serverPort: int = default_port,
        cb: Callable = None,
        hostName: str = default_host_name,
    ):
        """Start a web server

        Args:
            hostName (str, optional): host name for the server. Defaults to localhost.
            cb (str, optional): optional callback function called when app started runing.
            serverPort (int, optional): port for the server to run in. Defaults to 8000.

        Note:
            This function is intended to be at the bottom of the script, when
            all routes and error handlers has been loaded
        """
        self.default_port = serverPort
        self.default_host_name = hostName

        with make_server(hostName, serverPort, self.app) as httpd:
            # print("Server started http://%s:%s" % (hostName, serverPort))
            if cb:
                cb()

            # Serve until process is killed
            httpd.serve_forever()

    def url_for(self, name: str):
        """Returns a route depending on the function's name

        Args:
            name (str): name for the function

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
            error to redirect user, if it is being handled, redirects won't happend.
        """
        raise HTTPFound(location)

    def render(self, data: str, **context: any):
        """render a jinja2 string with some context

        Args:
            data (str): string template to be parsed
            context (any, optional): additional context to give to the template. Defaults to None.
            _minified: (bool, optional): make html, css, js a minified version of themselve. Defaults to False

        Waring:
            If the "_minified" parameter is set, both JavaScript, CSS will be also be minified alon with
            the HTML.

        Returns:
            str: a rendered version of the string
        """

        tm = Template(data)
        min = context.get("_minified", False)
        render = tm.render(**context)

        if min:
            return minify_html.minify(
                render,
                minify_js=True,
                minify_css=True,
                remove_processing_instructions=True,
            )

        return render

    def render_template(self, name: str, **context: any):
        """render a jinja2 template file with some context

        Args:
            name (str): template file to be parsed
            context (any, optional): additional context to give to the template. Defaults to None.
            _minified: (bool, optional): make html, css, js a minified version of themselve. Defaults to False

        Waring:
            If the "_minified" parameter is set, both JavaScript, CSS will be also be minified alon with
            the HTML.

        Returns:
            str: a rendered version of the template
        """
        template = self.jinja_env.get_template(name)
        rendered = template.render(**context)

        min = context.get("_minified", False)

        if min:
            return minify_html.minify(
                rendered,
                minify_js=True,
                minify_css=True,
                remove_processing_instructions=True,
            )

        return rendered

    def _add_route(self, _route: str, func: Callable, method: str):
        if _route == "/" and self.default_enpoint:
            _route = self.default_enpoint
        elif self.default_enpoint:
            _route = self.default_enpoint + _route

        self._check_for_repeated_route(_route, method, func)
        _repeated = self._check_for_mentioned_route(_route)

        if _repeated:
            _repeated.methods.append(method)
        else:
            route = Route(route=_route, methods=[method], func=func, app=self)
            self.app.add_route(_route, route)
            self.routes.append(route)

    def _check_for_mentioned_route(self, name):
        for route in self.routes:
            if str(route) == name:
                return route

        return None

    def _check_for_repeated_route(self, name, method, function):
        for route in self.routes:
            if name == str(route) and method in route.methods:
                raise RouteAlreadyExists(
                    f"Router with name {name} ({method}) already exists"
                )

    def _set_request(self, req: Request):
        """Set a request to the app

        Args: req (Request): request to be set
        """
        self.req = req

    def _set_response(self, res: Response):
        """Set a response to the app

        Args: res (Response): request to be set
        """
        self.res = res

    def __repr__(self):
        # default_port and default_host_name are being overieded
        # in the start() function
        return '<Expross port=%i host_name="%s">' % (
            self.default_port,
            self.default_host_name,
        )
