""" Scheduling of Production Tasks (for now just display of orders).
"""
from cns.web.sav.database import connection
from .querys import Query

from flask      import render_template, request, abort
from sqlalchemy import func
from datetime   import datetime


def update_date():
    # Tareas_ajax
    if request.method == 'POST':
        if request.form['id'] == 'date_delivery_eta':
            order_number, line_number = request.form['tarea'].split('-')
            value = request.form['value']

        if value == '____-__-__':
            fechaentrega = None
        else:
            try:
                fechaentrega = datetime.strptime(value, '%Y-%m-%d')
            except ValueError:
                return abort(400)

        q   = Query()
        row = q.query_update(order_number, line_number)

        if row.status not in ('Finalizado', 'Despachado'):
            row.date_delivery_eta = fechaentrega
            connection.session.commit()
        else:
            return abort(403)

        if fechaentrega is None:
            return ''
        else:
            return datetime.strftime(fechaentrega, "%Y-%m-%d")
    return abort(400)


def update_production():
    if request.method == 'POST':
        if request.form['id'] in ('program_saving', 'program_finishing'):
            order_number, line_number = request.form['tarea'].split('-')
            value = request.form['value']

            q   = Query()
            row = q.query_update(order_number, line_number)

            if request.form['id'] == 'program_saving':
                row.program_saving = value
            elif request.form['id'] == 'program_finishing':
                row.program_finishing = value
            else:
                return abort(500)

            session = connection.session()
            session.commit()

            if request.form['id'] == 'program_saving':
                return row.program_saving
            if request.form['id'] == 'program_finishing':
                return row.program_finishing
            else:
                return abort(500)
        return abort(400)
    return abort(400)


def update_observation():
    if request.method == 'POST':
        if request.form['id'] == 'observations':
            order_number, line_number = request.form['tarea'].split('-')
            value = request.form['value']

            q   = Query()
            row = q.query_update(order_number, line_number)

            row.observations = value

            session = connection.session()

            session.commit()
            return row.observations


def update_impregnado():
    if request.method == 'POST':
        if request.form['id'] == 'impregnated':
            order_number, line_number = request.form['tarea'].split('-')
            value = request.form['value']

            q   = Query()
            row = q.query_update(order_number, line_number)

            trans = {'true': True, 'false': False}
            if value in trans:
                row.impregnated = trans[value]
            else:
                return abort(400)

            session = connection.session()
            session.commit()

            return 'true' if row.impregnated else 'false'
    return abort(400)


def update_status():
    if request.method == 'POST':
        if request.form['id'] == 'status':
            order_number, line_number = request.form['tarea'].split('-')
            value = request.form['value']

            codes = {
                'null': None,
                'ase' : 'Aserrío',
                'aso' : 'Aserrado',
                'sec' : 'Secado',
                'asi' : 'Asignado',
                'imp' : 'Impregnando',
                'fin' : 'Finalizado',
                'des' : 'Despachado',
                'sus' : 'Suspendido',
                'anu' : 'Anulada'
            }

            for key in codes.keys():
                if key in codes:
                    value = codes[value]

                q   = Query()
                row = q.query_update(order_number, line_number)

                old_state  = row.status
                row.status = value

                if value == 'Finalizado':
                    row.date_delivery_eta = func.current_timestamp()
                elif old_state == 'Despachado' and value != 'Despachado':
                    row.date_delivery_eta = None

                session = connection.session()
                session.commit()

                if row.status is None:
                    return ''
                else:
                    return row.status
            else:
                return abort(400)
    return abort(400)


def update_quality():
    if request.method == 'POST':
        if request.form['id'] == 'quality_enum':
            order_number, line_number = request.form['tarea'].split('-')
            value = request.form['value']

            codes = {
                "null" : None,
                "00": "0-1",
                "01": "1-2",
                "02": "2-2",
                "03": "3-3",
                "04": "1-2",
                "05": "2-2",
                "06": "9-9"
            }

            for key in codes.keys():
                if key in codes:
                    value = codes[value]

                q   = Query()
                row = q.query_update(order_number, line_number)

                row.quality_enum = value

                session = connection.session()
                session.commit()

                if row.quality_enum is None:
                    return ""
                else:
                    return row.quality_enum
            else:
                return abort(400)
    return abort(400)


def orders():
    q      = Query()
    result = q.query()

    return render_template(
        "orders.html",
        title = "Ordenes",
        rows  = result
    )
