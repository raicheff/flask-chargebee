#
# Flask-Chargebee
#
# Copyright (C) 2017 Boris Raicheff
# All rights reserved
#


import warnings

import chargebee

from flask import Response
from six.moves.http_client import OK


class Chargebee(object):
    """
    Flask-Chargebee

    Documentation:
    https://flask-chargebee.readthedocs.io

    API:
    https://apidocs.chargebee.com

    :param app: Flask app to initialize with. Defaults to `None`
    """

    def __init__(self, app=None, blueprint=None):
        if app is not None:
            self.init_app(app, blueprint)

    def init_app(self, app, blueprint=None):

        api_key = app.config.get('CHARGEBEE_API_KEY')
        site = app.config.get('CHARGEBEE_SITE')
        if not all((api_key, site)):
            warnings.warn('CHARGEBEE config not set', RuntimeWarning, stacklevel=2)
            return

        chargebee.configure(api_key, site)

        if blueprint is not None:
            blueprint.add_url_rule('/chargebee', 'chargebee', self.handle_webhook, methods=('POST',))

    def handle_webhook(self):
        return Response(status=OK)

    def __getattr__(self, name):
        return getattr(chargebee, name)


# EOF
