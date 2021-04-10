import mysql.connector as mysql
from mysql.connector.cursor import MySQLCursor


class DBConnection:

    CLIENT = 'client'
    ADMIN = 'admin'
    DEALER = 'dealer'

    def __init__(self) -> None:
        self.connection = mysql.connect(
            host="remotemysql.com",
            user="AMLZ6ZziDM",
            passwd="UQ5ebtcX8m",
            database="AMLZ6ZziDM"
        )
        self.cursor: MySQLCursor = self.connection.cursor(prepared=True)

    def get_user_type(self, username: str, password: str) -> str:
        self.cursor.execute(
            "select * from admin where username = %s and password = %s", (username, password))
        if self.cursor.fetchone() is not None:
            return 'admin'
        self.cursor.execute(
            "select * from dealer where username = %s and password = %s")
        if self.cursor.fetchone() is not None:
            return 'dealer'
        self.cursor.execute(
            "select * from client where username = %s and password = %s")
        if self.cursor.fetchone() is not None:
            return 'client'
        return 'unknown user'
