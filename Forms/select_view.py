import customtkinter as tk
from functions import *

app = tk.CTk()
init(app, "Select Form")

button = ctk.CTkButton(app, text="Go Back", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "operations.py"))
button.place(relx=0.2, rely=0.1, anchor="center")

button = ctk.CTkButton(app, text="Main Page", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "main.py"))
button.place(relx=0.2, rely=0.9, anchor="center")

button = ctk.CTkButton(app, text="View One Entry", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "view_entry.py"))
button.place(relx=0.7, rely=0.5, anchor="center")

button = ctk.CTkButton(app, text="View All Entries", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "view_all.py"))
button.place(relx=0.3, rely=0.5, anchor="center")

app.mainloop()
