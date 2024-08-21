import time
datum1 = (2024, 2, 17, 17, 3, 38, 0, 0, 0)
Date1 = time.mktime(datum1)

datum2 = (2024, 2, 17, 17, 3, 37, 0, 0, 0)
Date2 = time.mktime(datum2)
print(Date1 - Date2)

datum3 = (2024, 12, 24, 0, 0, 0, 0, 0, 0)
Date3 = time.mktime(datum3)
print(Date3 - Date2)


