import os
import customtkinter as tk

def init(app, title):
    app.title(f"{title}")
    app.geometry("400x200")
    app.iconbitmap("../venv/Lib/site-packages/customtkinter/assets/icons/images.ico")
    app.resizable(False, False)

def on_button_click(app, form):
    app.destroy()  # Close the current Tkinter window
    os.system(f'python {form}')  # Run the specified script
