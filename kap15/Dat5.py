import datetime
now =  datetime.datetime.now()
datum1 = "12/24/17"
Date1 = datetime.datetime.strptime(datum1, "%m/%d/%y")
print( Date1 - now)

