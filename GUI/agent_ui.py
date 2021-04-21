from GUI.db_connection import DBConnection
from GUI.add_modify_property_ui import AddModifyProperty
from GUI.property_ui import PropertyUi
import tkinter as tk
from PIL.ImageTk import PhotoImage
from PIL import Image
from tkinter import ttk
from tkinter import messagebox


class AgentUi(tk.Canvas):
    def __init__(self, master, db_connection: DBConnection, username: str) -> None:
        super().__init__(master)
        self.master = master
        self.agent_bg_img = Image.open('images/agent_bg.jpg')
        self.agent_bg_pimg = PhotoImage(self.agent_bg_img)
        self.db_connection = db_connection
        self.username = username
        self.pack(fill=tk.BOTH, expand=True)
        self.bind('<Configure>', self.render)

    def render(self, event: tk.Event = None) -> None:
        if not self.winfo_exists():
            return
        height = self.winfo_height()
        width = self.winfo_width()
        self.delete('all')
        # set background
        self.agent_bg_pimg = PhotoImage(
            self.agent_bg_img.resize((width, height), Image.ANTIALIAS))
        self.create_image(0, 0, anchor='nw', image=self.agent_bg_pimg)

        self.create_text(width/4, 10, text="Property", anchor="n",
                         font=f'ariel {min(width, height) // 30} bold', fill="white")
        self.create_text(3*width/4, 10, text="Transaction", anchor="n",
                         font=f'ariel {min(width, height) // 30} bold', fill="white")

        self.property_tree = ttk.Treeview(
            self, columns=('Address', 'Price', 'Rent'))
        self.create_window(width//2 - 10, 50, anchor="ne",
                           width=width//2-10, window=self.property_tree)
        self.property_tree.column("#0", width=0, stretch="NO")
        self.property_tree.column("Address", minwidth=70, width=300)
        self.property_tree.column('Price', minwidth=50, width=50)
        self.property_tree.column('Rent', minwidth=40, width=50)

        self.property_tree.heading("#0", text="")
        self.property_tree.heading("Address", text="Address")
        self.property_tree.heading("Price", text="Price")
        self.property_tree.heading("Rent", text="Rent")

        self.transaction_tree = ttk.Treeview(
            self, selectmode="none", columns=('Date', 'Price', 'Rent', 'Client Name'))
        self.create_window(width//2 + 10, 50, anchor="nw",
                           width=width//2-10, window=self.transaction_tree)

        self.transaction_tree.column("#0", width=0, stretch="NO")
        self.transaction_tree.column("Date", width=70)
        self.transaction_tree.column('Price', width=70)
        self.transaction_tree.column('Rent', width=70)
        self.transaction_tree.column('Client Name', width=300)

        self.transaction_tree.heading("#0", text="")
        self.transaction_tree.heading("Date", text="Date")
        self.transaction_tree.heading("Price", text="Price")
        self.transaction_tree.heading("Rent", text="Rent")
        self.transaction_tree.heading("Client Name", text="Client Name")

        properties = self.db_connection.get_property(self.username)
        transactions = self.db_connection.get_transaction(self.username)

        if properties is not None:
            for i in range(len(properties)):
                self.property_tree.insert(
                    parent='', index='end', iid=i, values=properties[i])

        self.property_tree.bind("<Double-1>", self.show_property)

        if transactions is not None:
            for i in range(len(transactions)):
                self.transaction_tree.insert(
                    parent='', index='end', iid=i, values=transactions[i])

        add = tk.Button(self, text='Add Property', command=self.add_property, font=(
            "calibri", 20), activebackground="blue")
        self.create_window(width//4, 500, anchor="center", window=add)
        modify = tk.Button(self, text='Modify Property', command=self.modify_property, font=(
            "calibri", 20), activebackground="yellow")
        self.create_window(2*width//4, 500, anchor="center", window=modify)
        delete = tk.Button(self, text='Delete Property', command=self.delete_property, font=(
            "calibri", 20), activebackground="pink")
        self.create_window(3*width//4, 500, anchor="center", window=delete)

    def show_property(self, event):
        item = self.property_tree.focus()
        selected = self.property_tree.item(item)

        selected_id = self.db_connection.get_property_id(selected['values'][0])

        property_window = tk.Toplevel(self, width=1280, height=720)
        PropertyUi(property_window, self.db_connection, None, selected_id)

    def add_property(self) -> None:
        add_modify = tk.Toplevel(self, width=1280, height=720)
        AddModifyProperty(add_modify, self.db_connection, None, self.username)

    def modify_property(self) -> None:
        item = self.property_tree.focus()
        selected = self.property_tree.item(item)
        if len(selected['values']) == 0:
            messagebox.showerror("Error", "No Property Selected")
            return
        address = selected['values'][0]
        add_modify = tk.Toplevel(self, width=1280, height=720)
        AddModifyProperty(add_modify, self.db_connection,
                          self.db_connection.get_property_id(address), self.username)

    def delete_property(self) -> None:
        item = self.property_tree.focus()
        selected = self.property_tree.item(item)
        if len(selected['values']) == 0:
            messagebox.showerror("Error", "No Property Selected")
            return
        address = selected['values'][0]
        self.db_connection.delete_property(address)

        item = self.property_tree.selection()[0]
        self.property_tree.delete(item)
