import serial

# configure the serial connection
ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

ser.isOpen()

# read and print the string sent from the Raspberry Pi
string = ser.readline()
print(string)

ser.close()
