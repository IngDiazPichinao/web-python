import datetime


def dictify_sqla_object(sqla_object):
    devcols = [col for col in sqla_object.__table__.columns]
    devdict = {}

    for col in devcols:
        value = sqla_object.__getattribute__(col.name)

        if isinstance(value, datetime.datetime):
            value = str(value.timestamp())

        devdict[col.name] = value

    return devdict
