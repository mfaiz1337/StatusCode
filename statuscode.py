#!/usr/bin/env python3
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

from modules.color import Fcolor
from modules.banner import patern
import requests
import time
import sys
import os
import socket
import urllib3
import argparse
import threading
def Status():
    print(Fcolor.cyan+patern)
    subdo = []
    subdomain = []
    print(50*".")
    inp = input("[i] Enter Subdomain File Path: ")
    print(50*".")
    if os.path.isdir(inp) == False:
        try:
            readfile = open(inp, "r")
            filesw = readfile.readlines()
            for i in filesw:
                subdomain.append(i.replace("\n",""))
        except FileNotFoundError:
            print('[err]'+' File not Found')
            sys.exit()
        

    else:
        print("[err]"+" File PATH Directory Not Found ")
    print("\nTotal Subdomain Found :",str(len(subdomain)))
    print("SCode".center(0)+"Domain".center(25)+"IP".center(25))
    print(50*"_")
    for x in range(len(subdomain)):
        try:
            nb = socket.gethostbyname(subdomain[x])
            req = requests.get("http://"+subdomain[x])
            print(str(req.status_code)," | ",req.url," | ",nb)
        except socket.gaierror:
            print("[!] Host Not Found: ",subdomain[x])

        except socket.error:
            print("[!] Not Connected: ",subdomain[x])
        except KeyboardInterrupt:
            time.sleep(1)
            print(Fcolor.red+"Exit..."+"\033[1;1;0m")
            time.sleep(1)
            break
            sys.exit()

if __name__ == "__main__":
    x = threading.Thread(target=Status)          
    x.start()
    






