# Weather API

## Introduction to Programming

### Objective

The goal of this introduction project is to allow the user to look up the general weather by city or zip code by connecting to OpenWeatherApp API. The source code can be located in the "Final Project" folder within this repo. 

![Sun Logo](https://github.com/gabriel-valenzuela/Valenzuela_Gabriel_DSC510/blob/master/WeatherIcon.png)

### Environment

Python was utilized within PyCharm to complete the database.

![PyCharm Logo](https://github.com/gabriel-valenzuela/Valenzuela_Gabriel_DSC510/blob/master/PyCharmIcon.jpg)

### Methods

The application will welcome the user to the weather program and inform them if they are able to connect to the weather service.

```python
import requests

def main():
    print("Welcome to the Weather Wizard!")
    try:
        hearWeather()
    except:
        print("The wizard is unable to access the weather at this time.")
        print("Please check in at another time! Thank you for supporting the wizard!")

```
It will then ask the user if they would like to hear the weather once connected

```python
def hearWeather():
    userResponse = "yes"
    while userResponse == "yes" or userResponse == "y":
        userResponse = input("\nWould you like to know the weather? (yes/y or no/n): ").lower()
        if userResponse == "yes" or userResponse == "y":
            locationWeather()
        else:
            print("\nMaybe another time! BYE!")
```

If agreed, the user will enter a zip code or city which will then call on the program to use the appropriate API key for the user and try to connect to the OpenWeatherApp API using the zip code/city that was given by the user. If the program is unable to connect to the API based on an incorrect key, it alert that to the user. If the zip code/city given was typed incorrectly or does not exist, it will alert the user that is was not an acceptable zip code. If the program is able to connect to the zip code, it will then call on weatherPrint() to print the weather details and it will also alert the user that it was able to connect to the API.

City
```python
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

```

Zip Code
```python
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
```
### Conlcusion

When it comes to this project, it will allow a user to determine the weather for a city or zip code that is entered into the program. At the same time, the program is able to determine if the city or zip code entered does not exist and informs the user to attempt to re-enter the details once more again. With this program, the user is able to connect to a Weather API that will determine the weather in real-time for them. 
