# import modules
from tda.orders import EquityOrderBuilder, Duration, Session

# import files
from portfolio import capital
from portfolio import my_portfolio
#from config import account_id
#from main import c


# reference link
# https://tda-api.readthedocs.io/en/stable/order-templates.html#order-templates


# buy low, sell high
def long_order(symbol, current_price):  # price, stop_loss, take_profit
    # set the quantity
    quantity = round((0.01 * capital) / (0.10 * current_price), 2)
    # replace get_current_price(symbol)  with current_price !!!!!
    # // (%Risk per Trade x Capital) / (Risk per Share)
    # better to change the current_price(symbol) to 5days average IRA_price(symbol)

    trade = {'symbol': symbol, 'price': current_price, 'quantity': quantity}

    # # set the instruction
    # builder = EquityOrderBuilder(symbol, quantity)
    # builder.set_instruction(EquityOrderBuilder.Instruction.BUY)  # SELL
    # builder.set_order_type(EquityOrderBuilder.OrderType.MARKET)  # LIMIT
    # builder.set_duration(Duration.DAY)  # GOOD_TILL_CANCEL
    # builder.set_session(Session.NORMAL)  # AM, PM

    # WARNING: EquityOrderBuilder has moved from tda.orders to tda.orders.equities.
    # WARNING: Duration has moved from tda.orders to tda.orders.common.
    # WARNING: Session has moved from tda.orders to tda.orders.common.
    # It will be removed from tda.orders in a future version.
    # You can find documentation on its replacements here: https://tda-api.readthedocs.io/en/stable/order-templates.html

    # # place order
    # response = c.place_order(account_id, builder.build())

    my_portfolio.append(trade)
    print(f'ORDER OPENED: {symbol} -LONG')
    print('my_portfolio: ', my_portfolio)


# buy high, sell low
def short_order(symbol, current_price):
    trade = {'symbol': symbol, 'price': current_price}

    my_portfolio.append(trade)
    print(f'ORDER OPENED: {symbol} -SHORT')
    print('my_portfolio: ', my_portfolio)
