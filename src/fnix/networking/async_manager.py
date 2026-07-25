import asyncio
import inspect
from concurrent.futures import ThreadPoolExecutor


class AsyncManager:

    def __init__(self, max_workers=100):
        self._tasks = set()
        self._connections = set()

        self._executor = ThreadPoolExecutor(
            max_workers=max_workers
        )

    async def dispatch(self, handler, request):
        if inspect.iscoroutinefunction(handler):
            return await handler(request)

        loop = asyncio.get_running_loop()

        return await loop.run_in_executor(
            self._executor,
            handler,
            request
        )