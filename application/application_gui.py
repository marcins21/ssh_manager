import customtkinter
import tkinter as tk


class CheckBoxFrame(customtkinter.CTkFrame):
    def __init__(self, master, names, title="DefaultName"):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title

        self.names = names
        self.checkboxes = []
        self.values = {}

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10,0), sticky="ew")

        for i, name in enumerate(self.names):
            self.values[name] = tk.BooleanVar()
            checkbox = customtkinter.CTkCheckBox(self, text=name, variable=self.values[name])
            checkbox.grid(row=i+1, column=0, padx=10, pady=10, sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked = []
        for k,v in self.values.items():
            checked.append((k, v.get()))
        return checked

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title = "SSH MANAGER"
        self.geometry("780x540")
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        #LEFT MENU
        self.checkbox_frame_left = CheckBoxFrame(self, names=["check1", "check2", "check3"], title="Left menu")
        self.checkbox_frame_left.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nswe")

        #RIGHT MENU
        self.checkbox_frame_right = CheckBoxFrame(self, names=["check5","check6","check7"] )  #title="Right menu")
        self.checkbox_frame_right.grid(row=0, column=1, padx=(10,0), pady=(10,0), sticky="nsew")

        self.send_button = customtkinter.CTkButton(
            self, text="Send Data", command=self.button_callback
        )
        self.send_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew",columnspan=2)

    def button_callback(self):
        print("\nState of the checkboxes")
        print(f"left menu - {self.checkbox_frame_left.get()}")
        print(f"right menu - {self.checkbox_frame_right.get()}")

app = App()
app.mainloop()
