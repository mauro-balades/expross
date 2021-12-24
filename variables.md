# Variables

**Expross variables can contain a name, a value, or a constant value. The way you would add a new variable would be:**

```python
app = Expross()

app.set_var("Hello", "world")
print(app.get_var("hello") # Get a variable
```

Variables in Expross can also be constant (which means that they can't be changed)

```python
app = Expross()

app.set_var("Hello", "world", True)
app.set_var("Hello", "can't change") # Error, can't change a constant
```
