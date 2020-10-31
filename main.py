from geiger import GMtube,Buzzer
from utime import *

g=GMtube(duty=675,freq=20000)
last_tick = ticks_ms()
current_tick = ticks_ms()

CPM = []
event = 0

while True:
    # check if a new event happened
    if g.count > event:
        event = g.count
        current_tick = ticks_ms()
        diff_ticks = ticks_diff(current_tick, last_tick)
        last_tick = current_tick

        if diff_ticks < 120000:
            CPM.append(diff_ticks)
            while sum(CPM) > 60000:
                CPM.pop(0)
        
        Buzzer()
            
        cpm=str(len(CPM))
        uSv=str(len(CPM)*0.0057) # CF of SBM-20
        dt=str(diff_ticks)
        data = str(time())+","+cpm+","+uSv+","+dt
        print(data)
        

