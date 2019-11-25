# File: week4_fiberOpticCableDiscountFunction.py


# Name: Gabriel Valenzuela

# Date: 09/19/2019


# Course: DSC 510 - Introduction to Programming


# Purpose: To calculate order costs of optic fiber for an individual including any possible bulk discounts


#          and their company dependent on the amount of cable ordered


#          along with providing a receipt for the order


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


print("Welcome to Optic Fiber Installation & Sons\n")

nameCompany = input('What is the name of your company? ')

numFiberOpticCableLength = float(input('How much feet of fiber optic cable would you like to order? '))

costPerFootLessThan100 = 0.87  # cost for optic fiber cable per foot under 100

costPerFootMoreThan100 = 0.80  # cost for optic fiber cable per foot over 100 feet and under 250

costPerFootMoreThan250 = 0.70  # cost for optic fiber cable per foot over 250 feet and under 500

costPerFootMoreThan500 = 0.50  # cost for optic fiber cable per foot over 500 feet


def calculate_fiberLength(length, cost):
    total = round(length * cost, 2)
    return total


if numFiberOpticCableLength <= 100:
    costOfFiber = costPerFootLessThan100
    orderCost = calculate_fiberLength(numFiberOpticCableLength, costOfFiber)
elif numFiberOpticCableLength > 100 and numFiberOpticCableLength <= 250:
    costOfFiber = costPerFootMoreThan100
    orderCost = calculate_fiberLength(numFiberOpticCableLength, costOfFiber)
elif numFiberOpticCableLength > 250 and numFiberOpticCableLength <= 500:
    costOfFiber = costPerFootMoreThan250
    orderCost = calculate_fiberLength(numFiberOpticCableLength, costOfFiber)
elif numFiberOpticCableLength > 500:
    costOfFiber = costPerFootMoreThan500
    orderCost = calculate_fiberLength(numFiberOpticCableLength, costOfFiber)

totalCost = orderCost

print(" \nOptic Fiber Installation & Sons Receipt")

print(" - - - - - - - - - - - - - - - - - - - - \n")

print("Name of Company: ", nameCompany, "\n")

print("Fiber Optic Cable Ordered: ", numFiberOpticCableLength, "feet\n")

print("Order Cost: $", orderCost, "\n")

print("Total Cost: $", totalCost, "\n")

print(" - - - - - - - - - - - - - - - - - - - - ")
