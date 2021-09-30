---
description: 'You can do diferent responses like: xml, html, json, ...'
---

# ✍ Different responses

## How to make different responses

### HTML response

To make a simple HTML response, you simply need to return a string:

```python

html = """
<html>
    <body>
        <h1>Hello world!</h1>
    </body>
</html>
"""

@app.route("/")
def main():
    return html
```

{% hint style="info" %}
Alternatively, you can make a HTMLResponse using the following class:

```python

from expross import HTMLResponse

# ... 

html = """
<html>
    <body>
        <h1>Hello world!</h1>
    </body>
</html>
"""

@app.route("/")
def main():
    return HTMLResponse(html)
```
{% endhint %}

### JSON response

To make a JSON response, you need to return a dictionary:

```python

@app.route("/")
def main():
    return {"hello": "world"}
    
```

{% hint style="info" %}
Alternatively, you can make a JSONResponse using the following class:

```python

from expross import JSONResponse

# ... 

@app.route("/")
def main():
    return JSONResponse({"hello": "world"})
```
{% endhint %}

### XML response

To make a XML response, you need to return a XMLResponse class:

```python

from expross import XMLResponse

# ... 

html = """<?xml version="1.0" encoding="UTF-8"?>
<breakfast_menu>
<food>
    <name>Belgian Waffles</name>
    <price>$5.95</price>
    <description>
   Two of our famous Belgian Waffles with plenty of real maple syrup
   </description>
    <calories>650</calories>
</food>
<food>
    <name>Strawberry Belgian Waffles</name>
    <price>$7.95</price>
    <description>
    Light Belgian waffles covered with strawberries and whipped cream
    </description>
    <calories>900</calories>
</food>
<food>
    <name>Berry-Berry Belgian Waffles</name>
    <price>$8.95</price>
    <description>
    Belgian waffles covered with assorted fresh berries and whipped cream
    </description>
    <calories>900</calories>
</food>
<food>
    <name>French Toast</name>
    <price>$4.50</price>
    <description>
    Thick slices made from our homemade sourdough bread
    </description>
    <calories>600</calories>
</food>
<food>
    <name>Homestyle Breakfast</name>
    <price>$6.95</price>
    <description>
    Two eggs, bacon or sausage, toast, and our ever-popular hash browns
    </description>
    <calories>950</calories>
</food>
</breakfast_menu>
"""

@app.route("/")
def main():
    return XMLResponse(xml)
    
```

