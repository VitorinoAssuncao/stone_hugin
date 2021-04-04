import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.orm import scoping

from database.models import Stocks

class DBManager(object):
    def __init__(self,connection=None):
        self.connection = connection

        self.engine = sqlalchemy.create_engine(self.connection)
        self.DBSession = scoping.scoped_session(
            orm.sessionmaker(
                bind=self.engine,
                autocommit=True
            )
        )

    @property
    def session(self):
        return self.DBSession()
