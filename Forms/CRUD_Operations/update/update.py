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
init(app, "Choose what to update")

button = ctk.CTkButton(app, text="Go Back", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=90, command=lambda: on_button_click(app, "CRUD_Operations/operations.py"))
button.place(relx=0.15, rely=0.1, anchor="center")

button = ctk.CTkButton(app, text="Update Employees", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "CRUD_Operations/update/update_employees.py"))
button.place(relx=0.5, rely=0.25, anchor="center")

button = ctk.CTkButton(app, text="Update Courses", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "CRUD_Operations/update/update_courses.py"))
button.place(relx=0.5, rely=0.5, anchor="center")

button = ctk.CTkButton(app, text="Update Positions", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "CRUD_Operations/update/update_positions.py"))
button.place(relx=0.5, rely=0.75, anchor="center")

button = ctk.CTkButton(app, text="Main Page", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=90, command=lambda: on_button_click(app, "main.py"))
button.place(relx=0.15, rely=0.9, anchor="center")

app.mainloop()
