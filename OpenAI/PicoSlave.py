import smbus
import time

# configure the I2C connection
bus = smbus.SMBus(1)

# the Pico's I2C address
pico_address = 0x04

# send the string "hello, world" to the Pico
bus.write_i2c_block_data(pico_address, 0, list('hello, world'))
time.sleep(1)

import smbus

# configure the I2C connection
bus = smbus.SMBus(1)

# the Raspberry Pi's I2C address
pi_address = 0x03

# read and print the string sent from the Raspberry Pi
string = bus.read_i2c_block_data(pi_address, 0)
print(string)

import smbus

# configure the I2C connection
bus = smbus.SMBus(1)

# the Raspberry Pi's I2C address
pi_address = 0x03

# send the string "hello from the Pico" to the Raspberry Pi
bus.write_i2c_block_data(pi_address, 0, list('hello from the Pico'))


To use I2C to communicate between the Raspberry Pi and the Raspberry Pi Pico, you will need to connect the two devices using the I2C pins on each board.

On the Raspberry Pi, the I2C pins are located on the following GPIO pins:

SDA (Data Line): GPIO 2
SCL (Clock Line): GPIO 3
On the Raspberry Pi Pico, the I2C pins are located on the following pins:

SDA (Data Line): Pin 19
SCL (Clock Line): Pin 18
To connect the two devices, you will need to connect the SDA pin on the Raspberry Pi to the SDA pin on the Pico, and the SCL pin on the Raspberry Pi to the SCL pin on the Pico. You will also need to connect the ground (GND) pins on both devices. You can use jumper wires or a breadboard to make these connections.

Once the devices are connected, you can use the smbus library in Python to communicate over the I2C connection.
One thing to keep in mind is that you need to make sure that the I2C devices are properly connected and configured before you can start communicating over the I2C bus. This includes connecting the SDA, SCL, and GND pins on the devices, and setting the correct I2C address for each device.