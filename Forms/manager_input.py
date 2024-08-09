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
    from hiring_service.Datasets import *
finally:
    # Restore the original sys.path
    sys.path = original_sys_path


app = ctk.CTk()
init(app, "Manager input")
app.geometry("600x300+700+400")

label_rate_candidate = ctk.CTkLabel(master=app, text="Rate the candidate based on his interview")
label_rate_candidate.place(relx=0.5, rely=0.05, anchor=ctk.CENTER)


def slider_event(value):
    print(value)

var_soft = ctk.IntVar()
var_hard = ctk.IntVar()

label_soft_rating = ctk.CTkLabel(master=app, text="Soft skills")
label_soft_rating.place(relx=0.35, rely=0.2)

def update_soft_skills(value):
    label_slider_soft.configure(text=value)

def update_hard_skills(value):
    label_slider_hard.configure(text=value)
    

label_slider_soft = ctk.CTkLabel(master=app, text='50.0')
label_slider_soft.place(relx=0.75, rely=0.3)

slider_soft = ctk.CTkSlider(master=app, from_=0, to=100, command=update_soft_skills, number_of_steps=10)
slider_soft.place(relx=0.5, rely=0.35, anchor=ctk.CENTER)

label_slider_hard = ctk.CTkLabel(master=app, text='50.0')
label_slider_hard.place(relx=0.75, rely= 0.5)

label_hard_rating = ctk.CTkLabel(master=app, text="Hard skills")
label_hard_rating.place(relx=0.35, rely=0.4)

slider_hard = ctk.CTkSlider(master=app, from_=0, to=100, command=update_hard_skills, number_of_steps=10)
slider_hard.place(relx=0.5, rely=0.55, anchor=ctk.CENTER)


button_submit = ctk.CTkButton(app, text="Submit", corner_radius=32, hover_color="#0b3459",
                        fg_color="transparent", border_color="#028fc4", border_width=2, width=90)
button_submit.place(relx=0.5, rely=0.80, anchor="center")

button = ctk.CTkButton(app, text="Go Back", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=90, command=lambda: on_button_click(app, "main.py"))
button.place(relx=0.1, rely=0.1, anchor="center")

app.mainloop()
