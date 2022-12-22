import datetime as dt
import requests
import geocoder
import random
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def get_current_location():
    #Give the current latitud and longitud
    g = geocoder.ip('me')
    address = g.address
    cityGeo = address.split(",")
    lat_lon = g.latlng
    
    return cityGeo[0]

cities= ['Arrigorriaga','Lemona','Salamanca','Madrid','Zamora','Pamplona','Zaragoza','Palencia','Valencia','Sevilla','Granada','Jaen']
def random_city():
    result1 = random.choice(cities)
    return result1

#ENV
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "9aeb49edeaa630b5f221bf6bd0d45da9"
ci = random_city()

#FUNCTIONS
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def url(c):
    #URL
    url = BASE_URL + "appid="+ API_KEY + "&q="+ c
    response = requests.get(url).json()
    return response
response = url(ci)

def __main__(CITY,response):

    #TEMPERATURE
    temp_kelvin = response['main']['temp']
    temp_celsius = kelvin_to_celsius(temp_kelvin)

    #TEMPERATURE FEELS LIKE
    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius = kelvin_to_celsius(feels_like_kelvin)

    #HUMIDITY
    humidity = response['main']['humidity']

    #CLOUDS
    clouds = response['clouds']['all']

    #WIND SPEED
    wind_speed = response['wind']['speed']

    #MAIN AND DESCRPTION
    main = response['weather'][0]['main']
    description = response['weather'][0]['description']

    #SUNRISE - SUNSET TIME
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

    print(f"Temperature in {CITY} : {temp_celsius:.2f}ºC")
    print(f"Temperature in {CITY} feels like : {feels_like_celsius:.2f}ºC")
    print(f"Clouds in {CITY} : {clouds}%")
    print(f"Humidity in {CITY} : {humidity}%")
    print(f"Wind speed in {CITY} : {wind_speed}m/s")
    print(f"General weather in {CITY} : {main}")
    print(f"Description weather in {CITY} : {description}")
    print(f"Sunrises in {CITY} : {sunrise_time} local time")
    print(f"Sunsets in {CITY} : {sunset_time} local time")
    
    temp_celsius_interface = kelvin_to_celsius(temp_kelvin)
    temp_celsius_interface_round = round(temp_celsius_interface,2)
    clouds_interface = clouds
    wind_speed_interface = wind_speed
    wind_speed_interface_round = round(wind_speed_interface,2)

    temp_celsius_int = int(temp_celsius)
    clouds_int = int(clouds)
    wind_speed_int = int(wind_speed)
    humidity_int = int(humidity)

    #Recogida de variables y marcaje de rangos
    temp_celsius = ctrl.Antecedent(np.arange(0,50,1),'temp_celsius')
    clouds = ctrl.Antecedent(np.arange(0,100,1),'clouds')
    wind_speed = ctrl.Antecedent(np.arange(0,30,1),'wind_speed')

    result = ctrl.Consequent(np.arange(0,100,1),'result')

    temp_celsius['cold'] = fuzz.trimf(temp_celsius.universe, [0,3,15])
    temp_celsius['confortable'] = fuzz.trimf(temp_celsius.universe, [10,17,24])
    temp_celsius['hot'] = fuzz.trimf(temp_celsius.universe, [22,35,50])

    clouds['clear'] = fuzz.trimf(clouds.universe, [0,20,30])
    clouds['cloudy'] = fuzz.trimf(clouds.universe, [25,55,70])
    clouds['extremlyCloudy'] = fuzz.trimf(clouds.universe, [65,100,100])

    wind_speed['nonWind'] = fuzz.trimf(wind_speed.universe, [0,3,5])
    wind_speed['windy'] = fuzz.trimf(wind_speed.universe, [3,9,15])
    wind_speed['extremlyWindy'] = fuzz.trimf(wind_speed.universe,[10,15,30])

    result['green'] = fuzz.trimf(result.universe, [0,0,25])
    result['yellow'] = fuzz.trimf(result.universe, [25,40,60])
    result['red'] = fuzz.trimf(result.universe, [55,100,100])


    rule1 = ctrl.Rule(temp_celsius['hot'] & clouds['clear'] & wind_speed['nonWind'], result['green'])
    rule2 = ctrl.Rule(temp_celsius['hot'] & clouds['clear'] & wind_speed['windy'],result['green'])
    rule3 = ctrl.Rule(temp_celsius['hot'] & clouds['clear'] & wind_speed['extremlyWindy'],result['yellow'])

    rule4 = ctrl.Rule(temp_celsius['hot'] & clouds['cloudy'] & wind_speed['nonWind'],result['green'])
    rule5 = ctrl.Rule(temp_celsius['hot'] & clouds['cloudy'] & wind_speed['windy'],result['yellow'])
    rule6 = ctrl.Rule(temp_celsius['hot'] & clouds['cloudy'] & wind_speed['extremlyWindy'],result['red'])

    rule7 = ctrl.Rule(temp_celsius['hot'] & clouds['extremlyCloudy'] & wind_speed['nonWind'],result['green'])
    rule8 = ctrl.Rule(temp_celsius['hot'] & clouds['extremlyCloudy'] & wind_speed['windy'],result['yellow'])
    rule9 = ctrl.Rule(temp_celsius['hot'] & clouds['extremlyCloudy'] & wind_speed['extremlyWindy'],result['red'])

    rule10 = ctrl.Rule(temp_celsius['confortable'] & clouds['clear'] & wind_speed['nonWind'],result['green'])
    rule11 = ctrl.Rule(temp_celsius['confortable'] & clouds['clear'] & wind_speed['windy'],result['green'])
    rule12 = ctrl.Rule(temp_celsius['confortable'] & clouds['clear'] & wind_speed['extremlyWindy'],result['yellow'])

    rule13 = ctrl.Rule(temp_celsius['confortable'] & clouds['cloudy'] & wind_speed['nonWind'],result['green'])
    rule14 = ctrl.Rule(temp_celsius['confortable'] & clouds['cloudy'] & wind_speed['windy'],result['yellow'])
    rule15 = ctrl.Rule(temp_celsius['confortable'] & clouds['cloudy'] & wind_speed['extremlyWindy'],result['red'])

    rule16 = ctrl.Rule(temp_celsius['confortable'] & clouds['extremlyCloudy'] & wind_speed['nonWind'],result['yellow'])
    rule17 = ctrl.Rule(temp_celsius['confortable'] & clouds['extremlyCloudy'] & wind_speed['windy'],result['yellow'])
    rule18 = ctrl.Rule(temp_celsius['confortable'] & clouds['extremlyCloudy'] & wind_speed['extremlyWindy'],result['red'])

    rule19 = ctrl.Rule(temp_celsius['cold'] & clouds['clear'] & wind_speed['nonWind'],result['green'])
    rule20 = ctrl.Rule(temp_celsius['cold'] & clouds['clear'] & wind_speed['windy'],result['green'])
    rule21 = ctrl.Rule(temp_celsius['cold'] & clouds['clear'] & wind_speed['extremlyWindy'],result['yellow'])

    rule22 = ctrl.Rule(temp_celsius['cold'] & clouds['cloudy'] & wind_speed['nonWind'],result['yellow'])
    rule23 = ctrl.Rule(temp_celsius['cold'] & clouds['cloudy'] & wind_speed['windy'],result['red'])
    rule24 = ctrl.Rule(temp_celsius['cold'] & clouds['cloudy'] & wind_speed['extremlyWindy'],result['red'])

    rule25 = ctrl.Rule(temp_celsius['cold'] & clouds['extremlyCloudy'] & wind_speed['nonWind'],result['red'])
    rule26 = ctrl.Rule(temp_celsius['cold'] & clouds['extremlyCloudy'] & wind_speed['windy'],result['red'])
    rule27 = ctrl.Rule(temp_celsius['cold'] & clouds['extremlyCloudy'] & wind_speed['extremlyWindy'],result['red'])

    #1 Recoger reglas
    result_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27])
    resultN = ctrl.ControlSystemSimulation(result_ctrl)

    #Hacemos esto para que en caso de que alguna variable sea 0, sumemos 1 y no crashe el script por out of range del modelo
    if(temp_celsius_int==0):
        temp_celsius_int = temp_celsius_int+1
        
    if(clouds_int == 0):
        clouds_int = clouds_int + 1
    if(wind_speed_int == 0):
        wind_speed_int = wind_speed_int + 1

    #2 Meter valores de entrada
    resultN.input['temp_celsius'] = temp_celsius_int
    resultN.input['clouds'] = clouds_int
    resultN.input['wind_speed'] = wind_speed_int

    print("\nValores de entrada:")
    print(" Temperatura: {}".format(temp_celsius_int))
    print(" Nubes: {}".format(clouds_int))
    print(" Viento: {}\n".format(wind_speed_int))

    #3 Computar y crear valor numerico de salida
    resultN.compute()
    final_result = resultN.output['result']
    final_result_int = int(final_result)
    final_result_interface = final_result_int
    print("El resultado que se obtiene en {}: {}/100".format(CITY,final_result_int))
    
    #4 Seleccion de color dependiendo de temperatura
    if (final_result_int <40):
        color = "Green"
        print("El color del led sera GREEN (0,255,0)")
    elif (final_result_int >=40 | final_result_int<=70):
        color = "Yellow"
        print("El color del led sera YELLOW (230,230,10)")
    elif(final_result_int >70):
        color = "Red"
        print("El color del led sera RED (255,0,0)")
    else:
        print("ERROR colorway no seleccionado")
        
    temp_celsuis_str = str(temp_celsius_int)
    humidity_str = str(humidity_int)
    clouds_str = str(clouds_int)
    wind_speed_str = str(wind_speed_int)
    final_result_str = str(final_result_int)
    
    url_db = 'http://corlysis.com:8087/write'
    params = {"db": "safe_drivers", "u": "token", "p":"cfc1067a1f4d9f8a5a5f56f8ff624f3f"}
    payload = "temperature,place="+ci+" value="+temp_celsuis_str+"\n wind_speed,place="+ci+" value="+wind_speed_str+"\n humidity,place="+ci+" value="+humidity_str+"\n clouds,place="+ci+" value="+clouds_str+"\n result,place="+ci+" value="+final_result_str+"\n "
    r = requests.post(url_db, params=params, data=payload)
    print(r)
    
    return temp_celsius_interface_round,clouds_interface,wind_speed_interface_round,final_result_interface,color


    


    



