---
description: Here, we show you how to make a redirect in Expross
---

# 🔗 Redirect

## Simple redirect

To make a redirect, you can just call the redirect function:

```python

def main():
    app.redirect("https://google.com")
    
app.get("/", main)

```

{% hint style="danger" %}
&#x20;Do not **ever** make an error handler for **HTTPFound**. This error is being raised so that we can feagure out when you whant a redirect.

An example of a **bad redirect usage**:

{% code title="bad_example.py" %}
```python

def bad():
    try:
        app.redirect("https://google.com") 
    except HTTPFound: # Do not ever do this
        pass
```
{% endcode %}
{% endhint %}

## Function definition

```python
def redirect(self, location: str):
    """Redirects to the specified location

    Args:
        location (str): Location to be redirected

    Raises:
        HTTPFound (depends on code): A Exception used to redirect user

        Note:
            Please do not do any error handling for this. This is an intentionally
            error to redirect the user.
    """
```
