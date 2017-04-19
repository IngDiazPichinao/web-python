from flask    import render_template
from datetime import datetime

from .querys import Query


def tareas_ticket(tarea):
    order_number, line_number = tarea.split('-')

    q      = Query()
    ticket = q.query_update(order_number, line_number)

    ticket.date = datetime.now().strftime('%A %d %b %y')
    ticket.time = datetime.now().strftime('%H:%M %p')

    return render_template(
        "informe_tareas_ticket.html",
        tarea=ticket,
        title="Ticket Print"
    )
