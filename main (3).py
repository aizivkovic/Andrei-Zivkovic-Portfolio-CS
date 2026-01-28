import random

# Initialize player loss counters
player_1_losses = 0
player_2_losses = 0


def play_game():
    global player_1_losses, player_2_losses
    playing = True

    while playing:
        # Ask for the number of sticks to start with
        sticks_remaining = 0
        while sticks_remaining < 10 or sticks_remaining > 100:
            try:
                sticks_remaining = int(input("Enter the number of sticks (between 10 and 100): "))
            except ValueError:
                print("Please enter a valid number.")

        current_player = 1  # Start with player 1

        # Game loop while there are sticks remaining
        while sticks_remaining > 0:
            print(f"\nSticks remaining: {sticks_remaining}")
            print(f"Player {current_player}'s turn")

            # If current player is player 1 or player 2
            if current_player == 1 or current_player == 2:
                sticks_taken = 0
                while sticks_taken < 1 or sticks_taken > 3 or sticks_taken > sticks_remaining:
                    try:
                        sticks_taken = int(input(f"Player {current_player}, how many sticks will you take (1-3)? "))
                    except ValueError:
                        print("Please enter a valid number between 1 and 3.")
                print(f"Player {current_player} took {sticks_taken} sticks.")

            # If current player is the computer (player 3)
            elif current_player == 3:
                sticks_taken = random.randint(1, min(3, sticks_remaining))
                print(f"Computer (Player {current_player}) took {sticks_taken} sticks.")

            # Subtract the chosen number of sticks
            sticks_remaining -= sticks_taken

            # Check if current player lost
            if sticks_remaining == 0:
                print(f"Player {current_player} lost!")
                if current_player == 1:
                    player_1_losses += 1
                elif current_player == 2:
                    player_2_losses += 1
                break

            # Advance to the next player
            current_player = 1 if current_player == 2 else (2 if current_player == 1 else 1)

        # End of the game, display loss count
        print("\nCurrent loss counts:")
        print(f"Player 1 losses: {player_1_losses}")
        print(f"Player 2 losses: {player_2_losses}")

        # Ask if players want to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again == "no":
            playing = False

    # Game conclusion
    print("\nFinal loss counts:")
    print(f"Player 1 losses: {player_1_losses}")
    print(f"Player 2 losses: {player_2_losses}")
    print("Thanks for playing!")


# Start the game
play_game()
# Code goes here