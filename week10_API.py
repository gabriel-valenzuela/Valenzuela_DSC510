# File: week10_API.py
# Name: Gabriel Valenzuela
# Date: 11/3/2019
# Course: DSC 510 - Introduction to Programming
# Purpose: To ask the user if they would like to hear a Chuck Norris joke. If yes, the program will request a joke from
#           https://api.chucknorris.io/jokes/random and display it to the user, If not, it will say goodbye to the user
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import requests
import json

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Function: getJoke()
# Desc: Function will make a GET request to the URL which provides a Chuck Norris Joke upon each request. It will then
#       parse the JSON response into a dictionary. From there, it will then return the joke from the dictionary.
#
# In:   none
# Out:  string - the joke that was obtained from the request to the url
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def getJoke():
    url = "https://api.chucknorris.io/jokes/random"
    querystring = {"zip": "68144","APPID":"d5751b1a9e2e4b2b8c7983646072da8b"}
    headers = {'cache-control': 'no-cache'}
    response = requests.request("GET",url,headers=headers,params=querystring)
    json_data = (json.loads(response.text))
    return json_data["value"]


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Function: hearJoke()
# Desc: Function contains a loop asking if the user would like to hear a Chuck Norris joke.
#       It will run the loop until the user enters a value other than "y" or "yes". If the user enters a "yes" or "y",
#       it will tell the user to wait while it calls getJoke().
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def hearJoke():
    userResponse = "yes"
    while userResponse == "yes" or userResponse == "y":
        userResponse = input("Would you like to hear a Chuck Norris joke? (yes/y or no/n): ").lower()
        if userResponse == "yes" or userResponse == "y":
            print("Give me a second!")
            joke = getJoke()
            print(joke)
        else:
            print("Maybe another time! BYE!")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Function: main()
# Desc: Function will welcome the user and then call hearJoke() to question the user
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def main():
    print("Welcome to the World of Chuck Norris Jokes!")
    hearJoke()


main()
