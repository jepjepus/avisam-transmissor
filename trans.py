#! /usr/bin/python

from xbee.thread import ZigBee
import serial
import time

def main():
    """
    Sends an API AT command to read the lower-order address bits from
    an XBee Series 1 and looks for a response
    """
    try:

        # Open serial port
        ser = serial.Serial('/dev/ttyUSB5', 9600)

        # Create ZigBee Series 1 object
        zbee = ZigBee(ser)


        # Send
        while True:
            zbee.send('tx', dest_addr_long=b'\x00\x13\xA2\x00\x40\xB8\xF8\x07', dest_addr='\xC4\x5C', data=b'HOLA HAFID')
            time.sleep(1.00)
    except KeyboardInterrupt:
        pass
    finally:
        ser.close()

if __name__ == '__main__':
    main()
