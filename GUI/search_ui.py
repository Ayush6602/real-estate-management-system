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
        self.login_bg_img = Image.open('images/login_bg.jpg')
        self.login_bg_pimg = PhotoImage(self.login_bg_img)
        self.db_connection = db_connection
        self.pack(fill = tk.BOTH, expand=True)
        self.bind('<Configure>', self.render)
        
       
        # tk.Label(self, text = "Search By :-").grid(row=0, column=10)
        
        locality=db_connection.get_locality()
        locality.append("NULL")
        n=tk.StringVar()
        tk.Label(self, text = "Locality:").grid(row=5, column=0)
        self.m=ttk.Combobox(self,width = 30,textvariable = n)
        self.m.bind("<<ComboboxSelected>>",self.localitymethod)
        self.m['values']=(locality)
        self.m.grid(column = 1,pady=30, row = 5)
        self.m.current()
        
        tk.Label(self, text = "Size:").grid(row=6, column=0)
        self.size_lbl = self.create_text(50,100, )
        n2=tk.StringVar()
        self.size_entry=tk.Entry(self,textvariable=n2)
        self.size_entry.bind('<Return>', self.sizemethod)
        self.create_window(50,200, window=self.size_entry)
      
        
        bedroom=db_connection.get_bedroom()
        bedroom.append("NULL")
        n3=tk.StringVar()
        tk.Label(self, text = "Bedrooms:").grid(row=7, column=0)
        self.m3=ttk.Combobox(self,width = 30,textvariable = n3)
        self.m3.bind("<<ComboboxSelected>>",self.bedmethod)
        self.m3['values']=(bedroom)
        self.m3.grid(column = 1,pady=30,row = 7)
        self.m3.current()
        
        
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
        self.login_bg_pimg = PhotoImage(self.login_bg_img.resize((width, height), Image.ANTIALIAS))
        self.create_image(0, 0, anchor='nw', image=self.login_bg_pimg)
        self.width=width
        self.height=height
        property_head = self.create_text(self.width/2, 10, text= "Search By", anchor="n", font=f'ariel {min(self.width, self.height) // 30} bold', fill="white")
        tk.Label(self, text = "Size:").grid(row=6, column=0)
        self.size_lbl = self.create_text(50,100, )
        n2=tk.StringVar()
        self.size_entry=tk.Entry(self,textvariable=n2)
        self.size_entry.bind('<Return>', self.sizemethod)
        self.create_window(150,95, window=self.size_entry)
     
            
    def localitymethod(self,event):
        property_head = self.create_text(self.width/2, 250, text= "Results", anchor="center", font=f'ariel {min(self.width, self.height) // 30} bold', fill="white")

        property_frame = tk.Frame(master = self)
        self.create_window(10, 300, anchor="nw", width=self.width, window=property_frame)
        property_tree = ttk.Treeview(property_frame)
        property_tree['columns'] = ('Id', 'Locality_id', 'Images','Address','Size','Price','Rent','Name','Type','Status','Bedroom','Kitchen','Hall')

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
        property_tree.heading("Kitchen", text="Kitchen")
        property_tree.heading("Hall", text="Hall")
    
        
        properties = self.db_connection.outputlocality(self.m.get())  
        for i in range (len(properties)):
            property_tree.insert(parent='', index='end', iid=i, values=properties[i])
        property_tree.pack(fill = tk.X)  
        
    def sizemethod(self,event):
        property_head = self.create_text(self.width/2, 250, text= "Results", anchor="center", font=f'ariel {min(self.width, self.height) // 30} bold', fill="white")

        property_frame = tk.Frame(master = self)
        self.create_window(10, 300, anchor="nw", width=self.width, window=property_frame)
        property_tree = ttk.Treeview(property_frame)
        property_tree['columns'] = ('Id', 'Locality_id', 'Images','Address','Size','Price','Rent','Name','Type','Status','Bedroom','Kitchen','Hall')

        property_tree.column("#0", width=0, stretch="NO")
        property_tree.column("Id", minwidth = 40, width = 50)
        property_tree.column('Locality_id', minwidth = 40, width = 50)
        property_tree.column('Images', minwidth = 40, width = 50)
        property_tree.column('Address', minwidth = 70, width = 80)
        property_tree.column('Size', minwidth = 40, width = 50)
        property_tree.column('Price', minwidth = 40, width = 50)
        property_tree.column('Name', minwidth = 40, width = 50)
        property_tree.column('Rent', minwidth = 40, width = 50)
        property_tree.column('Type', minwidth = 50, width = 60)
        property_tree.column('Status', minwidth = 50, width =70)
        property_tree.column('Bedroom', minwidth = 20, width = 40)
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
        property_tree.heading("Kitchen", text="Kitchen")
        property_tree.heading("Hall", text="Hall")
    
        
        properties = self.db_connection.outputsize(self.size_entry.get()) 
        for i in range (len(properties)):
            property_tree.insert(parent='', index='end', iid=i, values=properties[i])
        property_tree.pack(fill = tk.X)
        
    def bedmethod(self,event):
        property_head = self.create_text(self.width/2, 250, text= "Results", anchor="center", font=f'ariel {min(self.width, self.height) // 30} bold', fill="white")

        property_frame = tk.Frame(master = self)
        self.create_window(10, 300, anchor="nw", width=self.width, window=property_frame)
        property_tree = ttk.Treeview(property_frame)
        property_tree['columns'] = ('Id', 'Locality_id', 'Images','Address','Size','Price','Rent','Name','Type','Status','Bedroom','Kitchen','Hall')

        property_tree.column("#0", width=0, stretch="NO")
        property_tree.column("Id", minwidth = 40, width = 50)
        property_tree.column('Locality_id', minwidth = 40, width = 50)
        property_tree.column('Images', minwidth = 40, width = 50)
        property_tree.column('Address', minwidth = 70, width = 80)
        property_tree.column('Size', minwidth = 40, width = 50)
        property_tree.column('Price', minwidth = 40, width = 50)
        property_tree.column('Name', minwidth = 40, width = 50)
        property_tree.column('Rent', minwidth = 40, width = 50)
        property_tree.column('Type', minwidth = 50, width = 60)
        property_tree.column('Status', minwidth = 50, width =70)
        property_tree.column('Bedroom', minwidth = 20, width = 40)
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
        property_tree.heading("Kitchen", text="Kitchen")
        property_tree.heading("Hall", text="Hall")
    
        
        properties = self.db_connection.outputbed(self.m3.get()) 
        for i in range (len(properties)):
            property_tree.insert(parent='', index='end', iid=i, values=properties[i])
        property_tree.pack(fill = tk.X)