# Programmers:Lauren Duffy & Andrei Zivkovic
# Course:CS151
# Due Date:2/26/25
# Lab Assignment:5
# Problem Statement: Things you do at an ATM: Deposit money; Withdraw money; check balance
# Data In: amount they want to deposit/withdraw or what to check what there current balance is
# Data Out: amount of money left in the back or amount taken out or what the current balance is
# Credits: Class Lab

# initialize the balance
balance = 1000

# Initial statement
print("your starting balance is $1000")

# main loop
choice = ""
while choice != "D" and choice != "W" and choice != "B" and choice != "E":
    print("D - Deposit")
    print("W - Withdraw")
    print("B - Balance")
    print("E - Exit")

    # get user choice
    choice = input("enter your choice: ")
    choice = choice.upper()

    #process the choice
    if choice == "D":
        amount_str = input("enter amount to deposit: ")
        try:
            amount = float(amount_str)
            if amount < 0:
                print("error: cannot deposit a negative amount")
            else:
                balance = balance + amount
                print("deposited: $" + str(amount))
                print("balance: $" + str(balance))
        except ValueError:
            print("Error: please enter a valid amount")

    elif choice == "W":
        amount_str = input("enter amount to withdraw: ")
        try:
            amount = float(amount_str)
            if amount < 0:
                print("error: cannot withdraw a negative amount")
            elif amount > balance:
                print("error: you don't have enough balance and you will have a 5% interest added to your account!")
            else:
                balance = balance - amount
                print("withdrawn: $" + str(amount))
                print("new balance: $" + str(balance))
        except ValueError:
            print("Error: please enter a valid amount")

    elif choice == "B":
        print("your current balance is: $" + str(balance))

    elif choice == "E":
        print("exit")

    else:
        print("Error: please enter D,W,B,E")

print("Thank you for using our application. Final balance: $" + str(balance))








