#!/usr/bin/env python

"""
Client Module for send data
"""

import os
import json
import websockets
import asyncio
from dotenv import load_dotenv

load_dotenv()

async def wsrun(uri):
    """
    Websocket Listen Channel And load
    params uri: str -> Uri to Connect data
    """
    async with websockets.connect(uri) as websocket:
        request = {
            'action': 'onMessage_test',
            'body': '1234556778',
            'client': os.getenv('SERVER_NAME'),
        }
        await websocket.send(json.dumps(request))

        while True:
            print('data - ')
            response = await websocket.recv()
            print('[Server]# {}'.format(response))


asyncio.get_event_loop().run_until_complete(
    wsrun(os.getenv('WS_HOST'))
)
