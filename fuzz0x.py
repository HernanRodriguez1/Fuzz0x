#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import urllib2,cookielib
import sys
from fake_useragent import UserAgent

mensaje = '\x1b[1;22m'+"Framework Fuzz0x".capitalize()
print ('\n'+mensaje.center(100, "=")+'\n'+'''

7MM"""YMM                                                   
  MM    `7                                                   
  MM   d   `7MM  `7MM  M"""MMV M"""MMV  ,pP""Yq.  `7M'   `MF'
  MM""MM     MM    MM  '  AMV  '  AMV  6W'    `Wb   `VA ,V'  
  MM   Y     MM    MM    AMV     AMV   8M      M8     XMX    
  MM         MM    MM   AMV  ,  AMV  , YA.    ,A9   ,V' VA.  
.JMML.       `Mbod"YML.AMMmmmM AMMmmmM  `Ybmmd9'  .AM.   .MA.

Fuzz0x - 2020
This project was created by Hernan Rodriguez. 
Copyright under the GPL license'''+'\n')


UserAgent= UserAgent()
cabecera = {'User-Agent':str(UserAgent.IE)} 
# "Si deseas puedes modificar el USER-AGENT simplemente reemplaza IE"

def request(link):
		try:

				return requests.get(link, headers=cabecera)
		except requests.exceptions.ConnectionError:
				pass

print('Tu User-Agent es: '+str(cabecera)+'\n')

URL = raw_input('Ingrese URL: ')
banner = urllib2.Request(URL, headers=cabecera)

try:
    pagina = urllib2.urlopen(banner)
except urllib2.HTTPError, e:
    print e.fp.info()
    sys.exit()

contenido = pagina.info()
print contenido


Carpeta = raw_input('Ingrese PATH si lo requiere: ')
#No es obligatorio añadir una carpeta
diccionario = raw_input("Ingrese la Diccionario: ")
#Añada la ruta de su archivo

try:
	archivo = open(diccionario,"r")

except:
		print ("No se encuentro diccionario")
		sys.exit()


for line in archivo:
	cadenas = line.strip()
	directorio_encontrado = URL+Carpeta+'/'+cadenas
	respuesta = request(directorio_encontrado)


	if respuesta:
		print("[+]Encontrado: "+directorio_encontrado)

