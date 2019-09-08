# File: week2_fiberOpticCable.py

# Name: Gabriel Valenzuela

# Date: 09/07/2019

# Course: DSC 510 - Introduction to Programming

# Purpose: To calculate installation costs of optic fiber for an individual

#          and their company along with providing a receipt for the installation

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


print("Welcome to Optic Fiber Installation & Sons\n")

nameCompany = input('What is the name of your company? ')

numFiberOpticCableLength = float(input('How much feet of fiber optic cable would you like to order? '))

costPerFoot = 0.87  # cost optic fiber cable per foot

orderCost = round(numFiberOpticCableLength * costPerFoot, 2)

totalCost = orderCost

print(" \nOptic Fiber Installation & Sons Receipt")

print(" - - - - - - - - - - - - - - - - - - - - \n")

print("Name of Company: ", nameCompany, "\n")

print("Fiber Optic Cable Ordered: ", numFiberOpticCableLength, "feet\n")

print("Order Cost: $", orderCost, "\n")

print("Total Cost: $", totalCost, "\n")

print(" - - - - - - - - - - - - - - - - - - - - ")
