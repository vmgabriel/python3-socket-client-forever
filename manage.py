"""
Manage Control data
"""

# Configuration
import os
import asyncio

# App
from client import wsrun


# Variables
from config import configurations as configs


def runserver():
    """Run the Server"""
    device = configs['server']['host']
    port = configs['server']['port']
    host = f'ws://{device}:{port}'
    print(f'host - {host}')
    asyncio.get_event_loop().run_until_complete(
        wsrun(host)
    )


if __name__ == '__main__':
    runserver()
