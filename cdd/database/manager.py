import os
import configparser
import psycopg2

import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.orm import scoping

from cdd.database.models import Stocks

class DBManager(object):
    def __init__(self):
        # Rota configurada para a base no docker           
        # self.connection = 'postgresql+psycopg2://dev:dev@localhost:5432/cdd_controller'
        
        # Rota Local
        # self.connection = 'postgresql+psycopg2://postgres:R@posinh@1@localhost:5432/cdd_controller'

        # Rota configurada para a base do heroku
        self.connection = 'postgresql+psycopg2://nmonwnodnkydnb:137c1c8d1013754f50de8ce05e22b3f096c3d830ac64f417c2e7e67867d1afff@ec2-52-1-115-6.compute-1.amazonaws.com:5432/dbt159vt4r4duk'
        
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
