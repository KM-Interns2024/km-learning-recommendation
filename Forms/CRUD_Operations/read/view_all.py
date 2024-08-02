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
init(app, "View All Entries")
app.geometry("1920x1080+0+0")

button = ctk.CTkButton(app, text="Go Back", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "CRUD_Operations/read/select_view.py"))
button.place(relx=0.15, rely=0.1, anchor="center")

textbox = ctk.CTkTextbox(app, width=400, height=300, corner_radius=10)
textbox.pack(padx=10)
textbox.place(relx=0.2, rely=0.5, anchor="center")
textbox.insert("0.0", f"{query_all('employees')}")

textbox = ctk.CTkTextbox(app, width=400, height=300, corner_radius=10)
textbox.pack(padx=10)
textbox.place(relx=0.5, rely=0.5, anchor="center")
textbox.insert("0.0", f"{query_all('courses')}")

textbox = ctk.CTkTextbox(app, width=400, height=300, corner_radius=10)
textbox.pack(padx=10)
textbox.place(relx=0.8, rely=0.5, anchor="center")
textbox.insert("0.0", f"{query_all('positions')}")

button = ctk.CTkButton(app, text="Main Page", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "main.py"))
button.place(relx=0.15, rely=0.9, anchor="center")

app.mainloop()
