from server.data_access_layer.abstract_classes.paper_trade_dao import PaperTradeDAO
from server.data_access_layer.implementation_classes.paper_trade_dao import PaperTradeDAOImp

from server.service_layer.implementation_classes.paper_trade_service import PaperTradeService, PaperTradeServiceImp

paper_trade_dao: PaperTradeDAO = PaperTradeDAOImp()
paper_trade_service: PaperTradeService = PaperTradeServiceImp(paper_trade_dao)


