import customtkinter as ctk

from Forms.employee_skills_plot import open_employee_section
from functions import *
import sys
import os

# Temporarily add the parent directory to the Python path
original_sys_path = sys.path.copy()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    # Import the api_key from the misc module
    from recommender import recommender
finally:
    # Restore the original sys.path
    sys.path = original_sys_path

app = ctk.CTk()
init(app, "View an Entries")
app.geometry("500x300+700+400")

text_var = ctk.CTkLabel(app, text="Enter Position ID", font=("Arial", 12))
text_var.place(relx=0.5, rely=0.1, anchor="center")

textbox_id = ctk.CTkTextbox(app, fg_color="transparent", border_color="#028fc4", border_width=1, height=20, width=240)
textbox_id.place(relx=0.5, rely=0.2, anchor="center")

textbox = ctk.CTkTextbox(app, width=300, height=120, corner_radius=10, state='disabled')
textbox.pack(padx=10)
textbox.place(relx=0.5, rely=0.55, anchor="center")

def on_submit():
    text = textbox_id.get("0.0", "end").strip()
    try:
        result = recommender(text)  # Call the recommender function
        if result is None:
            result = "No recommendations found."
    except Exception as e:
        result = f"Error: {str(e)}"

    textbox.configure(state='normal')
    textbox.delete("0.0", "end")
    textbox.insert("0.0", result)
    textbox.configure(state='disabled')

button = ctk.CTkButton(app, text="Submit", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=on_submit)
button.place(relx=0.5, rely=0.9, anchor="center")

button = ctk.CTkButton(app, text="Main Page", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=90, command=lambda: on_button_click(app, "main.py"))
button.place(relx=0.1, rely=0.9, anchor="center")

button_employee = ctk.CTkButton(app, text="Track Employee", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=90, command=lambda: open_employee_section(app))
button_employee.place(relx=0.9, rely=0.9, anchor="center")
# Properly handle window closing
def on_closing():
    app.withdraw()
    app.quit()

app.protocol("WM_DELETE_WINDOW", on_closing)


app.mainloop()
