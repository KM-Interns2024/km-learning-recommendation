import customtkinter as ctk
from functions import *

# Initialize the app
app = ctk.CTk()
init(app, "Employee Knowledge Management System")

# my_font = ctk.CTkFont(family="Helvetica", size=12)

# Form forwards
button = ctk.CTkButton(app, text="Check Employee's Status", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=300, command=lambda: on_button_click(app, "main.py"))
button.place(relx=0.5, rely=0.4, anchor="center")

button = ctk.CTkButton(app, text="Operations", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "CRUD_Operations/operations.py"))
button.place(relx=0.3, rely=0.6, anchor="center")

button = ctk.CTkButton(app, text="Check CV", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "main.py"))
button.place(relx=0.7, rely=0.6, anchor="center")

app.mainloop()
