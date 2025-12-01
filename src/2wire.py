import logging
import logger_setup
import asyncio
import socketio
from gpiozero.pins.lgpio import LGPIOFactory
from gpiozero import Device, Button

import datetime

def convert(date_time):
    format = '%H:%M' #24 hour
    datetime_str = datetime.datetime.strptime(date_time, format)

    return datetime_str

async def button_pressed_handler():
    #if convert("09:00") < datetime.datetime.now() and convert("23:00") > datetime.datetime.now():
    logging.info("Generator starting")

    with socketio.SimpleClient() as sio:
        logging.info("connecting to Webserver")
        await sio.connect('http://localhost:5000')
        
        logging.info("turn pump on")
        await sio.emit('pumpUpdate', { 'switchPump': True })
        await asyncio.sleep(2)

        logging.info("turn starter on")
        await sio.emit('starterUpdate', { 'switchStarter': True })
        await asyncio.sleep(5)

        logging.info("turn starter off")
        await sio.emit('starterUpdate', { 'switchStarter': False })
        await asyncio.sleep(5)

        logging.info("toggle ac on")
        await sio.emit('aconinteruptUpdate', { 'aconinteruptUpdate': True })
        await asyncio.sleep(1)

        logging.info("release ac toggle")
        await sio.emit('aconinteruptUpdate', { 'aconinteruptUpdate': False })
        await asyncio.sleep(0.5)
    
    logging.info("Generator started")

async def button_released_handler():
    #if convert("09:00") < datetime.datetime.now() and convert("23:00") > datetime.datetime.now():
    logging.info("Generator stopping")
    
    with socketio.SimpleClient() as sio:
        logging.info("connecting to Webserver")
        await sio.connect('http://localhost:5000')
        
        logging.info("turn pump off")
        await sio.emit('pumpUpdate', { 'switchPump': False })
        await asyncio.sleep(2)

    logging.info("Generator stopped")

async def main():
    button = Button(pin=26,bounce_time=0.2)
    loop = asyncio.get_running_loop()
    button.when_pressed = lambda: loop.call_soon_threadsafe(asyncio.create_task, button_pressed_handler())
    button.when_released = lambda: loop.call_soon_threadsafe(asyncio.create_task, button_released_handler())

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