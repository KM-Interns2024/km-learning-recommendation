import customtkinter as ctk
import sys
import os
from functions import *
from hiring_service.upload_file import upload_file


app = ctk.CTk()
init(app, "Upload a resume in pdf format")

button = ctk.CTkButton(app, text="Go Back", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=90, command=lambda: on_button_click(app, "CRUD_Operations/operations.py"))
button.place(relx=0.5, rely=0.9, anchor="center")

button = ctk.CTkButton(app, text="Upload a resume", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=150, height= 80, command=lambda: upload_file())
button.place(relx=0.5, rely=0.5, anchor="center")

textbox = ctk.CTkTextbox(app, )



app.mainloop()
