from hbclient.trade.model.order import Order


class OrderUpdateEvent:
    """
    The order update received by subscription of order update.

    :member
        symbol: The symbol you subscribed.
        timestamp: The UNIX formatted timestamp generated by server in UTC.
        data: The order detail.

    """

    def __init__(self):
        self.symbol = ""
        self.timestamp = 0
        self.data = Order()

    def print_object(self, format_data=""):
        from hbclient.trade.base.printobject import PrintBasic
        PrintBasic.print_basic(self.symbol, "Symbol")
        PrintBasic.print_basic(self.timestamp, "Timestamp")

        order = self.data
        order.print_object()