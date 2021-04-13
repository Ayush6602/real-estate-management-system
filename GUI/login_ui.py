from GUI.agent_ui import AgentUi
from GUI.db_connection import DBConnection
from GUI.admin_ui import AdminUi
import tkinter as tk
from PIL.ImageTk import PhotoImage
from PIL import Image


class LoginUi(tk.Canvas):
    def __init__(self, master: tk.Tk, db_connection: DBConnection) -> None:
        super().__init__(master)
        self.master = master
        self.configure(highlightthickness=0)
        self.db_connection = db_connection
        self.login_bg_img = Image.open('images/login_bg.jpg')
        self.login_bg_pimg = PhotoImage(self.login_bg_img)
        self.username_var = tk.StringVar(self, 'Username')
        self.password_var = tk.StringVar(self, 'Password')
        self.title_text = 'Welcome'
        self.pack(expand=True, fill='both')
        self.bind('<Configure>', self.render)

    def render(self, event: tk.Event = None) -> None:
        if not self.winfo_exists():
            return
        if event is None:
            height = self.winfo_height()
            width = self.winfo_width()
        else:
            height = event.height
            width = event.width
        # clear canvas
        self.delete('all')
        # set background
        self.login_bg_pimg = PhotoImage(self.login_bg_img.resize(
            (width, height), Image.ANTIALIAS))
        self.create_image(0, 0, anchor='nw',
                          image=self.login_bg_pimg)
        # set header text
        self.create_text(width // 2, height // 5, text=self.title_text,
                         font=f'ariel {min(width, height) // 20} bold', fill='yellow')
        # set username entry
        username_entry = tk.Entry(self, textvariable=self.username_var,
                                  font=f'ariel {min(width, height) // 40}')
        username_entry.bind('<ButtonRelease-1>', self.clear_username_entry)
        username_entry.bind('<Return>', self.login)
        self.create_window(width // 2, 2 * height //
                           5, window=username_entry)
        # set password entry
        password_entry = tk.Entry(self, textvariable=self.password_var,
                                  font=f'ariel {min(width, height) // 40}')
        if self.password_var.get() != 'Password':
            password_entry.configure(show='*')
        password_entry.bind('<ButtonRelease-1>', self.clear_password_entry)
        password_entry.bind('<Return>', self.login)
        self.create_window(width // 2, 2.5 * height //
                           5, window=password_entry)
        # set login button
        login_btn = tk.Button(self, text='Login',
                              borderwidth=0, background='green', font=f'ariel {min(width, height) // 50}', command=self.login, activebackground='yellow')
        self.create_window(width // 2, 3 * height //
                           5, window=login_btn)

    def clear_username_entry(self, event: tk.Event) -> None:
        if self.username_var.get() == 'Username':
            self.username_var.set('')
            self.render()

    def clear_password_entry(self, event: tk.Event) -> None:
        if self.password_var.get() == 'Password':
            self.password_var.set('')
            self.render()

    def login(self, event: tk.Event = None) -> None:
        user_type = self.db_connection.get_user_type(
            self.username_var.get(), self.password_var.get())
        if user_type == DBConnection.ADMIN:
            self.destroy()
            AdminUi(self.master, self.db_connection).pack(expand=True)
        elif user_type == DBConnection.DEALER:
            self.destroy()
            AgentUi(self.master, self.db_connection,
                    self.username_var.get()).pack(fill=tk.X)
        elif user_type == DBConnection.CLIENT:
            self.title_text = 'Welcome Client'
        else:
            self.title_text = 'Unknown User'
        self.render()
