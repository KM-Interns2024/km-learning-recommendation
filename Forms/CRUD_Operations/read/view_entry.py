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
init(app, "View an Entries")
app.geometry("500x300+700+400")

button = ctk.CTkButton(app, text="Go Back", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=90, command=lambda: on_button_click(app, "CRUD_Operations/read/select_view.py"))
button.place(relx=0.15, rely=0.1, anchor="center")

textbox_id = ctk.CTkTextbox(app, fg_color="transparent", border_color="#028fc4", border_width=1, height=20, width=240)
textbox_id.place(relx=0.5, rely=0.25, anchor="center")

combobox_namespace = ctk.CTkComboBox(master=app, values=["positions", "employees", "courses"])
combobox_namespace.place(relx=0.5, rely=0.4, anchor="center")

textbox = ctk.CTkTextbox(app, width=300, height=80, corner_radius=10, state='disabled')
textbox.pack(padx=10)
textbox.place(relx=0.5, rely=0.6, anchor="center")

def on_submit():
    text = textbox_id.get("0.0", "end").strip()
    combo = combobox_namespace.get()
    result = query_one(text, combo)
    textbox.configure(state='normal')
    textbox.delete("0.0", "end")
    textbox.insert("0.0", f"{result}")
    textbox.configure(state='disabled')

button = ctk.CTkButton(app, text="Submit", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=on_submit)
button.place(relx=0.8, rely=0.9, anchor="center")

button = ctk.CTkButton(app, text="Main Page", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=90, command=lambda: on_button_click(app, "main.py"))
button.place(relx=0.15, rely=0.9, anchor="center")

app.mainloop()
