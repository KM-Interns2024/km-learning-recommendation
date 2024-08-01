import customtkinter as ctk
from functions import *

# Temporarily add the parent directory to the Python path
original_sys_path = sys.path.copy()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    # Import the api_key from the misc module
    from CRUD.create_vector import *
finally:
    # Restore the original sys.path
    sys.path = original_sys_path


app = ctk.CTk()
init(app, "Confirm")

app.geometry("300x100")
app.grab_set()  # Make it modal

label = ctk.CTkLabel(app, text="Do you confirm the insertions?", font=("Arial", 16))
label.place(relx=0.5, rely=0.1, anchor="center")


label = ctk.CTkLabel(app, text="Please wait for the window to close after confirming!", font=("Arial", 10))
label.place(relx=0.5, rely=0.4, anchor="center")


button = ctk.CTkButton(app, text="yes", command=lambda: [create_all(), on_button_click(app, "done.py")])
button.place(relx=0.5, rely=0.7, anchor="center")


app.mainloop()

