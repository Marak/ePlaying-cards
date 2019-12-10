"""
This file has a couple helper functions
providing the users the ability to send
data to the arduino in string form through
I2C bus.
"""

import smbus

bus = smbus.SMBus(1)

# This is the address setup in arduino program
address = 0x04

def __StringToBytes(value):
    retVal = []
    for c in value:
        retVal.append(ord(c))
    return retVal

def writeData(value):
    byteValue = __StringToBytes(value)
    bus.write_i2c_block_data(address, 0x00, byteValue)
    return -1

def readData():
    data = bus.read_byte(address)
    return data
