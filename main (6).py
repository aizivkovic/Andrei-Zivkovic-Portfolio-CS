# Programmers: Mia McCloskey, Andrei Zivkovic
# Course: CS151, Professor Ebert
# Due Date: 03/19/25
# Programming Assignment: Lab 7
# Problem Statement:Refactor the ATM application using the given code so that it has proper error checking and functions.
# Data In: (D,W,B,E) with a valid positive amount for deposit or withdrawal
# Data Out: your final balance after choosing an atm function

#function name: display menu
#purpose: display menu options for the user
#parameters: none
#return: none
def display_menu():
    print("\nPlease select an option:"
        "\n\t D - Deposit"
        "\n\t W - Withdraw"
        "\n\t B - Current Balance"
        "\n\t E - Exit")


#function name: get_valid_choice
#purpose: Get a valid choice from the user
#parameters:none
#return:string - a valid single character menu option (D,W, B, E)
def get_valid_choice():
    valid_choices = ["D", "W", "B", "E"]
    while True:
        choice = input("Enter your choice: ").strip().upper()
        if choice in valid_choices:
            return choice
        print("invalid choice")
        display_menu()


#function name: get_valid_amount
#purpose: Get a valid positive amount from the user
#parameters
#return:
def get_valid_amount(prompt_message):
    while True:
        amount_str = input(prompt_message).strip()
        if amount_str.isdigit():
            amount = int(amount_str)
            if amount >= 0:
                return amount
            print("Please enter a positive amount")
        else:
            print("Please enter a valid amount")

#function name: deposit_action
#purpose: Deposit action
#parameters: current_balance (int) - the ci
#return: int- the updated balance after deposit
def deposit_action(current_balance):
    deposit_amount = get_valid_amount("Enter the desired amount for deposit:")
    current_balance += deposit_amount
    print(f"Your current balance is ${current_balance:.2f}.")
    return current_balance

#function name: withdrawal_action
#purpose: doing the withdrawal action
#parameters: current balance (int) - the current amount balance
#return: int- the updated balance after the withdrawal
def withdraw_action(current_balance):
    withdraw_amount = get_valid_amount("Enter the desired amount for withdraw:")
    current_balance -= withdraw_amount
    print(f"Your current balance is ${current_balance:.2f}.")

    # when balance is negative
    if current_balance < 0:
        print("You have a negative balance. You will be charged 5% interest.")

    return current_balance

#function name: display_balance
#purpose: To display the current account balance
#parameters: current_balance (int) - the current account balance
#return: None
def display_balance(current_balance):
    print(f"Your current balance is ${current_balance:.2f}.")

#function name: main
#purpose:main function for the ATM program
#parameters: None
#return: None
def main():
    #initialize variables
    INITIAL_BALANCE = 1000
    current_balance = INITIAL_BALANCE
    SENTINEL = 'E'
    choice = ''

    #main loop
    while choice != SENTINEL:
        display_menu()
        choice = get_valid_choice()

        if choice == 'D':
            current_balance = deposit_action(current_balance)
        elif choice == 'W':
            current_balance = withdraw_action(current_balance)
        elif choice == 'B':
            display_balance(current_balance)
        elif choice == 'E':
            print("Thank you for using the ATM. Goodbye.")

    print("ATM program has ended")

#Run the program
if __name__ == "__main__":
    main()






