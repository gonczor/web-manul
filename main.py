import sys

from flask import Flask

from .urls import register_urls


def create_app():
    production_app = Flask(__name__)
    production_app = register_urls(production_app)
    return production_app


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            from .tests import runner
            runner.run()

    else:
        app = create_app()
        app.run(host='0.0.0.0')
