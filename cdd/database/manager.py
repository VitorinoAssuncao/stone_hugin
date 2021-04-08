import os
import configparser
import psycopg2

import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.orm import scoping

from cdd.database.models import Stocks

class DBManager(object):
    def __init__(self):
        self.connection = 'postgresql+psycopg2://dev:dev@localhost:5432/cddcontroler'
#        self.connection = 'postgresql+psycopg2://postgres:R@posinh@1@localhost:5432/cdd_controller'
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
