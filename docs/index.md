<div class="badges">
    <a href="http://travis-ci.org/danpoland/drf-reverse-proxy">
        <img src="https://travis-ci.org/danpoland/drf-reverse-proxy.svg?branch=master">
    </a>
    <a href="https://pypi.python.org/pypi/drf-reverse-proxy">
        <img src="https://img.shields.io/pypi/v/drf-reverse-proxy.svg">
    </a>
</div>

---

# drf-reverse-proxy

Reverse proxy view for Django Rest Framework

---

## Overview

Reverse proxy view for Django Rest Framework

## Requirements

* Python (2.7, 3.3, 3.4)
* Django (1.6, 1.7)

## Installation

Install using `pip`...

```bash
$ pip install drf-reverse-proxy
```

## Example

TODO: Write example.

## Testing

Install testing requirements.

```bash
$ pip install -r requirements.txt
```

Run with runtests.

```bash
$ ./runtests.py
```

You can also use the excellent [tox](http://tox.readthedocs.org/en/latest/) testing tool to run the tests against all supported versions of Python and Django. Install tox globally, and then simply run:

```bash
$ tox
```

## Documentation

To build the documentation, you'll need to install `mkdocs`.

```bash
$ pip install mkdocs
```

To preview the documentation:

```bash
$ mkdocs serve
Running at: http://127.0.0.1:8000/
```

To build the documentation:

```bash
$ mkdocs build
```