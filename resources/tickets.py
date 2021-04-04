import falcon
import json

from database.models import Tickets
from resources import BaseResource
from sqlalchemy.exc import IntegrityError

class TicketsCollection(BaseResource):
    def on_get(self,req,resp):
        ticket_list = Tickets.get_list(self.db.session)
        obj = [ticket.serialize() for ticket in ticket_list]        
        resp.status = falcon.HTTP_200
        resp.media = obj

    def on_post(self,req,resp):
        model = Tickets(
            ticket_date = req.media.get('date'),
            ticket_base = req.media.get('base'),
            ticket_country_state = req.media.get('country_state'),
            ticket_consumption = 1  
        )

        try:
            model.save(self.db.session)

        except IntegrityError:
            raise falcon.HTTPBadRequest(
              'Ticket Já existente',
              'Não foi possível criar o registro pois CDD já existe.'  
            )

        resp.status = falcon.HTTP_200
        resp.media = model.serialize()


class TicketsItem(BaseResource):
    def on_get(self,req,resp,name):
        tickets_list = Tickets.get_all_base_tickets(self.db.session,name)
        obj = [ticket.serialize() for ticket in tickets_list]
        
        resp.status = falcon.HTTP_200
        resp.media = obj
        
    def on_put(self,req,resp,id):
        stock_model = Stocks.get_base_stock(self.db.session,id)
        stock_model.stock_value = req.media.get('value')
        
        try:
            stock_model.save(self.db.session)

        except IntegrityError:
            raise falcon.HTTPBadRequest(
                'Atualização Não Realizada',
                'Validar valor informado.'
            )

        resp.status = falcon.HTTP_200
        resp.media = stock_model.serialize()

class TicketAverage(BaseResource):
    def on_get(self,req,resp,name):
        actual_date = '1900-01-01'
        total = 0
        total_date = 0

        ticket_list = Tickets.get_all_base_tickets(self.db.session,name)
        for ticket in ticket_list:
            total += ticket.ticket_consumption

            if ticket.ticket_date != actual_date:
                total_date += 1
                actual_date = ticket.ticket_date    

        if total > 0:
            average_value = round(total / total_date)

        resp.status = falcon.HTTP_200
        resp.media = {
            'ticket_base' :  ticket_list[0].ticket_base,
            'average' : average_value
        }
              
