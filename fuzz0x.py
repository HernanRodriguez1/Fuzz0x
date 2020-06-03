#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import urllib2,cookielib
import sys
import shodan
from fake_useragent import UserAgent
import time

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

#----------Obtener nuestra IP Publica---------
ip = urllib2.urlopen('http://ident.me').read()
print ('Tu IP Publica es: '+ip)

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

URL = ('https://www.open-sec.com/') #https://www.example.com o http://wwww.example.com
banner = urllib2.Request(URL, headers=cabecera)

try:
    pagina = urllib2.urlopen(banner)
except:
    print ('[*] Error de conectividad con el servidor web'+'\n')
    sys.exit()

contenido = pagina.info()
print contenido

Carpeta = ('') #Elabora el fuzzing en un directorio del servidor
diccionario = ('test.txt') #Ingrese la ruta de archivo

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
print '\n'+"Recopilación de información con shodan"+'\n'

#---------------------API SHODAN-----------------------	


try:
    Key = 'WmoZbOoF5wjX2KDPtb442MLAR4FWCVlm' 
    api = shodan.Shodan(Key)
    target = ("open-sec.com")

    dnsResolve = 'https://api.shodan.io/dns/resolve?hostnames=' + target + '&key=' + Key


    resolved = requests.get(dnsResolve)
    hostIP = resolved.json()[target]
    
    #Obteniendo Banner Grabbing
    host = api.host(hostIP)
    print '\n'+"===================IFORMACIÓN SHODAN================"
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
                
                     
    file = open('shodan.txt','a+')
    for elemento in host['data']:
        lista = elemento.keys()
        for l in lista:
                     file.write(str(elemento[l]))

    file.close()

except:
        print 'Error consulta Shodan'
