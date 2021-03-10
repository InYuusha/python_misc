import datetime as d
try:
    while True:
      
       dt=d.datetime.now()
       print(dt.year,dt.month,dt.day,dt.hour,dt.minute)
except KeyboardInterrupt:
    print('Stopped')
