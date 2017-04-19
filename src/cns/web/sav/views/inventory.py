""" Views for displaying of the Inventory as provided (TEMP) by AHSE .
"""
from flask import g, render_template

from cns.orm.sav import InventoryTransfer


def inventory():
    db = g.db_ahse
    items       = InventoryTransfer.query(db.engine)
    consumption = InventoryTransfer.consumption(items, days=30)
    aggregated  = InventoryTransfer.aggregate(items)

    for hash_, row in consumption.items():
        aggregated[hash_].product_flow = row

    filter_correction = (obj for obj in aggregated.values() if obj.storage_id       != 18)
    filter_zeroed     = (obj for obj in filter_correction   if abs(obj.total_count) != 0)

    return render_template('inventory.html', items=filter_zeroed)
