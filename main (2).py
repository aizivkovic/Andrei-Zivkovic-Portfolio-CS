# Programmers:Andrei Zivkovic
# Course:  CS151, Eric Ebert
# Due Date: 3/24/25
# Program Assignment: PA-3
# Problem Statement:  You are creating a program to display ASCII art and string decorations to the user. ASCII art is
# just a combination of characters that make a design or pattern.
# Data In: Your input of choice of what shape to print
# Data Out: your desired shape

import random

#Function name:Main
#Purpose:This program will display ASCII art and string decorations
#Parameters:none
#Return:none

def main():
    print("This program will display ASCII art and string decorations ")
    print("you can print circles, lines, or random art patters.\n")

    while True:
        print("\nMenu:")
        print("1. Print a circle")
        print("2. Print a set of lines")
        print("3. Print a random art pattern")
        print("4. Exit")

        choice = get_valid_int("Enter your choice (1-4): ", 1, 4)

        if choice == 1:
            print_circle()
        elif choice == 2:
            print_lines()
        elif choice == 3:
            print_random_design()
        elif choice == 4:
            print("Thank you! This program will exit now.")
            break

#Function name:get valid integer
#Purpose:to get a valid choice between 1 and 4
#Parameters:prompt, minimum value, maximum value
#Return: value, one of the 4 options

def get_valid_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_val is not None and value < min_val) or \
                (max_val is not None and value > max_val):
                print("Please enter a number between {min_val} and {max_val}.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")

#Function name:Print circle
#Purpose: to print a circle
#Parameters: none
#Return: a circle pattern

def print_circle():
    print("\nHere is your Circle:")
    print("   ***   ")
    print(" *     * ")
    print("*       *")
    print("*       *")
    print(" *     * ")
    print("   ***   ")

#Function name:Print lines
#Purpose:to print a certain amount of lines
#Parameters:none
#Return:a number of lines in a certain character

def print_lines():
    num_lines = int(input("Enter number of lines you would like to print: "))
    symbol = input("what character(s) should make up the line? ")
    repetitions = get_valid_int("how many times should we repeat this line? ")

    print()
    for _ in range(num_lines):
        print(symbol * repetitions)

#Function name:Print rando design
#Purpose:to print a random design
#Parameters:none
#Return: a random design

def print_random_design():
    designs = [design1, design2, design3]
    chosen_design = random.choice(designs)
    chosen_design()

#Function name:design 1
#Purpose: to print one of the three random designs
#Parameters:none
#Return:a pyramid design

def design1():
    print("\nRandom Design 1 - Pyramid")
    for i in range(1, 10, 2):
        print(" " * ((9-i) // 2) + "*" * i)

#Function name:design 2
#Purpose:to print one of the three random designs
#Parameters:none
#Return:a zigzag pattern

def design2():
    print("\nRandom Design 2 - ZigZag")
    for i in range(6):
        if i % 2 == 0:
            print("~" * 10)
        else:
            print(" " * 2 + "~" * 6)

#Function name:design 3
#Purpose:to print one of the three random designs
#Parameters:none
#Return:a christmas tree pattern
#https://p-kane.medium.com/creating-a-christmas-tree-ascii-art-with-python-1426c82777be
def design3():
    print("\nRandom Design 3 - Christmas Tree")
    print('''
           #
          ###
         #####
        #######
       #########
      ###########
     #############
    ###############
           H
           H
           H
    ''')

#run the program
if __name__ == '__main__':
    main()
