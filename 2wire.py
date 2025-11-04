import asyncio
from gpiozero.pins.lgpio import LGPIOFactory
from gpiozero import Device, Button

async def button_pressed_handler():
    print("Button pressed asynchronously!")

async def main():
    button = Button(26)
    loop = asyncio.get_running_loop()
    button.when_pressed = lambda: loop.call_soon_threadsafe(asyncio.create_task, button_pressed_handler())

    print("Waiting for button presses...")
    await asyncio.Future()

if __name__ == '__main__':
    try:
        Device.pin_factory = LGPIOFactory(chip=0) #set default pin factory
        asyncio.run(main())
    except Exception as e:
        print(e)