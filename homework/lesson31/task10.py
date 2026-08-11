import asyncio


async def odliczanie(nazwa: str, start: int):
    for pozostalo in range(start, 0, -1):

        print(
            f"{nazwa}: zostało "
            f"{pozostalo} sekund"
        )

        await asyncio.sleep(1)


async def main():
    await asyncio.gather(
        odliczanie("Timer A", 5),
        odliczanie("Timer B", 3),
        odliczanie("Timer C", 7)
    )


if __name__ == "__main__":
    asyncio.run(main())