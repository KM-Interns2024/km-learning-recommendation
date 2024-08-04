import tkinter as tk
from tkinter import filedialog
import shutil
import os

def upload_file():
    # Open file dialog and ask the user to select a file
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=(("PDF files", "*.pdf"), ("all files", "*.*"))
    )
    
    # Check if a file was selected
    if file_path:
        # Get the directory where you want to save the file
        upload_directory = os.path.join(os.getcwd(), 'uploads')
        
        # Create the directory if it doesn't exist
        if not os.path.exists(upload_directory):
            os.makedirs(upload_directory)
        
        # Get the base name of the file to keep the original file name
        file_name = os.path.basename(file_path)
        
        # Define the path where the file will be copied
        destination = os.path.join(upload_directory, file_name)
        
        # Copy the file to the destination
        shutil.copy(file_path, destination)
        
        print(f'File uploaded to {destination}')
    else:
        print('No file selected')

# Create the main application window
root = tk.Tk()
root.title("File Upload")

# Create a button that calls the upload_file function when clicked
upload_button = tk.Button(root, text="Upload CV", command=upload_file)
upload_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()