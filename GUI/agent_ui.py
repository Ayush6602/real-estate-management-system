from GUI.db_connection import DBConnection
import tkinter as tk

class AgentUi(tk.Frame):
    def __init__(self, master, db_connection: DBConnection, username) -> None:
        super().__init__(master)
        self.master = master
        self.property_id = tk.StringVar(value="property")
        self.db_connection = db_connection
        self.username = username

        top_frame = tk.Frame(master = self)
        top_frame.grid_columnconfigure([0,1], weight=1)
        input_label = tk.Label(master = top_frame, text = "Enter Property ID:").grid(row=0, column=0)
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

    # def enterRent(self) -> None:
