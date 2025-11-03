import smbus2

DEVICE_ADDR = 0x01
CHIP_ADDR = 0x10
PUMP_ADDR = 0x01
STARTER_ADDR = 0x02
ACINTERUPT_ON_ADDR = 0x03
ACINTERUPT_OFF_ADDR = 0x04
ON = 0xFF
OFF = 0x00

bus = smbus2.SMBus(DEVICE_ADDR)

bus.write_byte_data(CHIP_ADDR, PUMP_ADDR, OFF)
bus.write_byte_data(CHIP_ADDR, STARTER_ADDR, OFF)
bus.write_byte_data(CHIP_ADDR, ACINTERUPT_ON_ADDR, OFF)
bus.write_byte_data(CHIP_ADDR, ACINTERUPT_OFF_ADDR, OFF)

def pump_on():
    bus.write_byte_data(CHIP_ADDR, PUMP_ADDR, ON)

def pump_off():
    bus.write_byte_data(CHIP_ADDR, PUMP_ADDR, OFF)

def starter_on():
    bus.write_byte_data(CHIP_ADDR, STARTER_ADDR, ON)

def starter_off():
    bus.write_byte_data(CHIP_ADDR, STARTER_ADDR, OFF)

def ac_on_interupt_enable():
    bus.write_byte_data(CHIP_ADDR, ACINTERUPT_ON_ADDR, ON)

def ac_on_interupt_disable():
    bus.write_byte_data(CHIP_ADDR, ACINTERUPT_ON_ADDR, OFF)

def ac_off_interupt_enable():
    bus.write_byte_data(CHIP_ADDR, ACINTERUPT_OFF_ADDR, ON)

def ac_off_interupt_disable():
    bus.write_byte_data(CHIP_ADDR, ACINTERUPT_OFF_ADDR, OFF)