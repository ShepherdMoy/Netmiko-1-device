# Netmiko-1-device
Connect securely to a device using ssh 
The script imports the ConnectHandler function from the netmiko library to securely log into a switch .
you have to create a dictionary and name if by the device type ,in this case 
iosv_l2
dictionary contents are as per the script but be mindful on device type as for cisco it has to be cisco_ios  (i have not tried the script on other vendors )
example device_type': 'cisco_ios
after connecting and successfull authentication ,the script will run the show ip int br command and give you the output as bash output *you can redirect it to a file *
the script will then move on to configure a loopback and the loopback ip address .
below is the sample expected output :

% ./netmiko1.py   
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0     unassigned      YES unset  up                    up      
GigabitEthernet0/1     unassigned      YES unset  up                    up      
GigabitEthernet0/2     unassigned      YES unset  up                    up      
GigabitEthernet0/3     unassigned      YES unset  up                    up      
GigabitEthernet1/0     unassigned      YES unset  up                    up      
GigabitEthernet1/1     unassigned      YES unset  up                    up      
GigabitEthernet1/2     unassigned      YES unset  up                    up      
GigabitEthernet1/3     unassigned      YES unset  up                    up      
Loopback0              1.1.1.1         YES manual up                    up      
Vlan1                  192.168.1.17    YES DHCP   up                    up      
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
SW1(config)#int loop 0
SW1(config-if)#ip address 1.1.1.1 255.255.255.0
SW1(config-if)#end
SW1#
