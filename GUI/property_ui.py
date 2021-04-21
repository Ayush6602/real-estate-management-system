import tkinter as tk
from GUI.db_connection import DBConnection
from PIL.ImageTk import PhotoImage
from PIL import Image
from urllib.request import Request, urlopen
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class PropertyUi(tk.Canvas):
    def __init__(self, master: tk.Tk, db_connection: DBConnection, username: str, property_id: int) -> None:
        super().__init__(master)
        self.master = master
        self.username = username
        self.property_id = property_id
        self.property_details = db_connection.get_property_details(
            self.property_id)
        self.property_bg_img = Image.open('images/property_bg.jpg')
        self.property_bg_pimg = PhotoImage(self.property_bg_img)
        self.property_img = Image.open(
            urlopen(Request(self.property_details['Image Link'], headers={'User-Agent': 'Mozilla/5.0'})))
        self.property_details.pop('Image Link')
        self.property_details.pop('locality_id')
        self.property_details.pop('id')
        self.property_pimg = PhotoImage(self.property_img)
        self.pack(expand=True, fill='both')
        self.bind('<Configure>', self.render)

    def render(self, event: tk.Event = None) -> None:
        if not self.winfo_exists():
            return
        height = self.winfo_height()
        width = self.winfo_width()
        # clear canvas
        self.delete('all')
        # set background image
        self.property_bg_pimg = PhotoImage(
            self.property_bg_img.resize((width, height), Image.ANTIALIAS))
        self.create_image(0, 0, anchor='nw',
                          image=self.property_bg_pimg)
        # set property image
        prop_img_w = width / 2
        prop_img_h = height / 2
        prop_img_x = width / 16
        prop_img_y = height / 3
        self.property_pimg = PhotoImage(self.property_img.resize(
            (int(prop_img_w), int(prop_img_h)), Image.ANTIALIAS))
        self.create_image(int(prop_img_x), int(prop_img_y), anchor='w',
                          image=self.property_pimg)
        # set property details
        i = 3
        for key, value in self.property_details.items():
            txt_x = width * 12 / 16
            txt_y = height * i / 16
            txt_fnt = f'arial {min(width, height) // 40} bold'
            self.create_text(txt_x, txt_y, text=key + ': ',
                             anchor='se', font=txt_fnt)
            txt_fnt = f'arial {min(width, height) // 40}'
            self.create_text(txt_x, txt_y, text=value,
                             anchor='sw', font=txt_fnt)
            i += 1
        # set buy button
        buy_btn_x = 2 * width / 16
        buy_btn_y = 2 * height / 3
        buy_btn_font = f'arial {min(width, height) // 40}'
        buy_btn = tk.Button(self, background='green',
                            text='Buy', borderwidth=0, activebackground='yellow', font=buy_btn_font)
        self.create_window(buy_btn_x, buy_btn_y, window=buy_btn, anchor='nw')
        # set rent button
        rnt_btn_x = 7 * width / 16
        rnt_btn_y = 2 * height / 3
        rnt_btn_font = f'arial {min(width, height) // 40}'
        rnt_btn = tk.Button(self, background='yellow',
                            text='Rent', borderwidth=0, activebackground='green', font=rnt_btn_font)
        self.create_window(rnt_btn_x, rnt_btn_y, window=rnt_btn, anchor='nw')
