from views.index import index
"""
Contains REGISTERED_URLS constant with urls used by app in a form of tuple consisting of dict with
parameters accepted by flask's add_url_rule
"""

REGISTERED_URLS = (
    {'rule': '/', 'endpoint': 'index', 'view_func': index}
)
