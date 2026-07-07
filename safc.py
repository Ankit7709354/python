try:

    a = float(input("First Number: "))
    b = float(input("Second Number: "))

    print("""
1. Add
2. Subtract
3. Multiply
4. Divide
""")

    choice = int(input("Choice: "))

    if choice == 1:
        print(a + b)

    elif choice == 2:
        print(a - b)

    elif choice == 3:
        print(a * b)

    elif choice == 4:
        print(a / b)

    else:
        print("Invalid Choice")

except ZeroDivisionError:

    print("Cannot divide by zero.")

except ValueError:

    print("Enter valid numbers.")