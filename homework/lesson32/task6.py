import asyncio


async def pobierz_pogode(miasto: str) -> dict:
    await asyncio.sleep(1.5)

    return {
        'miasto': miasto,
        'temperatura': 25,
        'stan': 'słonecznie'
    }


async def main():
    dane = await pobierz_pogode('Warszawa')
    print(dane)


if __name__ == '__main__':
    asyncio.run(main())