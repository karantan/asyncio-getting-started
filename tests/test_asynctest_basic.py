"""Tests for the basic.py task runner using `asynctest` lib."""
from testfixtures import LogCapture

import asynctest
import responses


class TestBasic(asynctest.TestCase):
    use_default_loop = True
    forbid_get_event_loop = False

    @asynctest.patch('src.basic.asyncio.sleep')
    async def test_non_blocking_single_call(self, asyncio_sleep):
        from src.basic import non_blocking_call

        with responses.RequestsMock() as rsps:
            rsps.add(responses.GET, 'https://www.google.com', status=200)
            with LogCapture() as log:
                await non_blocking_call(self.loop, 'https://www.google.com')
                log.check(
                    ('root', 'INFO', 'Received content from https://www.google.com'),  # noqa
                )
