import queue
import threading
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


START_URL = "https://example.com"
MAX_STRON = 50
LICZBA_WATKOW = 5

kolejka = queue.Queue()
odwiedzone = set()

lock = threading.Lock()

domena = urlparse(START_URL).netloc

kolejka.put(START_URL)


def pobierz_strone():
    while True:
        try:
            url = kolejka.get(timeout=1)
        except queue.Empty:
            return

        with lock:
            if url in odwiedzone or len(odwiedzone) >= MAX_STRON:
                kolejka.task_done()
                continue

            odwiedzone.add(url)

        print(f"Pobieranie: {url}")

        try:
            odpowiedz = requests.get(
                url,
                timeout=10,
            )

            odpowiedz.raise_for_status()

            soup = BeautifulSoup(
                odpowiedz.text,
                "html.parser",
            )

            for link in soup.find_all("a", href=True):
                nowy_url = urljoin(
                    url,
                    link["href"],
                )

                if urlparse(nowy_url).netloc == domena:
                    with lock:
                        if (
                            nowy_url not in odwiedzone
                            and len(odwiedzone) < MAX_STRON
                        ):
                            kolejka.put(nowy_url)

        except requests.RequestException as blad:
            print(f"Błąd dla {url}: {blad}")

        finally:
            kolejka.task_done()


with ThreadPoolExecutor(
    max_workers=LICZBA_WATKOW
) as executor:

    futures = [
        executor.submit(pobierz_strone)
        for _ in range(LICZBA_WATKOW)
    ]

    for future in futures:
        future.result()


print(f"\nOdwiedzono stron: {len(odwiedzone)}")

for url in odwiedzone:
    print(url)