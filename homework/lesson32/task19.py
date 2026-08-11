import asyncio


def czy_pierwsza(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


async def generator_liczb_pierwszych():
    n = 2

    while True:
        if czy_pierwsza(n):
            yield n
            await asyncio.sleep(0.1)

        n += 1


async def main():
    async for prime in generator_liczb_pierwszych():
        print(prime)

        if prime >= 100:
            break


if __name__ == "__main__":
    asyncio.run(main())