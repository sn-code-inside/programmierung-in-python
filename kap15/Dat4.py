import datetime
import time

datum1 = "10/10/21"
Date1 = datetime.datetime.strptime(datum1, "%m/%d/%y")
print("Das Jahr:", Date1.year)
print( "Monat:", Date1.month)
print( "Tag:", Date1.day)
print( "Stunde", Date1.hour)
print( "Minuten:", Date1.minute)
print( "Sekunden:", Date1.second)
print( "Millisekunden:", Date1.microsecond)

datum2 = (2024, 2, 17, 17, 3, 38, 0, 0, 0)
Date2 = time.mktime(datum2)
d2= time.gmtime(Date2)
print("Das Jahr:", d2.tm_year)
print( "Monat:", d2.tm_mon)
print( "Tag:", d2.tm_mday)
print( "Stunde", d2.tm_hour)
print( "Minuten:", d2.tm_min)
print( "Sekunden:", d2.tm_sec)

