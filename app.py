from GUI.login_ui import LoginUi
from GUI.property_ui import PropertyUi
from GUI.db_connection import DBConnection
import tkinter as tk
from tkinter import ttk


def main() -> None:
    db_connection = DBConnection()
    root = tk.Tk()
    root.title('Real Estate Management App')
    root.geometry('1280x720')
    root.minsize(640, 360)
    LoginUi(root, db_connection)
    root.mainloop()


if __name__ == '__main__':
    main()
