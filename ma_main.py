from hbclient.trade.model.constant import CandlestickInterval
from hbclient.trade.exception.huobiapiexception import HuobiApiException
from strategies.MaStrategy import MaStrategy
from hbclient.hbdm.rest.HuobiDMService import HuobiDM
import json
from apscheduler.schedulers.background import BackgroundScheduler
import time
from datetime import datetime
from pprint import pprint

import logging
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=format, filename='ema_strategy.txt')
logging.getLogger('apscheduler').setLevel(logging.WARNING)  # 设置apscheduler日记类型.


if __name__ == '__main__':

    url = "https://api.btcgateway.pro"
    key = "xxxx"
    secret = 'xxxx'
    symbol = 'BCH_CW'
    interval = CandlestickInterval.MIN1
    size = 500
    req_client = HuobiDM(url=url, access_key=key, secret_key=secret)

    ma_strategy = MaStrategy(req_client, symbol, CandlestickInterval.MIN1, size)

    scheduler = BackgroundScheduler()
    scheduler.add_job(ma_strategy.update_kline, trigger='cron', args=(), second='*/10')

    scheduler.start()



    # double_ema_strategy.on_1hour_kline_data(symbol=symbol, interval=CandlestickInterval.MIN60);


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
    while True:
        # double_ema_strategy.check_position()
        time.sleep(60)  # 2min.
        # 每两分钟需要检查下仓位信息, 检查订单有没有成交，
        # 是否符合自己的要求.