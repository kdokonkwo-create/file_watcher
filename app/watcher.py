from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import time
from organizer import organize_file


class FileHandler(FileSystemEventHandler):

    def __init__(self, root_folder: Path):
        super().__init__()
        self.root_folder = root_folder

    def on_created(self, event):

        if event.is_directory:
            return

        file_path = Path(event.src_path)

        # Ignore temporary download files
        if file_path.suffix.lower() in [".crdownload", ".tmp", ".part"]:
            return

        # Small delay to ensure file writing is complete
        time.sleep(1)

        try:
            message = organize_file(file_path, self.root_folder)
            print(message)
        except Exception as e:
            print(f"Error organizing {file_path.name}: {e}")


class FolderWatcher:

    def __init__(self, folder_to_watch: Path):
        self.folder_to_watch = folder_to_watch
        self.observer = Observer()
        self.event_handler = FileHandler(folder_to_watch)

    def start(self):
        self.observer.schedule(
            self.event_handler,
            str(self.folder_to_watch),
            recursive=True
        )
        self.observer.start()
        print(f"Started watching: {self.folder_to_watch}")

    def stop(self):
        self.observer.stop()
        self.observer.join()
        print("Stopped watching.")