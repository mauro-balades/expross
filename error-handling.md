---
description: How to handle an error when thrown
---

# 🛑 Error handling

## Basic HTTP error handling

to error handle it is a very straight forward process:

{% code title="errors.py" %}
```python

from expross import HTTPNotFound

# ...

def error():
    return "ups! 404"
    
app.error(HTTPNotFound)
    
```
{% endcode %}

{% hint style="info" %}
&#x20;Errors must be a reference to the error class, you can have multiple error handling
{% endhint %}

Here is a complete list of all the errors:

```python
_errors = (
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
```

{% hint style="danger" %}
You cant have 2 error handlers with the same error, an exception with being raised
{% endhint %}
