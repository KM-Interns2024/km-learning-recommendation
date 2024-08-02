import customtkinter as ctk
import sys
import os

# Temporarily add the parent directory to the Python path
original_sys_path = sys.path.copy()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from functions import *
finally:
    # Restore the original sys.path
    sys.path = original_sys_path

app = ctk.CTk()
init(app, "Operations")

button = ctk.CTkButton(app, text="Create All", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "CRUD_Operations/create/create_all.py"))
button.place(relx=0.3, rely=0.40, anchor="center")

button = ctk.CTkButton(app, text="Delete an Entry", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "CRUD_Operations/delete/delete.py"))
button.place(relx=0.7, rely=0.40, anchor="center")

button = ctk.CTkButton(app, text="View", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "CRUD_Operations/read/select_view.py"))
button.place(relx=0.3, rely=0.60, anchor="center")

button = ctk.CTkButton(app, text="Update", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "CRUD_Operations/update/update.py"))
button.place(relx=0.7, rely=0.60, anchor="center")

button = ctk.CTkButton(app, text="Main Page", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=90, command=lambda: on_button_click(app, "main.py"))
button.place(relx=0.15, rely=0.9, anchor="center")


app.mainloop()
