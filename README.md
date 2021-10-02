# Expross

Expross is a lightweight web server to introduce JavaScript developers familiar with [Express](http://expressjs.com) to Python.

### Instalation

To install `Expross`, you will need to have the following requirements:

* pip3
* [python3](https://python.org)

To install `Expross` you can do it by entering the follow commands in your command prompt.

```
$ pip3 install expross
```

### Basic usage

Here's an example of how to use Expross:

```python
# Import expross with capital leter
from expross import Expross

app = Expross()

@app.get("/")
def main():
  return "<h1>Hello, world!</h1>"

app.listen() # Can include a host name and port
```

### Documentation

* You can follow the documentation [here](https://mauro-balades.gitbook.io/expross/)

### License

```
The MIT License (MIT)

Copyright (c) 2021 expross

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
