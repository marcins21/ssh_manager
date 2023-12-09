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


class LoginForm(customtkinter.CTkFrame):
    #Hardcoded credentials
    CREDENTIALS = {"admin":["admin","admin"], "technician":["tech","tech"],"testuser":["test","test"]}

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.logged = False
        self.FontSettings = ("Helvetica", 25, "bold")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        self.user_data = {
            "login": tk.StringVar(self,value=""),
            "password": tk.StringVar(self,value="")
        }


        self.login_label = customtkinter.CTkLabel(self, text="Login")
        self.login_label.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nswe")

        self.password_label = customtkinter.CTkLabel(self, text="Password")
        self.password_label.grid(row=1, column=0, padx=10, pady=(10,0), sticky="nswe")


        self.login_input = tk.Entry(
            self, font=self.FontSettings ,textvariable=self.user_data["login"]
        ).grid(row=0, column=1, padx=(10, 0), pady=(10, 0), sticky="enws")

        self.password_input = tk.Entry(
            self, font=self.FontSettings, textvariable=self.user_data["password"]
        ).grid(row=1, column=1, padx=(10, 0), pady=(10, 0), sticky="enws")


        self.login_button = customtkinter.CTkButton(self,text="Submit", font=self.FontSettings,  command=self.submit_data)
        self.login_button.grid(row=2, column=0, columnspan=2,rowspan=3, padx=(10,0), pady=(10,0), sticky="nswe")


    def submit_data(self):
        submited_login = self.user_data["login"].get()
        submited_password = self.user_data["password"].get()
        for value in self.CREDENTIALS.values():
            if value[0] == submited_login:
                if submited_password == value[1]:
                    self.logged = True
                    login_label = customtkinter.CTkLabel(self.master, text="Login Sucessfull", text_color="lightGreen")
                    login_label.grid(row=0, column=0, sticky="new")



    def check_if_logged(self):
        print(self.logged)
