import asyncio
import time


class RateLimiter:

    def __init__(
        self,
        max_calls: int,
        period: float = 1.0
    ):
        self.max_calls = max_calls
        self.period = period
        self.calls = []
        self.lock = asyncio.Lock()

    async def acquire(self):
        async with self.lock:
            now = time.monotonic()

            self.calls = [
                t for t in self.calls
                if now - t < self.period
            ]

            if len(self.calls) >= self.max_calls:
                wait_time = (
                    self.period
                    - (now - self.calls[0])
                )

                if wait_time > 0:
                    await asyncio.sleep(wait_time)

                now = time.monotonic()

                self.calls = [
                    t for t in self.calls
                    if now - t < self.period
                ]

            self.calls.append(time.monotonic())


async def zadanie(
    id_zadania: int,
    limiter: RateLimiter,
    start_time: float
):
    await limiter.acquire()

    now = time.monotonic() - start_time

    print(
        f'[{now:.2f}s] Zadanie '
        f'{id_zadania} uzyskało dostęp'
    )


async def main():
    limiter = RateLimiter(
        max_calls=5,
        period=1.0
    )

    start_time = time.monotonic()

    tasks = [
        zadanie(i, limiter, start_time)
        for i in range(1, 21)
    ]

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())