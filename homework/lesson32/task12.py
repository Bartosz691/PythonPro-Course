import asyncio
import random


async def zadanie(id_zadania: int) -> float:
    czas = random.uniform(1, 10)
    await asyncio.sleep(czas)

    return czas


async def main():
    tasks = [
        asyncio.create_task(zadanie(i))
        for i in range(1, 6)
    ]

    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )

    pierwsze = done.pop()
    wynik = pierwsze.result()

    print(
        f'Pierwsze ukończone zadanie '
        f'zwróciło czas: {wynik:.2f} s'
    )

    for task in pending:
        task.cancel()


if __name__ == '__main__':
    asyncio.run(main())