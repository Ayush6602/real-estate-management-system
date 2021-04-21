from GUI.db_connection import DBConnection
import tkinter as tk
from PIL.ImageTk import PhotoImage
from PIL import Image
from prettytable import from_db_cursor


class AdminUi(tk.Canvas):
    def __init__(self, master, db_connection: DBConnection, login_ui_cls) -> None:
        super().__init__(master)
        self.master = master
        self.command_var = tk.StringVar(value='SQL Command')
        self.db_connection = db_connection
        self.login_ui_cls = login_ui_cls
        self.admin_bg_img = Image.open('images/admin_bg.jpg')
        self.admin_bg_pimg = PhotoImage(self.admin_bg_img)
        self.title_text = 'ADMIN'
        self.command_text = None
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
        self.admin_bg_pimg = PhotoImage(
            self.admin_bg_img.resize((width, height), Image.ANTIALIAS))
        self.create_image(0, 0, anchor='nw',
                          image=self.admin_bg_pimg)
        # set header text
        head_txt_x = width // 2
        head_txt_y = height // 5
        head_txt_font = f'ariel {min(width, height) // 20} bold'
        self.create_text(head_txt_x, head_txt_y,
                         text=self.title_text, font=head_txt_font, fill='yellow')
        # set command line text box
        cmd_ent_font = f'ariel {min(width, height) // 40}'
        cmd_ent_x = width / 2
        cmd_ent_y = 2 * height / 5
        self.command_text = tk.Text(
            self, height=height//100, width=width//20, font=cmd_ent_font)
        self.create_window(int(cmd_ent_x), int(
            cmd_ent_y), window=self.command_text)
        self.command_text.bind('<Control-Return>', self.submit)
        btn_font = f'ariel {min(width, height) // 50}'
        # set submit button
        sbmt_btn_x = width / 2
        sbmt_btn_y = 3 * height / 5
        submit_btn = tk.Button(self, text='Submit', background='green',
                               font=btn_font, command=self.submit, activebackground='yellow')
        self.create_window(int(sbmt_btn_x), int(sbmt_btn_y), window=submit_btn)
        # set rental report button
        rent_btn_x = width / 4
        rent_btn_y = 4 * height / 5
        rental_btn = tk.Button(self, text='Rental Report', background='yellow',
                               font=btn_font, command=self.rental_report, activebackground='orange')
        self.create_window(int(rent_btn_x), int(rent_btn_y), window=rental_btn)
        # set sales report button
        sale_btn_x = 2 * width / 4
        sale_btn_y = 4 * height / 5
        sales_btn = tk.Button(self, text='Sales Report', background='yellow',
                              font=btn_font, command=self.sales_report, activebackground='orange')
        self.create_window(int(sale_btn_x), int(sale_btn_y), window=sales_btn)
        # set logout button
        logout_btn_x = 3 * width / 4
        logout_btn_y = 4 * height / 5
        logout_btn = tk.Button(self, text='Logout', background='red',
                               font=btn_font, command=self.logout, activebackground='orange')
        self.create_window(int(logout_btn_x), int(
            logout_btn_y), window=logout_btn)

    def logout(self) -> None:
        self.destroy()
        self.login_ui_cls(self.master, self.db_connection)

    def sales_report(self):
        self.result = from_db_cursor(self.db_connection.get_sales_report())
        self.print_result()

    def rental_report(self):
        self.result = from_db_cursor(self.db_connection.get_rental_report())
        self.print_result()

    def submit(self, event: tk.Event = None) -> None:
        query = self.command_text.get('1.0', 'end')
        self.result = from_db_cursor(self.db_connection.command_result(query))
        self.print_result()
        self.db_connection.connection.commit()

    def print_result(self):
        result_ui = tk.Toplevel()
        result_ui.title('Result')
        result_ui.geometry('1280x720')
        res_font = f'courier'
        tk.Label(result_ui, text=self.result, font=res_font,
                 fg='green', background='black').pack(fill='both', expand=1)
        result_ui.mainloop()
