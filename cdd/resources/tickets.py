import falcon
import json

from cdd.database.models import Tickets
from cdd.resources import BaseResource
from sqlalchemy.exc import IntegrityError

class TicketsCollection(BaseResource):
    def on_get(self,req,resp):
        ticket_list = Tickets.get_list(self.db.session)
        obj = [ticket.serialize() for ticket in ticket_list]        
        resp.status = falcon.HTTP_200
        resp.media = obj

class TicketsItem(BaseResource):
    def on_get(self,req,resp,name):
        tickets_list = Tickets.get_all_base_tickets(self.db.session,name)
        obj = [ticket.serialize() for ticket in tickets_list]
        
        resp.status = falcon.HTTP_200
        resp.media = obj

class TicketAverage(BaseResource):
    def on_get(self,req,resp,name):
        average_value = self.calculate_average(name)
        resp.status = falcon.HTTP_200
        resp.media = {
            'average' : average_value
        }


    def calculate_average(self,name):
        total = Tickets.get_total_of_tickets(self.db.session,name)
        total_date = Tickets.get_distinct_count_dates_on_tickets(self.db.session,name)
        average_value = round(total / total_date)
        
        return average_value
