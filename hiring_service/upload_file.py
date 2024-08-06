import tkinter as tk
from tkinter import filedialog
import shutil
import os
from Forms.cv_insertion_check import check_cv_insertion



def upload_file():
    # Open file dialog and ask the user to select a file
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=(("PDF files", "*.pdf"), ("all files", "*.*"))
    )
    try:
        # Check if a file was selected
        if file_path:
            # Get the directory where you want to save the file
            upload_directory = os.path.join(os.getcwd(), '../hiring_service/uploads')

            # Create the directory if it doesn't exist
            if not os.path.exists(upload_directory):
                os.makedirs(upload_directory)

            # Get the base name of the file to keep the original file name
            # file_name = os.path.basename(file_path)
            file_name = "CV_to_be_rated.pdf"
            

            # Define the path where the file will be copied
            destination = os.path.join(upload_directory, file_name)

            # Copy the file to the destination
            shutil.copy(file_path, destination)

            print(f'File uploaded to {destination}')
            check_cv_insertion()
            return file_name
        else:
            print('No file selected')
            return None
    except Exception as e:
        print(f'Error: {e}')
        return None