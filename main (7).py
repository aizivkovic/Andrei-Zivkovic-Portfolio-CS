# Programmers:Timmy McCann & Andrei Zivkovic
# Course:CS151
# Due Date:3/12/25
# Lab Assignment:6
# Problem Statement: how much it will cost to re-do all the floors with the choice of hardwood, carpet and tile!
# Data In: the dimensions of each room along with the type of flooring
# Data Out: the price per room depending on flor choice, then the total price combined of flooring
# Credits: Class Lab

#function name: get_valid_dimension
#purpose: get a valid dimension input from the user
#parameters: dimension_name(string) - name of the dimension(width or length)
#return: float - valid positive dimension value
def get_valid_dimension(dimension_name):
    while True:
        user_input = input(f"Enter the {dimension_name} of the room in feet: ")

        # Check if input can be converted to float
        if user_input.replace('.', '', 1).isdigit():
            dimension = float(user_input)
            if dimension <= 0:
                print(f"Error: {dimension_name} must be a positive number.")
            else:
                return dimension
        else:
            print(f"Error: Please enter a valid number for {dimension_name}.")

#function name: get_valid_flooring_type
#purpose: get a valid flooring type from the user
#parameters: none
#return: string - valid flooring type (hardwood, carpet, tile)
def get_valid_flooring_type():
    valid_flooring_types = ["hardwood", "carpet", "tile"]

    while True:
        flooring_type = input(f"Enter the flooring type (hardwood, carpet, tile): ").strip().lower()
        if flooring_type in valid_flooring_types:
            return flooring_type
        else:
            print(f"Error: Please enter a valid flooring type")


#function name: calculate_room_cost
#purpose: calculate the cost of flooring for a single room
#parameters: width (float) - width of the room in feet
#           length (float) - length of the room in feet
#           flooring_type (string) - type of flooring
#return: float - cost of flooring for the room
def calculate_room_cost(width, length, flooring_type):
    area = (width * length)

    if flooring_type == "tile":
        cost_per_sqft = 4.99
    elif flooring_type == "carpet":
        cost_per_sqft = 3.99
    else: #hardwood cost
        cost_per_sqft = 1.39

    return area * cost_per_sqft

#function name: process_room
#purpose: process a single room by getting dimensions and flooring
#parameters: room_number (int) - room number being processed
#return: float - cost for this room
def process_room(room_number):
    print(f"\n Room {room_number} ")
    width = get_valid_dimension("width")
    length = get_valid_dimension("length")
    flooring_type = get_valid_flooring_type()

    cost = calculate_room_cost(width, length, flooring_type)
    print(f"Cost for Room {room_number} ({flooring_type}): ${cost:.2f}")

    return cost

#function name: main
#purpose: main function for the program
#parameters: none
#return: none
def main():
    print("Welcome to Rooms Calculator")
    print("Lets calculate the cost of your flooring:")

    total_cost = 0

    for room_number in range(1, 6):
        room_cost = process_room(room_number)
        total_cost += room_cost

    print("\n Summary ")
    print(f"The total cost of your room is ${total_cost:.2f}")
    print("Thank you for using Rooms Calculator")

#call the main function to start the program
if __name__ == "__main__":
    main()
