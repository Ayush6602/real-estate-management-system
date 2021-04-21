from GUI.login_ui import LoginUi
from GUI.add_modify_property_ui import AddModifyProperty
from GUI.db_connection import DBConnection
import tkinter as tk


def main() -> None:
    db_connection = DBConnection()
    root = tk.Tk()
    root.title('Real Estate Management App')
    root.geometry('1280x720')
    root.minsize(640, 360)
    # LoginUi(root, db_connection)
    AddModifyProperty(root, db_connection, 111)
    print(db_connection.get_property_all())
    root.mainloop()


if __name__ == '__main__':
    main()
