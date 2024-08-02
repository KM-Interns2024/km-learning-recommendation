import customtkinter as ctk
import sys
import os

# Temporarily add the parent directory to the Python path
original_sys_path = sys.path.copy()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

try:
    # Import the api_key from the misc module
    from functions import *
finally:
    # Restore the original sys.path
    sys.path = original_sys_path

app = ctk.CTk()
init(app, "Delete an Entry")

def get_text_value(textbox):
    text = textbox.get("0.0", "end").strip()
    return text

def get_combo_value(combobox):
    combo = combobox.get()
    return combo

textbox = ctk.CTkTextbox(app, fg_color="transparent", border_color="#028fc4", border_width=1, height=20, width=240)
textbox.place(relx=0.5, rely=0.2, anchor="center")
text = textbox.get("0.0", "end").strip()

combobox = ctk.CTkComboBox(master=app, values=["positions", "employees", "courses"])
combobox.place(relx=0.5, rely=0.4, anchor="center")
combo = combobox.get()

button = ctk.CTkButton(app, text="Delete", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=240, command=lambda: [delete_vector_by_id(get_text_value(textbox), get_combo_value(combobox)), on_button_click(app, "done.py")])
button.place(relx=0.5, rely=0.6, anchor="center")

button = ctk.CTkButton(app, text="Main Page", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=80, command=lambda: on_button_click(app, "main.py"))
button.place(relx=0.15, rely=0.9, anchor="center")

app.mainloop()
