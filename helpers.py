"""
Contains helper methods used for creating app. The idea behind storing it here instead of
in main.py file is to provide logical separation between creation an app for development,
production and tests.
"""
from flask import Flask

from urls import REGISTERED_URLS


def register_urls(app, urls):
    for url in urls:
        app.add_url_rule(url['rule'], url['endpoint'], url['view_func'])


def create_app():
    production_app = Flask(__name__)
    register_urls(production_app, REGISTERED_URLS)
    return production_app