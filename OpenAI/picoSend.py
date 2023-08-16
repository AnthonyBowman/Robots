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

# send the string "hello from the Pico" to the Raspberry Pi
ser.write('hello from the Pico')

ser.close()
