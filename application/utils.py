import customtkinter
import tkinter as tk

# THIS FILE -  Defines utility classes for different frames using custom tkinter components.
#
# CheckBoxFrame
# RadioButtonFrame
#
# Example usage :
#       self.radio_button_frame = RadioButtonFrame(self, names=["radio1", "radio2"], title="Radio")
#       self.radio_button_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
# -------------------------------------------------------------------------------------------


class CheckBoxFrame(customtkinter.CTkFrame):
    def __init__(self, master, names, title="DefaultCheckBoxFrame"):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title

        self.names = names
        self.checkboxes = []
        self.values = {}

        self.title = customtkinter.CTkLabel(
            self, text=self.title, fg_color="gray10", corner_radius=6
        )
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, name in enumerate(self.names):
            self.values[name] = tk.BooleanVar()
            checkbox = customtkinter.CTkCheckBox(
                self, text=name, variable=self.values[name]
            )
            checkbox.grid(row=i + 1, column=0, padx=10, pady=10, sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked = []
        for k, v in self.values.items():
            checked.append((k, v.get()))
        return checked


class RadioButtonFrame(customtkinter.CTkFrame):
    def __init__(self, master, names, title="DefaultRadioFrame"):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title

        self.names = names
        self.radio_buttons = []
        self.value = customtkinter.StringVar(value="")

        self.title = customtkinter.CTkLabel(
            self, text=self.title, fg_color="gray50", corner_radius=10
        )
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, name in enumerate(self.names):
            radio_button = customtkinter.CTkRadioButton(
                self, text=name, value=name, variable=self.value
            )
            radio_button.grid(row=i + 1, column=0, padx=10, pady=10, sticky="w")
            self.radio_buttons.append(radio_button)

    def get(self):
        return self.value.get()

    def set(self, value):
        self.value.set(value)
