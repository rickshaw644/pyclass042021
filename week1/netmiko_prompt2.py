#!/usr/bin/env python

"""
Grab NX-OS device nxos1.lasthop.io prompt 
"""

from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'nxos1.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
}
device2 = {
    "host": 'nxos2.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
}
for device in (device1, device2):
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())



