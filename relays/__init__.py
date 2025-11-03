from enum import IntEnum, unique
import smbus2

@unique
class State(IntEnum):
    def __new__(cls, value):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer.")
        if not 0 <= value <= 255:
            raise ValueError("Value must be between 0 and 255 (inclusive).")
        obj = int.__new__(cls, value)
        obj._value_ = value
        return obj

    ON = 0xFF
    OFF = 0x00

DEVICE_ADDR = 0x01
CHIP_ADDR = 0x10
PUMP_ADDR = 0x01
STARTER_ADDR = 0x02
ACINTERUPT_ON_ADDR = 0x03
ACINTERUPT_OFF_ADDR = 0x04

bus = smbus2.SMBus(DEVICE_ADDR)

bus.write_byte_data(CHIP_ADDR, PUMP_ADDR, State.OFF.value)
bus.write_byte_data(CHIP_ADDR, STARTER_ADDR, State.OFF.value)
bus.write_byte_data(CHIP_ADDR, ACINTERUPT_ON_ADDR, State.OFF.value)
bus.write_byte_data(CHIP_ADDR, ACINTERUPT_OFF_ADDR, State.OFF.value)

def pump(state: State):
    bus.write_byte_data(CHIP_ADDR, PUMP_ADDR, state.value)

def starter(state: State):
    bus.write_byte_data(CHIP_ADDR, STARTER_ADDR, state.value)

def ac_on_interupt(state: State):
    bus.write_byte_data(CHIP_ADDR, ACINTERUPT_ON_ADDR, state.value)

def ac_off_interupt(state: State):
    bus.write_byte_data(CHIP_ADDR, ACINTERUPT_OFF_ADDR, state.value)