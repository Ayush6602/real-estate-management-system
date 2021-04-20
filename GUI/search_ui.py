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
        self.login_bg_img = Image.open('images/4.jpg')
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
        property_head = self.create_text(self.width/2, 5, text= "Search By", anchor="n", font=f'ariel {min(self.width, self.height) // 30} bold', fill="white")
        self.create_text(self.width//2 + 170, 220, text="Size:", anchor = "nw", font=('arial', 20, 'bold'), fill="white")
        self.size_entry=tk.Entry(self,textvariable=self.get_size)
        self.create_window(self.width//2 + 400,240, window=self.size_entry)
        self.size_entry.bind('<Return>', self.make_treeview)
        
        
        self.locality=self.db_connection.get_locality()
        self.locality.append("NULL")
        self.create_text(10, 50, text="Locality:", anchor = "nw", font=('arial', 20, 'bold'), fill="white")
        self.local_select=ttk.Combobox(self,width = 30)
        self.create_window(220, 50, anchor="nw", window = self.local_select)
        self.local_select.bind("<<ComboboxSelected>>",self.make_treeview)
        self.local_select['values']=(self.locality)
        self.local_select.current()
        
        self.bedroom=self.db_connection.get_bedroom()
        self.bedroom.append("NULL")
        self.create_text(10, 90, text="Bedroom:", anchor = "nw", font=('arial', 20, 'bold'), fill="white")
        self.bedroom_select=tk.Entry(self)
        self.create_window(280,110, window=self.bedroom_select)
        self.bedroom_select.bind('<Return>', self.make_treeview)
       
          
        self.bathroom=self.db_connection.get_bathroom()
        self.bathroom.append("NULL")
        self.create_text(10, 130, text="Bathroom:", anchor = "nw", font=('arial', 20, 'bold'), fill="white")
        self.bathroom_select=tk.Entry(self)
        self.create_window(280,150, window=self.bathroom_select)
        self.bathroom_select.bind('<Return>', self.make_treeview)
        
        self.kitchen=self.db_connection.get_kitchen()
        self.kitchen.append("NULL")
        self.create_text(10, 170, text="Kitchen:", anchor = "nw", font=('arial', 20, 'bold'), fill="white")
        self.kitchen_select=tk.Entry(self)
        self.create_window(280,190, window=self.kitchen_select)
        self.kitchen_select.bind('<Return>', self.make_treeview)
        
        
        self.hall=self.db_connection.get_hall()
        self.hall.append("NULL")
        self.create_text(10, 210, text="Halls:", anchor = "nw", font=('arial', 20, 'bold'), fill="white")
        self.hall_select=tk.Entry(self)
        self.create_window(280,230, window=self.hall_select)
        self.hall_select.bind('<Return>', self.make_treeview)
        
        self.price=self.db_connection.get_price()
        self.price.append("NULL")
        self.create_text(10, 250, text="Price:", anchor = "nw", font=('arial', 20, 'bold'), fill="white")
        self.price_select=tk.Entry(self)
        self.create_window(280,270, window=self.price_select)
        self.price_select.bind('<Return>', self.make_treeview)
        
        
        self.rent=self.db_connection.get_rent()
        self.rent.append("NULL")
        self.create_text(self.width//2 + 170, 90, text="Rent:", anchor = "nw", font=('arial', 20, 'bold'), fill="white")
        self.rent_select=tk.Entry(self)
        self.create_window(self.width//2+400,110, window=self.rent_select)
        self.rent_select.bind('<Return>', self.make_treeview)
        
        self.type=self.db_connection.get_type()
        self.type.append("NULL")
        self.create_text(self.width//2 + 170, 150, text="Type:", anchor = "nw", font=('arial', 20, 'bold'), fill="white")
        self.type_select=ttk.Combobox(self,width = 28)
        self.create_window(self.width//2 + 300, 150, anchor="nw", window = self.type_select)
        self.type_select.bind("<<ComboboxSelected>>",self.make_treeview)
        self.type_select['values']=(self.type)
        self.type_select.current()
        
        self.status=self.db_connection.get_status()
        self.status.append("NULL")
        self.create_text(self.width//2 + 170, 190, text="Status:", anchor = "nw", font=('arial', 20, 'bold'), fill="white")
        self.status_select=ttk.Combobox(self,width = 28)
        self.create_window(self.width//2 + 300,190, anchor="nw", window = self.status_select)
        self.status_select.bind("<<ComboboxSelected>>",self.make_treeview)
        self.status_select['values']=(self.status)
        self.status_select.current()
        
        property_head = self.create_text(self.width/2, 300, text= "Results", anchor="center", font=f'ariel {min(self.width, self.height) // 30} bold', fill="white")
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
        if(self.price_select.get()!='' and self.price_select.get()!="NULL"):
            result= result.intersection(set(self.db_connection.get_property_price(self.price_select.get())))
        return list(result)
    
    def make_treeview(self,event=None):
        self.property_tree = ttk.Treeview(self)
        self.create_window(10,350, anchor="nw", width=self.width, window=self.property_tree)
        self.property_tree['columns'] = ('Address','Size','Price','Rent','Name','Type','Status','Bedroom','Bathroom', 'Kitchen','Hall')
        
        self.property_tree.column("#0", width=0, stretch="NO")
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
            self.property_tree.insert(parent='', index='end', iid=i, values=self.properties[i][3:])
        self.property_tree.bind("<Double-1>", self.show_property)
        
    def show_property(self, event):
        item = self.property_tree.focus()
        selected = self.property_tree.item(item)
        selected_id = self.db_connection.get_property_id(selected['values'][0])
        property_window = tk.Toplevel(self, height = '1280', width = '720')
        PropertyUi(property_window, self.db_connection, "xyz", selected_id)