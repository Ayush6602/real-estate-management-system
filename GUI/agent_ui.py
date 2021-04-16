from GUI.db_connection import DBConnection
import tkinter as tk
from PIL.ImageTk import PhotoImage
from PIL import Image
from tkinter import ttk


class AgentUi(tk.Canvas):
    def __init__(self, master, db_connection: DBConnection, username) -> None:
        super().__init__(master)
        self.master = master
        self.property_id = tk.StringVar(value="property")
        self.login_bg_img = Image.open('C:\\Users\\Almas\\Documents\\Visual Studio 2019\\Code\\real-estate-management-system\\images\\login_bg.jpg')
        self.login_bg_pimg = PhotoImage(self.login_bg_img)
        self.db_connection = db_connection
        self.username = username
        self.pack(fill=tk.BOTH, expand=True)
        self.bind('<Configure>', self.render)
        """
        # # Add image file
        # bg = PhotoImage(file = 'images/login_bg.jpg')
        
        # # Show image using label
        # label1 = tk.Label(self.master, image = bg)
        # label1.pack(fill = tk.X)

        top_frame = tk.Frame(master = self)
        top_frame.grid_columnconfigure([0,1], weight=1)
        input_label = tk.Label(master = top_frame, text = "Enter Property ID:").grid(row=0, column=0)
        property_lbl = self.create_text(30, 20, )
        property_entry = tk.Entry(top_frame).grid(row=0, column=1)
        rent = tk.Button(master = top_frame, text="RENT").grid(row=1, column=0, pady=20)
        sell = tk.Button(master = top_frame, text="SELL").grid(row=1, column=1, pady=20)
        top_frame.pack(fill = tk.X, expand=True)

        output_prop = tk.Frame(master = self, bg="yellow")
        prop_lbl = tk.Label(master=output_prop, text = "Properties", bg="yellow").pack()
        output_prop.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)

        output_trans = tk.Frame(master = self, bg="green")
        trans_lbl = tk.Label(master=output_trans, text = "Transactions", bg="green").pack()
        output_trans.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)
        """

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
        self.login_bg_pimg = PhotoImage(
            self.login_bg_img.resize((width, height), Image.ANTIALIAS))
        self.create_image(0, 0, anchor='nw', image=self.login_bg_pimg)
        """
        property_lbl = self.create_text(3*width//8, 60, text="Enter property ID:", anchor="e", font=f'ariel {min(width, height) // 20} bold', fill="yellow")
        property_entry = tk.Entry(self, textvariable=self.property_id, font=f'ariel {min(width, height) // 20}')
        self.create_window(5*width//8, 60, anchor = "w", window= property_entry)

        rent = tk.Button(master = self, text="RENT")
        sell = tk.Button(master = self, text="SELL")

        self.create_window(2*width//6, 120, anchor = "e", window = rent)
        self.create_window(4*width//6, 120, anchor = "w", window = sell)
        """
        property_head = self.create_text(
            width/4, 10, text="Property", anchor="n", font=f'ariel {min(width, height) // 30} bold', fill="white")
        transaction_head = self.create_text(
            3*width/4, 10, text="Transaction", anchor="n", font=f'ariel {min(width, height) // 30} bold', fill="white")

        property_frame = tk.Frame(master=self)
        self.create_window(width//2 - 10, 50, anchor="ne",
                           width=width//2-10, window=property_frame)
        property_tree = ttk.Treeview(property_frame)
        property_tree['columns'] = ('Address', 'Price', 'Rent')

        property_tree.column("#0", width=0, stretch="NO")
        property_tree.column("Address", minwidth=70, width=width//4)
        property_tree.column('Price', minwidth=50, width=50)
        property_tree.column('Rent', minwidth=40, width=50)

        property_tree.heading("#0", text="")
        property_tree.heading("Address", text="Address")
        property_tree.heading("Price", text="Price")
        property_tree.heading("Rent", text="Rent")

        transaction_frame = tk.Frame(master=self)
        self.create_window(width//2 + 10, 50, anchor="nw",
                           width=width//2-10, window=transaction_frame)
        transaction_tree = ttk.Treeview(transaction_frame)
        transaction_tree['columns'] = ('Date', 'Price', 'Rent', 'Client Name')

        transaction_tree.column("#0", width=0, stretch="NO")
        transaction_tree.column("Date", width=50)
        transaction_tree.column('Price', width=50)
        transaction_tree.column('Rent', width=50)
        transaction_tree.column('Client Name', width=50)

        transaction_tree.heading("#0", text="")
        transaction_tree.heading("Date", text="Date")
        transaction_tree.heading("Price", text="Price")
        transaction_tree.heading("Rent", text="Rent")
        transaction_tree.heading("Client Name", text="Client Name")
        # transaction_tree.pack(fill = tk.X)

        properties = self.db_connection.get_property(self.username)
        for i in range(len(properties)):
            property_tree.insert(parent='', index='end',
                                 iid=i, values=properties[i])
        property_tree.pack(fill=tk.X)

        transactions = self.db_connection.get_transaction(self.username)
        if transactions is not None:
            for i in range(len(transactions)):
                transaction_tree.insert(
                    parent='', index='end', iid=i, values=localities[i])
        transaction_tree.pack(fill=tk.X)

        # get_property_transaction(self.username, rent, sale)
