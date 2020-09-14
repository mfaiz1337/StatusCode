#!/usr/bin/env python
# Coding: utf-8
# Made By Md. Faizal

'''
=====================================================================
This tool purpose for check http status code.

Advance Option created By Md. Faizal 
=====================================================================
'''
__author__ = "Md. Faizal"
__version__ = "croll 1.0dev"
import requests
import time
import sys
import re
import os
import socket
import urllib3
from modules.color import Fcolor
subdo = []

subdomain = []

print(Fcolor.cyan+50*".")
inp = input(Fcolor.yellow+"[i] Enter Subdomain File Path: ")
print(50*".")
if os.path.isdir(inp) == False:
    try:
        readfile = open(inp, "r")
        filesw = readfile.readlines()
        for i in filesw:
            subdomain.append(i.replace("\n",""))
    except FileNotFoundError:
        print(Fcolor.red+'[err]'+Fcolor.cyan+' File not Found')
        sys.exit()
        

else:
    print(Fcolor.red+"[err]"+Fcolor.cyan+" File PATH Directory Not Found ")
print(Fcolor.white+"\nTotal Subdomain Found :",Fcolor.cyan+str(len(subdomain)))
print(Fcolor.yellow+"SCode".center(0)+"Domain".center(25)+"IP".center(25))
print(Fcolor.purple+50*"_")
for x in range(len(subdomain)):
    try:
        nb = socket.gethostbyname(subdomain[x])
        req = requests.get("http://"+subdomain[x])
        print(Fcolor.black+str(req.status_code)," | ", Fcolor.blue+req.url," | ", Fcolor.cyan+nb)
    except socket.gaierror:
        print(Fcolor.red+"[!] Host Not Found: ",Fcolor.blue+subdomain[x])

    except socket.error:
        print(Fcolor.red+"[!] Not Connected: ", Fcolor.blue+subdomain[x])

    except urllib3.exceptions.NewConnectionError:
        print("New Connection Error")
    except requests.exceptions.ConnectionError:
        print("Conection Error ")
    except urllib3.exceptions.MaxRetryError:
        print("Over Retry")
    except KeyboardInterrupt:
        time.sleep(1)
        print(Fcolor.red+"Exit..."+"\033[1;1;0m")
        time.sleep(1)
        break
        sys.exit()






