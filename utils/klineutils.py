from hbclient.trade.exception.huobiapiexception import HuobiApiException


def update_klines(klins, new_klines, size):
    if len(new_klines) == 1:
        if new_klines[-1]["id"] == klins[-1]["id"]:
            klins = new_klines[-1]
        else:
            klins.append(new_klines[-1])
            if len(klins) > size:
                klins.pop(0)
    else:
        if new_klines[-1]["id"] == klins[-1]["id"]:
            klins = new_klines[-1]
        elif new_klines[-2]["id"] == klins[-1]["id"]:
            klins[-1] = new_klines[-2]
            klins.append(new_klines[-1])
            if len(klins) > size:
                klins.pop(0)
        else:
            raise HuobiApiException(HuobiApiException.INPUT_ERROR, "update klines error")


def interval_handler(values, periods=[5, 10, 30], vtype="close"):
    ret = dict()
    index = 0
    template_values = dict()
    value_size = len(values)
    for period in periods:
        ret[period] = list()
    while index < value_size:
        for period in periods:
            template_values[period] = 0
            for p in range(0, period):
                if index + p > value_size - 1:
                    break
                template_values[period] += values[index + p][vtype]
            ret[period].append(template_values[period]/period)
        index += 1
    return ret


def periods_handler(values, periods=[1]):
    ret = dict()
    index = 0
    template_values = dict()
    value_size = len(values)
    for period in periods:
        ret[period] = list()
    while index < value_size:
        for period in periods:
            template_values[period] = 0       
            for p in range(0, period):
                if index + p > value_size - 1:
                    break
                template_values[period] += values[index + p]
            ret[period].append(template_values[period]/period)
        index += 1
    return ret


# def interval_handler(klines, interval=1, type="close"):
#     ret = list()
#     value = 0
#     for index, node in enumerate(klines):
#         if not hasattr(node, type):
#             raise HuobiApiException(HuobiApiException.KEY_MISSING, type + " not exit")
#         v = getattr(node, type)
#         if interval == 1:
#             ret.append(v)
#         else:
#             value += v
#             if index != 0 and (index+1) % interval == 0:
#                 ret.append(value/interval)
#                 value = 0
#
#     return ret

