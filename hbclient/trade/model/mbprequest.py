from hbclient.trade.constant.result import OutputKey
from hbclient.trade.impl.utils.channelparser import ChannelParser
from hbclient.trade.model.pricedepth import PriceDepth
from hbclient.trade.model.mbp import Mbp



class MbpRequest:
    """
    The price depth received by subscription of price depth.

    :member
        symbol: The symbol you subscribed.
        timestamp: The UNIX formatted timestamp generated by server in UTC.
        data: The price depth.

    """

    def __init__(self):
        self.symbol = ""
        self.rep = ""
        self.id = ""

        self.data = PriceDepth()


    @staticmethod
    def json_parse(json_wrapper):
        rep = json_wrapper.get_string(OutputKey.KeyChannelRep)
        parse = ChannelParser(rep)
        mbp_event = MbpRequest()
        mbp_event.symbol = parse.symbol
        mbp_event.id = json_wrapper.get_int("id")
        mbp_event.rep = rep
        data = json_wrapper.get_object(OutputKey.KeyData)
        mbp = Mbp.json_parse(data)
        mbp_event.data = mbp
        return mbp_event
