---
description: 'Here, we will show you how to serve static files'
---

# 📦 Serve static folders

## How to serve a static folder

You will need to create your static folder \(example: `public`, `static`\) 

```
public/
  ├── style.css
  └── script.js
app.py
```

{% hint style="warning" %}
 Folder can be named as you whant.
{% endhint %}

Once you have your static files, you can do the following at the top of your python script:

```python

# ...

app = Expross()

app.serve_static(
    route="Your route" # should start with '/' (http://localhost:8000/{{YOUR ROUTE}})
    folder="./public" # Or what ever you named it    
)

# ...

```

### Now what?

* Once you have complete it, you can start the server and go to that route you have written inside the `route` parameter.

