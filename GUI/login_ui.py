from GUI.db_connection import DBConnection
import tkinter as tk


class LoginUi(tk.Frame):
    def __init__(self, master, db_connection: DBConnection) -> None:
        super().__init__(master)
        self.master = master
        self.username = tk.StringVar(value='Username')
        self.password = tk.StringVar(value='Password')
        self.db_connection = db_connection
        tk.Entry(self, textvariable=self.username).pack()
        tk.Entry(self, textvariable=self.password, show='*').pack()
        tk.Button(self, text='Login', command=self.login).pack()
        self.status_label = tk.Label(self, text='Enter Username and Password')
        self.status_label.pack()

    def login(self) -> None:
        user_type = self.db_connection.get_user_type(
            self.username.get(), self.password.get())
        if user_type == DBConnection.ADMIN:
            self.status_label.configure(
                text='Welcome Admin', foreground='green')
        elif user_type == DBConnection.DEALER:
            self.status_label.configure(
                text='Welcome Dealer', foreground='green')
        elif user_type == DBConnection.CLIENT:
            self.status_label.configure(
                text='Welcome Client', foreground='green')
        else:
            self.status_label.configure(
                text='Username Or Password Is Incorrect', foreground='red')
