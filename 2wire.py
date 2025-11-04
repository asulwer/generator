import asyncio
from gpiozero.pins.lgpio import LGPIOFactory
from gpiozero import Device, Button

async def button_pressed_handler():
    print("Button pressed asynchronously!")

async def button_released_handler():
    print("Button released asynchronously!")

async def main():
    button = Button(26)
    loop = asyncio.get_running_loop()
    button.when_pressed = lambda: loop.call_soon_threadsafe(asyncio.create_task, button_pressed_handler())
    button.when_released = lambda: loop.call_soon_threadsafe(asyncio.create_task, button_released_handler())

    print("Waiting for button presses...")
    await asyncio.Future()

if __name__ == '__main__':
    try:
        Device.pin_factory = LGPIOFactory()
        asyncio.run(main())
    except Exception as e:
        print(e)