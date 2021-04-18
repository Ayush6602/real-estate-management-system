from GUI.db_connection import DBConnection
import tkinter as tk
from PIL.ImageTk import PhotoImage
from PIL import Image



class AdminUi(tk.Canvas):
    def __init__(self, master, db_connection: DBConnection) -> None:
        super().__init__(master)
        self.master = master
        self.command_var = tk.StringVar(value='SQL Command')
        self.db_connection = db_connection
        self.admin_bg_img = Image.open('C:\\Users\\Almas\\Documents\\Visual Studio 2019\\Code\\real-estate-management-system\\images\\admin_bg.jpg')
        self.admin_bg_pimg = PhotoImage(self.admin_bg_img)
        self.title_text = 'ADMIN'
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
        # set command line entry
        cmd_ent_font = f'ariel {min(width, height) // 40}'
        cmd_ent_x = width / 2
        cmd_ent_y = 2 * height / 5
        command_entry = tk.Entry(
            self, textvariable=self.command_var, font=cmd_ent_font)
        command_entry.bind('<ButtonRelease-1>', self.clear_command_line_entry)
        command_entry.bind('<Return>', self.submit)
        self.create_window(int(cmd_ent_x), int(
            cmd_ent_y), window=command_entry)
        # set submit button
        sbmt_btn_font = f'ariel {min(width, height) // 50}'
        sbmt_btn_x = width / 2
        sbmt_btn_y = 3 * height / 5
        submit_btn = tk.Button(self, text='Submit', borderwidth=0, background='green',
                              font=sbmt_btn_font, command=self.submit, activebackground='yellow')
        self.create_window(int(sbmt_btn_x), int(sbmt_btn_y), window=submit_btn)
        # set rental report button
        rent_btn_font = f'ariel {min(width, height) // 50}'
        rent_btn_x= width / 3
        rent_btn_y= 4 * height / 5
        rental_btn = tk.Button(self, text = 'Rental Report', borderwidth=0, background= 'red',
                                font=rent_btn_font, command=self.rental_report, activebackground='orange')
        self.create_window(int(rent_btn_x), int(rent_btn_y), window=rental_btn)
        # set sales report button
        sale_btn_font = f'ariel {min(width, height) // 50}'
        sale_btn_x= 2 * width / 3
        sale_btn_y= 4 * height / 5
        sales_btn = tk.Button(self, text = 'Sales Report', borderwidth=0, background= 'red',
                                font=sale_btn_font, command=self.sales_report, activebackground='orange')
        self.create_window(int(sale_btn_x), int(sale_btn_y), window=sales_btn)

    def clear_command_line_entry(self, event: tk.Event) -> None:
        if self.command_var.get() == 'SQL Command':
            self.command_var.set('')
            self.render()

    def sales_report(self) :
        self.result = self.db_connection.get_sales_report()
        self.print_result()

    def rental_report(self) :
        self.result = self.db_connection.get_rental_report()
        self.print_result()

    def submit(self, event: tk.Event = None) -> None:
        query = self.command_var.get()
        self.result = self.db_connection.command_result (query)
        self.print_result()

    def print_result(self) :
        ResultUi = tk.Tk()
        ResultUi.title('Result')
        ResultUi.geometry('1280x720')
        res_font = f'courier'
        tk.Label(ResultUi,text = self.result, font = res_font, fg='green', background='black').pack(fill='both', expand=1)
        ResultUi.mainloop()
        
        