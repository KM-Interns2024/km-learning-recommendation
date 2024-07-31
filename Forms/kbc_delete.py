from pytube import *
import customtkinter as ctk
from functions import *

app = ctk.CTk()
init(app, "Delete All")

def get_text_value(textbox):
    text = textbox.get("0.0", "end").strip()
    return text

def get_combo_value(combobox):
    combo = combobox.get()
    return combo

textbox = ctk.CTkTextbox(app, fg_color="transparent", border_color="#028fc4", border_width=1, height=20, width=240)
textbox.place(relx=0.5, rely=0.2, anchor="center")
text = textbox.get("0.0", "end").strip()

combobox = ctk.CTkComboBox(master=app, values=["positions", "employees"])
combobox.place(relx=0.5, rely=0.4, anchor="center")
combo = combobox.get()

button = ctk.CTkButton(app, text="Delete", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=240, command=lambda: [kbc_delete_vector_by_id(get_text_value(textbox), get_combo_value(combobox)), on_button_click(app, "main.py")])
button.place(relx=0.5, rely=0.6, anchor="center")

app.mainloop()
