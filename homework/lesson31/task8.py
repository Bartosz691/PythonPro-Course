import asyncio
import random


async def ping(host: str) -> str:
    delay = random.uniform(0.1, 1.0)

    await asyncio.sleep(delay)

    return f"Host {host} odpowiada"


async def main():
    hosty = [
        "8.8.8.8",
        "1.1.1.1",
        "google.com",
        "github.com",
        "python.org"
    ]

    wyniki = await asyncio.gather(
        *(ping(h) for h in hosty)
    )

    for res in wyniki:
        print(res)


if __name__ == "__main__":
    asyncio.run(main())