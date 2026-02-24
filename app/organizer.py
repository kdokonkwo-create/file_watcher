from pathlib import Path
import shutil
import json
import datetime
import sys


# Handle PyInstaller path
import sys
from pathlib import Path
import json

if getattr(sys, 'frozen', False):
    BASE_PATH = Path(sys._MEIPASS)
else:
    BASE_PATH = Path(__file__).parent

CONFIG_PATH = BASE_PATH / "config.json"

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

EXTENSION_RULES = config.get("extension_rules", {})
KEYWORD_RULES = config.get("keyword_rules", {})

EXTENSION_RULES = config.get("extension_rules", {})
KEYWORD_RULES = config.get("keyword_rules", {})


def determine_destination(file_path: Path, root_folder: Path) -> Path:
    """
    Determines destination folder based on:
    1. Keyword match
    2. Extension match
    3. Default fallback
    """

    file_name_lower = file_path.name.lower()
    file_extension = file_path.suffix.lower().replace(".", "")

    # 1️⃣ Keyword rules (highest priority)
    for keyword, folder in KEYWORD_RULES.items():
        if keyword.lower() in file_name_lower:
            return root_folder / folder

    # 2️⃣ Extension rules
    for ext, folder in EXTENSION_RULES.items():
        clean_ext = ext.lower().replace(".", "")
        if file_extension == clean_ext:
            return root_folder / folder

    # 3️⃣ Default
    return root_folder / "Others"


def add_date_subfolder(destination: Path) -> Path:
    """
    Adds year/month subfolder.
    Example: Documents/2026/March
    """

    now = datetime.datetime.now()
    year = str(now.year)
    month = now.strftime("%B")

    return destination / year / month


def resolve_duplicate(destination_path: Path) -> Path:
    """
    Prevents overwriting existing files.
    """

    counter = 1
    new_path = destination_path

    while new_path.exists():
        new_name = f"{destination_path.stem}_{counter}{destination_path.suffix}"
        new_path = destination_path.parent / new_name
        counter += 1

    return new_path


def organize_file(file_path: Path, root_folder: Path):

    if not file_path.exists():
        return

    file_name_lower = file_path.name.lower()
    file_extension = file_path.suffix.lower().replace(".", "")

    # Keyword match
    for keyword, folder in KEYWORD_RULES.items():
        if keyword.lower() in file_name_lower:
            destination_base = root_folder / folder
            break
    else:
        # Extension match
        destination_base = root_folder / "Others"

        for ext, folder in EXTENSION_RULES.items():
            if file_extension == ext.lower().replace(".", ""):
                destination_base = root_folder / folder
                break

    # Add date structure
    now = datetime.datetime.now()
    destination = destination_base / str(now.year) / now.strftime("%B")

    destination.mkdir(parents=True, exist_ok=True)

    # Duplicate safety
    final_destination = resolve_duplicate(destination / file_path.name)

    print(f"Moving {file_path.name} -> {final_destination}")

    shutil.move(str(file_path), str(final_destination))


def organize_existing_files(folder: Path):

   

    print("Starting batch scan...")
    print("Folder passed in:", folder)
    print("Folder exists:", folder.exists())

    files_to_process = []

    for file in folder.rglob("*"):
        print("Found:", file)

        if file.is_file():

            print("  It is a file.")

            relative_parts = file.relative_to(folder).parts

            if relative_parts and relative_parts[0].lower() in ["documents", "images", "others"]:
                continue

            files_to_process.append(file)

    print("Files collected:", files_to_process)

    for file in files_to_process:
        organize_file(file, folder)

    print("Batch scan complete.")