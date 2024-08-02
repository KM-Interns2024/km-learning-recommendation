import customtkinter as tk
from functions import *
from CRUD.update import *


# Temporarily add the parent directory to the Python path
original_sys_path = sys.path.copy()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    # Import the api_key from the misc module
    from CRUD.update import *
finally:
    # Restore the original sys.path
    sys.path = original_sys_path


app = tk.CTk()
init(app, "Update")

button = ctk.CTkButton(app, text="Go Back", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "operations.py"))
button.place(relx=0.2, rely=0.8, anchor="center")


def get_text_value(textbox):
    text = textbox.get("0.0", "end").strip()
    return text

def get_combo_value(combobox):
    combo = combobox.get()
    return combo

    
index_combo_box = ctk.CTkComboBox(app, values=['Employee', 'Course'])
index_combo_box.place(relx=0.5, rely=0.2, anchor="center")

button = ctk.CTkButton(app, text="Submit", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: [update_vector_metadata(id = vector_id, value1 = value1, value2 = value2, namespace = get_combo_value(index_combo_box), metadata = metadata), on_button_click(app, "operations.py")])
button.place(relx=0.8, rely=0.8, anchor="center")

# update_vector(index_name = 'kbc', namespace = namespace, id = vector_id)

app.mainloop()
