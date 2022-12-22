import time
import weather_condition as wc
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from grove.grove_light_sensor_v1_2 import GroveLightSensor
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
entry = 0


def main():
    GPIO.output(24,False)
    
    sensor_distance = GroveUltrasonicRanger(22)
    sensor_light = GroveLightSensor(24)
    
    city_location = "Bilbao"
    response = wc.url(city_location)
    temp_celsius_interface_round,clouds_interface,wind_speed_interface_round,final_result_interface,color = wc.__main__(city_location,response)
    entry = 1
    while (True):
        print(color)
        light = sensor_light.light
        distance = sensor_distance.get_distance()
        if(distance < 60.00):
            GPIO.output(24,True)

        else:
            GPIO.output(24,False)
        print(distance)
        
    
    GPIO.output(24,False)

main()

