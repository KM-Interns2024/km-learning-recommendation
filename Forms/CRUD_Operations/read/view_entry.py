import customtkinter as ctk
import sys
import os

# Temporarily add the parent directory to the Python path
original_sys_path = sys.path.copy()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

try:
    # Import the api_key from the misc module
    from functions import *
finally:
    # Restore the original sys.path
    sys.path = original_sys_path

app = ctk.CTk()
init(app, "View All Entries")

textbox = ctk.CTkTextbox(app, width=400, height=300, corner_radius=10)
textbox.pack(padx=10)
textbox.place(relx=0.2, rely=0.5, anchor="center")
textbox.insert("0.0", f"{query_all('employees')}")

app.mainloop()
