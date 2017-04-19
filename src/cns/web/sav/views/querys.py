from cns.web.sav.database import connection
from cns.web.sav.helpers  import dictify_sqla_object
from cns.orm.sav          import ProductionOrder, ConstQuality
from sqlalchemy           import and_


class Query(object):

    def __init__(self):
        self.session = connection.session()
        self._list   = []
        self.clean   = "----"
        self.t       = "Si"
        self.n       = "No"

    def query(self):
        for obj in self.session.query(ProductionOrder).all():
            d = dictify_sqla_object(obj)

            for key in d.keys():
                if d[key] is True:
                    d[key] = self.t
                if d[key] is False:
                    d[key] = self.n
                if d['quality_side_first'] == 1:
                    d['quality_side_first'] = "1era"
                if d['quality_side_first'] == 2:
                    d['quality_side_first'] = "2da"
                if d['quality_side_first'] == 0:
                    d['quality_side_first'] = "SN"

            self._list.append(d)

        return self._list

    def query_update(self, number, line):
        query = self.session.query(ProductionOrder).filter(
            and_(
                ProductionOrder.order_number == number,
                ProductionOrder.line_number  == line
            )
        )
        row = query.one()
        return row

    def query_quality(self, value):
        query = self.session.query(ConstQuality).filter(
            ConstQuality.side_first == value
        )

        quality = query.one()

        return quality
