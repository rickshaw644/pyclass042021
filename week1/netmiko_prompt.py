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
net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())


