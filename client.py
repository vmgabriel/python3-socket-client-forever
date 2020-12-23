#!/usr/bin/env python

"""
Client Module for send data
"""

# Libraries
import json
import websockets


async def wsrun(uri):
    """
    Websocket Listen Channel And load
    params uri: str -> Uri to Connect data
    """
    async with websockets.connect(uri) as websocket:
        request = {
            'action': 'onMessage_test',
            'body': '1234556778',
        }
        await websocket.send(json.dumps(request))

        while True:
            print('data - ')
            response = await websocket.recv()
            print('[Server]# {}'.format(response))
