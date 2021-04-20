from GUI.db_connection import DBConnection
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
        
        locality=db_connection.get_locality()
        locality.append("NULL")
        tk.Label(self, text = "Locality:").grid(row=5, column=0)
        self.local_select=ttk.Combobox(self,width = 30)
        self.local_select.bind("<<ComboboxSelected>>",self.render)
        self.local_select['values']=(locality)
        self.local_select.grid(column = 1,pady=30, row = 5)
        self.local_select.current()
        
        self.size_lbl = None
        self.size_entry=None
      
        
        bedroom=db_connection.get_bedroom()
        bedroom.append("NULL")
        tk.Label(self, text = "Bedrooms:").grid(row=7, column=0)
        self.bedroom_select=ttk.Combobox(self,width = 28)
        self.bedroom_select.bind("<<ComboboxSelected>>",self.render)
        self.bedroom_select['values']=(bedroom)
        self.bedroom_select.grid(column = 1,pady=30,row = 7)
        self.bedroom_select.current()
        
        
    def render(self, event: tk.Event = None) -> None:
        if not self.winfo_exists():
            return
        height = self.winfo_height()
        width = self.winfo_width()
        self.delete('all')
        # set background
        self.login_bg_pimg = PhotoImage(self.login_bg_img.resize((width, height), Image.ANTIALIAS))
        self.create_image(0, 0, anchor='nw', image=self.login_bg_pimg)
        self.width=width
        self.height=height
        property_head = self.create_text(self.width/2, 10, text= "Search By", anchor="n", font=f'ariel {min(self.width, self.height) // 30} bold', fill="white")
        tk.Label(self, text = "Size:").grid(row=6, column=0)
        self.size_lbl = self.create_text(50,100, )
        self.size_entry=tk.Entry(self,textvariable=self.get_size)
        self.size_entry.bind('<Return>', self.render)
        self.create_window(150,95, window=self.size_entry)
        property_head = self.create_text(self.width/2, 250, text= "Results", anchor="center", font=f'ariel {min(self.width, self.height) // 30} bold', fill="white")

        # property_frame = tk.Frame(master = self)
        property_tree = ttk.Treeview(self)
        self.create_window(10, 300, anchor="nw", width=self.width, window=property_tree)
        property_tree['columns'] = ('Id', 'Locality_id', 'Images','Address','Size','Price','Rent','Name','Type','Status','Bedroom','Bathroom', 'Kitchen','Hall')

        property_tree.column("#0", width=0, stretch="NO")
        property_tree.column("Id", minwidth = 40, width = 50)
        property_tree.column('Locality_id', minwidth = 40, width = 50)
        property_tree.column('Images', minwidth = 40, width = 50)
        property_tree.column('Address', minwidth = 70, width = 80)
        property_tree.column('Size', minwidth = 40, width = 50)
        property_tree.column('Price', minwidth = 40, width = 50)
        property_tree.column('Rent', minwidth = 40, width = 50)
        property_tree.column('Name', minwidth = 40, width = 50)
        property_tree.column('Type', minwidth = 50, width = 60)
        property_tree.column('Status', minwidth = 50, width = 70)
        property_tree.column('Bedroom', minwidth = 20, width = 40)
        property_tree.column('Bathroom', minwidth = 20, width = 40)
        property_tree.column('Kitchen', minwidth = 20, width = 40)
        property_tree.column('Hall', minwidth = 20, width = 40)

        property_tree.heading("#0", text="")
        property_tree.heading("Id", text="ID")
        property_tree.heading("Locality_id", text="Locality_Id")
        property_tree.heading("Images", text="Images")
        property_tree.heading("Address", text="Address")
        property_tree.heading("Size", text="Size")
        property_tree.heading("Price", text="Price")
        property_tree.heading("Rent", text="Rent")
        property_tree.heading("Name", text="Name")
        property_tree.heading("Type", text="Type")
        property_tree.heading("Status", text="Status")
        property_tree.heading("Bedroom", text="Bedroom")
        property_tree.heading('Bathroom', text="Bathroom")
        property_tree.heading("Kitchen", text="Kitchen")
        property_tree.heading("Hall", text="Hall")
        self.properties = self.get_results()
        # print(self.properties)
        for i in range(len(self.properties)):
            property_tree.insert(parent='', index='end', iid=i, values=self.properties[i])
                    
    def get_results(self,event=None):
        result= set(self.db_connection.get_property_all())
        if(self.local_select.get()!='' and self.local_select.get()!="NULL"):
            result= result.intersection(set(self.db_connection.get_property_locality(self.local_select.get())))
        if(self.get_size.get()!=''):
            result= result.intersection(set(self.db_connection.get_property_size(self.get_size.get())))
        if(self.bedroom_select.get()!='' and self.bedroom_select.get()!="NULL"):
            result= result.intersection(set(self.db_connection.get_property_bed(self.bedroom_select.get())))
        return list(result)
        
    