drf-reverse-proxy
======================================

[![pypi-version]][pypi]
[![build-status-image]][travis]

Overview
--------

This is a Django REST Framework port of the excellent django-revproxy (https://github.com/TracyWebTech/django-revproxy) library.

This port allows you to reverse proxy HTTP requests while still utilizing DRF
features such as authentication, permissions and throttling.

This library works exactly like the django-revproxy library, except that it 
allwos for some configuration. The documentation for django-revproxy can be
found at: http://django-revproxy.readthedocs.org/


Features
---------

* Proxies all HTTP methods: HEAD, GET, POST, PUT, DELETE, OPTIONS, TRACE, CONNECT and PATCH
* Copy all http headers sent from the client to the proxied server
* Copy all http headers sent from the proxied server to the client (except `hop-by-hop <http://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html#sec13.5.1>`_)
* Basic URL rewrite
* Handles redirects
* Few external dependencies
* Maintains the usability of DRF features like authentication, permissions and throttling.


Requirements
------------

-  Python (2.7, 3.3, 3.4, 3.5)
-  Django (1.8, 1.9, 1.10)
-  Django REST Framework (3.3, 3.4, 3.5)

Installation
------------

Install using ``pip``\ …

```bash
$ pip install drf-reverse-proxy
```

Example
-------

Create a custom reverse proxy view:

```python
from drfreverseproxy import ProxyView

class TestProxyView(ProxyView):
   upstream = 'http://example.com'
```

Or just use the default:

```python
from drfreverseproxy import ProxyView

urlpatterns = [
   url(r'^(?P<path>.*)$', ProxyView.as_view(upstream='http://example.com/')),
]
```

Configuration
-------------

Here's a Django settings file snippet illustrating the available settings with their
default values:

```python
[…]
 
DRF_REVPROXY = {
  'MIN_STREAMING_LENGTH': 4 * 1024,  # 4 KB
  'DEFAULT_CHARSET': 'latin-1',
  'IGNORE_HEADERS': (
      'HTTP_ACCEPT_ENCODING',
      'HTTP_HOST',
      'HTTP_REMOTE_USER',
  ),
  'HTML_CONTENT_TYPES': (
      'text/html',
      'application/xhtml+xml',
  ),
  'DEFAULT_AMT': 2 ** 16, # 64 KB
}
 
[…]
```

For many use cases, you might be fine just using these default values.

### MIN_STREAMING_LENGTH

Minimum content length that should return a stream response, namely a
 `django.http.StreamingHttpResponse` object (which might be preferable e.g. for
 transferring large files). Default value is 4096 (4KB).  
Set this to `None` to disable the stream repsonse option altogether and always return a
`django.http.HttpResponse`.

### DEFAULT_CHARSET

Default charset to be used if the `Content-Type` header doesn't indicate any. 

### IGNORE_HEADERS

An iterable (tuple or list) containing header names that don't have to be
normalized for the outgoing request. By default, all headers from the request
object that are prefixed with `HTTP_` as well as the `CONTENT-TYPE` are
normalized, unless they are listed here.

### HTML_CONTENT_TYPES

An iterable (tuple or list) containing content types that should be considered
valid types for HTML.

### DEFAULT_AMT

The amount of data to be read with each iteration from a streamed response. The
actual amount of data returned might be less, e.g. when using compressed data.
For further details refer to the [urllib3 docs](https://urllib3.readthedocs.io/en/latest/reference/index.html?highlight=httpresponse#urllib3.response.HTTPResponse.stream).

[build-status-image]: https://travis-ci.org/danpoland/drf-reverse-proxy.svg?branch=master
[travis]: https://travis-ci.org/danpoland/drf-reverse-proxy
[pypi-version]: https://img.shields.io/pypi/v/drf-reverse-proxy.svg
[pypi]: https://pypi.python.org/pypi/drf-reverse-proxy
