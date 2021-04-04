import falcon

from database.manager import DBManager
from resources.stocks import StocksCollection, StocksItem
from resources.tickets import TicketsCollection, TicketsItem, TicketAverage

api = falcon.API()
db = DBManager('postgresql+psycopg2://postgres:R@posinh@1@localhost:5432/cdd_controller')

stocks = StocksCollection(db)
stock_item = StocksItem(db)

tickets = TicketsCollection(db)
ticket_item = TicketsItem(db)
ticket_average = TicketAverage(db)

api.add_route('/stocks',stocks)
api.add_route('/stocks/{id}',stock_item)
api.add_route('/tickets',tickets)
api.add_route('/tickets/{name}',ticket_item)
api.add_route('/tickets/{name}/average',ticket_average)