#!/usr/bin/env python3

from netmiko import ConnectHandler

S1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.90',
    'username': 'shepherd',
    'password': 'cisco',
}
S2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.91',
    'username': 'shepherd',
    'password': 'cisco',
}

SW4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.92',
    'username': 'shepherd',
    'password': 'cisco',
}


for device in (S1, S2, SW4):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command('show ip int br')
    print(output)

    config_commands = ['int loop 0','ip address 1.1.1.1 255.255.255.0']
    output = net_connect.send_config_set(config_commands)
    print(output)


