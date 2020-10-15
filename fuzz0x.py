#! /usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import urllib2,cookielib
import sys
import shodan
from fake_useragent import UserAgent
import time
import socket

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
cabecera = {'User-Agent':str(UserAgent.firefox)}
#--Si deseas puedes modificar el USER-AGENT simplemente reemplaza IE--

def request(link):
        try:

                return requests.get(link, headers=cabecera)
        except requests.exceptions.ConnectionError:
                pass

print('Tu User-Agent es: '+str(cabecera)+'\n')

#------------------------Banner Grabbing---------------------------

print ('/nEjemplo: https://www.example.com o http://wwww.example.com')
URL = raw_input('Ingrese URL: ')
banner = urllib2.Request(URL, headers=cabecera)

try:
    pagina = urllib2.urlopen(banner)
except:
    print ('[*] Error de conectividad con el servidor web'+'\n')
    sys.exit()

contenido = pagina.info()
print contenido

r  = requests.get(URL)
data = r.text
print "\n-------------------------Web Crawling------------------------------"
soup = BeautifulSoup(data, 'lxml')
for link in soup.find_all('a'):
    print(link.get('href'))




Carpeta = raw_input('Ingrese un directorio (opcional): ') #Elabora el fuzzing en un directorio si lo requiere.

print '\n'+'EJEMPLO: /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt'+'\n'

diccionario = raw_input('Ingrese la ruta de archivo: ')  #Ingrese la ruta de archivo

#Añadir extensión de archivo
extension1 = ('txt')
extension2 = ('php')
extension3 = ('html')

##----------------------Brute Force - FUZZ-------------------------

print '\n'+'=======================RESULTADO========================'+'\n'

try:
    archivo = open(diccionario,"r")

except:
        print ("No se encuentro diccionario")+'\n'
        sys.exit()

for linea in archivo:
    cadenas = linea.strip()
    directorio_encontrado = URL+Carpeta+'/'+cadenas
    respuesta = request(directorio_encontrado)
    if respuesta.status_code in [301,302,200,401,403,500]:
        print("[+] Encontrado: "+directorio_encontrado+' '+str(respuesta))
        pass
    
    directorio_encontrado = URL+Carpeta+'/'+cadenas+'.'+extension1
    respuesta = request(directorio_encontrado)
    if respuesta.status_code in [301,302,200,401,403,500]:
        print("[+] Encontrado: "+directorio_encontrado+' '+str(respuesta))
        pass

    directorio_encontrado = URL+Carpeta+'/'+cadenas+'.'+extension2
    respuesta = request(directorio_encontrado)
    if respuesta.status_code in [301,302,200,401,403,500]:
        print("[+] Encontrado: "+directorio_encontrado+' '+str(respuesta))
        pass

    directorio_encontrado = URL+Carpeta+'/'+cadenas+'.'+extension3
    respuesta = request(directorio_encontrado)
    if respuesta.status_code in [301,302,200,401,403,500]:
        print("[+] Encontrado: "+directorio_encontrado+' '+str(respuesta))
        pass

pass

#---------------------API hackertarget---------------------- 

print '\n'+"===================OBTENIENDO SUBDOMINIOS================"+'\n'

target = raw_input("Ingrese el nombre de dominio: ")
request = requests.get('https://api.hackertarget.com/hostsearch/?q='+target)
response = request.text
print(response)
pass
#---------------------API SHODAN----------------------- 

print '\n'+"Recopilación de información con shodan"+'\n'

try:
    Key = 'BcF3osQdO171ouiv3Dx3yG8SM5HvphDN' ##Añade API de SHODAN
    api = shodan.Shodan(Key)
    #Obteniendo la IP del servidor
    dnsResolve = 'https://api.shodan.io/dns/resolve?hostnames=' + target + '&key=' + Key

    resolved = requests.get(dnsResolve)
    hostIP = resolved.json()[target]

    #Obteniendo Banner Grabbing
    host = api.host(hostIP)
    print '\n'+"===================INFORMACIÓN SHODAN================"
    print('''

[!] Direccion IP: {}
[!] Ciudad: {}
[!] ISP: {}
[!] Organización: {}
[!] Puertos: {}
[!] Sistema Operativo: {}

    '''.format(host['ip_str'],host['city'],host['isp'],host['org'],host['ports'],host['os']))

except:
        print "Error de API"+'\n'
try:

    for item in host['data']:
        print "Port: %s" % item['port']
        print "Banner: %s" % item['data']


    for item in host['vulns']:
        CVE = item.replace('!','')
        print '[+] VULNERABILIDAD: %s' % item
        exploits = api.exploits.search(CVE)
        for item in exploits['matches']:
            if item.get('cve')[0] == CVE:
                print item.get('description')+'\n'
                time.sleep(1)

    file.close()

except:
        'Error consulta SHODAN'
