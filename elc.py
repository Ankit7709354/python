units = int(input("Enter Units: "))

if units <= 100:
    bill = units * 2

elif units <= 300:
    bill = units * 3

else:
    bill = units * 5

print("Total Bill =", bill)