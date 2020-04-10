#!/usr/bin/env python
# Coding: utf-8
# Made By Md. Faizal

'''
=====================================================================
This tool purpose for all subdomain find and check http status code.

Advance Option created By Md. Faizal 
=====================================================================
'''
__author__ = "Md. Faizal"
__version__ = "croll 1.0dev"
import requests
import sys
import spyse
import re
import os
import socket
import urllib3
from modules.color import Fcolor
from modules.banner import banner
print(banner)
subdo = []
spyse = spyse.spyse()

w =  open(os.path.join(sys.path[0],"subdomain.txt"), "w")

def findsub(target):
    subdomain = spyse.subdomains(target,param='domain')
    #do= subdomain["records"]
    for i in subdomain["records"]:
        var = i["domain"]
        subdo.append(var)





r = open(os.path.join(sys.path[0],"subdomain.txt"), 'r')

inpu = str(input(Fcolor.red+"Enter Website without http or https: "+Fcolor.blue))
findsub(inpu)

print(Fcolor.white+"\nTotal Subdomain Found :",Fcolor.cyan+str(len(subdo)))
print(Fcolor.yellow+"SCode".center(0)+"Domain".center(25)+"IP".center(25))
print(Fcolor.purple+50*"_")
for x in range(len(subdo)):
    try:
        nb = socket.gethostbyname(subdo[x])
        req = requests.get("http://"+subdo[x])
        print(Fcolor.black+str(req.status_code)," | ", Fcolor.blue+req.url," | ", Fcolor.cyan+nb)
    except socket.gaierror:
        print(Fcolor.red+"[!] Host Not Found: ",Fcolor.blue+subdo[x])

    except socket.error:
        print(Fcolor.red+"[!] Not Connected: ", Fcolor.blue+subdo[x])

    except urllib3.exceptions.NewConnectionError:
        print("New Connection Error")
    except requests.exceptions.ConnectionError:
        print("Conecttion ")
    except urllib3.exceptions.MaxRetryError:
        print("Over Retry")







