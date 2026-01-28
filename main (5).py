# Programmers:  Mark Pirro Andrei Zivkovic
  # Course:  CS151, Eric Ebert
  # Due Date: [3/26/25]
  # Lab assignment: Lab 8
  # Problem Statement:  [To show the amount of stars to represent amount of times a number was rolled]
  # Data In: [The amount of time the user wants to roll the dice]
  # Data Out:  [*s resenting the amount of time a number was rolled]
  # Credits { Book ]




import random
#interger validator
#Purpose: To validate number as an integer
#Parameters: Value to be inputted
#Returns: Validate numbers, or asked user to input an integer

def int_validator(value):
    try:
        return int(value)
    except ValueError:
        print("Please enter a valid integer.")
        return None
#Fuction to roll roll dice
#Purpose: To act a roll dice program
#Parameters:None
#Return: Sum_dice

def roll_dice():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    sum_dice = dice_1 + dice_2
    return sum_dice

Num_list = [0] * 12  # To store sums from 2 to 12
#Main function
#Purpose: Main function to print the results
#Parameters:none
#Returns: List of sum amounts as *
def main():
    # Validate input
    user_input = int_validator(input("How many times would you like to roll? "))
    while user_input <= 0:
        print("Please enter a positive integer.")
        user_input = int_validator(input("How many times would you like to roll? "))


    # Roll the dice user_input times
    for i in range(user_input):
        sum_rolled = roll_dice()
        sumcounter(sum_rolled)

    # Print the results from the rolls
    print("Sum amounts rolled:")
    for i in range(2, 13):  # Sums can only be between 2 and 12
        stars = '*' * Num_list[i - 2]
        print(f"Sum {i} : {stars}")
#Sum counter
#Purpose:To change index in num_list for amount of sum is rolled
#Parameters: Sum-rolled
#Returns:Num_list with proper changed indexs

def sumcounter(sum_rolled):
    # Update of the sum rolled
    Num_list[sum_rolled - 2] += 1

# Call the main function to run the program
if __name__ == "__main__":
    main()