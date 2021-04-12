import falcon
import json

from cdd.database.models import Stocks
from cdd.resources.tickets import TicketAverage
from cdd.resources import BaseResource
from sqlalchemy.exc import IntegrityError,SQLAlchemyError

class StocksCollection(BaseResource):
    def on_get(self,req,resp):
        model_list = Stocks.get_list(self.db.session)

        obj = [stock.serialize() for stock in model_list]
        for cdd in obj:
            cdd['average'] = TicketAverage.calculate_average(self, cdd['base'])       

        resp.status = falcon.HTTP_200
        resp.media = obj


class StocksItem(BaseResource):
    def on_get(self,req,resp,id):
        stock_model = Stocks.get_stocks_by_id(self.db.session,id).serialize()
        stock_model['average'] = TicketAverage.calculate_average(self,stock_model['base'])
        resp.status = falcon.HTTP_200
        resp.media = stock_model
        
    def on_put(self,req,resp,id):
        stock_model = Stocks.get_stocks_by_id(self.db.session,id)
        stock_model.stock_value = req.media.get('value')
        
        try:
            stock_model.save(self.db.session)

        except SQLAlchemyError:
            raise falcon.HTTPBadRequest(
                'Atualização Não Realizada',
                'Validar valor informado.'
            )

        resp.status = falcon.HTTP_200
        resp.media = stock_model.serialize()
