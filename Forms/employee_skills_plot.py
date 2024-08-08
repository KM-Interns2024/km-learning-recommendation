import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from plot_employee_development import employee_skills_plot
from CRUD.read import query_vector_id

def open_employee_section(app):
    employee_window = ctk.CTkToplevel(app)
    employee_window.title("Track Employee Development")
    employee_window.geometry("500x300+700+400")

    employee_id_label = ctk.CTkLabel(employee_window, text="Enter Employee ID", font=("Arial", 12))
    employee_id_label.place(relx=0.5, rely=0.2, anchor="center")

    employee_id_entry = ctk.CTkTextbox(employee_window, fg_color="transparent", border_color="#028fc4", border_width=1, height=20, width=240)
    employee_id_entry.place(relx=0.5, rely=0.3, anchor="center")

    employee_id_error = ctk.CTkLabel(employee_window, text="", font=("Arial", 10), text_color="red")
    employee_id_error.place(relx=0.5, rely=0.35, anchor="center")

    position_title_label = ctk.CTkLabel(employee_window, text="Enter Position Title", font=("Arial", 12))
    position_title_label.place(relx=0.5, rely=0.5, anchor="center")

    position_title_entry = ctk.CTkTextbox(employee_window, fg_color="transparent", border_color="#028fc4", border_width=1, height=20, width=240)
    position_title_entry.place(relx=0.5, rely=0.6, anchor="center")

    position_title_error = ctk.CTkLabel(employee_window, text="", font=("Arial", 10), text_color="red")
    position_title_error.place(relx=0.5, rely=0.65, anchor="center")

    def validate_employee_id(employee_id):
        """ Validate employee_id and return True if valid, False otherwise. """
        try:
            query_vector_id(employee_id, 'employees')[0]
            return True, None
        except IndexError:
            return False, "Invalid Employee ID. Please check and try again."

    def validate_position_title(position_title):
        """ Validate position_title and return True if valid, False otherwise. """
        try:
            query_vector_id(position_title, 'positions')[0]
            return True, None
        except IndexError:
            return False, "Invalid Position Title. Please check and try again."

    def on_employee_submit():
        employee_id = employee_id_entry.get("0.0", "end").strip()
        position_title = position_title_entry.get("0.0", "end").strip()

        employee_id_error.configure(text="")
        position_title_error.configure(text="")

        is_valid_employee, employee_error_message = validate_employee_id(employee_id)
        is_valid_position, position_error_message = validate_position_title(position_title)

        if not is_valid_employee:
            employee_id_error.configure(text=employee_error_message)

        if not is_valid_position:
            position_title_error.configure(text=position_error_message)

        if not is_valid_employee or not is_valid_position:
            return

        try:
            fig = employee_skills_plot(employee_id, position_title)

            # Create a new window (Toplevel) for the graph
            graph_window = ctk.CTkToplevel(app)
            graph_window.title("Employee Skills Plot")
            graph_window.geometry("800x600+700+400")  # Size for displaying the graph

            # Embed the plot in the graph_window
            canvas = FigureCanvasTkAgg(fig, master=graph_window)  # A Tkinter canvas that holds the figure
            canvas.draw()
            canvas.get_tk_widget().pack(padx=10, pady=10, fill='both', expand=True)

            # Destroy the employee_window
            employee_window.destroy()

        except Exception as e:
            # Display a general error message for other exceptions
            employee_id_error.configure(text=f"Error: {str(e)}")

    submit_button = ctk.CTkButton(employee_window, text="Submit", corner_radius=32, hover_color="#0b3459",
                                  fg_color="transparent", border_color="#028fc4", border_width=2, width=140,
                                  command=on_employee_submit)
    submit_button.place(relx=0.5, rely=0.8, anchor="center")
