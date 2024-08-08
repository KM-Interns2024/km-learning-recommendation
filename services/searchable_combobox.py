# searchable_combobox.py
import customtkinter as ctk
from tkinter import ttk

class SearchableCombobox(ctk.CTkComboBox):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._completion_list = []
        self._hits = []
        self._hit_index = 0
        self.position = 0
        self.bind('<KeyRelease>', self.handle_keyrelease)

    def set_completion_list(self, completion_list):
        self._completion_list = sorted(completion_list)
        self.configure(values=self._completion_list)

    def autocomplete(self, delta=0):
        current_text = self.get()

        if current_text == '':
            self._hits = []
            self.configure(values=self._completion_list)
            return

        _hits = [item for item in self._completion_list if item.lower().startswith(current_text.lower())]

        if _hits != self._hits:
            self._hit_index = 0
            self._hits = _hits

        if _hits:
            self._hit_index = (self._hit_index + delta) % len(_hits)
            self.configure(values=_hits)  # Update the dropdown values with filtered hits
            self.event_generate('<Down>') 

    def handle_keyrelease(self, event):
        if event.keysym in ('BackSpace', 'Left', 'Right', 'Up', 'Down'):
            pass  # Handle cursor movement and deletion separately if needed
        if event.keysym in ('Up', 'Down'):
            self.autocomplete(1 if event.keysym == 'Down' else -1)
        if len(event.keysym) == 1:  # If it's a single character (alphanumeric)
            self.autocomplete()

