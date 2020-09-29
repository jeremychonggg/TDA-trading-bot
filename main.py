# import modules
import time
import requests
from tda import auth, client
from datetime import datetime
import pytz


# import files
# //Authentication
from config import client_id, token_path, redirect_uri
# //Looping
from close_order import close_order
from company_name import symbols
from portfolio import my_portfolio
from strategies import long_strategy


# Config - Authentication
try:
    c = auth.client_from_token_file(token_path, client_id)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome(executable_path='D:\Documents\Python\Project\TD Ameritrade\chromedriver.exe') as driver:
        c = auth.client_from_login_flow(
            driver, client_id, redirect_uri, token_path
        )


# set current time
def get_current_time():
    now = datetime.now(pytz.timezone('America/New_York'))
    return (9, 50)  # (now.hour, now.minute)  # <-- Need to change back
    # time - Tuple containing hours and minutes


# set valid time
def is_valid_time(time):
    return (time[0] == 9 and time[1] >= 30) or (time[0] > 9 and time[0] < 16)


# check if the symbol already contain in my_portfolio
def check_symbol(name):
    if str(name) not in str(my_portfolio):
        return True
# convert my_portfolio into string
# find if the string contain the string of (symbol)
# if not in the string, return True
# return True will run the following code


# run if current time is a valid time:
while is_valid_time(get_current_time()):
    # check close_order()
    print('##################################################')
    print('Loop: Close Order')
    close_order()
    print('')
    print('')
    print('')

    # run long_strategy()
    print('##################################################')
    print('Loop: Long Strategy')
    for symbol in symbols:
        if check_symbol(symbol):
            long_strategy(symbol)
    print('')
    print('')
    print('')
