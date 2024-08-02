import customtkinter as ctk
from functions import *

app = ctk.CTk()
init(app, "Operations")

button = ctk.CTkButton(app, text="Create All", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "create_all.py"))
button.place(relx=0.3, rely=0.40, anchor="center")

button = ctk.CTkButton(app, text="Delete an Entry", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "delete.py"))
button.place(relx=0.7, rely=0.40, anchor="center")

button = ctk.CTkButton(app, text="View", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "select_view.py"))
button.place(relx=0.3, rely=0.60, anchor="center")

button = ctk.CTkButton(app, text="Update", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "update.py"))
button.place(relx=0.7, rely=0.60, anchor="center")

button = ctk.CTkButton(app, text="Main Page", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=90, command=lambda: on_button_click(app, "main.py"))
button.place(relx=0.15, rely=0.9, anchor="center")


app.mainloop()
