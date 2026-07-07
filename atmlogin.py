password = input("Enter Password: ")

if password == "1234":

    balance = 5000

    print("Login Successful")

    choice = int(input("""
1. Check Balance
2. Exit

Enter Choice: """))

    if choice == 1:
        print("Balance =", balance)

    else:
        print("Thank You")

else:
    print("Wrong Password")