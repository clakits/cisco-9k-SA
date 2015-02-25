#!/usr/bin/python

import requests
import json
import sys
import logging
import getpass
from optparse import OptionParser


"""
from N9K vsh: python bootflash:/scripts/xxxx.py
from guestshell  
guestshell:/bootflash/scripts$ chvrf management python getInfData_CL.py
Neighbor IP: 10.29.221.136
Username: admin
Password: 
7.0(3)I1(1)
"""

optp = OptionParser()

# JID and password options.
optp.add_option("-i", "--IP", dest="IP",
             help="IP to use")
optp.add_option("-u", "--USER", dest="USER",
              help="Username")

opts, args = optp.parse_args()

if opts.IP is None:
     nei = raw_input("Neighbor IP: ")
else:
     nei = opts.IP

if opts.USER is None:
     user = raw_input("Username: ")
else:
     user = opts.USER

passer = getpass.getpass("Password: ")

url='http://' + nei + '/ins'
switchuser=user
switchpassword=passer


myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show version",
      "version": 1
    },
    "id": 1
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
print response['result']['body']['kickstart_ver_str']
