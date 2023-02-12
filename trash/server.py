#!/usr/bin/env python

import asyncio
import websockets


async def hello(websocket):
    print('i am hello')
    name = await websocket.recv()
    print(f"<<< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f">>> {greeting}")


async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    print('hw')
    asyncio.run(main())
