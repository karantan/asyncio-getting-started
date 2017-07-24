"""Simple demonstration of asyncio works."""
from asyncio import BaseEventLoop

import asyncio
import functools
import requests


async def factorial(loop: BaseEventLoop, page: str):
    if page == 'https://www.yahoo.com':
        await asyncio.sleep(1.0)
    if page == 'https://www.google.com':
        await asyncio.sleep(3.0)
    try:
        # NOTE: make requests.get non-blocking. i.e. part of the event loop.
        future = loop.run_in_executor(
            None,
            functools.partial(requests.get, page, timeout=10)
        )
        resp = await future

        # resp = requests.get(page, timeout=10)
        print('{} - {}'.format(resp.url, resp.status_code))
        return resp.url

    except Exception as e:
        return e


def run_coroutines():
    loop = asyncio.get_event_loop()
    coros = [
        factorial(loop, 'https://www.google.com'),
        factorial(loop, 'https://www.yahoo.com'),
        factorial(loop, 'http://www.apple.com'),
    ]
    status = asyncio.gather(*coros)
    loop.run_until_complete(status)
    res = status.result()
    loop.close()

    return res


run_coroutines()
