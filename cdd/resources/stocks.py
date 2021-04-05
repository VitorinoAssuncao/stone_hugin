import falcon
import json

from cdd.database.models import Stocks
from cdd.resources import BaseResource
from sqlalchemy.exc import IntegrityError,SQLAlchemyError

class StocksCollection(BaseResource):
    def on_get(self,req,resp):
        model_list = Stocks.get_list(self.db.session)

        obj = [stock.serialize() for stock in model_list]
        
        resp.status = falcon.HTTP_200
        resp.media = obj

    def on_post(self,req,resp):
        model = Stocks(
          stock_base = req.media.get('base'),
          stock_value = req.media.get('value')  
        )

        try:
            model.save(self.db.session)

        except IntegrityError:
            raise falcon.HTTPBadRequest(
              'CDD Já existente',
              'Não foi possível criar o registro pois CDD já existe.'  
            )

        resp.status = falcon.HTTP_200
        resp.media = model.serialize()


class StocksItem(BaseResource):
    def on_get(self,req,resp,id):
        stock_model = Stocks.get_stocks_by_id(self.db.session,id)
        resp.status = falcon.HTTP_200
        resp.media = stock_model.serialize()
        
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
