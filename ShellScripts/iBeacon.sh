# add packet flags
# 1E
# 02 		# Number of bytes that follow in first AD structure
# 01  	# Flags AD type
# 1A  	# Flags value 0x1A = 000011010  
#           bit 0 (OFF) LE Limited Discoverable Mode
#           bit 1 (ON) LE General Discoverable Mode
#           bit 2 (OFF) BR/EDR Not Supported
#           bit 3 (ON) Simultaneous LE and BR/EDR to Same Device Capable (controller)
#           bit 4 (ON) Simultaneous LE and BR/EDR to Same Device Capable (Host)
# 1A  	# Number of bytes that follow in second (and last) AD structure

# vendor specific - iBeacon are apple specific
# FF 		# Manufacturer specific data AD type
# 4C 00 	# Company identifier code (0x004C == Apple)
# 02 		# Byte 0 of iBeacon advertisement indicator
# 15 		# Byte 1 of iBeacon advertisement indicator

# our values
# 63 6F 3F 8F 64 91 4B EE 95 F7 D8 CC 64 A8 63 B5 # our iBeacon proximity uuid - TODO change to Grandpa UUID
# 00 01 	# Major - Raspberry pi based iBeacon 
# 00 01 	# Minor - iBeacon serial number
# C8 00 	# Calibrated Tx power
  
sudo tools/hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 63 6F 3F 8F 64 91 4B EE 95 F7 D8 CC 64 A8 63 B5 00 00 00 00 C8 00

