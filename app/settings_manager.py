import json
from pathlib import Path

SETTINGS_FILE = Path("settings.json")


DEFAULT_SETTINGS = {
    "watched_folder": "",
    "start_on_login": False
}


def load_settings():
    if SETTINGS_FILE.exists():
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    return DEFAULT_SETTINGS.copy()


def save_settings(settings: dict):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)
