---
description: Get a route depending on the function's name
---

# ♻ url for

## How to use it

It is very easy to use it, you just need to follow this instructions:

* Create a function with a route
* then you can do `app.url_for("function_name")`&#x20;
  * This will return the route for that function

```python

app = Expross()

def main():
    return app.url_for("other_route")  # /test

def other_route():
    return "Hi!"

app.get("/test", other_route)
app.get("/", main)
app.listen()
```

{% hint style="warning" %}
If the function is not found or route is not set, it will return `None`
{% endhint %}
