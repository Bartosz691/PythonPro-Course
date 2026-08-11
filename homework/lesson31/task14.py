import asyncio


async def producent(kolejka: asyncio.Queue):
    for i in range(1, 21):

        await asyncio.sleep(0.5)

        await kolejka.put(i)


async def konsument(
    id_konsumenta: int,
    kolejka: asyncio.Queue
):
    while True:

        liczba = await kolejka.get()

        print(
            f"Konsument {id_konsumenta} "
            f"przetworzył liczbę: {liczba}"
        )

        kolejka.task_done()


async def main():
    kolejka = asyncio.Queue()

    prod_task = asyncio.create_task(
        producent(kolejka)
    )

    cons1 = asyncio.create_task(
        konsument(1, kolejka)
    )

    cons2 = asyncio.create_task(
        konsument(2, kolejka)
    )

    await prod_task

    await kolejka.join()

    cons1.cancel()
    cons2.cancel()


if __name__ == "__main__":
    asyncio.run(main())