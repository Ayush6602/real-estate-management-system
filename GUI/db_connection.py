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
            return DBConnection.ADMIN
        self.cursor.execute(
            "select * from dealer where username = %s and password = %s", (username, password))
        if self.cursor.fetchone() is not None:
            return DBConnection.DEALER
        self.cursor.execute(
            "select * from client where username = %s and password = %s", (username, password))
        if self.cursor.fetchone() is not None:
            return DBConnection.CLIENT
        return 'unknown user'

    def report(self, query: str):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_property_details(self, property_id: int) -> dict:
        self.cursor.execute(
            'select * from property natural join description natural join locality where id = %s', (property_id,))
        result = self.cursor.fetchone()
        if result is None:
            return {}
        return {
            'locality_id': result[0],
            'id': result[1],
            'image_link': result[2],
            'Locality': result[13],
            'Address': result[3],
            'Price': result[5],
            'Rent': result[6],
            'Type': result[7],
            'Status': result[8],
            'Bedrooms': result[9],
            'Bathrooms': result[10],
            'Kitchens': result[11],
            'Halls': result[12],
            'Size sq.ft.': result[4],
        }

    def get_property(self, username: str):
        self.cursor.execute(
            "SELECT address, price, rent FROM property NATURAL JOIN description NATURAL JOIN property_dealer NATURAL JOIN dealer WHERE username = %s;", (username,))
        return(self.cursor.fetchall())

    def get_transaction(self, username: str):
        self.cursor.execute(
            "SELECT date, price, rent, client FROM transaction WHERE dealer = %s", (username,))
        return (self.cursor.fetchall())
