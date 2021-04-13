from GUI.login_ui import LoginUi
from GUI.agent_ui import AgentUi
from GUI.db_connection import DBConnection
import tkinter as tk


def main() -> None:
    db_connection = DBConnection()
    root = tk.Tk()
    root.title('Real Estate Management App')
    root.geometry('1280x720')
    root.minsize(450, 300)
    LoginUi(root, db_connection)
    root.mainloop()


if __name__ == '__main__':
    main()
