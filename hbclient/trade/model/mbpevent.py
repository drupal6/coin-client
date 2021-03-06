from hbclient.trade.constant.result import OutputKey
from hbclient.trade.impl.utils.channelparser import ChannelParser
from hbclient.trade.model.mbp import Mbp


class MbpEvent:
    """
    increasement of price depth.

    :member
        symbol: The symbol you subscribed.
        timestamp: The UNIX formatted timestamp generated by server in UTC.
        data: The price depth.

    """

    def __init__(self):
        self.symbol = ""
        self.ch = ""
        self.ts = 0
        self.data = Mbp()

    @staticmethod
    def json_parse(json_wrapper):
        ch = json_wrapper.get_string(OutputKey.KeyChannelCh)
        parse = ChannelParser(ch)
        mbp_event = MbpEvent()
        mbp_event.symbol = parse.symbol
        mbp_event.ts = json_wrapper.get_int("ts")
        mbp_event.ch = ch
        data = json_wrapper.get_object(OutputKey.KeyTick)
        mbp = Mbp.json_parse(data)
        mbp_event.data = mbp
        return mbp_event
