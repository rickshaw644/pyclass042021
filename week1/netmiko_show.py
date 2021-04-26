#!/usr/bin/env python

"""
Grab IOS device cisco3.lasthop.io show version
"""

from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_xe',
}
net_connect = ConnectHandler(**device1)
output = net_connect.send_command("show version", expect_string=r'#')
 
with open("show_version.txt", "w") as f:
    f.write(output)

net_connect.disconnect()


