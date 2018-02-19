from .settings import db_config, db_loggs
from sqlalchemy import inspect, create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session, mapper


class DbProxy(object):

    # Initialization db configurations
    def __init__(self):
        self._init_engine(uri='postgresql://{}:{}@{}:{}/{}'.format(*db_config),
                          echo=db_loggs)
        self._init_db()
        self.metadata = MetaData()

    def _init_engine(self, uri, **kwargs):
        self.engine = create_engine(uri, **kwargs)

    def _init_db(self):
        self.session = scoped_session(sessionmaker(bind=self.engine))
        Base.metadata.create_all(self.engine)
