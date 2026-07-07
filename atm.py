balance = 5000

try:

    amount = float(input("Withdraw Amount: "))

    if amount > balance:

        raise Exception("Insufficient Balance")

    balance -= amount

    print("Remaining Balance =", balance)

except Exception as e:

    print(e)