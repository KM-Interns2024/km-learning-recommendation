import customtkinter as ctk
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

def submit_courses(combobox_course_id, textbox_hard_skill, textbox_soft_skill, course_id_meta, recommended_for_course_meta, technology_meta):
    combobox_course_id = combobox_course_id.get()
    textbox_hard_skill = get_text_value(textbox_hard_skill)
    textbox_soft_skill = get_text_value(textbox_soft_skill)
    course_id_meta = combobox_category.get()
    recommended_for_course_meta = combobox_recommended_for_position.get()
    technology_meta = combobox_technology_meta.get()
    update_vector_metadata_courses(combobox_course_id, textbox_hard_skill, textbox_soft_skill, course_id_meta, recommended_for_course_meta, technology_meta)
    on_button_click(app, "CRUD_Operations/operations.py")
# END FUNCTIONS

app = ctk.CTk()
init(app, "Update course")

app.geometry("800x300+700+400")

button_back = ctk.CTkButton(app, text="Go Back", corner_radius=32, hover_color="#0b3459", fg_color="transparent",
                        border_color="#028fc4", border_width=2, width=90, command=lambda: on_button_click(app, "CRUD_Operations/update/update.py"))
button_back.place(relx=0.1, rely=0.1, anchor="center")

label = ctk.CTkLabel(app, text="Select course id", font=("Arial", 12))
label.place(relx=0.15, rely=0.25, anchor="center")

list_entries = get_list_of_ids('courses')
combobox_course_id = SearchableCombobox(app)
combobox_course_id.set_completion_list(list_entries)
combobox_course_id.place(relx=0.15, rely = 0.375, anchor = "center")

label = ctk.CTkLabel(app, text="Recommended for:", font=("Arial", 12))
label.place(relx=0.15, rely=0.5, anchor="center")

list_entries = get_list_of_ids('positions')
combobox_recommended_for_position = SearchableCombobox(app)
combobox_recommended_for_position.set_completion_list(list_entries)
combobox_recommended_for_position.place(relx=0.15, rely=0.6, anchor="center")

label = ctk.CTkLabel(app, text="Technical skill form 0 to 1", font=("Arial", 12))
label.place(relx=0.5, rely=0.25, anchor="center")
textbox_hard_skill = ctk.CTkTextbox(app, height=20, width=200)
textbox_hard_skill.place(relx=0.5, rely=0.375, anchor="center")

label = ctk.CTkLabel(app, text="Soft skill form 0 to 1", font=("Arial", 12))
label.place(relx=0.5, rely=0.5, anchor="center")
textbox_soft_skill = ctk.CTkTextbox(app, height=20, width=200)
textbox_soft_skill.place(relx=0.5, rely=0.6, anchor="center")

label = ctk.CTkLabel(app, text="Select category", font=("Arial", 12))
label.place(relx=0.85, rely=0.25, anchor="center")

combobox_category = ctk.CTkComboBox(app, values=["Soft", "Hard"])
combobox_category.place(relx=0.85, rely=0.375, anchor="center")

label = ctk.CTkLabel(app, text="Select technology", font=("Arial", 12))
label.place(relx=0.85, rely=0.5, anchor="center")

combobox_technology_meta = ctk.CTkComboBox(app, values=["Java", "AI", "Python", "ML"])
combobox_technology_meta.place(relx=0.85, rely=0.6, anchor="center")

button_submit = ctk.CTkButton(app, text="Submit", corner_radius=32, hover_color="#0b3459", fg_color="transparent",
                        border_color="#028fc4", border_width=2, width=100, command=lambda: submit_courses(combobox_course_id, textbox_hard_skill, textbox_soft_skill, combobox_course_id, combobox_recommended_for_position, combobox_technology_meta))
button_submit.place(relx=0.9, rely=0.9, anchor="center")

button = ctk.CTkButton(app, text="Main Page", corner_radius=32, hover_color="#0b3459", fg_color="transparent",
                        border_color="#028fc4", border_width=2, width=90, command=lambda: on_button_click(app, "main.py"))
button.place(relx=0.1, rely=0.9, anchor="center")

app.mainloop()
