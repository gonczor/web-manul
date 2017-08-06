from views.index import index


def register_urls(app):
    app.add_url_rule('/', 'index', index)
    return app
