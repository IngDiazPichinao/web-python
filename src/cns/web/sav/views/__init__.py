from .home          import home
from .inventory     import inventory
from .scheduling    import (
    orders,
    update_date,
    update_production,
    update_impregnado,
    update_observation,
    update_status,
    update_quality
)
from .orders_ticket import tareas_ticket
from .login         import login, logout

__all__ = [
    'home',
    'inventory',
    'orders',
    'update_date',
    'update_production',
    'update_impregnado',
    'update_observation',
    'update_status',
    'update_quality',
    "tareas_ticket",
    'login',
    'logout'
]
