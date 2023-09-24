from datetime import datetime
import time


while True:
    now = datetime.now()
    second = str(now.second)
    hour = str(now.hour)
    minute = str(now.minute)
    if(len(hour) == 1):
        hour = "0" + hour
    if len(minute) == 1:
        minute = "0" + minute
    if len(second) == 1:
        second = "0" + second
    print("► ", hour, ":", minute, ":", second," ◄" , sep = "", end='\r')

    time.sleep(0.5)