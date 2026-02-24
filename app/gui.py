import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from watcher import FolderWatcher
from tray import setup_tray
from settings_manager import load_settings, save_settings
from organizer import organize_existing_files


class OrganizerApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Smart File Organizer")
        self.root.geometry("420x230")

        self.settings = load_settings()
        self.folder_path = None
        self.watcher = None
        self.is_watching = False

        # ---------------- UI ---------------- #

        self.label = tk.Label(root, text="No folder selected", wraplength=380)
        self.label.pack(pady=10)

        self.status_label = tk.Label(root, text="Status: Idle", fg="gray")
        self.status_label.pack(pady=5)

        self.select_button = tk.Button(root, text="Select Folder", command=self.select_folder)
        self.select_button.pack(pady=5)

        self.start_button = tk.Button(root, text="Start Watching", command=self.start_watching)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop Watching", command=self.stop_watching, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.hide_window)

        # Tray setup
        self.tray_icon = setup_tray(self)

        # Restore previous folder
        if self.settings["watched_folder"]:
            self.folder_path = Path(self.settings["watched_folder"])
            self.label.config(text=f"Selected Folder:\n{self.folder_path}")
            self.status_label.config(text="Status: Folder Loaded", fg="blue")

    # ---------------- Window Controls ---------------- #

    def hide_window(self):
        self.root.withdraw()

    def show_window(self):
        self.root.deiconify()

    def quit_app(self):
        if self.watcher:
            self.watcher.stop()
        self.root.destroy()

    # ---------------- Folder Selection ---------------- #

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path = Path(folder)
            self.label.config(text=f"Selected Folder:\n{self.folder_path}")

            self.settings["watched_folder"] = str(self.folder_path)
            save_settings(self.settings)

            self.status_label.config(text="Status: Folder Selected", fg="blue")

    # ---------------- Watching Logic ---------------- #

    def start_watching(self):

        import os

        if not self.folder_path:
            messagebox.showwarning(
            "No Folder Selected",
            "Please select a folder first"
            )
            return

        print("Starting automation on:", self.folder_path)

    
        

    # Step 1 — Batch organize existing files
        print("Running initial organization pass...")
        organize_existing_files(self.folder_path)

    # Step 2 — Start watcher AFTER batch scan completes
        print("Starting watcher...")

        self.watcher = FolderWatcher(self.folder_path)
        self.watcher.start()

        self.is_watching = True

        self.status_label.config(
        text="Status: Watching",
        fg="green"
        )

        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        messagebox.showinfo(
            "Automation Started",
            "Existing files have been organized.\n"
            "The app is now monitoring new files."
        )
    def stop_watching(self):

        if self.watcher and self.is_watching:
            self.watcher.stop()
            self.is_watching = False

            self.status_label.config(text="Status: Stopped", fg="red")
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

            messagebox.showinfo("Watcher Stopped", "Folder monitoring has been stopped.")