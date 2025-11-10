import asyncio
from gpiozero.pins.lgpio import LGPIOFactory
from gpiozero import Device, Button
import logging
import logging.config
import os
import sys

def setup_logging(config_path):
    """Setup logging from a fileConfig INI file."""
    if not os.path.isfile(config_path):
        print(f"Error: Logging configuration file not found: {config_path}")
        sys.exit(1)  # Exit or raise an exception

    try:
        logging.config.fileConfig(config_path, disable_existing_loggers=False)
        logging.info("Logging configured successfully.")
    except Exception as e:
        print(f"Failed to configure logging: {e}")
        sys.exit(1)

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
    config_file = os.path.abspath("/home/asulwer/generator/src/logging.conf")
    setup_logging(config_file)

    logger = logging.getLogger(__name__)
    logging.info("starting 2wire")

    try:
        logging.info("use pin factory LGPIO")
        Device.pin_factory = LGPIOFactory()
        asyncio.run(main())
    except Exception as e:
        logging.error(e)