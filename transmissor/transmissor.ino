#include <XBee.h>
#include <Printers.h>

/*

transmissor xbee arduino ide. proves

EPSEM curs 1718, quadrimestre de tardor, enginyeria de sistemes

Marc Brunet Hafid Karbouch Alejandro Jabalquinto Josep Lladonosa
*/

#include <Wire.h> // el nostre Wire

#include <string.h>

#define ADXL_ADDRESS 0x53 // adreça de l'accelerometre
#define ADXL_DATA 0x32 // adreça dels 6 bytes XYZ 

// Create an XBee object at the top of your sketch
XBee xbee = XBee();

// adxl_read_sb: reads single byte from an ADXL register
byte adxl_llegeix_sb(byte registre)
{
    byte valor;
    Wire.beginTransmission(ADXL_ADDRESS); //seleccionem dispositiu 0x53
    Wire.write(registre); //registre d'on llegirem
    Wire.endTransmission();  
    Wire.requestFrom(ADXL_ADDRESS,1);
    return Wire.read(); //retornem el byte que llegim
}    

// adxl_llegeix_mb: llegeix n bytes des d'un registre i desa a buffer d'enters
// els bytes llegits son en ordre lsb msb lsb msb lsb msb
// retorna el nombre de bytes llegits i buffer queda amb els n/2 enters llegits
byte adxl_llegeix_mb(byte registre, int n, int * buffer) 
{
    Wire.beginTransmission(ADXL_ADDRESS); //seleccionem dispositiu ADXL_ADDRESS
    Wire.write(byte(registre)); //a partir del byte que llegim
    Wire.endTransmission();
    Wire.beginTransmission(ADXL_ADDRESS);
    Wire.requestFrom(ADXL_ADDRESS, n); //llegim n bytes des del registre 
    int i=0;
    while (i<n)
    {
     byte lsb, msb;
     lsb = Wire.read();
     msb = Wire.read();
     *buffer = (msb << 8) | lsb;
     buffer++;
     i+=2;
    }
    Wire.endTransmission();
    return i;
}


void adxl_envia_sb(byte registre, byte valor) // per enviar un sl byte a un registre
{
 Wire.beginTransmission(ADXL_ADDRESS); //seleccionem dispositiu
 Wire.write(registre); //enviem registre on escriure
 Wire.write(valor); //enviem valor
 Wire.endTransmission(); 
}

boolean adxl_present()
{
  // read Device ID. It should be 11100101 = 0xe5 if present
  return (adxl_llegeix_sb(0x00) == 0xe5);
  // if present returns true, else returns false
}


void adxl_configura() //configuracio inicial adxl
{
   adxl_envia_sb(0x2D,0x08); //POWER_CTL, bit D3 (measure)
}

void serie_inicia(void)
{
   // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

}

void wire_inicia(void)
{
   Wire.begin(WIRE_DISABLE_PULLUPS); //start Wire with pullups disabled 
}


void setup()  
{
  serie_inicia();
  //wire_inicia();
  xbee.setSerial(Serial); // Tell XBee to use Hardware Serial. It's also possible to use SoftwareSerial
//  while(!adxl_present()) 
//  {
//  }
//   adxl_configura();
}

void avisa_caiguda(void)
{
  //Serial.print() 
  // Create an array for holding the data you want to send.
  uint8_t payload[] = { 'H', 'i', ' ', 'H', 'a', 'f' };

  // Specify the address of the remote XBee (this is the SH + SL)
  // mac router (18): XBeeAddress64(0x0013a200, 0x40b8f807);
  //XBeeAddress64 addr64 = XBeeAddress64(0x0013a200, 0x408b99f4);
  XBeeAddress64 addr64 = XBeeAddress64(0x0, 0x0);

  // Create a TX Request
  ZBTxRequest zbTx = ZBTxRequest(addr64, payload, sizeof(payload));

  // Send your request
  xbee.send(zbTx);
}



int valor[3]; //lectura xyz de l'adxl

void loop() // run over and over
{
  int i=0;
  //M_STATE estat; // estat obtingut de la maquina d'estats
  while (-1)
  {
    // adxl_llegeix_mb(ADXL_DATA, 6, valor); //llegim 3 int de l'adxl
   //  estat=maquina(valor[0],valor[1],valor[2]); // crida a maquina d'estats
    // if (estat == S_KO ) // caiguda!
     {
       avisa_caiguda(); // mostrem missatge caiguda
       // s.o.s, enviarem un avis VERMELL
       delay(3000); // esperem 1 segon
     }
     //delay(20);
  }
}

