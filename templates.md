---
description: How to use and implement templates
---

# 🛕 Templates

## Defining templates folder

If you whant to use templates, you can store them in a folder. By default, this folder will be in `templates`

```python
app = Expross(
    # Can define folders templates here
    templates = "your folder"
)

# Or here
app.set_templates("your folder")
```

{% hint style="info" %}
&#x20;By default, this folder will be called `templates`
{% endhint %}

## Render a template

You can render a jinja template, by giving it context

```python

def main():
    return render_template('users.html', users={...})
    
app.get("/", main)

```

{% code title="templates/users.html" %}
```markup
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8" />
    <title></title>
  </head>
  <body>
    {% for user in users %}
      {{ user }}
    {% endfor %}
  </body>
</html>
```
{% endcode %}

{% hint style="info" %}
&#x20;You can add a parameter to make this a minified version of it

**NOTE:** It also minifies CSS, js inside this file and tags like `pre` or `code` won't be minified. This would be an example response:

```python

def main():
    return render_template('users.html', users={...}, _minified=True)
    
app.get("/", main)

```

{% code title="templates/users.html" %}
```markup
<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8" /><title>...</title></head><body>...</body></html>
```
{% endcode %}
{% endhint %}

## Render a string template

You can render a jinja string template, by giving it context and it also supports jinja2

```python

def main():
    return render("Hello {{ user }}", user="programmer")
    
app.get("/", main)
```
