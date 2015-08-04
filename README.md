# UDPRedistributePyProxy
Script de python que actúa como proxy local para redistribuir paquetes recibidos en un puerto entre otros puertos, siguiendo un orden secuencial para la repartición.

Usage: UDPRedistributePyProxy.py [options]

Options:
  -h, --help            show this help message and exit
  -v, --verbose         Muestra detalles de la operacion del proxy
  -p hookPortValue, --hook_port=hookPortValue
                        El puerto a interceptar
  -s startRedirectPortValue, --start_redirect_port=startRedirectPortValue
                        Puerto inicial para redirigir datos
  -n numberRedirectPortsValue, --number_redirect_ports=numberRedirectPortsValue
                        cantidad de puertos a redirigir