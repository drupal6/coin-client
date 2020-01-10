from hbclient.trade.requstclient import RequestClient
from hbclient.trade.subscriptionclient import SubscriptionClient
from hbclient.trade.model.constant import CandlestickInterval
from strategies.BollbandStrategy import BollbandStrategy
from apscheduler.schedulers.background import BackgroundScheduler
import time
from datetime import datetime

import logging
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=format, filename='ema_strategy.txt')
logging.getLogger('apscheduler').setLevel(logging.WARNING)  # 设置apscheduler日记类型.

if __name__ == '__main__':

    key = ""
    secret = ''
    req_client = RequestClient()
    sub_client = SubscriptionClient()

    symbol = 'btcusdt'
    double_ema_strategy = BollbandStrategy(req_client=req_client, sub_client=sub_client, symbol=symbol)
    double_ema_strategy.on_1hour_kline_data(symbol=symbol, interval=CandlestickInterval.MIN60);
    # scheduler = BackgroundScheduler()


    # binance_ws = BinanceDataWebsocket(on_tick_callback=double_ema_strategy.on_tick)
    # binance_ws.subscribe("btcusdt")
    #
    # # 获取K线数据.
    # scheduler.add_job(double_ema_strategy.on_1hour_kline_data, trigger='cron', args=(symbol,), hour='*/1')
    #
    # # 获取当前的挂单没有成交的订单.  30 秒请求一次.
    # scheduler.add_job(double_ema_strategy.on_open_orders, trigger='cron', args=(symbol,), second='*/30')
    #
    # # 获取当前的仓位信息.
    # scheduler.add_job(double_ema_strategy.on_position, trigger='cron', args=(symbol,), second='*/15')
    #
    # scheduler.start()
    #
    # double_ema_strategy.on_1hour_kline_data(symbol)
    #
    # while True:
    #     double_ema_strategy.check_position()
    #     time.sleep(60)  # 2min.
    #     # 每两分钟需要检查下仓位信息, 检查订单有没有成交，
    #     # 是否符合自己的要求.