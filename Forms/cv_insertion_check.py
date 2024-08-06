import customtkinter as ctk
from functions import *

def check_cv_insertion():

    app = ctk.CTk()
    init(app, "The CV has been uploaded.")

    app.geometry("300x100")
    app.grab_set()  # Make it modal

    label = ctk.CTkLabel(app, text="The CV has been uploaded!", font=("Arial", 16))
    label.place(relx=0.5, rely=0.4, anchor="center")

    button = ctk.CTkButton(app, text="ok", command=lambda: app.destroy())
    button.place(relx=0.5, rely=0.7, anchor="center")

    app.mainloop()