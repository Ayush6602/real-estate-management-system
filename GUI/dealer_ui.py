import tkinter as tk
from tkinter import ttk
from GUI.db_connection import DBConnection
from PIL.ImageTk import PhotoImage
from PIL import Image

class DealerUi(tk.Canvas):
    def __init__(self, master: tk.Tk, db_connection: DBConnection, property_id:int) -> None:
        super().__init__(master)
        self.master = master
        self.db_connection = db_connection
        self.property_id = property_id
        self.dealer_bg_img = Image.open('images/property_bg.jpg')
        self.dealer_bg_pimg = PhotoImage(self.dealer_bg_img)
        self.title_text = 'Dealers'
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
        self.dealer_bg_pimg = PhotoImage(self.dealer_bg_img.resize((width, height), Image.ANTIALIAS))
        self.create_image(0, 0, anchor='nw',image=self.dealer_bg_pimg)

        # set header text
        head_txt_x = width // 2
        head_txt_y = height // 5
        head_txt_font = f'ariel {min(width, height) // 20} bold'
        self.create_text(head_txt_x, head_txt_y,text=self.title_text, font=head_txt_font, fill='green')

        dealers = self.db_connection.get_dealers(self.property_id)

        dealer_tree = ttk.Treeview(self, selectmode="none")
        self.create_window(width//2, 2*height//5, window=dealer_tree)
        dealer_tree['columns'] = ('Name', 'Contact Number', 'Email Id')

        dealer_tree.heading("#0", text="")
        dealer_tree.heading("Name", text="Name")
        dealer_tree.heading("Contact Number", text="Contact Number")
        dealer_tree.heading("Email Id", text="Email Id")

        dealer_tree.column("#0", width=0, stretch="NO")
        dealer_tree.column('Name')
        dealer_tree.column('Contact Number')
        dealer_tree.column('Email Id')

        if dealers is not None:
            for i in range(len(dealers)):
                dealer_tree.insert(parent='', index='end', iid=i, values=dealers[i])