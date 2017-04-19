""" Server for "Aserradero Produccion".
"""
import os.path as ospath

from flask import Blueprint

from cns.web import LoadingTemplate

templates = []


def main():
    bp = Blueprint('sav', 'production',
                   static_folder='static',
                   template_folder='templates')
    bp.root_path = ospath.abspath(ospath.dirname(__file__))

    from .views import home, inventory, orders
    bp.add_url_rule('/',          view_func=home,      methods=['GET'])
    bp.add_url_rule('/inventory', view_func=inventory, methods=['GET'])
    bp.add_url_rule('/orders',    view_func=orders,    methods=['GET'])

    templates.append(LoadingTemplate(bp, url_namespace='sav'))

# Externalized as entry point (setuptools)
main()
