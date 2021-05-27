from GUI.db_connection import DBConnection
from GUI.search_ui import SearchUi
import tkinter as tk
from PIL.ImageTk import PhotoImage
from PIL import Image

class SignupUi(tk.Canvas):
    def __init__(self, master: tk.Tk, db_connection: DBConnection, login_ui_cls) -> None:
        super().__init__(master)
        self.master = master
        self.configure(highlightthickness=0)
        self.db_connection = db_connection
        self.login_ui_cls = login_ui_cls
        self.login_bg_img = Image.open('images/login_bg.jpg')
        self.login_bg_pimg = PhotoImage(self.login_bg_img)
        self.username_var = tk.StringVar(self, 'Username')
        self.password_var = tk.StringVar(self, 'Password')
        self.name_var = tk.StringVar(self, "Name")
        self.contact_var = tk.StringVar(self, "Contact No.")
        self.mail_var = tk.StringVar(self, "Email")
        self.title_text = 'Create Account'
        self.pack(expand=True, fill='both')
        self.bind('<Configure>', self.render)

    def render(self, event: tk.Event = None) -> None:
        if not self.winfo_exists():
            return
        height = self.winfo_height()
        width = self.winfo_width()
        # clear canvas
        self.delete('all')

        # set background
        self.login_bg_pimg = PhotoImage(self.login_bg_img.resize((width, height), Image.ANTIALIAS))
        self.create_image(0, 0, anchor='nw',image=self.login_bg_pimg)

        # set header text
        head_txt_x = width // 2
        head_txt_y = height // 5
        head_txt_font = f'ariel {min(width, height) // 20} bold'
        self.create_text(head_txt_x, head_txt_y,text=self.title_text, font=head_txt_font, fill='yellow')

        # set username entry
        usrnm_ent_font = f'ariel {min(width, height) // 40}'
        usrnm_ent_x = width / 2
        usrnm_ent_y = 1.5 * height / 5
        username_entry = tk.Entry(self, textvariable=self.username_var, font=usrnm_ent_font)
        username_entry.bind('<ButtonRelease-1>', self.clear_username_entry)
        username_entry.bind('<Return>', self.signup)
        self.create_window(int(usrnm_ent_x), int(usrnm_ent_y), window=username_entry, width = width//4)

        # set password entry
        pwd_ent_font = f'ariel {min(width, height) // 40}'
        pwd_ent_x = width / 2
        pwd_ent_y = 2 * height / 5
        password_entry = tk.Entry(self, textvariable=self.password_var, font=pwd_ent_font)


        if self.password_var.get() != 'Password':
            password_entry.configure(show='*')
        password_entry.bind('<ButtonRelease-1>', self.clear_password_entry)
        password_entry.bind('<Return>', self.signup)
        self.create_window(int(pwd_ent_x), int(pwd_ent_y), window=password_entry,  width = width//4)

        #get user name
        user_name = tk.Entry(self, textvariable=self.name_var, font = pwd_ent_font)
        user_name.bind('<ButtonRelease-1>', self.clear_user_name)
        self.create_window(int(pwd_ent_x), int(2.5*height/5), window=user_name, width = width//4)

        #get contact no.
        contact = tk.Entry(self, textvariable=self.contact_var, font = pwd_ent_font)
        contact.bind('<ButtonRelease-1>', self.clear_contact)
        self.create_window(int(pwd_ent_x), int(3*height/5), window=contact, width = width//4)

        #get email
        mail = tk.Entry(self, textvariable=self.mail_var, font = pwd_ent_font)
        mail.bind('<ButtonRelease-1>', self.clear_mail)
        self.create_window(int(pwd_ent_x), int(3.5*height/5), window=mail, width = width//4)

        lgn_btn_font = f'ariel {min(width, height) // 50}'
        signup_btn = tk.Button(self, text='Sign Up', borderwidth=0, background='green', font=lgn_btn_font, command=self.signup, activebackground='yellow')
        self.create_window(width // 2, int(4*height/5),  window=signup_btn)

    def clear_username_entry(self, event: tk.Event) -> None:
        if self.username_var.get() == 'Username':
            self.username_var.set('')
            self.render()

    def clear_password_entry(self, event: tk.Event) -> None:
        if self.password_var.get() == 'Password':
            self.password_var.set('')
            self.render()
    
    def clear_user_name(self, event: tk.Event) -> None:
        if self.name_var.get() == 'Name':
            self.name_var.set('')
            self.render()

    def clear_contact(self, event: tk.Event) -> None:
        if self.contact_var.get() == 'Contact No.':
            self.contact_var.set('')
            self.render()
    
    def clear_mail(self, event: tk.Event) -> None:
        if self.mail_var.get() == 'Email':
            self.mail_var.set('')
            self.render()

    def signup(self, event: tk.Event = None) -> None:
        sucess_bool = self.db_connection.add_client(self.username_var.get(), self.password_var.get(), self.name_var.get(), self.contact_var.get(), self.mail_var.get())
        if sucess_bool:
            self.destroy()
            SearchUi(self.master, self.db_connection, self.login_ui_cls)
        else:
            self.render()
