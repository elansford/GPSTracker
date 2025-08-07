# Imports libraries for using the system date and time
import time
import datetime as dt

#imports modules for networking and reading the sensors
import network
import socket
from machine import Pin, I2C
import bme280

#imports file creation library
import csv

#Initialize network settings
ssid = 'Cisco05250' #Your network name
password = 'goober1234567' #Your WiFi password

#initialize I2C
#i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

#Connect to WLAN
def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

#Initialize x as 0 to limit my 'while' loop this won't be in the final version
x = 0
#while loop to simulate receiving GPS and weather data from sensors
while x < 6:
    #The print statement in this block are only so I can see what is
    #going on during development, they will not be in the final version.

    #forces the date/time variable to update every loop
    t = dt.datetime.now()
    #pulls new data from the weather sensor every loop
    bme = bme280.BME280(i2c=i2c)
    temp = bme.values[0]
    pressure = bme.values[1]
    humidity = bme.values[2]
    # formats the output
    t1 = t.strftime("%Y" + "," + "%m" + "," + "%d" + "," + "%H:%M:%S" + "temp" + "pressure" + "humidity")
    print(t1)

    #opens data file to store readings in
    file = open('rawdata.csv', "a")
    file.write("\n" + t1)

    #waits two seconds to iterate. This will be increased to five or ten minutes in the final code
    time.sleep(2)
    x += 1

file.close()
#Just to clean things up. I don't think I technically need it anymore but it's how
#I learned and it doesn't break anything.
quit()

