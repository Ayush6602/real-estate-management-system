from GUI.db_connection import DBConnection
from GUI.add_modify_property_ui import AddModifyProperty
import tkinter as tk
from PIL.ImageTk import PhotoImage
from PIL import Image
from tkinter import ttk


class AgentUi(tk.Canvas):
    def __init__(self, master, db_connection: DBConnection, username) -> None:
        super().__init__(master)
        self.master = master
        self.agent_bg_img = Image.open('images/agent_bg.jpeg')
        self.agent_bg_pimg = PhotoImage(self.agent_bg_img)
        self.db_connection = db_connection
        self.username = username
        self.pack(fill=tk.BOTH, expand=True)
        self.bind('<Configure>', self.render)
        self.properties = self.db_connection.get_property(self.username)
        self.transactions = self.db_connection.get_transaction(self.username)

        
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
        
        property_head = self.create_text(width/4, 10, text="Property", anchor="n", font=f'ariel {min(width, height) // 30} bold', fill="white")
        transaction_head = self.create_text(3*width/4, 10, text="Transaction", anchor="n", font=f'ariel {min(width, height) // 30} bold', fill="white")

        property_tree = ttk.Treeview(self)
        self.create_window(width//2 - 10, 50, anchor="ne", width=width//2-10, window=property_tree)
        property_tree['columns'] = ('Address', 'Price', 'Rent')

        property_tree.column("#0", width=0, stretch="NO")
        property_tree.column("Address", minwidth=70, width=300)
        property_tree.column('Price', minwidth=50, width=50)
        property_tree.column('Rent', minwidth=40, width=50)

        property_tree.heading("#0", text="")
        property_tree.heading("Address", text="Address")
        property_tree.heading("Price", text="Price")
        property_tree.heading("Rent", text="Rent")

        transaction_tree = ttk.Treeview(self, selectmode="none")
        self.create_window(width//2 + 10, 50, anchor="nw", width=width//2-10, window=transaction_tree)
        transaction_tree['columns'] = ('Date', 'Price', 'Rent', 'Client Name')

        transaction_tree.column("#0", width=0, stretch="NO")
        transaction_tree.column("Date", width=70)
        transaction_tree.column('Price', width=70)
        transaction_tree.column('Rent', width=70)
        transaction_tree.column('Client Name', width=300)

        transaction_tree.heading("#0", text="")
        transaction_tree.heading("Date", text="Date")
        transaction_tree.heading("Price", text="Price")
        transaction_tree.heading("Rent", text="Rent")
        transaction_tree.heading("Client Name", text="Client Name")

        if self.properties is not None:
            for i in range(len(self.properties)):
                property_tree.insert(parent='', index='end', iid=i, values=self.properties[i])

        if self.transactions is not None:
            for i in range(len(self.transactions)):
                transaction_tree.insert(parent='', index='end', iid=i, values=self.transactions[i])

        add = tk.Button(self, text='Add Property', command = self.add_property, font=("calibri", 20), activebackground="blue")
        self.create_window(width//4, 500, anchor="center", window=add)
        modify = tk.Button(self, text='Modify Property', command = lambda: self.modify_property(property_tree), font=("calibri", 20), activebackground="yellow")
        self.create_window(2*width//4, 500, anchor="center", window=modify)
        delete = tk.Button(self, text='Delete Property', command = lambda: self.delete_property(property_tree), font=("calibri", 20), activebackground="pink")
        self.create_window(3*width//4, 500, anchor="center", window=delete)

    def add_property(self)->None:
        add_property = tk.Tk()
        add_property.title("ADD PROPERTY")
        add_property.geometry("1280x720")
        AddModifyProperty(add_property, self.db_connection, None)
        
    def modify_property(self, tv:ttk.Treeview)->None:
        item = tv.focus()
        selected = tv.item(item)
        # print(selected['values'][0])
        if len(selected['values']) == 0:
            print("No property selected")
            return
        address = selected['values'][0]

        add_property = tk.Tk()
        add_property.title("MODIFY PROPERTY")
        add_property.geometry("1280x720")
        AddModifyProperty(add_property, self.db_connection, self.db_connection.get_id(address))

    def delete_property(self, tv:ttk.Treeview)->None:
        item = tv.focus()
        selected = tv.item(item)
        # print(selected['values'][0])
        if len(selected['values']) == 0:
            print("No property selected")
            return
        address = selected['values'][0]
        self.db_connection.delete_property(address)

        item = tv.selection()[0]
        tv.delete(item)
        
        print(address)