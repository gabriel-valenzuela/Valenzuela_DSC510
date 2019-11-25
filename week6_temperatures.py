# File: week5_temperature.py
# Name: Gabriel Valenzuela
# Date: 10/6/2019
# Course: DSC 510 - Introduction to Programming
# Purpose: To allow the user to enter a certain amount of temperatures and determine the highest and lowest of the
#           the temperatures entered by the user
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Function: main()
# Desc: Function calls upon the temperature function
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def main():
    temperatureMaxMin()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Function: performCalculation(operator)
# Desc: Function will ask the user how many temperatures to enter and then determine what the largest and smallest
#       temperature was that the user entered
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def temperatureMaxMin():
    temperatures = []
    amountOfTemps = input("How many temperatures would you like to enter? ")
    for _ in range(int(amountOfTemps)):
        value = float(input("Enter the temperature: "))
        temperatures.append(value)
    maxTemp = max(temperatures)
    minTemp = min(temperatures)
    print("The largest temperature you enntered was: ", maxTemp)
    print("The smallest temperature you enntered was: ", minTemp)
    print("The list of temperatures contains", amountOfTemps, "temperatures")

main()
