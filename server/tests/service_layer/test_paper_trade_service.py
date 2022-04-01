from server.data_access_layer.abstract_classes.paper_trade_dao import PaperTradeDAO
from server.data_access_layer.implementation_classes.paper_trade_dao import PaperTradeDAOImp

from server.service_layer.implementation_classes.paper_trade_service import PaperTradeService, PaperTradeServiceImp

paper_trade_dao: PaperTradeDAO = PaperTradeDAOImp()
paper_trade_service: PaperTradeService = PaperTradeServiceImp(paper_trade_dao)


# Creation Tests ----------------------------------------------------------------------------
# Read Tests --------------------------------------------------------------------------------
# Update Tests ------------------------------------------------------------------------------
# Delete Tests ------------------------------------------------------------------------------
# id not string
def test_delete_paper_trade_id_not_string(invalid_id):
    try:
        paper_trade_service.delete_paper_trade(invalid_id)
        assert False
    except UserIdMustBeString as e:
        assert str(e) == user_id_must_be_string


# id missing
def test_delete_paper_trade_no_id(missing_id):
    try:
        paper_trade_service.delete_paper_trade(missing_id)
        assert False
    except MissingUserId as e:
        assert str(e) == user_id_not_provided
