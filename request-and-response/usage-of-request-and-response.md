# Usage of request and response

## How to access them

```python

@app.get("/")
def main():

    print(app.req)
    print(app.res)
    return "hey!", 200

```

{% hint style="info" %}
 This classes can only be accesed when a route is being called
{% endhint %}

