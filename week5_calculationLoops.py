# File: week5_calculationLoops.py
# Name: Gabriel Valenzuela
# Date: 09/29/2019
# Course: DSC 510 - Introduction to Programming
# Purpose: To calculate an answer based on the operator inputted by the user and two numbers. At the same time,
#          it will ask the user how many numbers they would like to average and what numbers they would like to average
#          then it will produce the average for the user. The program is ran under a loop to ask if the user would
#          like to run calculations and if they would like to continue doing so.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Function: main()
# Desc: Function contains the main loop of the program asking if the user would like to perform
#       calculations and what type of calculation. It will run the loop until the user enters a
#       a value other than 'Y'
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def main():
    x = 'Y'
    while x == 'Y':
        x = input("Would you like to perform calculations? Enter 'Y' ")
        if x == 'Y':
            print("Time for some calculations!")
            operatorChosen = input('What operation would you like to perform:\n'
                                   'Addition is +\nSubtraction is -\nMultiplication is *\nDivision is /\n')
            performCalculation(operatorChosen)
            calculateAverage()
        else:
            print("We can do some calculations another time! BYE!")


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Function: performCalculation(operator)
# Desc: Function will calculate a result based on the operator and two numbers inputted by the user.
#
# In:   string operator - calculation operator such as +, -, *, or /
# Out:  none
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def performCalculation(operator):
    firstNumber = float(input("What is the first number for the calculation? "))
    secondNumber = float(input("What is the second number for the calculation? "))
    if operator == "+":
        result = firstNumber + secondNumber
    elif operator == "-":
        result = firstNumber - secondNumber
    elif operator == "*":
        result = firstNumber * secondNumber
    elif operator == "/":
        result = firstNumber / secondNumber
    print(firstNumber, " ", operator, " ", secondNumber, " = ", result)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Function: calculateAverage()
# Desc: Function will calculate the average based on the amount of numbers and which numbers inputted by the user.
#
# In:   none
# Out:  none
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def calculateAverage():
    averageList = []
    amountOfNumbers = int(input("How many numbers would you like to average? "))
    for _ in range(int(amountOfNumbers)):
        value = float(input("Enter number: "))
        averageList.append(value)
    totalNumber = sum(averageList)
    average = float(totalNumber / amountOfNumbers)
    print("The average is: ", average)


main()
