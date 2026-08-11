import asyncio
import time


async def pobierz_id_uzytkownika(nazwa_uzytkownika: str) -> int:
    await asyncio.sleep(1)
    return 101


async def pobierz_posty(id_uzytkownika: int) -> list[int]:
    await asyncio.sleep(1)
    return [1, 2, 3]


async def pobierz_komentarze(id_postu: int) -> list[str]:
    await asyncio.sleep(1)
    return [
        f"Komentarz A do postu {id_postu}",
        f"Komentarz B do postu {id_postu}"
    ]


async def main():
    start = time.perf_counter()

    user_id = await pobierz_id_uzytkownika("jan_kowalski")
    posty_ids = await pobierz_posty(user_id)

    komentarze = await asyncio.gather(
        *(pobierz_komentarze(post_id) for post_id in posty_ids)
    )

    print(f"ID użytkownika: {user_id}")
    print(f"Posty: {posty_ids}")

    for post_id, komentarze_postu in zip(posty_ids, komentarze):
        print(f"Post {post_id}: {komentarze_postu}")

    elapsed = time.perf_counter() - start
    print(f"Czas wykonania: {elapsed:.2f} s")


if __name__ == "__main__":
    asyncio.run(main())