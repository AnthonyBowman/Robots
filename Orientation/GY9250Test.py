import time
import math
import smbus2

# MPU-9250 I2C address
MPU9250_ADDRESS = 0x68

# Register addresses for sensor data
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43
MAG_XOUT_L = 0x03

# Conversion factors
ACCEL_SCALE_FACTOR = 16384.0  # LSB/g
GYRO_SCALE_FACTOR = 131.0     # LSB/degree/s

# Initialize I2C bus
bus = smbus2.SMBus(1)

def read_raw_data(addr):
    high = bus.read_byte_data(MPU9250_ADDRESS, addr)
    low = bus.read_byte_data(MPU9250_ADDRESS, addr + 1)
    value = (high << 8) + low
    return value

def read_accel_data():
    x = read_raw_data(ACCEL_XOUT_H) / ACCEL_SCALE_FACTOR
    y = read_raw_data(ACCEL_XOUT_H + 2) / ACCEL_SCALE_FACTOR
    z = read_raw_data(ACCEL_XOUT_H + 4) / ACCEL_SCALE_FACTOR
    return x, y, z

def read_gyro_data():
    x = read_raw_data(GYRO_XOUT_H) / GYRO_SCALE_FACTOR
    y = read_raw_data(GYRO_XOUT_H + 2) / GYRO_SCALE_FACTOR
    z = read_raw_data(GYRO_XOUT_H + 4) / GYRO_SCALE_FACTOR
    return x, y, z

def calculate_orientation(accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z):
    roll = math.atan2(accel_y, accel_z)
    pitch = math.atan(-accel_x / (accel_y * math.sin(roll) + accel_z * math.cos(roll)))
    yaw = gyro_z * 0.01  # Assuming gyro is calibrated and in degrees per second
    return roll, pitch, yaw

try:
    while True:
        accel_x, accel_y, accel_z = read_accel_data()
        gyro_x, gyro_y, gyro_z = read_gyro_data()
        roll, pitch, yaw = calculate_orientation(accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z)
        
        print(f"Roll: {math.degrees(roll):.2f}°, Pitch: {math.degrees(pitch):.2f}°, Yaw: {yaw:.2f}°")
        
        time.sleep(0.1)  # Delay between readings
        
except KeyboardInterrupt:
    print("Exiting...")
