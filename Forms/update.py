import customtkinter as tk
from functions import *
from CRUD.update import *

app = tk.CTk()
init(app, "Update")

# on_button_click(app, "main.py")

button = ctk.CTkButton(app, text="Go Back", corner_radius=32, hover_color="#0b3459", fg_color="transparent", border_color="#028fc4", border_width=2, width=140, command=lambda: on_button_click(app, "operations.py"))
button.place(relx=0.5, rely=0.8, anchor="center")

namespace = ''
def combo_box_callback(choice):
    print("Combobox dropdown clicked: ", choice)
    if(choice.lower() == 'employee'):
        namespace = 'employees'
    elif(choice.lower() == 'position'):
        namespace = 'positions'
    else:
        namespace = 'courses'

    print(namespace)
    return namespace
    
index_combo_box = ctk.CTkComboBox(master= app,
                                values=['Employee', 'Position', 'Course'],
                                command=combo_box_callback)

index_combo_box.pack(padx=20, pady=10)
index_combo_box.set("Employee")

# update_vector(index_name = 'kbc', namespace = namespace, id = vector_id)

app.mainloop()