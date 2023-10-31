#!/bin/bash 

# Delete any existing MegadishH connection
nmcli con delete MegadishH

# Create new hotspot connection named MegadishH 
nmcli con add type wifi ifname wlan0 mode ap con-name MegadishH ssid MegadishH autoconnect true

# Set IP address and DHCP range 
nmcli con modify MegadishH ipv4.method shared ipv4.addresses 192.168.3.1/24
#nmcli con modify MegadishH ipv4.dhcp-start 192.168.3.100 ipv4.dhcp-end 192.168.3.200

# Disable IPv6
nmcli con modify MegadishH ipv6.method disabled

# Set password  
nmcli con modify MegadishH wifi-sec.key-mgmt wpa-psk
nmcli con modify MegadishH wifi-sec.psk "Raspberry13" 

# Save and activate connection
nmcli con up MegadishH
