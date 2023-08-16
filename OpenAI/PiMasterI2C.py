import smbus

# Create an SMBus object
bus = smbus.SMBus(1)

# Set the slave address of the Pico
SLAVE_ADDRESS = 0x12

while True:
    # Send a message to the Pico over the I2C bus
    message = input('Enter a message to send: ')
    bus.write_i2c_block_data(SLAVE_ADDRESS, 0, list(message.encode('utf-8')))
    
    # Read the response from the Pico
    response = bus.read_i2c_block_data(SLAVE_ADDRESS, 0, 64)
    response_str = ''.join([chr(b) for b in response])
    print('Received response:', response_str)
