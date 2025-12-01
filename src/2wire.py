import logging
import logger_setup
import asyncio
from gpiozero.pins.lgpio import LGPIOFactory
from gpiozero import Device, Button

import datetime
import relays

def convert(date_time):
    format = '%H:%M' #24 hour
    datetime_str = datetime.datetime.strptime(date_time, format)

    return datetime_str

async def button_pressed_handler():
    #if convert("09:00") < datetime.datetime.now() and convert("23:00") > datetime.datetime.now():
    logging.info("Generator starting")

    await asyncio.sleep(2)
    relays.pump(relays.State.ON)
    await asyncio.sleep(0.5)
    relays.starter(relays.State.ON)
    await asyncio.sleep(5)
    relays.starter(relays.State.OFF)
    await asyncio.sleep(5)
    relays.ac_on_interupt(relays.State.ON)
    await asyncio.sleep(0.5)
    relays.ac_on_interupt(relays.State.OFF)

    logging.info("Generator started")

async def button_released_handler():
    #if convert("09:00") < datetime.datetime.now() and convert("23:00") > datetime.datetime.now():
    logging.info("Generator stopping")
    
    await asyncio.sleep(2)
    relays.pump(relays.State.OFF)

    logging.info("Generator stopped")

async def main():
    button = Button(pin=26,bounce_time=0.2)
    loop = asyncio.get_running_loop()
    button.when_pressed = lambda: loop.call_soon_threadsafe(asyncio.create_task, button_pressed_handler())
    button.when_released = lambda: loop.call_soon_threadsafe(asyncio.create_task, button_released_handler())

    relays.initialize()

    logging.info("Waiting to start generator...")
    await asyncio.Future()

if __name__ == '__main__':
    logger_setup.configure("/home/asulwer/generator/src/2wire.conf")
    logging.info("starting 2wire")

    try:
        logging.info("use pin factory LGPIO")
        Device.pin_factory = LGPIOFactory()
        asyncio.run(main())
    except Exception as e:
        logging.error(e)