import customtkinter
import tkinter as tk
from application.utils.database_handler import get_handle


class ServerDataInputForm(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.database = get_handle()

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.FontSettings = ("Helvetica", 25, "bold")

        self.data = {
            "server_name": tk.StringVar(self),
            "server_ip": tk.StringVar(self),
            "password": tk.StringVar(self),
            "username": tk.StringVar(self),
        }

        self.server_name = customtkinter.CTkLabel(
            self, text="Server Name", fg_color="gray30"
        )
        self.server_name.grid(
            row=0, column=0, padx=(10, 0), pady=(10, 0), sticky="nsew"
        )

        self.username = customtkinter.CTkLabel(self, text="Username", fg_color="gray30")
        self.username.grid(row=1, column=0, padx=(10, 0), pady=(10, 0), sticky="nwes")

        self.password = customtkinter.CTkLabel(self, text="Password", fg_color="gray30")
        self.password.grid(row=2, column=0, padx=(10, 0), pady=(10, 0), sticky="nwes")

        self.ip = customtkinter.CTkLabel(self, text="Ip", fg_color="gray30")
        self.ip.grid(row=3, column=0, padx=(10, 0), pady=(10, 0), sticky="nwes")

        self.user_input_server_name = tk.Entry(
            self, font=self.FontSettings, textvariable=self.data["server_name"]
        ).grid(row=0, column=1, padx=(10, 0), pady=(10, 0), sticky="enws")

        self.user_input_username = tk.Entry(
            self, font=self.FontSettings, textvariable=self.data["username"]
        ).grid(row=1, column=1, padx=(10, 0), pady=(10, 0), sticky="enws")

        self.user_input_password = tk.Entry(
            self, font=self.FontSettings, textvariable=self.data["password"]
        ).grid(row=2, column=1, padx=(10, 0), pady=(10, 0), sticky="enws")

        self.user_input_ip = tk.Entry(
            self, font=self.FontSettings, textvariable=self.data["server_ip"]
        ).grid(row=3, column=1, padx=(10, 0), pady=(10, 0), sticky="enws")

        # Submit Button
        submit_button = customtkinter.CTkButton(
            self, text="Submit", command=self.submit_data
        )
        submit_button.grid(
            row=4, column=0, pady=(10, 0), padx=(10, 0), sticky="sew", columnspan=2
        )

    def logs(self):
        print(f"LOG - CURRENT STATE OF DATABSE - {self.database}")
        print()
        for k, v in self.data.items():
            print(f"LOG - COLLECTED DATA - '{k}' --> {v.get()}")
        print("---------------------------------------------------")

    def submit_data(self):
        # Debug INFO
        # self.logs()
        data_to_write = {}
        for k, v in self.data.items():
            if v == "":
                data_to_write[k] = None
            else:
                data_to_write[k] = v.get()

        self.database.write_data(data_to_write)
