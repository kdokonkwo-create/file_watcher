import pystray
from pystray import MenuItem as item
from PIL import Image
import threading


def create_image():
    """
    Creates a simple square icon.
    In production, you'd load a real .ico file.
    """
    return Image.new("RGB", (64, 64), "blue")


def setup_tray(app):
    """
    Creates and runs system tray icon in a separate thread.
    """

    def on_open(icon, item):
        app.show_window()

    def on_exit(icon, item):
        icon.stop()
        app.quit_app()

    menu = (
        item("Open", on_open),
        item("Exit", on_exit),
    )

    icon = pystray.Icon(
        "SmartOrganizer",
        create_image(),
        "Smart Organizer",
        menu
    )

    # Run tray icon in separate thread
    tray_thread = threading.Thread(target=icon.run, daemon=True)
    tray_thread.start()

    return icon
