from datetime import datetime

date1 = input("Enter first date (DD-MM-YYYY): ")
date2 = input("Enter second date (DD-MM-YYYY): ")

d1 = datetime.strptime(date1, "%d-%m-%Y")
d2 = datetime.strptime(date2, "%d-%m-%Y")

if d1 < d2:
    print(date1, "is earlier.")
elif d2 < d1:
    print(date2, "is earlier.")
else:
    print("Both dates are the same.")


