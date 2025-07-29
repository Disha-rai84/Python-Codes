

import time
import datetime  
#returns the current datetime object     
print(datetime.datetime.now())
# time.sleep(2)
# print("hello")

# print(time.time())  
# print(time.localtime(time.time())) 
# print(time.asctime(time.localtime(time.time())))   


# from datetime import datetime as dt    
# #Compares the time. If the time is in between 8AM and 4PM, then it prints working hours otherwise it prints fun hours    
# if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,16):    
#     print("Working hours....")    
# else:    
#     print("fun hours")


import calendar;    
cal = calendar.month(2025,7)    
#printing the calendar of December 2018    
s = calendar.prcal(2020)  
print(cal)    


