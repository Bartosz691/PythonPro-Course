import asyncio
import random


async def dlugie_zadanie():
    czas = random.uniform(1, 5)

    print(
        f"Zadanie oszacowane na "
        f"{czas:.2f} s"
    )

    await asyncio.sleep(czas)

    return "Sukces"


async def main():
    try:

        wynik = await asyncio.wait_for(
            dlugie_zadanie(),
            timeout=3.0
        )

        print(
            f"Wynik: {wynik}"
        )

    except asyncio.TimeoutError:

        print(
            "Błąd: Przekroczono limit czasu "
            "(asyncio.TimeoutError)"
        )


if __name__ == "__main__":
    asyncio.run(main())