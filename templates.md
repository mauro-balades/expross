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
 By default, this folder will be called `templates`
{% endhint %}

## Render a template

You can render a template, by giving it context

```python

app.get("/")
def main():
    return render_template('users.html', users={...})

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
 This templates support [jinja 2](https://jinja2docs.readthedocs.io/en/stable/)
{% endhint %}

## Render a string template

You can render a string template, by giving it context and it also supports jinja2

```python

app.get("/")
def main():
    return render("Hello {{ user }}", user="programmer")
```

