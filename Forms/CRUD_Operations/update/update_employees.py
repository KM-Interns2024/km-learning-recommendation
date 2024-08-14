import customtkinter as tk
import sys
import os

# Temporarily add the parent directory to the Python path
original_sys_path = sys.path.copy()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

try:
    # Import the api_key from the misc module
    from functions import *
    from services.searchable_combobox import *
finally:
    # Restore the original sys.path
    sys.path = original_sys_path

# FUNCTIONS

def get_text_value(textbox):
    return textbox.get("0.0", "end").strip()

def submit_employee():
    id_value = combobox_employee_id.get()
    value1_text = get_text_value(value1)
    value2_text = get_text_value(value2)
    metadata_text = get_text_value(metadata)
    update_vector_metadata_employees(id_value, value1_text, value2_text, metadata_text)
    on_button_click(app, "CRUD_Operations/operations.py")
# END FUNCTIONS

app = tk.CTk()
init(app, "Update employee")

app.geometry("600x300+700+400")

button = ctk.CTkButton(app, text="Go Back", corner_radius=32, hover_color="#0b3459", fg_color="transparent",
                        border_color="#028fc4", border_width=2, width=90, command=lambda: on_button_click(app, "CRUD_Operations/update/update.py"))
button.place(relx=0.1, rely=0.1, anchor="center")

label = ctk.CTkLabel(app, text="Select the employee's ID", font=("Arial", 12))
label.place(relx=0.5, rely=0.1, anchor="center")

list_entries = get_list_of_ids('employees')
combobox_employee_id = SearchableCombobox(app)
combobox_employee_id.set_completion_list(list_entries)
combobox_employee_id.place(relx=0.375, rely=0.15)

label = ctk.CTkLabel(app, text="Technical skill form 0 to 1", font=("Arial", 12))
label.place(relx=0.5, rely=0.3, anchor="center")
value1 = ctk.CTkTextbox(app, height=20, width=200)
value1.place(relx=0.5, rely=0.40, anchor="center")

label = ctk.CTkLabel(app, text="Soft skill form 0 to 1", font=("Arial", 12))
label.place(relx=0.5, rely=0.5, anchor="center")
value2 = ctk.CTkTextbox(app, height=20, width=200)
value2.place(relx=0.5, rely=0.60, anchor="center")

label = ctk.CTkLabel(app, text="Enter position", font=("Arial", 12))
label.place(relx=0.5, rely=0.7, anchor="center")
metadata = ctk.CTkTextbox(app, height=20, width=200)
metadata.place(relx=0.5, rely=0.80, anchor="center")

button = ctk.CTkButton(app, text="Submit", corner_radius=32, hover_color="#0b3459", fg_color="transparent",
                        border_color="#028fc4", border_width=2, width=100, command=lambda: submit_employee())
button.place(relx=0.9, rely=0.9, anchor="center")

button = ctk.CTkButton(app, text="Main page", corner_radius=32, hover_color="#0b3459", fg_color="transparent",
                        border_color="#028fc4", border_width=2, width=90, command=lambda: on_button_click(app, "main.py"))
button.place(relx=0.1, rely=0.9, anchor="center")

app.mainloop()
