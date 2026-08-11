import asyncio


async def pobierz_pogode(miasto: str) -> dict:
    await asyncio.sleep(1.5)

    return {
        'miasto': miasto,
        'temperatura': 25,
        'stan': 'słonecznie'
    }


async def main():
    miasta = ['Warszawa', 'Kraków', 'Gdańsk']

    wyniki = await asyncio.gather(
        *(pobierz_pogode(m) for m in miasta)
    )

    for dane in wyniki:
        print(dane)


if __name__ == '__main__':
    asyncio.run(main())