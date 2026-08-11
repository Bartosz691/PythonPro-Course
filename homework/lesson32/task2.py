import asyncio


async def licznik(n: int):
    for i in range(1, n + 1):
        print(i)
        await asyncio.sleep(1)


async def main():
    await licznik(5)


if __name__ == '__main__':
    asyncio.run(main())