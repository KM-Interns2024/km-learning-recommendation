import os
import sys
import threading
import customtkinter as ctk

# Temporarily add the parent directory to the Python path
original_sys_path = sys.path.copy()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    # Import the api_key from the misc module
    from CRUD.create_vector import *
    from CRUD.delete import *
    from CRUD.update import *
    from CRUD.read import *
finally:
    # Restore the original sys.path
    sys.path = original_sys_path


def init(app, title):
    app.title(f"{title}")
    app.geometry("400x200+700+400")
    ctk.set_appearance_mode("dark")
    app.iconbitmap("../venv/Lib/site-packages/customtkinter/assets/icons/images.ico")
    app.resizable(False, False)

def on_button_click(app, form):
    app.destroy()
    os.system(f'python {form}')  # Run the specified script
