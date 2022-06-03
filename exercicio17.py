from datetime import datetime

# input datetime
dt = datetime(2018, 10, 22, 0, 0)
# epoch time
epoch_time = datetime(1970, 1, 1)

# subtract Datetime from epoch datetime
delta = (dt - epoch_time)
print('Datetime to Seconds since epoch:', delta.total_seconds())