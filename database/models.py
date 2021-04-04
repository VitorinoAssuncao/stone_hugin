from sqlalchemy import Date,func
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class Stocks(BaseModel):
    __tablename__ = 'stocks'
    stock_id = sa.Column(sa.Integer,primary_key=True)
    stock_base = sa.Column(sa.String,nullable=False)
    stock_value = sa.Column(sa.Integer,nullable=False)

    def __init__(self,**args):
        super(Stocks,self).__init__(**args)

    def serialize(self) -> dict:
        return {
            'id' : self.stock_id,
            'base': self.stock_base,
            'value': self.stock_value
        }

    @classmethod
    def get_list(cls,session):
        models = []

        with session.begin():
            query = session.query(cls)
            models = query.all()
        
        return models

    @classmethod
    def get_stocks_by_id(cls,session,value):
        models = []
        with session.begin():
            query = session.query(cls)
            models  = query.filter_by(stock_id=value).first()        
        return models

    def save(self,session):
        with session.begin():
            session.add(self)

class Tickets(BaseModel):
    __tablename__ = 'tickets'
    ticket_id = sa.Column(sa.Integer,primary_key=True)
    ticket_date = sa.Column(sa.Date,nullable=False)
    ticket_base = sa.Column(sa.String,nullable=False)
    ticket_country_state = sa.Column(sa.String,nullable=False)
    ticket_consumption = sa.Column(sa.Integer,nullable=False)

    def __init__(self,**args):
        super(Tickets,self).__init__(**args)

    def serialize(self) -> dict:
        return {
            'id' : self.ticket_id,
            'date' :  str(self.ticket_date),
            'base': self.ticket_base,
            'country_state': self.ticket_country_state,
            'consumption': self.ticket_consumption            
            }

    @classmethod
    def get_list(cls,session):
        models = []
        with session.begin():
            query = session.query(cls)
            models = query.all()        
        return models

    @classmethod
    def get_all_base_tickets(cls,session,value):
        models = []
        with session.begin():
            query = session.query(cls)
            models  = query.filter_by(ticket_base=value).order_by(cls.ticket_date).all()        
        return models

    def save(self,session):
        with session.begin():
            session.add(self)