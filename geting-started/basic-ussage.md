---
description: Instructions to create a basic app.
---

# 🚀 Basic usage

## Creating a basic expross application

To start creating a basic expross app, you will need to create a new python file

```bash
$ expross new my-app
$ cd my-app

# Not necesary
$ python3 -m venv venv
$ source venv/bin/activate
```

{% hint style="info" %}
&#x20;You can also simply make a python file with the following content
{% endhint %}

This is an example application

{% code title="app.py" %}
```python

from expross import Expross

app = Expross()

def main():
    return "<h1>Hello!</h1>"
    
app.get("/", main)
app.start()
```
{% endcode %}
