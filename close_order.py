# import files
from portfolio import my_portfolio
from info import Info


def close_order():
    for each in my_portfolio:
        symbol = each['symbol']
        percentage = round(Info(symbol).get_current_price(
            symbol) / each['price'], 2)
        if percentage >= 1.02:
            # still need to add a close order action
            my_portfolio.remove(each)
            print(f'ORDER CLOSED: {symbol}, {percentage} %')
