from GUI.db_connection import DBConnection
from GUI.property_ui import PropertyUi
import tkinter as tk
from tkinter import ttk
from PIL.ImageTk import PhotoImage
from PIL import Image
from tkinter import ttk

class SearchUi(tk.Canvas):
    def __init__(self, master, db_connection: DBConnection) -> None:
        super().__init__(master)
        self.master = master
        self.login_bg_img = Image.open('images/1.jpeg')
        self.login_bg_pimg = PhotoImage(self.login_bg_img)
        self.properties=[]
        self.db_connection = db_connection
        self.pack(fill = tk.BOTH, expand=True)
        self.bind('<Configure>', self.render)
        self.get_size = tk.StringVar(self)
        self.bathroom=None
        self.locality=None
        self.bedroom=None
        self.kitchen=None
        self.hall=None
        self.price=None
        self.status=None
        self.rent=None
        self.address=None
        self.type=None 
        self.size_lbl = None
        self.size_entry=None
        self.property_tree=None
        
    def render(self, event: tk.Event = None) -> None:
        if not self.winfo_exists():
            return
        height = self.winfo_height()
        width = self.winfo_width()
        self.delete('all')
        self.login_bg_pimg = PhotoImage(self.login_bg_img.resize((width, height), Image.ANTIALIAS))
        self.create_image(0, 0, anchor='nw', image=self.login_bg_pimg)
        self.width=width
        self.height=height
        property_head = self.create_text(self.width/2, 5, text= "Search By", anchor="n", font=f'ariel {min(self.width, self.height) // 30} bold', fill="red")
        self.create_text(self.width//2 + 170, 210, text="Size:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        self.size_entry=tk.Entry(self,textvariable=self.get_size)
        self.create_window(self.width//2 + 400,230, window=self.size_entry)
        self.size_entry.bind('<Return>', self.make_treeview)
        
        
        self.locality=self.db_connection.get_locality()
        self.locality.append("NULL")
        self.create_text(10, 50, text="Locality:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        self.local_select=ttk.Combobox(self,width = 30)
        self.create_window(280, 50, anchor="nw", window = self.local_select)
        self.local_select.bind("<<ComboboxSelected>>",self.make_treeview)
        self.local_select['values']=(self.locality)
        self.local_select.current()
        
        self.bedroom=self.db_connection.get_bedroom()
        self.bedroom.append("NULL")
        self.create_text(10, 90, text="Bedroom:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        self.bedroom_select=ttk.Combobox(self,width = 28)
        self.create_window(280,90, anchor="nw", window = self.bedroom_select)
        self.bedroom_select.bind("<<ComboboxSelected>>",self.make_treeview)
        self.bedroom_select['values']=(self.bedroom)
        self.bedroom_select.current()
          
        self.bathroom=self.db_connection.get_bathroom()
        self.bathroom.append("NULL")
        self.create_text(10, 130, text="Bathroom:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        self.bathroom_select=ttk.Combobox(self,width = 28)
        self.create_window(280, 130, anchor="nw", window = self.bathroom_select)
        self.bathroom_select.bind("<<ComboboxSelected>>",self.make_treeview)
        self.bathroom_select['values']=(self.bathroom)
        self.bathroom_select.current()
        
        self.kitchen=self.db_connection.get_kitchen()
        self.kitchen.append("NULL")
        self.create_text(10, 170, text="Kitchen:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        self.kitchen_select=ttk.Combobox(self,width = 28)
        self.create_window(280, 170, anchor="nw", window = self.kitchen_select)
        self.kitchen_select.bind("<<ComboboxSelected>>",self.make_treeview)
        self.kitchen_select['values']=(self.kitchen)
        self.kitchen_select.current()
        
        self.hall=self.db_connection.get_hall()
        self.hall.append("NULL")
        self.create_text(10, 210, text="Halls:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        self.hall_select=ttk.Combobox(self,width = 28)
        self.create_window(280,210, anchor="nw", window = self.hall_select)
        self.hall_select.bind("<<ComboboxSelected>>",self.make_treeview)
        self.hall_select['values']=(self.hall)
        self.hall_select.current()
        
        self.price=self.db_connection.get_price()
        self.price.append("NULL")
        self.create_text(10, 250, text="Price:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        self.price_select=ttk.Combobox(self,width = 28)
        self.create_window(280,250, anchor="nw", window = self.price_select)
        self.price_select.bind("<<ComboboxSelected>>",self.make_treeview)
        self.price_select['values']=(self.price)
        self.price_select.current()
        
        self.address=self.db_connection.get_address()
        self.address.append("NULL")
        self.create_text(self.width//2 + 170, 50, text="Address:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        self.address_select=ttk.Combobox(self,width = 28)
        self.create_window(self.width//2 + 300, 50, anchor="nw", window = self.address_select)
        self.address_select.bind("<<ComboboxSelected>>",self.make_treeview)
        self.address_select['values']=(self.address)
        self.address_select.current()
        
        self.rent=self.db_connection.get_rent()
        self.rent.append("NULL")
        self.create_text(self.width//2 + 170, 90, text="Rent:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        self.rent_select=ttk.Combobox(self,width = 28)
        self.create_window(self.width//2 + 300, 90, anchor="nw", window = self.rent_select)
        self.rent_select.bind("<<ComboboxSelected>>",self.make_treeview)
        self.rent_select['values']=(self.rent)
        self.rent_select.current()
        
        self.type=self.db_connection.get_type()
        self.type.append("NULL")
        self.create_text(self.width//2 + 170, 130, text="Type:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        self.type_select=ttk.Combobox(self,width = 28)
        self.create_window(self.width//2 + 300, 130, anchor="nw", window = self.type_select)
        self.type_select.bind("<<ComboboxSelected>>",self.make_treeview)
        self.type_select['values']=(self.type)
        self.type_select.current()
        
        self.status=self.db_connection.get_status()
        self.status.append("NULL")
        self.create_text(self.width//2 + 170, 170, text="Status:", anchor = "nw", font=('arial', 20, 'bold'), fill="red")
        self.status_select=ttk.Combobox(self,width = 28)
        self.create_window(self.width//2 + 300,170, anchor="nw", window = self.status_select)
        self.status_select.bind("<<ComboboxSelected>>",self.make_treeview)
        self.status_select['values']=(self.status)
        self.status_select.current()
        
        property_head = self.create_text(self.width/2, 300, text= "Results", anchor="center", font=f'ariel {min(self.width, self.height) // 30} bold', fill="red")
        self.make_treeview()
    
    def get_results(self,event=None):
        result= set(self.db_connection.get_property_all())
        if(self.local_select.get()!='' and self.local_select.get()!="NULL"):
            result= result.intersection(set(self.db_connection.get_property_locality(self.local_select.get())))
        if(self.get_size.get()!=''):
            result= result.intersection(set(self.db_connection.get_property_size(self.get_size.get())))
        if(self.bedroom_select.get()!='' and self.bedroom_select.get()!="NULL"):
            result= result.intersection(set(self.db_connection.get_property_bed(self.bedroom_select.get())))
        if(self.bathroom_select.get()!='' and self.bathroom_select.get()!="NULL"):
            result= result.intersection(set(self.db_connection.get_property_bathroom(self.bathroom_select.get())))
        if(self.kitchen_select.get()!='' and self.kitchen_select.get()!="NULL"):
            result= result.intersection(set(self.db_connection.get_property_kitchen(self.kitchen_select.get())))
        if(self.hall_select.get()!='' and self.hall_select.get()!="NULL"):
            result= result.intersection(set(self.db_connection.get_property_hall(self.hall_select.get())))
        if(self.type_select.get()!='' and self.type_select.get()!="NULL"):
            result= result.intersection(set(self.db_connection.get_property_type(self.type_select.get())))
        if(self.rent_select.get()!='' and self.rent_select.get()!="NULL"):
            result= result.intersection(set(self.db_connection.get_property_rent(self.rent_select.get())))
        if(self.status_select.get()!='' and self.status_select.get()!="NULL"):
            result= result.intersection(set(self.db_connection.get_property_status(self.status_select.get())))
        if(self.address_select.get()!='' and self.address_select.get()!="NULL"):
            result= result.intersection(set(self.db_connection.get_property_address(self.address_select.get())))
        if(self.price_select.get()!='' and self.price_select.get()!="NULL"):
            result= result.intersection(set(self.db_connection.get_property_price(self.price_select.get())))
        return list(result)
    
    def make_treeview(self,event=None):
        self.property_tree = ttk.Treeview(self)
        self.create_window(10,350, anchor="nw", width=self.width, window=self.property_tree)
        self.property_tree['columns'] = ('Id', 'Locality_id', 'Images','Address','Size','Price','Rent','Name','Type','Status','Bedroom','Bathroom', 'Kitchen','Hall')
        
        self.property_tree.column("#0", width=0, stretch="NO")
        self.property_tree.column("Id", minwidth = 40, width = 50)
        self.property_tree.column('Locality_id', minwidth = 40, width = 50)
        self.property_tree.column('Images', minwidth = 40, width = 50)
        self.property_tree.column('Address', minwidth = 70, width = 80)
        self.property_tree.column('Size', minwidth = 40, width = 50)
        self.property_tree.column('Price', minwidth = 40, width = 50)
        self.property_tree.column('Rent', minwidth = 40, width = 50)
        self.property_tree.column('Name', minwidth = 40, width = 50)
        self.property_tree.column('Type', minwidth = 50, width = 60)
        self.property_tree.column('Status', minwidth = 50, width = 70)
        self.property_tree.column('Bedroom', minwidth = 20, width = 40)
        self.property_tree.column('Bathroom', minwidth = 20, width = 40)
        self.property_tree.column('Kitchen', minwidth = 20, width = 40)
        self.property_tree.column('Hall', minwidth = 20, width = 40)
        
        self.property_tree.heading("#0", text="")
        self.property_tree.heading("Id", text="ID")
        self.property_tree.heading("Locality_id", text="Locality_Id")
        self.property_tree.heading("Images", text="Images")
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
        self.properties = self.get_results()
        for i in range(len(self.properties)):
            self.property_tree.insert(parent='', index='end', iid=i, values=self.properties[i])
        self.property_tree.bind("<Double-1>", self.show_property)
        
    def show_property(self, event):
        item = self.property_tree.focus()
        selected = self.property_tree.item(item)
        # print(selected['values'])
        # print(item)
        selected_id = self.db_connection.get_property_id(selected['values'][3])
        property_window = tk.Toplevel(self, height = '1280', width = '720')
        PropertyUi(property_window, self.db_connection, "xyz", selected_id)