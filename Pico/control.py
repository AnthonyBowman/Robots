### control.py
### receives commands from i2C and processes them 
import utime
import time
from machine import mem32,Pin
import UnUsed.led as led
#import hal.py
from i2cSlave import i2c_slave

### --- check pico power on --- ###
led.led_power_on()

### --- pico connect i2c as slave --- ###
s_i2c = i2c_slave(0,sda=0,scl=1,slaveAddress=0x41)

try:
    decode_array = ['0', '0', '0', '0', '0']
    while True:
        data = s_i2c.get()
        print(data)
        # decifer the input which should be of the form
        # M99D999 - e.g. M01F050 - motor 1 forward 50%
        # S99P999 - e.g. S01P270 - servo 1 position 270 
        # F999T0999 - e.g. F075P0500 - move forward with 75% power for 500ms
        # B, L and R as above but backward
                 
        # servo or motor or other
        if data[0] in ('F', 'B', 'R', 'L'):
            # get power setting
            decode_array[0] = data[1];
            decode_array[1] = data[2];
            decode_array[2] = data[3];
            decode_array[3] = 0;
            numeric_string = ''.join(decode_array)
            motor_power = int(numeric_string)

            # get the time setting
            if data[4] not in ('T'):
                print("error in message format")
            decode_array[0] = data[5];
            decode_array[1] = data[6];
            decode_array[2] = data[7];
            decode_array[3] = data[8];
            decode_array[4] = 0;
            numeric_string = ''.join(decode_array)
            time_int = int(numeric_string)

        elif data[0] == 'B'
                # back
                
        elif :
            # anything else

        
            led.led_on()
            time.sleep(0.5)
            led.led_off()
            time.sleep(0.5)

# send back telemetry
        # M99R999 - M01R060 - motor 1 rpm 60 
        # S99P999 - servo 1 position 220
        

except KeyboardInterrupt:
    pass