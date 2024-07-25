import os
import tkinter as tk

def init(root, title):
    root.title(title)
    root.geometry("600x400")

def goto(root, form, text):
    def on_button_click():
        root.destroy()  # Close the current Tkinter window
        os.system(f'python {form}')  # Run the specified script

    button = tk.Button(root, text=text, command=on_button_click)
    button.pack()