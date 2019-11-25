# File: week11_Classes.py
# Name: Gabriel Valenzuela
# Date: 11/10/2019
# Course: DSC 510 - Introduction to Programming
# Purpose: To create a Cash Register class that handles how many items and the total price of the items within an
#           instance of the class.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import locale


class CashRegister:
    """To create a register object that keeps track of its the total amount and cost"""
    items = []
    totalCost = 0

    def __init__(self):
        """Initializes only itself"""
        pass

    def addItem(self, price):
        """Adds the price of the item to the list of items entered by the user"""
        self.items.append(price)

    def getTotal(self):
        """Returns the total price of the items in the list"""
        for price in self.items:
            self.totalCost = self.totalCost + price
        return self.totalCost

    def getCount(self):
        """Returns the amount of items in the list"""
        return self.items.__len__()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Function: quitPrint(register)
# Desc: Function will print out the total amount and price of the register in the correct format
#
# In:   object register - an instance of the ClassRegister class
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def quitPrint(register):
    locale.setlocale(locale.LC_ALL, '')
    print("Thank you for shopping!")
    print("Total Items in Cart: ", register.getCount())
    print("Total Price of your Cart: ", locale.currency(register.getTotal(), grouping=True))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Function: main()
# Desc: Function will welcome the user to the store and ask them if they would like to add an item to their cart. From
#       there, they will be asked to enter the price of item. This process will continue until the user no longer
#       wants to add an item. Once this happens, the amount of items in the cart and the total price will be presented
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def main():
    print("Welcome to the Store!")
    register = CashRegister()
    userResponse = "yes"
    while userResponse == "yes" or userResponse == "y":
        userResponse = input("Would you like to add an item to your cart? (yes/y or no/n): ").lower()
        if userResponse == "yes" or userResponse == "y":
            priceOfItem = float(input("What is the price of the item? "))
            register.addItem(priceOfItem)
        else:
            quitPrint(register)

main()
