"""
Usage:
    cns-web-sav --config <path>
                [--listen-address <addr> --listen-port <port>]
                [--db-user <user> --db-passwd <passwd> --db-host <host> --db-port <port>  ]
                [--db-name <db>]
                [--debug]


Options:
    -c --config <path>         # Path to configuratio file [default: /etc/cns/cns-daemon-sav.yml]

    --listen-address <addr>    # Address to listen on [default: 0.0.0.0]
    --listen-port <port>       # Port to listen on [default: 4446]

    --db-host <host>           # pgSQL Database Host
    --db-port <port>           # pgSQL Database Port
    --db-user <user>           # pgSQL Database User
    --db-passwd <passwd>       # pgSQL Database User Password
    --db-name <db>             # pgSQL Database Name

"""

import os
import docopt

from flask  import Flask

from . import __version__
from . import views

from .database import connection
from .config   import Config

DATABASE = 'database'

app = Flask(
    'sav',
    static_folder   = 'static',
    template_folder = 'templates'
)

app.root_path = os.path.abspath(os.path.dirname(__file__))


app.add_url_rule('/',     'login', views.login, methods=['POST', 'GET'])
app.add_url_rule('/home', 'home',  views.home,  methods=['POST', 'GET'])

app.add_url_rule('/inventory', 'inventory', views.inventory)
app.add_url_rule('/orders',    'orders',    views.orders)

app.add_url_rule('/tareas_ticket/<tarea>', 'tareas_ticket', views.tareas_ticket, methods=['GET'])

app.add_url_rule('/update_date',        'update_date',        views.update_date,        methods=['POST'])
app.add_url_rule('/update_production',  'update_production',  views.update_production,  methods=['POST'])
app.add_url_rule('/update_impregnado',  'update_impregnado',  views.update_impregnado,  methods=['POST'])
app.add_url_rule('/update_observation', 'update_observation', views.update_observation, methods=['POST'])
app.add_url_rule('/update_status',      'update_status',      views.update_status,      methods=['POST'])
app.add_url_rule('/update_quality',     'update_quality',     views.update_quality,     methods=['POST'])

app.add_url_rule('/logout', 'logout', views.logout)


def setup_database(user, passwd, host, port, db):
    connstr = '{user}:{passwd}@{host}:{port}/{db}'.format(
        user   = user,
        passwd = passwd,
        host   = host,
        port   = port,
        db     = db
    )

    connection.connect_postgresql(connstr)


def setup_app(host='0.0.0.0', port='4446', debug=True, run=True):
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        connection.session.remove()

    if run:
        app.run(host=host, port=port, debug=debug)
    else:
        return app


def main():
    args = docopt.docopt(__doc__, version=__version__, help=True)

    setup_database(
        user   = args['--db-user'],
        passwd = args['--db-passwd'],
        host   = args['--db-host'],
        port   = int(args['--db-port']),
        db     = args['--db-name']
    )

    setup_app(
        host  = args['--listen-address'],
        port  = int(args['--listen-port']),
        debug = args['--debug']
    )

    return data

if __name__ == '__main__':
    main()
else:

    args = docopt.docopt(__doc__, help=True)

    data = Config(args, args['--config'])

    db_user   = data.user
    db_passwd = data.passwd
    db_host   = data.host
    db_port   = data.port
    db_name   = data.bd

    setup_database(db_user, db_passwd, db_host, db_port, db_name)
    app = setup_app(run=False)
