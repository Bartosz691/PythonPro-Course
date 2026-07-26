from pathlib import Path

projekt = Path("Projekt")

src = projekt / "src"
data = projekt / "data"
docs = projekt / "docs"

src.mkdir(parents=True, exist_ok=True)
data.mkdir(parents=True, exist_ok=True)
docs.mkdir(parents=True, exist_ok=True)

print(f"Folder src istnieje: {src.exists()}")
print(f"Folder data istnieje: {data.exists()}")
print(f"Folder docs istnieje: {docs.exists()}")