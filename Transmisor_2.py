#! /usr/bin/python

from xbee import XBee
import serial
import telepot
import time

# Posar el nostre valor                             
TOKEN = "382644880:AAHwTuttqr-2vnI_atLFwq6UmFj57GYNGAM"
# Connexi amb el nostre Bot
bot = telepot.Bot(TOKEN)
PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

# Create API object
xbee = XBee(ser,escaped=True)

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

            
def avisa(ll,msg):
    for element in ll:
        bot.sendMessage(int(element), msg)

    
bot.message_loop(handle)



# Continuously read and print packets
while True:
    try:
        print "waiting"
        response = xbee.wait_read_frame()
        mult = len(response["source_addr"])**100
        res = ""
        for a in response["source_addr"]:
            res +=  str(ord(a))+","
        msg="Hi ha hagut caiguda del dispositiu "+res[0:-1]
        avisa(ll,msg)
        print
        print
        #response = ser.readline();
    except KeyboardInterrupt:
        break

ser.close()
 
