import tkinter as tk
from PIL.ImageTk import PhotoImage
from PIL import Image
from GUI.db_connection import DBConnection

class AddModifyProperty(tk.Canvas):
    def __init__(self, master, db_connection:DBConnection, id:int) -> None:
        super().__init__(master)
        self.master = master
        self.id = id
        self.agent_bg_img = Image.open('images/agent_bg.jpeg')
        self.agent_bg_pimg = PhotoImage(self.agent_bg_img)
        self.db_connection = db_connection
        self.property_id = tk.StringVar()
        self.description_type = tk.StringVar()
        self.description_status = tk.StringVar()
        self.description_bedroom = tk.StringVar()
        self.description_bathroom = tk.StringVar()
        self.description_kitchen = tk.StringVar()
        self.description_hall = tk.StringVar()
        self.property_image = tk.StringVar()
        self.property_address = tk.StringVar()
        self.property_size = tk.StringVar()
        self.property_price = tk.StringVar()
        self.property_rent = tk.StringVar()
        self.property_lid = tk.StringVar()

        self.pack(fill=tk.BOTH, expand=True)
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
        self.delete('all')
         # set background
        # self.agent_bg_pimg = PhotoImage(self.agent_bg_img.resize((width, height), Image.ANTIALIAS))
        # self.create_image(0, 0, anchor='nw', image=self.agent_bg_pimg)

        self.create_text(10, 10, text="Enter property id:", font=('calibri', 10), anchor = "nw")
        property_id = tk.Entry(self)
        self.create_window(200, 10, anchor="nw", window = property_id)

        self.create_text(10, 30, text="Enter property type:", anchor = "nw")
        type = tk.Entry(self, textvariable=self.description_type)
        self.create_window(200, 30, anchor="nw", window = type)

        self.create_text(10, 50, text="Enter property status:", anchor = "nw")
        status = tk.Entry(self, textvariable=self.description_status)
        self.create_window(200, 50, anchor="nw", window = status)

        self.create_text(10, 70, text="Enter bedrooms:", anchor = "nw")
        bedroom = tk.Entry(self, textvariable=self.description_bedroom)
        self.create_window(200, 70, anchor="nw", window = bedroom)

        self.create_text(10, 90, text="Enter bathrooms:", anchor = "nw")
        bathroom = tk.Entry(self, textvariable=self.description_bathroom)
        self.create_window(200, 90, anchor="nw", window = bathroom)

        self.create_text(10, 110, text="Enter kitchens:", anchor = "nw")
        kitchen = tk.Entry(self, textvariable=self.description_kitchen)
        self.create_window(200, 110, anchor="nw", window = kitchen)

        self.create_text(10, 130, text="Enter halls:", anchor = "nw")
        hall = tk.Entry(self, textvariable=self.description_hall)
        self.create_window(200, 130, anchor="nw", window = hall)

        self.create_text(width//2, 10, text="Enter image link:", anchor = "nw")
        image = tk.Entry(self, textvariable=self.property_image)
        self.create_window(width//2 + 200, 10, anchor="nw", window = image)

        self.create_text(width//2, 30, text="Enter address:", anchor = "nw")
        address = tk.Entry(self, textvariable=self.property_address)
        self.create_window(width//2 + 200, 30, anchor="nw", window = address)

        self.create_text(width//2, 50, text="Enter size:", anchor = "nw")
        size = tk.Entry(self, textvariable=self.property_size)
        self.create_window(width//2 + 200, 50, anchor="nw", window = size)

        self.create_text(width//2, 70, text="Enter price:", anchor = "nw")
        price = tk.Entry(self, textvariable=self.property_price)
        self.create_window(width//2 + 200, 70, anchor="nw", window = price)

        self.create_text(width//2, 90, text="Enter rent price:", anchor = "nw")
        rent = tk.Entry(self, textvariable=self.property_rent)
        self.create_window(width//2 + 200, 90, anchor="nw", window = rent)

        self.create_text(width//2, 110, text="Enter locality id:", anchor = "nw")
        lid = tk.Entry(self, textvariable=self.property_lid)
        self.create_window(width//2 + 200, 110, anchor="nw", window = lid)

        if self.id is None:
            btn_text = 'Add Property'
            btn_cmd = self.add_property
        else:
            btn_text = 'Modify Property'
            btn_cmd = self.modify_property

        add = tk.Button(self, text=btn_text, command = btn_cmd, font=("calibri", 20), activebackground="blue")
        self.create_window(width//2, 500, anchor="center", window=add)

    def add_property(self)->None:
        id = self.property_id.get()
        print(id)