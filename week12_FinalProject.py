# File: week12_FinalProject.py
# Name: Gabriel Valenzuela
# Date: 11/16/2019
# Course: DSC 510 - Introduction to Programming
# Purpose: To allow the user to communicate with a weather API that has an appropriate API key
#           that wil allow them to enter a city or zip code that will return the weather for the entered area.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import requests

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Function: getWeatherCity(zipCode)
# Desc: Function will use the appropriate API key for the user and try to connect to the OpenWeatherApp API using the
#       zip code that was given by the user. If the program is unable to connect to the API based on an incorrect key,
#       it alert that to the user. If the zip code given was typed incorrectly or does not exist, it will alert
#       the user that is was not an acceptable zip code. If the program is able to connect to the zip code, it will then
#       call on weatherPrint() to print the weather details and it will also alert the user that it was able to connect
#       to the API.
# In: string zipCode - the zip code of an area
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def getWeatherZip(zipCode):
    try:
        API_key = "0ebb566de6959ef7937173d1147aa159"

        response = requests.get("http://api.openweathermap.org/data/2.5/weather?" +
                                "appid=" + API_key + "&units=imperial" + "&zip=" + zipCode).json()

        if response["cod"] == "404":
            raise Exception("\nThe zip code you entered was invalid for the wizard \nAsk to know the weather again\n")
        elif response["cod"] == 401:
            raise Exception("\nYou did not provide a valid API key for the wizard to use\n"
                            "Please find the right key and try again\n")
        else:
            print("\nThe wizard was able to connect to the weather!\n")
            weatherPrint(response)
    except Exception as e:
        print(e)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Function: getWeatherCity(cityName)
# Desc: Function will use the appropriate API key for the user and try to connect to the OpenWeatherApp API using the
#       city name that was given by the user. If the program is unable to connect to the API based on an incorrect key,
#       it alert that to the user. If the city given was spelled incorrectly or does not exist, it will alert the user
#       that is was not an acceptable city name. If the program is able to connect to the city, it will then call
#       on weatherPrint() to print the weather details and it will also alert the user that it was able to connect to
#       the API.
# In: string cityName - the name of the city
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def getWeatherCity(cityName):
    API_key = "0ebb566de6959ef7937173d1147aa159"
    try:
        response = requests.get("http://api.openweathermap.org/data/2.5/weather?" +
                    "appid=" + API_key + "&units=imperial" + "&q=" + cityName).json()
        if response["cod"] == "404":
            raise Exception("\nThe city you entered was invalid for the wizard \nAsk to know the weather again\n")
        elif response["cod"] == 401:
            raise Exception("\nYou did not provide a valid API key for the wizard to use\n"
                            "Please find the right key and try again\n")
        else:
            print("\nThe wizard was able to connect to the weather!\n")
            weatherPrint(response)
    except Exception as e:
        print(e)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Function: weatherPrint(weather)
# Desc: Function will print out weather details about the area that the user had requested which include the
#       temperature, pressure, humidity, the max temperature, and the min temperature. If a zip code was given, it will
#       print the name of the city for which the zip code is in.
# In: dictionary weather - a dictionary containing all of the weather details about a certain area
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def weatherPrint(weather):
    print("The weather forcast for " + weather["name"] + " is as follows: ")
    print("Weather: " + str(weather["weather"][0]["description"]))
    print("Temperature: " + str(weather["main"]["temp"]) + " degrees Fahrenheit")
    print("Pressure: " + str(weather["main"]["pressure"]))
    print("Humidity: " + str(weather["main"]["humidity"]) + " degrees Fahrenheit")
    print("Max Temperature: " + str(weather["main"]["temp_max"]) + " degrees Fahrenheit")
    print("Min Temperature: " + str(weather["main"]["temp_min"]) + " degrees Fahrenheit")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Function: locationWeather()
# Desc: Function will ask the user for a zip code or the name of a city they would like to know the weather for. It
#       will call the appropriate function based on if a zip code or a name is entered by the user
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def locationWeather():
    userRequest = input("\nWhat city or zip code would you like to know the weather for? ")
    if userRequest.isdigit():
        getWeatherZip(userRequest)
    else:
        getWeatherCity(userRequest)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Function: hearWeather()
# Desc: Function will ask the user if they would like to hear the weather until they say no or any other response
#       instead of "Y" or "YES". If they respond with yes, it call upon locationWeather() to ask for where they
#       would like to know the weather for
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def hearWeather():
    userResponse = "yes"
    while userResponse == "yes" or userResponse == "y":
        userResponse = input("\nWould you like to know the weather? (yes/y or no/n): ").lower()
        if userResponse == "yes" or userResponse == "y":
            locationWeather()
        else:
            print("\nMaybe another time! BYE!")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Function: main()
# Desc: Function will welcome the user to the weather program. It will then try to call hearWeather() to ask the user
#       if they would like to hear the weather. If the method could not be called, it will alert the user that the
#       weather API is not able to be used
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def main():
    print("Welcome to the Weather Wizard!")
    try:
        hearWeather()
    except:
        print("The wizard is unable to access the weather at this time.")
        print("Please check in at another time! Thank you for supporting the wizard!")


main()
