from hbclient.trade.constant.system import ApiVersion
from hbclient.trade.impl.websocketrequest import WebsocketRequest
from hbclient.trade.impl.utils.channels import *
from hbclient.trade.impl.utils.inputchecker import *
from hbclient.trade.model.account import AccountBalanceMode
from hbclient.trade.model.tradeclearingevent import TradeClearingEvent
from hbclient.trade.model.accountsupdateevent import AccountsUpdateEvent


class WebsocketRequestImplV2(object):

    def __init__(self, api_key):
        self.__api_key = api_key

    def subscribe_trade_clearing_event(self, symbols, callback, error_handler=None):
        if ("*" in symbols):
            symbols = ["*"]
        else:
            check_symbol_list(symbols)

        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            for val in symbols:
                connection.send(trade_clearing_channel(val))
                time.sleep(0.01)

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.auto_close = False
        request.is_trading = True
        request.json_parser = TradeClearingEvent.json_parse
        request.update_callback = callback
        request.error_handler = error_handler
        request.api_version = ApiVersion.VERSION_V2
        return request

    def subscribe_accounts_update_event(self, mode, callback, error_handler=None):
        check_should_not_none(callback, "callback")
        if str(mode) == AccountBalanceMode.TOTAL:
            mode = AccountBalanceMode.TOTAL
        else:
            mode = AccountBalanceMode.BALANCE

        def subscription_handler(connection):
            connection.send(accounts_update_channel(mode))

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.auto_close = False
        request.is_trading = True
        request.json_parser = AccountsUpdateEvent.json_parse
        request.update_callback = callback
        request.error_handler = error_handler
        request.api_version = ApiVersion.VERSION_V2
        return request