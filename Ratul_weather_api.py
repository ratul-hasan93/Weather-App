# Weather Api
import requests

def format_response(weather_data):
    # format weather data
    try:
        city_name = weather_data['name']
        condition = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        icon_name = weather_data['weather'][0]['icon']
        weather_report = 'City: %s \nCondition: %s \nTemperature (°F): %s ' % (city_name, condition,temperature)

    except:
        weather_report = 'opps!, Faild to retrieving informations'
        icon_name = ''
    return (weather_report, icon_name)
    

def weather_information(city_name):
    # get weather information by calling open weather api
    weather_key = '928e52aa7cbbd11150a8e8b744f5fa6b'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q':city_name, 'units': 'imperial'}
    response = requests.get(url, params)
    weather_data = response.json()
    weather_report = format_response(weather_data)
    return weather_report

# print(weather_information('Dhaka'))
