"""Tests for the basic.py task runner."""

from unittest.mock import MagicMock
from unittest.mock import patch
from testfixtures import LogCapture

import responses


class AsyncMock(MagicMock):
    async def __call__(self, *args, **kwargs):
        return super(AsyncMock, self).__call__(*args, **kwargs)


class TestBasic(object):

    @responses.activate
    @patch('src.basic.asyncio.sleep', new_callable=AsyncMock)
    def test_non_blocking_single_call(self, asyncio_sleep, loop):
        from src.basic import non_blocking_call

        responses.add(responses.GET, 'https://www.google.com', status=200)

        async def run_test():
            await non_blocking_call(loop, 'https://www.google.com')

        with LogCapture() as log:
            loop.run_until_complete(run_test())
            log.check(
                ('root', 'INFO', 'Received content from https://www.google.com'),  # noqa
            )
        loop.run_until_complete(run_test())

    @responses.activate
    @patch('src.basic.asyncio.sleep', new_callable=AsyncMock)
    def test_non_blocking_multiple_calls(self, asyncio_sleep, loop):
        from src.basic import non_blocking_call

        responses.add(responses.GET, 'https://www.google.com', status=200)
        responses.add(responses.GET, 'https://www.yahoo.com', status=200)
        responses.add(responses.GET, 'https://www.apple.com', status=500)

        async def run_test():
            await non_blocking_call(loop, 'https://www.google.com')
            await non_blocking_call(loop, 'https://www.yahoo.com')
            await non_blocking_call(loop, 'https://www.apple.com')

        with LogCapture() as log:
            loop.run_until_complete(run_test())
            log.check(
                ('root', 'INFO', 'Received content from https://www.google.com'),  # noqa
                ('root', 'INFO', 'Received content from https://www.yahoo.com'),  # noqa
                ('root', 'INFO', 'Received content from https://www.apple.com'),  # noqa
            )
        loop.run_until_complete(run_test())

    @responses.activate
    @patch('src.basic.time.sleep')
    def test_blocking_single_call(self, time_sleep, loop):
        from src.basic import blocking_call

        responses.add(responses.GET, 'https://www.google.com', status=200)

        async def run_test():
            await blocking_call(loop, 'https://www.google.com')

        with LogCapture() as log:
            loop.run_until_complete(run_test())
            log.check(
                ('root', 'INFO', 'Received content from https://www.google.com'),  # noqa
            )
        loop.run_until_complete(run_test())

    @responses.activate
    @patch('src.basic.time.sleep')
    def test_blocking_multiple_calls(self, time_sleep, loop):
        from src.basic import blocking_call

        responses.add(responses.GET, 'https://www.google.com', status=200)
        responses.add(responses.GET, 'https://www.yahoo.com', status=200)
        responses.add(responses.GET, 'https://www.apple.com', status=500)

        async def run_test():
            await blocking_call(loop, 'https://www.google.com')
            await blocking_call(loop, 'https://www.yahoo.com')
            await blocking_call(loop, 'https://www.apple.com')

        with LogCapture() as log:
            loop.run_until_complete(run_test())
            log.check(
                ('root', 'INFO', 'Received content from https://www.google.com'),  # noqa
                ('root', 'INFO', 'Received content from https://www.yahoo.com'),  # noqa
                ('root', 'INFO', 'Received content from https://www.apple.com'),  # noqa
            )
        loop.run_until_complete(run_test())
