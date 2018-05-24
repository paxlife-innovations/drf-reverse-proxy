"""
Settings for drf-reverse-proxy are all namespaced in the DRF_REVPROXY setting.
In your project's `settings.py` file you might have something like this:

DRF_REVPROXY = {
    'MIN_STREAMING_LENGTH': 4 * 1024
}

This module provides the `settings` object, that is used to access
drf-reverse-proxy settings, checking for user settings first, then falling
back to the defaults.
"""

from django.conf import settings
from django.test.signals import setting_changed


DEFAULTS = {
    # Variable used to represent a minimal content size required for response
    # to be turned into stream
    'MIN_STREAMING_LENGTH':
    4 * 1024,  # 4 KB

    'DEFAULT_CHARSET':
    # Default from HTTP RFC 2616
    # See: http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.7.1
    'latin-1',

    # List containing string constants that are used to represent headers
    # that can be ignored in the required_header function
    'IGNORE_HEADERS': (
        # We want content to be uncompressed so we remove
        # the Accept-Encoding from original request
        'HTTP_ACCEPT_ENCODING',
        'HTTP_HOST',
        'HTTP_REMOTE_USER',
    ),

    # string constants that represent possible html content types
    'HTML_CONTENT_TYPES': (
        'text/html',
        'application/xhtml+xml',
    ),

    # Default number of bytes that are going to be read in a file lecture
    'DEFAULT_AMT':
    2 ** 16,
}


class Config(object):
    """
    A config object, allowing config to be accessed as properties.
    For example:
        from drfreverseprovy.conf import conf
        print(conf.DEFAULT_CHARSET)
    """
    def __init__(self, user_config=None, defaults=None):
        self.defaults = defaults or DEFAULTS
        self._user_config = user_config
        self._cached_attrs = set()

    @property
    def user_config(self):
        if self._user_config is None:
            self._user_config = getattr(settings, 'DRF_REVPROXY', {})
        return self._user_config

    def __getattr__(self, attr):
        # all valid user settings have defaults
        if attr not in self.defaults:
            raise AttributeError("Invalid DRF_REVPROXY setting: '%s'" % attr)

        try:
            # Check if present in user settings
            val = self.user_config[attr]
        except KeyError:
            # Fall back to defaults
            val = self.defaults[attr]

        # Cache the result
        self._cached_attrs.add(attr)
        setattr(self, attr, val)
        return val

    def reload(self):
        for attr in self._cached_attrs:
            delattr(self, attr)
        self._cached_attrs.clear()
        if hasattr(self, '_user_config'):
            delattr(self, '_user_config')


conf = Config(None, DEFAULTS)


def reload_conf(*args, **kwargs):
    setting = kwargs['setting']
    if setting == 'DRF_REVPROXY':
        conf.reload()


setting_changed.connect(reload_conf)
