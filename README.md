---
description: This are the official documents for Expross
---

# 🌟 Expross



Expross is a lightweight web server to introduce JavaScript developers familiar with Express to Python.\
[**Explore the docs »**](https://mauro-balades.gitbook.io/expross/)\
\
[Example app](https://mauro-balades.gitbook.io/expross/geting-started/basic-ussage) · [Report Bug](https://github.com/mauro-balades/expross/issues) · [Request Feature](https://github.com/mauro-balades/expross/pulls)

### About The Project

Theres a lot of people that work with express.js and they whant to change to python for many diferent reasons. That is why Expross it created. To give web development from express.js users a nice and clean introduction to web development in python.

Here's why:

* Function names are very similar to express.js
* It is faster than other web frameworks
* Secure and continuesly maintained :smile:

Of course, this is not a perfect project but. We have shown people with no idea of web development for python how to use this framework. They said it is the most easy framework to learn because it's similarities with express.js

### Getting Started

Here, we will show you how easy is to run a web server in expros To get a local copy up and running follow these simple example steps.

#### Prerequisites

You will need to install the package (obviously) with `pip3` and run the application with `python3` (wich normally comes with pip3 integrated).

#### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Install Expross

```
pip3 install Expross
```

... is that simple

### Usage

This is an example of a hello world with Expross

```python
# Import expross with capital leter
from expross import Expross

app = Expross()

@app.get("/")
def main():
  return "<h1>Hello, world!</h1>"

app.listen() # Can include a host name and port
```

* then, run `python3 [file].py`

That is all....

_For more examples, please refer to the Documentation_

### Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### License

Distributed under the MIT License. See `LICENSE.md` for more information.

### Contact

Mauro Baladés - [mauro.balades@tutanota.com](mailto:mauro.balades@tanota.com)

Project Link: [https://github.com/mauro-balades/expross/](https://github.com/mauro-balades/expross/)
