
import time
import grovepi
import math

# Connections
sound_sensor = 0              # port A0
light_sensor = 1              # port A1
temperature_sensor = 2        # port D2
green_led = 3                 # port D3
blue_led =4                    # port D4
red_led = 5                    # port D5

while True:


    # Error handling in case of problems communicating with the GrovePi
    try:

         # Get value from light sensor
        light_intensity = grovepi.analogRead(light_sensor)
        
        # Give PWM output to LED
        grovepi.analogWrite(led,light_intensity/4)
        
         # Get value from temperature sensor
        [t,h]=[0,0]
        [t,h] = grovepi.dht(temperature_sensor,0)

    except IOError:
        print("Error")
    except KeyboardInterrupt:
        exit()
    except Exception as e:
          print("Duplicate Tweet or Twitter Refusal: {}".format(e))

    time.sleep(30)