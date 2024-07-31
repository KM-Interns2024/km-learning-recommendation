import customtkinter as ctk
from functions import *

app = ctk.CTk()
init(app, "Delete All")

button = ctk.CTkButton(app, text="Delete an Employee or a Position", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=240, command=lambda: on_button_click(app, "kbc_delete.py"))
button.place(relx=0.5, rely=0.4, anchor="center")

button = ctk.CTkButton(app, text="Delete a Course", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=240, command=lambda: on_button_click(app, "course_delete.py"))
button.place(relx=0.5, rely=0.6, anchor="center")

app.mainloop()
