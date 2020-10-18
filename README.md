# TD Ameritrade Trading Bot
This is a trading bot based on TD Ameritrade API to fetch stock prices from the US stock market in real-time. Reference resources can be found here: 

1. Documentation: https://developer.tdameritrade.com/apis
2. YouTube Video: https://www.youtube.com/watch?v=qJ94sSyPGBw&ab_channel=SigmaCoding 
3. External Module Source: https://tda-api.readthedocs.io/en/stable/ 


## How it works
1. RUN 'main.py' 
2. GET info from 'info.py' 
3. PUT info into 'strategies.py' 
4. TRIGGER 'open_order.py' 
5. RECORD order in 'portfolio.py' 
6. TRIGGER take profit / stop loss in 'close_order.py 
7. REPEAT from step 2 to step 6 again and again 


###### Do List:
1. Authentication 
2. Time 
3. Indicator 
4. Open Order 
5. Check Profit 