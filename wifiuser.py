import sys
import os
import nmap
os.system("clear")
os.system("figlet -f standard Wifi  User")
print
print 'Author : Rahat Khan Tusar(RKT)'
print
print 'Github : https://github.com/r3k4t'
print
print 'Information : This program can get all wifi user ip and mac address.'
print
ip = raw_input("Router IP :")
nm = nmap.PortScanner()
nm.scan('127.0.0.1', '22-443')
nm.command_line()
nm.scaninfo()
nm.all_hosts()
nm.all_hosts()
nm['127.0.0.1'].hostname()
nm['127.0.0.1'].state()
nm['127.0.0.1'].all_protocols()
nm['127.0.0.1']['tcp'].keys()
nm['127.0.0.1'].all_tcp()
print (nm.scan(hosts='192.168.0.0/24', arguments='-n -sP -PE -PA21,23,80,3389'))
