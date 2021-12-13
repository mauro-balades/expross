---
description: 'You can do diferent responses like: xml, html, json, ...'
---

# ✍ Different responses

## How to make different responses

### Simple function return

Expross auto-detects whether the response is gonna be html or json

```python
def main():
    return "<h1>Hello, world!</h1>"
    
def json():
    return {"hello": "world"}

app.get("/json", json)
app.get("/", main)
```

### Class return

```python
class html():
    # ...


class json():
    # ...


class xml():
    # ...


class text():
    # ...


class csv():
    # ...


class zip():
    # ...


class pdf():
    # ...

# And more comming!
```

To make a class return, you can just initiate it with some content, for example:

```python

def main():
    return xml("...")
    
app.get("/", main)
    
```
