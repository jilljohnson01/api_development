import time

time.gmtime(0)

from datetime import datetime, timedelta

current_datetime = datetime.now()
print("Epoch:", current_datetime)

epoch_plus_thirty = current_datetime + timedelta(minutes=30)
print("Epoch + 30 Min:", epoch_plus_thirty)
