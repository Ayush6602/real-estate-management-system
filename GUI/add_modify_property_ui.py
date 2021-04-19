import tkinter as tk
from tkinter import ttk
from PIL.ImageTk import PhotoImage
from PIL import Image
from GUI.db_connection import DBConnection

class AddModifyProperty(tk.Canvas):
    def __init__(self, master, db_connection:DBConnection, id:int, dealer:str) -> None:
        super().__init__(master)
        self.master = master
        self.dealer = dealer
        self.id = id
        self.agent_bg_img = Image.open('images/agent_bg.jpg')
        self.agent_bg_pimg = PhotoImage(self.agent_bg_img)
        self.db_connection = db_connection
        self.property_id_var = tk.StringVar(self)
        self.description_type = tk.StringVar(self)
        self.description_status = tk.StringVar(self)
        self.description_bedroom = tk.StringVar(self)
        self.description_bathroom = tk.StringVar(self)
        self.description_kitchen = tk.StringVar(self)
        self.description_hall = tk.StringVar(self)
        self.property_image = tk.StringVar(self)
        self.property_address = tk.StringVar(self)
        self.property_size = tk.StringVar(self)
        self.property_price = tk.StringVar(self)
        self.property_rent = tk.StringVar(self)
        self.property_locality = tk.StringVar(self)

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
        self.agent_bg_pimg = PhotoImage(self.agent_bg_img.resize((width, height), Image.ANTIALIAS))
        self.create_image(0, 0, anchor='nw', image=self.agent_bg_pimg)

        self.create_text(10, 10, text="Enter property id:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        property_id = tk.Entry(self, textvariable = self.property_id_var)
        # property_id.bind('<Return>', self.add_property)
        self.create_window(320, 10, anchor="nw", window = property_id)

        self.create_text(10, 50, text="Enter property type:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        type = tk.Entry(self, textvariable=self.description_type)
        self.create_window(320, 50, anchor="nw", window = type)

        self.create_text(10, 90, text="Enter property status:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        status = tk.Entry(self, textvariable=self.description_status)
        self.create_window(320, 90, anchor="nw", window = status)

        self.create_text(10, 130, text="Enter bedrooms:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        bedroom = tk.Entry(self, textvariable=self.description_bedroom)
        self.create_window(320, 130, anchor="nw", window = bedroom)

        self.create_text(10, 170, text="Enter bathrooms:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        bathroom = tk.Entry(self, textvariable=self.description_bathroom)
        self.create_window(320, 170, anchor="nw", window = bathroom)

        self.create_text(10, 210, text="Enter kitchens:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        kitchen = tk.Entry(self, textvariable=self.description_kitchen)
        self.create_window(320, 210, anchor="nw", window = kitchen)

        self.create_text(10, 250, text="Enter halls:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        hall = tk.Entry(self, textvariable=self.description_hall)
        self.create_window(320, 250, anchor="nw", window = hall)

        self.create_text(width//2 + 170, 10, text="Enter image link:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        image = tk.Entry(self, textvariable=self.property_image)
        self.create_window(width//2 + 400, 10, anchor="nw", window = image)

        self.create_text(width//2 + 170, 50, text="Enter address:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        address = tk.Entry(self, textvariable=self.property_address)
        self.create_window(width//2 + 400, 50, anchor="nw", window = address)

        self.create_text(width//2 + 170, 90, text="Enter size:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        size = tk.Entry(self, textvariable=self.property_size)
        self.create_window(width//2 + 400, 90, anchor="nw", window = size)

        self.create_text(width//2 + 170, 130, text="Enter price:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        price = tk.Entry(self, textvariable=self.property_price)
        self.create_window(width//2 + 400, 130, anchor="nw", window = price)

        self.create_text(width//2 + 170, 170, text="Enter rent price:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        rent = tk.Entry(self, textvariable=self.property_rent)
        self.create_window(width//2 + 400, 170, anchor="nw", window = rent)

        self.create_text(width//2 + 170, 210, text="Choose locality:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        locality = ttk.Combobox(self, width=18, textvariable = self.property_locality)
        self.create_window(width//2 + 400, 210, anchor="nw", window = locality)
        localities = self.db_connection.get_locality()
        locality['values'] = (localities)

        if self.id is None:
            btn_text = 'Add Property'
            btn_cmd = self.add_property
        else:
            btn_text = 'Modify Property'
            btn_cmd = self.modify_property

        add = tk.Button(self, text=btn_text, command = btn_cmd, font=("calibri", 20), activebackground="blue")
        self.create_window(width//2, 500, anchor="center", window=add)

    def add_property(self)->None:
        self.db_connection.add_property(
            description_id = self.property_id_var.get(),
            description_type = self.description_type.get(),
            description_status = self.description_status.get(),
            description_bathroom = self.description_bathroom.get(),
            description_bedroom = self.description_bedroom.get(),
            description_hall = self.description_hall.get(),
            description_kitchen = self.description_kitchen.get(),
            property_image = self.property_image.get(),
            property_address = self.property_address.get(),
            property_size = self.property_size.get(),
            property_price = self.property_price.get(),
            property_rent = self.property_rent.get(),
            property_locality = self.db_connection.get_locality_id(self.property_locality.get()),
            dealer = self.dealer
        )
        
    def modify_property(self) -> None:
        self.db_connection.modify_property(
            description_id = self.property_id_var.get(),
            description_type = self.description_type.get(),
            description_status = self.description_status.get(),
            description_bathroom = self.description_bathroom.get(),
            description_bedroom = self.description_bedroom.get(),
            description_hall = self.description_hall.get(),
            description_kitchen = self.description_kitchen.get(),
            property_image = self.property_image.get(),
            property_address = self.property_address.get(),
            property_size = self.property_size.get(),
            property_price = self.property_price.get(),
            property_rent = self.property_rent.get(),
            property_locality = self.db_connection.get_locality_id(self.property_locality.get()),
            dealer = self.dealer
        )