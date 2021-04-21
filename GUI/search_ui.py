from GUI.db_connection import DBConnection
from GUI.property_ui import PropertyUi
import tkinter as tk
from tkinter import ttk
from PIL.ImageTk import PhotoImage
from PIL import Image


class SearchUi(tk.Canvas):
    def __init__(self, master, db_connection: DBConnection, login_ui_cls) -> None:
        super().__init__(master)
        self.master = master
        self.login_bg_img = Image.open('images/search_bg.jpg')
        self.login_bg_pimg = PhotoImage(self.login_bg_img)
        self.login_ui_cls = login_ui_cls
        self.db_connection = db_connection
        vcmd = (self.register(self.callback))
        self.bathroom_select = tk.Entry(
            self, validate='all', validatecommand=(vcmd, '%P'))
        self.locality_select = tk.Entry(self)
        self.bedroom_select = tk.Entry(
            self, validate='all', validatecommand=(vcmd, '%P'))
        self.kitchen_select = tk.Entry(
            self, validate='all', validatecommand=(vcmd, '%P'))
        self.hall_select = tk.Entry(
            self, validate='all', validatecommand=(vcmd, '%P'))
        self.price_select = tk.Entry(
            self, validate='all', validatecommand=(vcmd, '%P'))
        self.status_select = tk.Entry(self)
        self.rent_select = tk.Entry(
            self, validate='all', validatecommand=(vcmd, '%P'))
        self.type_select = tk.Entry(self)
        self.size_select = tk.Entry(
            self, validate='all', validatecommand=(vcmd, '%P'))
        self.property_tree = ttk.Treeview(self)
        self.pack(fill=tk.BOTH, expand=True)
        self.bind('<Configure>', self.render)

    def render(self, event: tk.Event = None) -> None:
        if not self.winfo_exists():
            return
        height = self.winfo_height()
        width = self.winfo_width()
        # clear all
        self.delete('all')
        # set background image
        self.login_bg_pimg = PhotoImage(
            self.login_bg_img.resize((width, height), Image.ANTIALIAS))
        self.create_image(0, 0, anchor='nw', image=self.login_bg_pimg)
        # title text
        self.create_text(width/2, 5, text="Search By", anchor="n",
                         font=f'ariel {min(width, height) // 30} bold', fill="white")
        # locality combobox
        btn_fnt = f"arial {min(height, width) // 40} bold"
        locality = self.db_connection.get_locality()
        locality.append("All")
        self.create_text(width//7, 2*height//20, text="Locality:", anchor="nw",
                         font=btn_fnt, fill="white")
        self.local_select = ttk.Combobox(self, width=30, values=locality)
        self.create_window(2*width//7, 2*height//20 + 5,
                           anchor="nw", window=self.local_select)
        self.local_select.bind("<<ComboboxSelected>>", self.make_treeview)
        self.local_select.current(len(locality) - 1)
        # type combo box
        type = self.db_connection.get_type()
        type.append("All")
        self.create_text(width//7, 3.5*height//20, text="Type:",
                         anchor="nw", font=btn_fnt, fill="white")
        self.type_select = ttk.Combobox(self, width=28, values=type)
        self.create_window(2*width//7, 3.5*height//20 + 5,
                           anchor="nw", window=self.type_select)
        self.type_select.bind("<<ComboboxSelected>>", self.make_treeview)
        self.type_select.current(len(type) - 1)
        # status combobox
        status = self.db_connection.get_status()
        status.append("All")
        self.create_text(width//7, 5*height//20, text="Status:",
                         anchor="nw", font=btn_fnt, fill="white")
        self.status_select = ttk.Combobox(self, width=28, values=status)
        self.create_window(2*width//7, 5*height//20 + 5,
                           anchor="nw", window=self.status_select)
        self.status_select.bind("<<ComboboxSelected>>", self.make_treeview)
        self.status_select.current(len(status) - 1)
        # price entry
        self.create_text(width//7, 6.5*height//20, text="Price:", anchor="nw",
                         font=btn_fnt, fill="white")
        self.create_window(2*width//7, 6.5*height//20 +
                           15, window=self.price_select)
        self.price_select.bind('<Return>', self.make_treeview)
        # rent entry
        self.create_text(width//7, 8*height//20, text="Rent:",
                         anchor="nw", font=btn_fnt, fill="white")
        self.create_window(2*width//7, 8*height//20 +
                           15, window=self.rent_select)
        self.rent_select.bind('<Return>', self.make_treeview)
        # bedroom entry
        self.create_text(5*width//7 - 35, 2*height//20, text="Bedroom:", anchor="nw",
                         font=btn_fnt, fill="white")
        self.create_window(6*width//7, 2*height//20 + 15,
                           window=self.bedroom_select)
        self.bedroom_select.bind('<Return>', self.make_treeview)
        # bathroom entry
        self.create_text(5*width//7 - 35, 3.5*height//20, text="Bathroom:", anchor="nw",
                         font=btn_fnt, fill="white")
        self.create_window(6*width//7, 3.5*height//20 +
                           15, window=self.bathroom_select)
        self.bathroom_select.bind('<Return>', self.make_treeview)
        # kitchen entry
        self.create_text(5*width//7 - 35, 5*height//20, text="Kitchen:", anchor="nw",
                         font=btn_fnt, fill="white")
        self.create_window(6*width//7, 5*height//20 + 15,
                           window=self.kitchen_select)
        self.kitchen_select.bind('<Return>', self.make_treeview)
        # hall entry
        self.create_text(5*width//7 - 35, 6.5*height//20, text="Halls:", anchor="nw",
                         font=btn_fnt, fill="white")
        self.create_window(6*width//7, 6.5*height//20 +
                           15, window=self.hall_select)
        self.hall_select.bind('<Return>', self.make_treeview)
        # size entry
        self.create_text(5*width//7 - 35, 8*height//20, text="Size:",
                         anchor="nw", font=btn_fnt, fill="white")
        self.create_window(6*width//7, 8*height//20 +
                           15, window=self.size_select)
        self.size_select.bind('<Return>', self.make_treeview)
        # result title
        self.create_text(width//2, 10*height//20, text="Results", anchor="center",
                         font=f'ariel {min(width, height) // 30} bold', fill="white")
        self.make_treeview()
        # logout button
        logout_btn_x = width / 2
        logout_btn_y = 18 * height / 20
        logout_btn = tk.Button(self, text='Logout', background='red',
                               font=btn_fnt, command=self.logout, activebackground='orange')
        self.create_window(int(logout_btn_x), int(
            logout_btn_y), window=logout_btn)

    def logout(self) -> None:
        self.destroy()
        self.login_ui_cls(self.master, self.db_connection)

    def get_results(self, event=None):
        result = set(self.db_connection.get_property_all())
        if(self.local_select.get() != "All"):
            result = result.intersection(
                set(self.db_connection.get_property_locality(self.local_select.get())))
        if(self.size_select.get() != ''):
            result = result.intersection(
                set(self.db_connection.get_property_size(self.size_select.get())))
        if(self.bedroom_select.get() != ''):
            result = result.intersection(
                set(self.db_connection.get_property_bed(self.bedroom_select.get())))
        if(self.bathroom_select.get() != ''):
            result = result.intersection(
                set(self.db_connection.get_property_bathroom(self.bathroom_select.get())))
        if(self.kitchen_select.get() != ''):
            result = result.intersection(
                set(self.db_connection.get_property_kitchen(self.kitchen_select.get())))
        if(self.hall_select.get() != ''):
            result = result.intersection(
                set(self.db_connection.get_property_hall(self.hall_select.get())))
        if(self.type_select.get() != "All"):
            result = result.intersection(
                set(self.db_connection.get_property_type(self.type_select.get())))
        if(self.rent_select.get() != ''):
            result = result.intersection(
                set(self.db_connection.get_property_rent(self.rent_select.get())))
        if(self.status_select.get() != "All"):
            result = result.intersection(
                set(self.db_connection.get_property_status(self.status_select.get())))
        if(self.price_select.get() != ''):
            result = result.intersection(
                set(self.db_connection.get_property_price(self.price_select.get())))
        return list(result)

    def make_treeview(self, event=None):
        self.property_tree = ttk.Treeview(self, columns=(
            'Address', 'Size', 'Price', 'Rent', 'Name', 'Type', 'Status', 'Bedroom', 'Bathroom', 'Kitchen', 'Hall'))
        height = self.winfo_height()
        width = self.winfo_width()
        self.create_window(5, 11*height//20, anchor="nw",
                           width=width - 5, window=self.property_tree)

        self.property_tree.column("#0", width=0, stretch="NO")
        self.property_tree.column('Address', minwidth=70, width=80)
        self.property_tree.column('Size', minwidth=40, width=50)
        self.property_tree.column('Price', minwidth=40, width=50)
        self.property_tree.column('Rent', minwidth=40, width=50)
        self.property_tree.column('Name', minwidth=40, width=50)
        self.property_tree.column('Type', minwidth=50, width=60)
        self.property_tree.column('Status', minwidth=50, width=70)
        self.property_tree.column('Bedroom', minwidth=20, width=40)
        self.property_tree.column('Bathroom', minwidth=20, width=40)
        self.property_tree.column('Kitchen', minwidth=20, width=40)
        self.property_tree.column('Hall', minwidth=20, width=40)

        self.property_tree.heading("#0", text="")
        self.property_tree.heading("Address", text="Address")
        self.property_tree.heading("Size", text="Size")
        self.property_tree.heading("Price", text="Price")
        self.property_tree.heading("Rent", text="Rent")
        self.property_tree.heading("Name", text="Name")
        self.property_tree.heading("Type", text="Type")
        self.property_tree.heading("Status", text="Status")
        self.property_tree.heading("Bedroom", text="Bedroom")
        self.property_tree.heading('Bathroom', text="Bathroom")
        self.property_tree.heading("Kitchen", text="Kitchen")
        self.property_tree.heading("Hall", text="Hall")
        properties = self.get_results()
        for i in range(len(properties)):
            self.property_tree.insert(
                parent='', index='end', iid=i, values=properties[i][3:])
        self.property_tree.bind("<Double-1>", self.show_property)

    def show_property(self, event):
        item = self.property_tree.focus()
        selected = self.property_tree.item(item)
        selected_id = self.db_connection.get_property_id(selected['values'][0])
        property_window = tk.Toplevel(self)
        property_window.geometry('1280x720')
        PropertyUi(property_window, self.db_connection, selected_id)

    def callback(self, p):
        if str.isdigit(p) or p == "":
            return True
        else:
            return False
