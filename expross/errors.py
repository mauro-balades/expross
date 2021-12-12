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

# Errors
__all__ = (
    "CompatibilityError",
    "DelimiterError",
    "HeaderNotSupported",
    "HTTPBadGateway",
    "HTTPBadRequest",
    "HTTPConflict",
    "HTTPFailedDependency",
    "HTTPForbidden",
    "HTTPGatewayTimeout",
    "HTTPGone",
    "HTTPInsufficientStorage",
    "HTTPInternalServerError",
    "HTTPInvalidHeader",
    "HTTPInvalidParam",
    "HTTPLengthRequired",
    "HTTPLocked",
    "HTTPLoopDetected",
    "HTTPMethodNotAllowed",
    "HTTPMissingHeader",
    "HTTPMissingParam",
    "HTTPNetworkAuthenticationRequired",
    "HTTPNotAcceptable",
    "HTTPNotFound",
    "HTTPNotImplemented",
    "HTTPPayloadTooLarge",
    "HTTPPreconditionFailed",
    "HTTPPreconditionRequired",
    "HTTPRangeNotSatisfiable",
    "HTTPRequestHeaderFieldsTooLarge",
    "HTTPRouteNotFound",
    "HTTPServiceUnavailable",
    "HTTPTooManyRequests",
    "HTTPUnauthorized",
    "HTTPUnavailableForLegalReasons",
    "HTTPUnprocessableEntity",
    "HTTPUnsupportedMediaType",
    "HTTPUriTooLong",
    "HTTPVersionNotSupported",
    "MediaMalformedError",
    "MediaNotFoundError",
    "OperationNotAllowed",
    "PayloadTypeError",
    "UnsupportedError",
    "UnsupportedScopeError",
    "WebSocketDisconnected",
    "WebSocketHandlerNotFound",
    "WebSocketPathNotFound",
    "WebSocketServerError",
)


class NoRouteName(Exception):
    """when a router's name has not been specified"""


class NoFunctionSpecified(Exception):
    """when a router's function has not been specified"""


class RouteAlreadyExists(Exception):
    """when a router is repeated"""


class MethodNotAvailable(Exception):
    """this is triggered when a method is not avaiable for a route"""


class ErrorCodeExists(Exception):
    """When a error code (like 404) is repeated"""


class CustomBaseException(Exception):
    """Error used for server errors like 500 or 404"""


class VariableIsConstant(Exception):
    """Thrown when a variable is a constant and user tryes to change it."""
