"""Simple demonstration of asyncio works."""
from asyncio import BaseEventLoop

import asyncio
import functools
import requests
import time
import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


async def blocking_call(loop: BaseEventLoop, page: str):
    if page == 'https://www.yahoo.com':
        time.sleep(5.0)
    if page == 'https://www.google.com':
        time.sleep(10.0)

    # NOTE: make requests.get non-blocking. i.e. part of the event loop.
    future = loop.run_in_executor(
        None,
        functools.partial(requests.get, page, timeout=10)
    )
    resp = await future
    logger.info('Received content from {}'.format(page))
    return resp.url


async def non_blocking_call(loop: BaseEventLoop, page: str):
    if page == 'https://www.yahoo.com':
        await asyncio.sleep(5.0)
    if page == 'https://www.google.com':
        await asyncio.sleep(10.0)

    # NOTE: make requests.get non-blocking. i.e. part of the event loop.
    future = loop.run_in_executor(
        None,
        functools.partial(requests.get, page, timeout=10)
    )
    resp = await future
    logger.info('Received content from {}'.format(page))

    return resp.url


if __name__ == '__main__':  # pragma: no cover
    loop = asyncio.get_event_loop()
    """
    Non-blocking code will always complete in ~10s
    """
    non_blocking_coros = [
        non_blocking_call(loop, 'https://www.google.com'),
        non_blocking_call(loop, 'https://www.yahoo.com'),
        non_blocking_call(loop, 'http://www.apple.com'),
    ]
    status = asyncio.gather(*non_blocking_coros)
    logger.info('Running non-blocking calls ...')
    loop.run_until_complete(status)
    status.result()

    """
    Just before `Starting new HTTPS connection (1): www.google.com` we wait for
    10 seconds because of the blocking `sleep(10)`

    Blocking code will complete in 10s + 5s = 15s.
    """
    blocking_coros = [
        blocking_call(loop, 'https://www.google.com'),
        blocking_call(loop, 'https://www.yahoo.com'),
        blocking_call(loop, 'http://www.apple.com'),
    ]
    status = asyncio.gather(*blocking_coros)
    logger.info('Running blocking calls ...')
    loop.run_until_complete(status)
    status.result()

    logger.info('Closing asyncio loop ...')
    loop.close()
