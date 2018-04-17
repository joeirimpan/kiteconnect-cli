# -*- coding: utf-8 -*-
"""
    cli.py
    :copyright: (c) 2018 by Joe Paul.
    :license: see LICENSE for details.
"""
import os
import json
import time
import webbrowser
import argparse

from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound, abort
from werkzeug.serving import run_simple
from kiteconnect import KiteConnect


class KiteConnectApp(object):

    def __init__(self, api_key, api_secret, redirect_path):
        self.url_map = Map([
            Rule('/%s' % redirect_path, endpoint='authorize')
        ])
        self.api_key = api_key
        self.api_secret = api_secret
        self.access_token = None

    @property
    def kite_client(self):
        """Returns a kite client object"""
        kite = KiteConnect(api_key=self.api_key)
        if self.access_token:
            kite.set_access_token(self.access_token)
        return kite

    def on_authorize(self, request):
        request_token = request.args.get("request_token")
        data = self.kite_client.generate_session(
            request_token,
            api_secret=self.api_secret
        )
        self.access_token = data["access_token"]
        print "ACCESS_TOKEN: %s" % self.access_token
        return Response(json.dumps({"access_token": self.access_token}))

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, 'on_' + endpoint)(request, **values)
        except NotFound, e:
            return abort(404)
        except HTTPException, e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


class KiteConnectCLI(argparse.ArgumentParser):
    info = ({
        'prog': 'kiteconnect-cli',
        'description': 'Starts a local server to handle kiteconnect auth',
    })

    def __init__(self):
        super(KiteConnectCLI, self).__init__(**self.info)

        self.add_argument(
            'api_key', type=str, help='KiteConnect API KEY'
        )
        self.add_argument(
            'api_secret', type=str, help='KiteConnect API SECRET'
        )
        self.add_argument(
            'redirect_path', type=str, help='KiteConnect redirect path'
        )
        self.add_argument(
            '-p', '--port', type=int,
            default=8080, dest='port', help='auth calback port'
        )

    def run(self, args=None):
        webbrowser.open(
            "https://kite.trade/connect/login?api_key=%s&v=3" %
            args.api_key
        )
        app = KiteConnectApp(args.api_key, args.api_secret, args.redirect_path)
        run_simple('localhost', args.port, app)


def cli_execute():
    cli = KiteConnectCLI()
    cli.run(cli.parse_args())


if __name__ == '__main__':
    cli_execute()
