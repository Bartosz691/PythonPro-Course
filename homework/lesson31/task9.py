
import asyncio
import aiohttp


async def sprawdz_status(
    session: aiohttp.ClientSession,
    url: str
):
    try:
        async with session.get(url) as response:
            print(f"{url} - Status: {response.status}")

    except Exception as e:
        print(f"{url} - Błąd: {e}")


async def main():
    urls = [
        "https://google.com",
        "https://github.com",
        "https://python.org",
        "https://httpbin.org/status/404"
    ]

    async with aiohttp.ClientSession() as session:

        zadania = [
            sprawdz_status(session, url)
            for url in urls
        ]

        await asyncio.gather(*zadania)


if __name__ == "__main__":
    asyncio.run(main())