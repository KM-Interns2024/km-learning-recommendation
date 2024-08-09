import customtkinter as ctk
import sys
import os
from functions import *

# Temporarily add the parent directory to the Python path
original_sys_path = sys.path.copy()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hiring_service')))
print(sys.path)

try:
    # Import the api_key from the misc module
    from hiring_service.Algorithm import *
    from hiring_service.upload_file import upload_file
    from hiring_service.Datasets import *
finally:
    # Restore the original sys.path
    sys.path = original_sys_path


app = ctk.CTk()
init(app, "Upload a resume in pdf format")
app.geometry("600x300+700+400")

button = ctk.CTkButton(app, text="Go Back", corner_radius=32, hover_color="#0b3459", fg_color="transparent",
                        border_color="#028fc4", border_width=2, width=90, command=lambda: on_button_click(app, "main.py"))
button.place(relx=0.1, rely=0.1, anchor="center")

button = ctk.CTkButton(app, text="Upload a resume", corner_radius=32, hover_color="#0b3459",
                        fg_color="transparent", border_color="#028fc4", border_width=2, width=150, command=lambda: upload_file())
button.place(relx=0.5, rely=0.2, anchor="center")

label = ctk.CTkLabel(master=app, text="Please insert your job description")
label.place(relx = 0.35, rely= 0.3)
textbox = ctk.CTkTextbox(app, width=150, height=100, corner_radius=10)
textbox.pack(padx=10)
textbox.place(relx=0.5, rely=0.55, anchor="center")

button = ctk.CTkButton(app, text="Submit", corner_radius=32, hover_color="#0b3459", fg_color="transparent",
                        border_color="#028fc4", border_width=2, width=90, command=lambda: [algorithm(textbox.get("0.0", "end"), '../hiring_service/'),
                        app.destroy()])
button.place(relx=0.5, rely=0.9, anchor="center")

app.mainloop()
