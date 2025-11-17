import asyncio
from gpiozero.pins.lgpio import LGPIOFactory
from gpiozero import Device, Button
import logging
import logger_setup

async def button_pressed_handler():
    logging.info("Button pressed asynchronously!")

async def button_released_handler():
    logging.info("Button released asynchronously!")

async def main():
    button = Button(26)
    loop = asyncio.get_running_loop()
    button.when_pressed = lambda: loop.call_soon_threadsafe(asyncio.create_task, button_pressed_handler())
    button.when_released = lambda: loop.call_soon_threadsafe(asyncio.create_task, button_released_handler())

    logging.info("Waiting for button presses...")
    await asyncio.Future()

if __name__ == '__main__':
    logger_setup.setup("/home/asulwer/generator/src/2wire.conf")
    logging.info("starting 2wire")

    try:
        logging.info("use pin factory LGPIO")
        Device.pin_factory = LGPIOFactory()
        asyncio.run(main())
    except Exception as e:
        logging.error(e)