from sqlalchemy     import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from cns.orm import CommonBase

base = CommonBase


class Connection(object):

    def __init__(self):
        self._engine  = None
        self._session = None

    @property
    def session(self):
        if not self._session:
            sess_maker    = sessionmaker(bind=self._engine)
            self._session = scoped_session(sess_maker)

        return self._session

    def connect_postgresql(self, url, echo=False):
        url                = 'postgresql+psycopg2://{url}'.format(url=url)
        self._engine       = create_engine(url, echo=echo)
        base.metadata.bind = create_engine


connection = Connection()
