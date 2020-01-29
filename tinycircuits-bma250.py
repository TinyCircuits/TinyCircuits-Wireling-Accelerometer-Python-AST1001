# BMA250 Accelerometer Python Package
# Written by: Laverena Wienclaw for TinyCircuits

import pigpio 

_BMA250_I2CADDR          = 0x18
_BMA250_update_time_64ms = 0x08
_BMA250_update_time_32ms = 0x09
_BMA250_update_time_16ms = 0x0A
_BMA250_update_time_8ms  = 0x0B
_BMA250_update_time_4ms  = 0x0C
_BMA250_update_time_2ms  = 0x0D
_BMA250_update_time_1ms  = 0x0E
_BMA250_update_time_05ms = 0xF
_BMA250_range_2g         = 0x03
_BMA250_range_4g         = 0x05
_BMA250_range_8g         = 0x08
_BMA250_range_16g        = 0x0C

class BMA250: 
    def __init__(self, range, bandwidth):
        # Setup range measurement setting
        pi = pigpio.pi()
        h = pi.i2c_open(1, _BMA250_I2CADDR)
        pi.i2c_write_byte(h, 0x0F)
        pi.i2c_write_byte(h, range)
        pi.i2c_close(h)

        # Setup bandwidth
        pi = pigpio.pi()
        h = pi.i2c_open(1, _BMA250_I2CADDR)
        pi.i2c_write_byte(h, 0x10)
        pi.i2c_write_byte(h, bandwidth)
        pi.i2c_close(h)

        # Init Accel variables
        self.X = None
        self.Y = None
        self.Z = None
        self.rawTemp = None

    def readSensor(self):
        # Set register index
        pi = pigpio.pi()
        h = pi.i2c_open(1, _BMA250_I2CADDR)
        pi.i2c_write_byte(h, 0x02)
        

        # Request 7 data bytes
        (b, d) = pi.i2c_read_i2c_block_data(h, _BMA250_I2CADDR, 7)
        pi.i2c_close(h)
        if b>= 0:
            for x in d:
                print(d)
        else:
            print("There was an error reading data")
