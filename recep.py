#! /usr/bin/python

from xbee import XBee
import serial

PORT = '/dev/ttyUSB4'
BAUD_RATE = 9600

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

# Create API object
xbee = XBee(ser,escaped=True)

# Continuously read and print packets
while True:
    try:
        print "waiting"
        response = xbee.wait_read_frame()
        #response = ser.readline();
        print response
    except KeyboardInterrupt:
        break

ser.close()
