from datetime import date
from datetime import time
from datetime import datetime

today = date.today()
now = datetime.now()
d = today.strftime("%d%b%y")
print(d)


current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
