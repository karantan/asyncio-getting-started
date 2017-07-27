"""Various specific py.test fixtures."""
# from unittest.mock import MagicMock

import asyncio
import pytest


@pytest.fixture()
def loop(request):
    """Create a asyncio event loop."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    def teardown():
        loop.close()

    request.addfinalizer(teardown)

    return loop
