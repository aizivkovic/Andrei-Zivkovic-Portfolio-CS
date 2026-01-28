# Programmers:Lauren Duffy & Anderi Zivkovic
# Course:CS151
# Due Date:2/19/25
# Lab Assignment:4
# Problem Statement: Determine how far the skier will jump based on the high and speed in witch they are going
# Data In:
# Data Out:
# Credits: class Lab

import math

print("This program will calculate the number of points a skier will recieve based off a large or normal jump")

hill_size=input("Please tell us the height of the hill. Normal or large?").lower().strip()

hill_height = 0
par = 0
points_per_meter = 0

if hill_size == "normal":
    hill_height = 46
    par = 90
    points_per_meter = 2
elif hill_size == "large":
    hill_height = 70
    par = 120
    points_per_meter = 1.8
else:
    print("Please enter a valid hill size.")

#Get the jumper's speed
jumpers_speed = float(input("what is your jumping speed (in meters/second)?"))


#calculate the time in air
time_in_air = math.sqrt((2 * hill_height) / 9.8)
print("time in air"+ str(time_in_air))

#calculate distance
distance = jumpers_speed * time_in_air
print("distance"+str(distance))

#calculate total points
total_points = 60 + (distance - par) * points_per_meter
print("total points" + str(total_points))

#output the results
print("Distance jumped: " +str(round(distance, 2)) + " meters")
print("Points earned: " +str(round(total_points, 2)))

#results with points
if total_points >= 61:
    print("Great job for doing better than par!")
elif total_points < 10:
    print("What happened?")
else:
    print("Sorry you didn't go very far.")

