import os
import shutil
from pathlib import Path
from file_types import FILE_TYPES_MAP

DOWNLOADS_FOLDER = Path.home() / "Downloads" # / "TestCat"
TARGET_FOLDER = DOWNLOADS_FOLDER

def get_category(file_suffix):
    ext = file_suffix.lower()
    for category, extensions in FILE_TYPES_MAP.items():
        if ext in extensions:
            return category
    return "Sonstiges"

def sort_files():
    for file in DOWNLOADS_FOLDER.iterdir():
        if file.is_file():
            category = get_category(file.suffix)
            category_folder = TARGET_FOLDER / category
            category_folder.mkdir(exist_ok=True)
            

            target_path = category_folder / file.name

            # falls datei mit 1:1 dem selben namen existiert => neuen namen / counter
            counter = 1
            while target_path.exists():
                target_path = TARGET_FOLDER / f"{file.stem}_{counter}{file.suffix}"
                counter += 1

            shutil.move(str(file), str(target_path))
            print(f"[x] Verschoben: {file.name} → {category}/")
 

if __name__ == "__main__":
    print(f" Starte Sortierung im Ordner: {DOWNLOADS_FOLDER}")
    sort_files()
    print("Alle Dateien wurden sortiert.")