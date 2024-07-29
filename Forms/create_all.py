import customtkinter as ctk
from functions import *

app = ctk.CTk()
init(app, "Create All")

button = ctk.CTkButton(app, text="Go Back", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "operations.py"))
button.place(relx=0.2, rely=0.1, anchor="center")

textbox = ctk.CTkEntry(app)
textbox.place(relx=0.5, rely=0.4, anchor="center")

button = ctk.CTkButton(app, text="Main Page", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "main.py"))
button.place(relx=0.2, rely=0.9, anchor="center")

button = ctk.CTkButton(app, text="Submit", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "operations.py"))
button.place(relx=0.8, rely=0.9, anchor="center")

app.mainloop()
