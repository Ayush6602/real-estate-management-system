from GUI.login_ui import LoginUi
from GUI.db_connection import DBConnection
import tkinter as tk


def main() -> None:
    db_connection = DBConnection()
    root = tk.Tk()
    root.title('Real Estate Management App')
    root.geometry('1280x720')
    login_ui_canvas = LoginUi(root, db_connection)
    root.mainloop()


if __name__ == '__main__':
    main()
