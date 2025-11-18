import logging
import logger_setup
import asyncio
from gpiozero.pins.lgpio import LGPIOFactory
from gpiozero import Device, Button
import datetime

def convert(date_time):
    format = '%H:%M' #24 hour
    datetime_str = datetime.datetime.strptime(date_time, format)

    return datetime_str

async def button_pressed_handler():
    #if convert("09:00") < datetime.datetime.now() and convert("23:00") > datetime.datetime.now():
    logging.info("Button pressed asynchronously!")

async def button_released_handler():
    #if convert("09:00") < datetime.datetime.now() and convert("23:00") > datetime.datetime.now():
    logging.info("Button released asynchronously!")

async def main():
    button = Button(pin=26,bounce_time=0.2)
    loop = asyncio.get_running_loop()
    button.when_pressed = lambda: loop.call_soon_threadsafe(asyncio.create_task, button_pressed_handler())
    button.when_released = lambda: loop.call_soon_threadsafe(asyncio.create_task, button_released_handler())

    logging.info("Waiting for button presses...")
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