import customtkinter as ctk
from functions import *

app = ctk.CTk()
init(app, "Done!")

app.geometry("300x100")
app.grab_set()  # Make it modal

label = ctk.CTkLabel(app, text="All done!", font=("Arial", 16))
label.place(relx=0.5, rely=0.4, anchor="center")

button = ctk.CTkButton(app, text="ok", command=lambda:  on_button_click(app, "main.py"))
button.place(relx=0.5, rely=0.7, anchor="center")

app.mainloop()
