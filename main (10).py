# Programmers: Judy Rivas, Andrei Zivkovic
# Course: CS151, Professor Ebert
# Due Date: 02/12/25
# Programming Assignment: Lab 3
# Problem Statement: Determine the future expected population for a country
# Data In: Seconds between births, seconds between deaths, seconds between immigration, current population, years into the future
# Data Out: Expected population and whether population increased or decreased


print("This program will determine the expected population in the future for a country of your choice.")
print("We will need some information from you to determine the expected population.")

# Data input to get calculations
seconds_between_births = input("what is the seconds_between_births")
seconds_between_births = float(seconds_between_births)

seconds_between_deaths = input("what is the seconds_between_deaths")
seconds_between_deaths = float(seconds_between_deaths)

seconds_between_immigrations = input("what is the seconds_between_immigration")
seconds_between_immigrations = float(seconds_between_immigrations)

current_population = input("what is the current_population")
current_population = float(current_population)

Years_into_the_future = input("How many years_into_the_future")
Years_into_the_future = float(Years_into_the_future)

# Number of seconds in one year
seconds_per_year = 60 * 60 * 24 * 365



#Calculations for future population

births_per_year = seconds_per_year / seconds_between_births

deaths_per_year = seconds_per_year / seconds_between_deaths

immigrants_per_year = seconds_per_year / seconds_between_immigrations

yearly_population_change = births_per_year - deaths_per_year + immigrants_per_year

future_population = current_population + yearly_population_change * Years_into_the_future

# If statements to determine whether there is a population increase or decrease
if future_population > current_population:
    print("population increase")

elif future_population < current_population:
    print("population decrease")
