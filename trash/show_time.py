#!/usr/bin/env python

import asyncio
import datetime
import random
import websockets

CONNECTIONS = set()


async def register(websocket):
    print('connection added')
    CONNECTIONS.add(websocket)
    try:
        await websocket.wait_closed()
        print('connection closed')
    finally:
        CONNECTIONS.remove(websocket)


async def show_time():
    while True:
        message = str(random.random() * 2 + 1) + "is a message"

        websockets.broadcast(CONNECTIONS, message)
        print('message sent to {} connections'.format(len(CONNECTIONS)))
        await asyncio.sleep(random.random() * 2 + 1)


async def main():
    async with websockets.serve(register, "localhost", 5678):
        print('server started')
        await show_time()


if __name__ == "__main__":
    asyncio.run(main())