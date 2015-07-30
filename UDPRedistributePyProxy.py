#!/usr/bin/env python
import sys, socket
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, help="Muestra detalles de la operacion del proxy")
parser.add_option("-p", "--hook_port", dest="hookPort", help="El puerto a interceptar", metavar="hookPortValue")
parser.add_option("-s", "--start_redirect_port", dest="startRedirectPort", help="Puerto inicial para redirigir datos", metavar="startRedirectPortValue")
parser.add_option("-n", "--number_redirect_ports", dest="numberRedirectPorts", help="cantidad de puertos a redirigir", metavar="numberRedirectPortsValue")
(options, args) = parser.parse_args()
#eg python cosa.py --verbose --hook_port 8787 --start_redirect_port 9999 --number_redirect_ports 5

BUFF_SIZE = 512

def showErrorMsg(msg):
	sys.stderr.write(msg + '\n')
	sys.exit(1)

#Recuperar Puerto a interceptar
try:
	localPort = int(options.hookPort)
except:
	showErrorMsg('Error en puerto a interceptar: ' + str(options.hookPort))

#Recuperar Puertos a redirigir
try:
	firstRedistributePort = int(options.startRedirectPort)
except:
	showErrorMsg('Error en puertos a redirigir: ' + str(options.startRedirectPort))
try:
	totalPorts = int(options.numberRedirectPorts)
except:
	showErrorMsg('Error en cantidad de puertos a redirigir: ' + str(options.numberRedirectPorts))

redistributePortsArray = range(firstRedistributePort, firstRedistributePort+totalPorts)


#Mostrar Configuracion de operacion
print('LocalPort = '+str(localPort)+', RedistributePorts = '+str(redistributePortsArray))


#Interceptar puerto
try:
	hookSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	hookSocket.bind(('', localPort))
except:
	showErrorMsg('Failed to bind on port ' + str(localPort))

#Crear tuplas para redirigir paquetes
redistributeSockets = []
try:
	for port in redistributePortsArray:
		redistributeTuple = ('', port)
		redistributeSockets.append(redistributeTuple)
except:
	showErrorMsg('Failed to bind on port ' + str(port))	

#Reenviar paquetes a otros puertos
while True:
	data, addr = hookSocket.recvfrom(BUFF_SIZE)
	redistributeTuple = redistributeSockets.pop(0)
	if(options.verbose):
		print(data)
		print(redistributeTuple)
	redistributeSockets.append(redistributeTuple)
	hookSocket.sendto(data, redistributeTuple)