import datetime
import time

datum1 = "10/10/21"
Date1 = datetime.datetime.strptime(datum1, "%m/%d/%y")
print("Ein Datum in der Zukunft:", Date1)

datum2 = (2024, 2, 17, 17, 3, 38, 0, 0, 0)
Date2 = time.mktime(datum2)
print("Das Datum als Zeitstempel:", Date2);
print(time.gmtime(Date2))
print("Ein anderes Datum in der Zukunft:",
      time.strftime("%b %d %Y %H:%M:%S", time.gmtime(Date2)))
datum3 = (2024, 2, 17, 0, 0, 0, 0, 0, 0)
Date3 = time.mktime(datum3)
print("Noch ein anderes Datum in der Zukunft:",
      time.strftime("%b %d %Y %H:%M:%S", time.gmtime(Date3)))

