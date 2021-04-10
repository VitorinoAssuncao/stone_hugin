import falcon

from cdd.database.manager import DBManager
from cdd.resources.stocks import StocksCollection, StocksItem
from cdd.resources.tickets import TicketsCollection, TicketsItem, TicketAverage
from cdd.middleware import HandleCORS

api = falcon.API(middleware=[HandleCORS()])
db = DBManager()

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

if __name__ == "__main__":
    from wsgiref import simple_server

    httpd = simple_server.make_server("127.0.0.1",5000,api)
    httpd.serve_forever()