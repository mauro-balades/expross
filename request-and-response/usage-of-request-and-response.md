# Usage of request and response

## How to access them

```python

def main():

    print(app.req)
    print(app.res)
    return "hey!", 200
    
app.get("/", main)

```

{% hint style="info" %}
&#x20;These classes can only be accessed when a route is being called
{% endhint %}
