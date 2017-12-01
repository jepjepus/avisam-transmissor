#! /usr/bin/python
# coding: latin-1

#from xbee import XBee
from xbee import ZigBee
import serial
import telepot
import time

# Posar el nostre valor                             
TOKEN = "382644880:AAHwTuttqr-2vnI_atLFwq6UmFj57GYNGAM"
# Connexi amb el nostre Bot
bot = telepot.Bot(TOKEN)
PORT = '/dev/ttyUSB4'
BAUD_RATE = 9600

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

# Create API object
zigbee = ZigBee(ser,escaped=True)

global ll
ll=[]

def handle(msg, val = ll ):
    # Mostra el missatge per pantalla
    missatge = msg["text"]
    if missatge=="/start":
    # El retorna a l'usuari
        if msg["from"]["id"]  not in  val:
            val+=[msg["from"]["id"]]
            ll = val 

#            
# avisa: procediment
# paràmetres:
#  ll: llista identificadors Telegram dels cuidadors
#  msg: missatge a enviar a la llista
#
def avisa(ll,msg):
    for element in ll:
        bot.sendMessage(int(element), msg)
  
bot.message_loop(handle)

# int2hex: funció
# paràmetre:
#  a caràcter ascii (valor entre 0 i 255)
# retorn:
#  conversió a hexa (val entre 00 i FF)
#
def int2hex(a):
     return "{0:02x}".format(ord(a))

#print int2hex('\0')
#print int2hex('M')
#print int2hex(chr(255))

# Continuously read and print packets             
while True:
    try:
        print "waiting"
        response = zigbee.wait_read_frame()
        res = ""
        for a in response["source_addr_long"]:
            res += int2hex(a) + ":"
        msg="Hi ha hagut caiguda del dispositiu "+res[0:-1]
        print msg
        #avisa(ll,msg) # envia missatge als cuidadors via bot Telegram
	myRouterAL = response["source_addr_long"]
	
	# zigbee.remote_at(dest_addr_long=myRouter, command='DB', frame_id='A')
	# dest_addr=response["source_addr"]
	print "Enviem EI!"
	zigbee.tx(dest_addr_long=myRouterAL, data="EI!", frame_id='A') #enviem un ok
        response2 = zigbee.wait_read_frame() # llegeix missatge dB del caigut
        print response2
        #response = ser.readline();
    except KeyboardInterrupt:
        break

ser.close()
 
