# File: week3_fiberOpticCableDiscount.py

# Name: Gabriel Valenzuela

# Date: 09/15/2019

# Course: DSC 510 - Introduction to Programming

# Purpose: To calculate order costs of optic fiber for an individual including any possible bulk discounts

#          and their company dependent on the amount of cable ordered

#          along with providing a receipt for the order

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


print("Welcome to Optic Fiber Installation & Sons\n")

nameCompany = input('What is the name of your company? ')

numFiberOpticCableLength = float(input('How much feet of fiber optic cable would you like to order? '))

costPerFootLessThan100 = 0.87  # cost for optic fiber cable per foot under 100 feet
costPerFootMoreThan100 = 0.80  # cost for optic fiber cable per foot over 100 feet and under 250 feet
costPerFootMoreThan250 = 0.70  # cost for optic fiber cable per foot over 250 feet and under 500 feet
costPerFootMoreThan500 = 0.50  # cost for optic fiber cable per foot over 500 feet

if numFiberOpticCableLength <= 100:
  orderCost = round(numFiberOpticCableLength * costPerFootLessThan100, 2)
elif numFiberOpticCableLength > 100 and numFiberOpticCableLength <= 250:
  orderCost = round(numFiberOpticCableLength * costPerFootMoreThan100, 2)
elif numFiberOpticCableLength > 250 and numFiberOpticCableLength <= 500:
  orderCost = round(numFiberOpticCableLength * costPerFootMoreThan250, 2)
elif numFiberOpticCableLength > 500:
  orderCost = round(numFiberOpticCableLength * costPerFootMoreThan500, 2)

totalCost = orderCost

print(" \nOptic Fiber Installation & Sons Receipt")

print(" - - - - - - - - - - - - - - - - - - - - \n")

print("Name of Company: ", nameCompany, "\n")

print("Fiber Optic Cable Ordered: ", numFiberOpticCableLength, "feet\n")

print("Order Cost: $", orderCost, "\n")

print("Total Cost: $", totalCost, "\n")

print(" - - - - - - - - - - - - - - - - - - - - ")
