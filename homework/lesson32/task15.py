import asyncio
import aiofiles


async def zapisz_log(
    id_korutyny: int,
    lock: asyncio.Lock,
    sciezka_pliku: str
):
    tekst = f'Log z korutyny {id_korutyny}\n'

    async with lock:
        async with aiofiles.open(
            sciezka_pliku,
            mode='a',
            encoding='utf-8'
        ) as f:
            await f.write(tekst)


async def main():
    sciezka = 'logi.txt'

    lock = asyncio.Lock()

    async with aiofiles.open(
        sciezka,
        mode='w',
        encoding='utf-8'
    ) as f:
        await f.write('')

    zadania = [
        zapisz_log(i, lock, sciezka)
        for i in range(1, 6)
    ]

    await asyncio.gather(*zadania)

    print(f'Zapisano logi do pliku: {sciezka}')


if __name__ == '__main__':
    asyncio.run(main())