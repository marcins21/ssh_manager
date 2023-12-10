import customtkinter

from application.utils.frames import CheckBoxFrame, RadioButtonFrame
from application.utils.forms import ServerDataInputForm, LoginForm


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title = "SSH MANAGER"
        self.geometry("780x540")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # LEFT MENU
        self.checkbox_frame_left = CheckBoxFrame(
            self, names=["check1", "check2", "check3"], title="Left menu"
        )
        self.checkbox_frame_left.grid(
            row=0, column=0, padx=10, pady=(10, 0), sticky="nswe"
        )

        # RIGHT MENU
        self.checkbox_frame_right = CheckBoxFrame(
            self, names=["check5", "check6", "check7"], title="Right menu"
        )
        self.checkbox_frame_right.grid(
            row=0, column=1, padx=(10, 0), pady=(10, 0), sticky="nsew"
        )

        # ADDITIONAL RADIO MENU
        self.radio_button_frame = RadioButtonFrame(
            self, names=["radio1", "radio2"], title="Radio"
        )
        self.radio_button_frame.grid(
            row=1, column=0, padx=10, pady=10, sticky="ew", columnspan=2
        )

        # SENDING DATA - BUTTON
        self.send_button = customtkinter.CTkButton(
            self, text="Send Data", command=self.send_data_button
        )
        self.send_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.form_button = customtkinter.CTkButton(
            self, text="Form", command=self.go_to_form_button
        )
        self.form_button.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    # testing purposes
    def send_data_button(self):
        print("\nState of the checkboxes")
        print(f"left menu - {self.checkbox_frame_left.get()}")
        print(f"right menu - {self.checkbox_frame_right.get()}")
        print(f"RADIO - {self.radio_button_frame.get()}")

    def go_to_form_button(self):
        add_server_from = AddServerForm()
        add_server_from.mainloop()


class AddServerForm(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title = "Adding New Server"
        self.geometry("780x540")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        server_info_form = ServerDataInputForm(self)
        server_info_form.grid(row=0, column=0, padx=10, pady=10, sticky="ewns")


class LoginIntoApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("540x400")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.wrong_login_credentials = "Wrong Login Or Passowrd"

        self.login_form = LoginForm(self)
        self.login_form.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")

        self.login_label = customtkinter.CTkLabel(
            self, text=self.wrong_login_credentials, text_color="red"
        )
        self.login_label.grid(row=0, column=0, sticky="new")

        self.confirm_button = customtkinter.CTkButton(
            self,
            text="Go to App",
            command=self.check_login,
            corner_radius=6,
            fg_color="gray30",
        )
        self.confirm_button.grid(
            row=0, column=0, padx=(10, 0), pady=(20, 0), sticky="sew"
        )

    def check_login(self):
        if self.login_form.logged:
            app = App()
            app.mainloop()


login = LoginIntoApp()
login.mainloop()
