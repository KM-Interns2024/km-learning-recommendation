import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Forms.functions import on_button_click
from plot_employee_development import employee_skills_plot
from CRUD.read import query_vector_id

def show_frame(frame):
    frame.tkraise()

def open_employee_section(app):
    # Main Frame for Employee Section
    main_frame = ctk.CTkFrame(app)
    main_frame.grid(row=0, column=0, sticky="nsew")

    # Frame for Graph Display
    graph_frame = ctk.CTkFrame(app, fg_color="white")
    graph_frame.grid(row=0, column=0, sticky="nsew")

    # Configure the grid layout
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    # Employee Section Widgets
    employee_id_label = ctk.CTkLabel(main_frame, text="Enter Employee ID", font=("Arial", 12))
    employee_id_label.place(relx=0.5, rely=0.2, anchor="center")

    employee_id_entry = ctk.CTkTextbox(main_frame, fg_color="transparent", border_color="#028fc4", border_width=1, height=20, width=240)
    employee_id_entry.place(relx=0.5, rely=0.3, anchor="center")

    employee_id_error = ctk.CTkLabel(main_frame, text="", font=("Arial", 10), text_color="red")
    employee_id_error.place(relx=0.5, rely=0.35, anchor="center")

    position_title_label = ctk.CTkLabel(main_frame, text="Enter Position Title", font=("Arial", 12))
    position_title_label.place(relx=0.5, rely=0.5, anchor="center")

    position_title_entry = ctk.CTkTextbox(main_frame, fg_color="transparent", border_color="#028fc4", border_width=1, height=20, width=240)
    position_title_entry.place(relx=0.5, rely=0.6, anchor="center")

    position_title_error = ctk.CTkLabel(main_frame, text="", font=("Arial", 10), text_color="red")
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

            for widget in graph_frame.winfo_children():
                widget.destroy()

            canvas = FigureCanvasTkAgg(fig, master=graph_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(padx=10, pady=10, fill='both', expand=True)

            main_page_button_graph = ctk.CTkButton(graph_frame, text="Main Page", corner_radius=32, hover_color="#0b3459",
                                                   fg_color="#242424", border_color="#028fc4", border_width=2, width=90,
                                                   command=lambda: on_button_click(app, "main.py"))
            main_page_button_graph.place(relx=0.08, rely=0.95, anchor="center")

            app.geometry("800x500+700+400")

            show_frame(graph_frame)

        except Exception as e:
            employee_id_error.configure(text=f"Error: {str(e)}")

    submit_button = ctk.CTkButton(main_frame, text="Submit", corner_radius=32, hover_color="#0b3459",
                                  fg_color="transparent", border_color="#028fc4", border_width=2, width=140,
                                  command=on_employee_submit)
    submit_button.place(relx=0.5, rely=0.8, anchor="center")

    main_page_button = ctk.CTkButton(main_frame, text="Main Page", corner_radius=32, hover_color="#0b3459",
                                     fg_color="#242424",border_color="#028fc4", border_width=2, width=90,
                                     command=lambda: on_button_click(app, "main.py"))
    main_page_button.place(relx=0.1, rely=0.9, anchor="center")

    def on_closing_employee():
        app.destroy()

    app.protocol("WM_DELETE_WINDOW", on_closing_employee)

    show_frame(main_frame)

if __name__ == "__main__":
    main_app = ctk.CTk()
    main_app.geometry("800x600+700+400")
    open_employee_section(main_app)
    main_app.mainloop()
