from GUI.login_ui import LoginUi
from GUI.db_connection import DBConnection
import tkinter as tk


def main() -> None:
    db_connection = DBConnection()
    root = tk.Tk()
    root.title('Real Estate Management App')
    root.geometry('450x300')
    app = LoginUi(root, db_connection)
    app.pack(expand=True)
    root.mainloop()


if __name__ == '__main__':
    main()
