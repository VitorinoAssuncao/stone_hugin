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
            'value': self.stock_value,
            'average': 0
        }

    @classmethod
    def get_list(cls,session):
        '''Funcao responsavel por retornar a listagem completa de Estoque (Stocks) do banco. Recebe respectivamente a classe de estoque (Stocks) e a sessao atual.'''
        models = []

        with session.begin():
            query = session.query(cls)
            query = query.order_by(cls.stock_id)
            models = query.all()
        
        return models

    @classmethod
    def get_stocks_by_id(cls,session,value):
        '''Funcao responsavel por retornar responsavel por retornar os dados de um estoque individual, recebe como chave o ID (stock_id).'''
        models = []
        with session.begin():
            query = session.query(cls)
            models  = query.filter_by(stock_id=value).first()        
        return models

    def save(self,session):
        '''Funcao responsavel por salvar os dados a serem adicionados, recebendo os novos dados (self) e a sessao atual.'''     
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
    '''Funcao responsavel por retornar a listagem completa de Chamados (Tickets) do banco. Recebe respectivamente a classe de chamado (Ticket) e a sessao atual.'''
        models = []
        with session.begin():
            query = session.query(cls)
            models = query.all()        
        return models

    @classmethod
    def get_all_base_tickets(cls,session,value):
    '''Funcao responsavel por retornar a listagem completa de Chamados (Tickets) do banco de uma respectiva unidade (CDD). Recebe respectivamente a classe de chamado (Ticket), a sessao atual e o valor do nome do cdd (ticket_base) para pesquisa.'''
        models = []
        with session.begin():
            query = session.query(cls)
            models  = query.filter_by(ticket_base=value.upper()).order_by(cls.ticket_date).all()        
        return models

    @classmethod
    def get_total_of_tickets(cls,session,value):
    '''Funcao responsavel por trazer a quantidade de chamados ao todo referente aquela unidade.'''
        models = []
        with session.begin():
            query = session.query(cls)
            query  = query.filter_by(ticket_base=value.upper())
            models = query.count()       
        return models

    @classmethod
    def get_distinct_count_dates_on_tickets(cls,session,value):
    '''Funcao responsavel por trazer a quantidade de dias nos quais foram atendidos chamados para a unidade em questao'''
        models = []
        with session.begin():
            query = session.query(cls)
            query  = query.filter_by(ticket_base=value.upper())
            query = query.distinct(cls.ticket_date)
            models = query.count()
        return models

    def save(self,session):
        '''Funcao responsavel por salvar os dados a serem adicionados, recebendo os novos dados (self) e a sessao atual.'''     
        with session.begin():
            session.add(self)