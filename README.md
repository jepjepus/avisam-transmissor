# avisam-transmissor
EPSEM curs 1718, quadrimestre de tardor, integració de sistemes

Marc Brunet Hafid Karbouch Alejandro Jabalquinto Josep Lladonosa

#carpeta "transmissor": avi-sa'm: Codi C i d'arduino IDE per usar un acceleròmetre ADXL345 per detectar caigudes de persones grans. Utilitza biblioteca XBee (ZigBee) per comunicar la caiguda a un supervisor.

./Transmisor_2.py: programari Python del coordinador. Rep avisos de caiguda els mostra i connecta amb el bot de Telegram.


Carpetes addicionals:

./Wire

biblioteca arduino IDE modificada per tal d'admetre la inicialització del bus i2c sense resistències internes de pullup. Habitualment aquestes resistències van lligades a +5 V i el nostre prototip treballa amb +3,3 V. La biblioteca Wire estàndard de l'arduino IDE no contempla aquesta situació i aquesta, modificada i retrocompatible, admet activar(per defecte)/desactivar els pullups interns.

./xbee

biblioteca Python que permet la recepció de trames ZigBee. S'ha modificat per permetre la recepció de les trames amb codis 0x90 i 0x91 les quals es reben en mode ZigBee.

El codi del programari web (Django), donada la seva grandària, es pot baixar des de l'enllaç:

https://github.com/marcbrunet/avis_uni. Es pot baixar en format .zip a https://github.com/marcbrunet/avis_uni/archive/master.zip

