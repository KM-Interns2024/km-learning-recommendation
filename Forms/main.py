import os
import tkinter as tk
from functions import *

root = tk.Tk()
init(root, "Main Page")

goto(root, "create_all.py", "Go To Create All page")
goto(root, "delete_all.py", "Go To Delete All page")
goto(root, "select.py", "Go To View an entry page")
goto(root, "update.py", "Go To Update an entry page")


name_label = tk.Label(root, text="Enter Employee")
name_label.pack()
name_textbox = tk.Entry(root)
name_textbox.pack()

submit_button = tk.Button(root, text="Submit")
submit_button.pack()

root.mainloop()
