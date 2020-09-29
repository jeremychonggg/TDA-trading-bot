Documentation: https://developer.tdameritrade.com/apis
YouTube Video: https://www.youtube.com/watch?v=qJ94sSyPGBw&ab_channel=SigmaCoding 
External Module Source: https://tda-api.readthedocs.io/en/stable/ 

Flow of this program 
1. RUN 'main.py' 
2. GET info from 'info.py' 
3. PUT info into 'strategies.py' 
4. TRIGGER 'open_order.py' 
5. RECORD order in 'portfolio.py' 
6. TRIGGER take profit / stop loss in 'close_order.py 


main -> info -> strategies -> open_order -> portfolio -> close_order 
         ^                                                     | 
         |_____________________________________________________| 
                                  repeat    


Do List:
1. Authentication 
2. Time 
3. Indicator 
4. Open Order 
5. Check Profit 