import mysql.connector as mysql
from mysql.connector.cursor import MySQLCursor
from tkinter import messagebox


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

    def command_result(self, query: str) -> MySQLCursor:
        self.cursor.execute(query)
        return self.cursor

    def get_rental_report(self) -> MySQLCursor:
        self.cursor.execute(
            "select p_id,date,rent,rent_duration,dealer,client from transaction where rent is not null"
        )
        return self.cursor

    def get_sales_report(self) -> MySQLCursor:
        self.cursor.execute(
            "select p_id,date,price,dealer,client from transaction where price is not null"
        )
        return self.cursor

    def get_property_details(self, property_id: int) -> dict:
        self.cursor.execute(
            'select * from property natural join description natural join locality where id = %s', (property_id,))
        result = self.cursor.fetchone()
        if result is None:
            return {}
        return {
            'locality_id': result[0],
            'id': result[1],
            'Image Link': result[2],
            'Locality': result[14],
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
            'Summary': result[13]
        }

    def get_property_id(self, address: str) -> int:
        self.cursor.execute(
            "SELECT id FROM property WHERE address = %s;", (address,))
        return (self.cursor.fetchall()[0][0])

    def get_locality_id(self, locality: str) -> int:
        self.cursor.execute(
            "SELECT locality_id FROM locality WHERE name = %s;", (locality,))
        print(locality)
        return self.cursor.fetchall()[0][0]

    def get_property(self, username: str) -> list:
        self.cursor.execute(
            "SELECT address, price, rent FROM property NATURAL JOIN description NATURAL JOIN property_dealer NATURAL JOIN dealer WHERE username = %s;", (username,))
        return(self.cursor.fetchall())

    def get_transaction(self, username: str) -> list:
        self.cursor.execute(
            "SELECT date, price, rent, client FROM transaction WHERE dealer = %s", (username,))
        return(self.cursor.fetchall())

    def get_locality(self):
        self.cursor.execute("SELECT distinct name from locality;")
        return [result[0] for result in self.cursor.fetchall()]

    def get_size(self):
        self.cursor.execute("SELECT distinct size from property;")
        return [result[0] for result in self.cursor.fetchall()]

    def get_bedroom(self):
        self.cursor.execute("SELECT distinct bedroom from description;")
        return [result[0] for result in self.cursor.fetchall()]

    def get_bathroom(self):
        self.cursor.execute("SELECT distinct bathroom from description;")
        return [result[0] for result in self.cursor.fetchall()]

    def get_kitchen(self):
        self.cursor.execute("SELECT distinct kitchen from description;")
        return [result[0] for result in self.cursor.fetchall()]

    def get_hall(self):
        self.cursor.execute("SELECT distinct hall from description;")
        return [result[0] for result in self.cursor.fetchall()]

    def get_price(self):
        self.cursor.execute("SELECT distinct price from property;")
        return [result[0] for result in self.cursor.fetchall()]

    def get_rent(self):
        self.cursor.execute("SELECT distinct rent from property;")
        return [result[0] for result in self.cursor.fetchall()]

    def get_type(self):
        self.cursor.execute("SELECT distinct type from description;")
        return [result[0] for result in self.cursor.fetchall()]

    def get_status(self):
        self.cursor.execute("SELECT distinct status from description;")
        return [result[0] for result in self.cursor.fetchall()]

    def get_property_locality(self, input):
        self.cursor.execute(
            "SELECT * from property natural join locality natural join description where locality.name=%s;", (input,))
        return(self.cursor.fetchall())

    def get_property_size(self, input1):
        self.cursor.execute(
            "SELECT * from property natural join locality natural join description where property.size>=%s;", (input1,))
        return(self.cursor.fetchall())

    def get_property_bed(self, input2):
        self.cursor.execute(
            "SELECT * from property natural join locality natural join description where description.bedroom>=%s;", (input2,))
        return(self.cursor.fetchall())

    def get_property_bathroom(self, input3):
        self.cursor.execute(
            "SELECT * from property natural join locality natural join description where description.bathroom>=%s;", (input3,))
        return(self.cursor.fetchall())

    def get_property_kitchen(self, input4):
        self.cursor.execute(
            "SELECT * from property natural join locality natural join description where description.kitchen>=%s;", (input4,))
        return(self.cursor.fetchall())

    def get_property_hall(self, input5):
        self.cursor.execute(
            "SELECT * from property natural join locality natural join description where description.hall>=%s;", (input5,))
        return(self.cursor.fetchall())

    def get_property_type(self, input6):
        self.cursor.execute(
            "SELECT * from property natural join locality natural join description where description.type=%s;", (input6,))
        return(self.cursor.fetchall())

    def get_property_rent(self, input7):
        self.cursor.execute(
            "SELECT * from property natural join locality natural join description where property.rent>=%s;", (input7,))
        return(self.cursor.fetchall())

    def get_property_status(self, input8):
        self.cursor.execute(
            "SELECT * from property natural join locality natural join description where description.status=%s;", (input8,))
        return(self.cursor.fetchall())

    def get_property_price(self, input10):
        self.cursor.execute(
            "SELECT * from property natural join locality natural join description where property.price>=%s;", (input10,))
        return(self.cursor.fetchall())

    def add_property(self, **kwargs) -> None:
        try:
            self.cursor.execute(
                "INSERT INTO property VALUES (%s, %s, %s, %s, %s, %s, %s);", (kwargs['description_id'], kwargs['property_image'], kwargs[
                    'property_address'], kwargs['property_size'], kwargs['property_price'], kwargs['property_rent'], kwargs['property_locality'])
            )
            self.cursor.execute(
                "INSERT INTO description VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (kwargs['description_id'], kwargs['description_type'], kwargs['description_status'], kwargs[
                    'description_bedroom'], kwargs['description_bathroom'], kwargs['description_kitchen'], kwargs['description_hall'], kwargs['summary'])
            )
            self.cursor.execute("INSERT INTO property_dealer VALUES (%s, %s);",
                                (kwargs['description_id'], kwargs['dealer']))
            messagebox.showinfo(
                "SUCCESS", "Property has been added successfully")
            self.connection.commit()

        except mysql.Error as error:
            messagebox.showerror(
                "Error", "Failed to add record to database: {}".format(error))
            self.connection.rollback()

    def modify_property(self, **kwargs) -> None:
        try:
            self.cursor.execute(
                "UPDATE property SET images=%s, address=%s, size=%s, price=%s, rent=%s, locality_id=%s WHERE id = %s;", (
                    kwargs['property_image'], kwargs['property_address'], kwargs['property_size'], kwargs['property_price'], kwargs['property_rent'], kwargs['property_locality'], kwargs['description_id'])
            )
            self.cursor.execute(
                "UPDATE description SET type=%s, status=%s, bedroom=%s, bathroom=%s, kitchen=%s, hall=%s, summary=%s WHERE id = %s;", (
                    kwargs['description_type'], kwargs['description_status'], kwargs['description_bedroom'], kwargs['description_bathroom'], kwargs['description_kitchen'], kwargs['description_hall'], kwargs['summary'], kwargs['description_id'])
            )
            messagebox.showinfo(
                "SUCCESS", "Property has been modified successfully")
            self.connection.commit()

        except mysql.Error as error:
            messagebox.showerror(
                "Error", "Failed to update record to database: {}".format(error))
            self.connection.rollback()

    def delete_property(self, address: str) -> None:
        try:
            self.cursor.execute(
                "DELETE property FROM description INNER JOIN property INNER JOIN property_dealer WHERE address = %s;", (
                    address,)
            )
            self.connection.commit()

        except mysql.Error as error:
            print("Failed to delete record to database: {}".format(error))
            self.connection.rollback()

    def add_client(self, username, password, name, contact, mail) -> bool:
        try:
            self.cursor.execute("INSERT INTO client VALUES (%s, %s, %s, %s, %s);",
                                (username, password, name, contact, mail))
            self.connection.commit()
            messagebox.showinfo(
                "SUCCESS", "Your client account has been created!")
            return True
        except mysql.Error as error:
            messagebox.showerror(
                "Error", "Failed to update record to database rollback: {}".format(error))
            self.connection.rollback()
            return False

    def get_max_id(self, username: str) -> int:
        self.cursor.execute("select max(id) from property;")
        return self.cursor.fetchone()[0]

    def get_property_all(self):
        self.cursor.execute(
            "SELECT * from property natural join locality natural join description")
        return(self.cursor.fetchall())

    def get_dealers(self, property_id:int):
        self.cursor.execute("SELECT name, contact_no, mail FROM property_dealer NATURAL JOIN dealer WHERE id = %s", (property_id,))
        return self.cursor.fetchall()