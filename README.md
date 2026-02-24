# Smart File Watcher & Auto Organizer

## 📌 Overview

Smart File Watcher is a desktop automation tool that continuously monitors a selected folder and automatically organizes files into a structured directory system.

The application features a simple graphical user interface (GUI) that allows users to select a folder to monitor. Once activated, it recursively tracks all files and subfolders in real time.

Even when the main window is closed, the application remains active in the system tray and continues monitoring in the background.

---

## 🚀 Problem It Solves

Folders such as Downloads, Desktop, or shared work directories quickly become cluttered.

Manually sorting files by type and date is repetitive and inefficient.

This tool eliminates that problem by:

- Monitoring a folder recursively
- Detecting newly added files automatically
- Sorting them into a structured, chronological system
- Running silently in the background

---

## 🖥 How to Use

1. Launch the application.
2. Click **Select Folder**.
3. Choose the directory you want to monitor.
4. The watcher starts immediately.
5. Any new file added to the monitored folder (or its subfolders) will be automatically sorted.

When the window is closed:
- The app minimizes to the system tray.
- Monitoring continues in the background.
- You can reopen or exit the application from the tray icon.

---

## 📂 Output Directory Structure

Files are organized into a flat, scalable structure based on:

- File Type
- Year
- Month
reference the sample data directory to see the folder before and after organization

## ✨ Key Features

- Recursive directory monitoring
- Real-time file detection
- Automatic file type classification
- Chronological folder structure
- Background monitoring via system tray
- Minimal user interaction required
- Modular and scalable code architecture

---

## 🛠 Technologies Used

- Python
- Watchdog (file system monitoring)
- Tkinter (GUI)
- Pystray (system tray integration)
- Pillow (tray icon support)
- OS & Shutil modules
- PyInstaller (for packaging)



