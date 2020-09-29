# import modules
import requests

# import files
from info import Info
import open_order


# buy low, sell high
def long_strategy(symbol):
    score = 0
    current_price = Info(symbol).get_current_price(symbol)
    previous_price = Info(symbol).get_previous_price(symbol)

    print('\n')
    print(symbol)
    print('--------------------------------')
    print('Valid: ')

    if current_price > previous_price:
        score += 1
        print(f'{score}. current_price > previous_price ')

    if score >= 1:  # Need to edit to '>=3'
        print('--------------------------------')
        open_order.long_order(symbol, current_price)
