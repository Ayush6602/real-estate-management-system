from GUI.db_connection import DBConnection
import tkinter as tk


class AdminUi(tk.Frame):
    def __init__(self, master, db_connection: DBConnection) -> None:
        super().__init__(master)
        self.master = master
        self.cmd = tk.StringVar(value='SQL Command')
        self.db_connection = db_connection
        tk.Entry(self, textvariable=self.cmd).pack()
        tk.Button(self, text='Submit', command=self.given_query).pack()
        tk.Button(self, text='Sales report', command=self.sales_report).pack()
        tk.Button(self, text='Rental report', command=self.rental_report).pack()

    def sales_report(self) :
        self.query = "select * from transaction where price is not null"
        self.print_result()

    def rental_report(self) :
        self.query = "select * from transaction where rent is not null"
        self.print_result()

    def given_query(self) :
        self.query = self.cmd.get()
        self.print_result()
    
    def print_result(self) :
        result = self.db_connection.report(self.query)
        ResultUi = tk.Tk()
        ResultUi.title('Result')
        ResultUi.geometry('1000x1000')
        tk.Label(ResultUi,text = result).pack()
        ResultUi.mainloop()
        