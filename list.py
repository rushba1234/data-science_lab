list1 = input("Enter elements of first list separated by spaces: ").split()
list2 = input("Enter elements of second list separated by spaces: ").split()

common = False

for item in list1:
    if item in list2:
        common = True
        break

print("Have common member:", common)

