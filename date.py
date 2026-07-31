date1 = input("Enter the first date (day month year): ").split()
date2 = input("Enter the second date (day month year): ").split()

day1 = int(date1[0])
month1 = int(date1[1])
year1 = int(date1[2])

day2 = int(date2[0])
month2 = int(date2[1])
year2 = int(date2[2])

d1 = (year1, month1, day1)
d2 = (year2, month2, day2)

if d1 < d2:
    print("The first date is earlier.")
elif d2 < d1:
    print("The second date is earlier.")
else:
    print("Both dates are the same.")
