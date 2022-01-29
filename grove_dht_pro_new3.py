#!/usr/bin/env python
#
# GrovePi Example for using the Grove Temperature & Humidity Sensor Pro 
# (http://www.seeedstudio.com/wiki/Grove_-_Temperature_and_Humidity_Sensor_Pro)
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  
# You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this example?  Ask on the forums here:  http://forum.dexterindustries.com/c/grovepi
#
'''
## License
The MIT License (MIT)
GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
from grovepi import *
import math
import json
import time
#from grove_rgb_lcd import *


# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# This example uses the blue colored sensor.
# SIG,NC,VCC,GND
temperature_sensor = 4  # The Sensor goes on digital port 4.

# temp_humidity_sensor_type
# Grove Base Kit comes with the blue sensor.
blue = 0    # The Blue colored sensor.
# white = 1   # The White colored sensor.


# Connections
blue_led =2                   # port D2
light_sensor = 1              # port A1
green_led = 3                 # port D3
temperature_sensor             # port D4
red_led = 5                    # port D5

filename = 'output.txt'
file = open(filename, 'w')

outputData = {}
outputData['measurements'] = []

while True:
    try:
        # This example uses the blue colored sensor. 
        # The first parameter is the port, the second parameter is the type of sensor.
        [temp_celsius,humidity] = dht(temperature_sensor,blue)  
        
        if math.isnan(temp_celsius) == False and math.isnan(humidity) == False:
            temp_f = temp_celsius*(9.0/5) + 32
            if temp_f > 60 and temp_f < 85 and humidity < 80:
              digitalWrite(green_led, 1)
              digitalWrite(blue_led, 0)
              digitalWrite(red_led,0)
            elif temp_f >= 85 and temp_f < 95 and humidity < 80:
              digitalWrite (green_led, 0) 
              digitalWrite(blue_led,1)
              digitalWrite(red_led,0)
            elif temp_f >= 95:
              digitalWrite(red_led,1)
              digitalWrite(blue_led,0)
              digitalWrite(green_led,0)
            elif humidity >= 80:
              digitalWrite(blue_led,1)
              digitalWrite(green_led,1)
              digitalWrite(red_led,0)
              
            #collect data if the  light is daytime
            light_intensity = analogRead(light_sensor)
          #  print(light_intensity)
            if light_intensity > 200:
              print("temp = %.02f F humitemp,dity =%.02f%%"%(temp_f, humidity))   #send temp and humidity to the commnd line
              outputData['measurements'].append({'temperature': temp_f, 'humidity':humidity})
         #   setRGB(200,50,100)
         #   setText("temp: " + str(temp_f) + "F "+ "humidity: " + str(humidity) + "%")  #send temp and humidity to lcd display
            time.sleep(1800)



    except IOError:
        print ("Error")

    except KeyboardInterrupt:
        json.dump(outputData, file)
        file.close()
        print("Writing file...done.")
        break

