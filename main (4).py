#Programmers: Andrei Zivkovic
#Course: CS151, Eric Ebert
#Due Date: 2/17/25
#Programming Assignment 1
#Problem Assignment: Determing the output if you study or practice when you have an exam and game on the same day
#Data in:study time, practice time, confidence level, focus choices 
#Data out: none
#Credits: None

print("This program is to help you figure out what to do when you have a game and exam on the same day")

# Ask user for their name
player_name = input("What is your name? ")

# The player must choose whether they want to study for an exam or practice for a sport.
study_or_practice = input("Are you going to study or practice? ").lower()

# The player is asked how much time they plan to dedicate to their focus (either studying or practicing).
study_time = 0
practice_time = 0

if study_or_practice == "study":
    print('You decide to study hard for your exam.')
    study_time = float(input("How long do you want to study for your exam? (hours) "))
elif study_or_practice == "practice":
    print("You decide to practice for your game.")
    practice_time = float(input("How long do you want to practice for your game? (hours) "))
else:
    print("Invalid choice. Please restart the program.")
    exit()

# Output for studying
if study_or_practice == "study":
    if study_time < 3:
        print("You didn't study much today. You feel a little unprepared for your exam.")
    elif 3 <= study_time <= 6:
        print("You studied for a decent amount of time. You feel reasonably ready for your exam.")
    else:
        print("You studied for many hours. You're extremely well-prepared for your exam!")

# Output for practicing
if study_or_practice == "practice":
    if practice_time < 3:
        print("You didn't practice much today. You're not feeling very confident for the game.")
    elif 3 <= practice_time <= 6:
        print("You practiced well enough. You're feeling good about your performance.")
    else:
        print("You practiced intensely. You're confident and ready for the big game!")

# The player is now asked to rate their confidence level (on a scale of 0.0 to 10.0).
confidence_level = float(input("What is your confidence level on a scale of 0-10? "))

# Output for studying
if study_or_practice == "study":
    if confidence_level < 5:
        print("You're feeling unsure about your exam.")
    elif 5.0 <= confidence_level <= 8.0:
        print("You're feeling somewhat confident about the exam.")
    else:
        print("You're extremely confident in your exam preparation!")

# Output for practicing
if study_or_practice == "practice":
    if confidence_level < 5.0:
        print("You're feeling unsure about the game.")
    elif 5.0 <= confidence_level < 8.0:
        print("You're feeling decent about your performance.")
    else:
        print("You're feeling very confident about the game!")

# The player is now asked what they'd like to do on the day of the exam or game (relax or prepare).
event_day = input("Are you going to relax or prepare on the day of the exam or game? ").lower()

# For studying
if study_or_practice == "study":
    if event_day == "relax":
        print("You decide to relax before your exam.")
    elif event_day == "prepare":
        print("You do some last-minute review. It gives you a bit more confidence for the exam.")
    else:
        print("Invalid choice. Please choose 'relax' or 'prepare'.")

# For practicing
if study_or_practice == "practice":
    if event_day == "relax":
        print("You decide to take it easy before the game.")
    elif event_day == "prepare":
        print("You do some final drills to sharpen your skills before the game.")
    else:
        print("Invalid choice. Please choose 'relax' or 'prepare'.")

# The game will now ask about the player's final evaluation, whether they feel ready, and the outcome will depend on their preparation and confidence level on a 1-10 scale.
final_decision = 0

if study_or_practice == "study":
    final_decision = study_time
elif study_or_practice == "practice":
    final_decision = practice_time

# Final evaluation based on preparation and confidence
if final_decision < 3:
    print(player_name + ", you walk into the exam unprepared.")
elif 3 <= final_decision <= 6:
    print(player_name + ", you walk into the exam somewhat ready.")
else:
    print(player_name + ", you walk into the exam feeling very confident.")

# The game concludes with a personalized message.
focus_choice = study_or_practice
if (focus_choice== "study" and study_time > 5) or (confidence_level > 7.0 and event_day == "prepare"):
    print(player_name + ", you have a great chance of succeeding in your exam!")
elif (focus_choice == "practice" and practice_time > 5) or (confidence_level > 7.0 and event_day == "prepare"):
    print(player_name + ", you're sure to perform great in your game!")
else:
    print(player_name + ", you might need to put in more effort to succeed.")