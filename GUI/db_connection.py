import mysql.connector as mysql
from mysql.connector.cursor import MySQLCursor
# from prettytable import from_db_cursor


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

    def command_result(self, query: str):
        self.cursor.execute(query)
        return from_db_cursor(self.cursor)

    def get_rental_report(self):
        self.cursor.execute(
            "select p_id,date,rent,rent_duration,dealer,client from transaction where rent is not null"
        )
        return from_db_cursor(self.cursor)
    
    def get_sales_report(self):
        self.cursor.execute(
            "select p_id,date,price,dealer,client from transaction where price is not null"
        )
        return from_db_cursor(self.cursor)

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

    def get_property_id(self, address:str) -> int:
        self.cursor.execute("SELECT id FROM property WHERE address = %s;", (address,))
        return (self.cursor.fetchall()[0][0])

    def get_locality_id(self, locality:str) -> int:
        self.cursor.execute("SELECT locality_id FROM locality WHERE name = %s;", (locality,))
        return self.cursor.fetchall()[0][0]

    def get_property(self, username:str) -> list:
        self.cursor.execute("SELECT address, price, rent FROM property NATURAL JOIN description NATURAL JOIN property_dealer NATURAL JOIN dealer WHERE username = %s;", (username,))
        return(self.cursor.fetchall())

    def get_transaction(self, username:str) -> list:
        self.cursor.execute("SELECT date, price, rent, client FROM transaction WHERE dealer = %s", (username,))
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
    
    # def get_name(self):
    #     self.cursor.execute("SELECT name from description;")
    #     return [result[0] for result in self.cursor.fetchall()]
    
    def get_type(self):
        self.cursor.execute("SELECT type from description;")
        return [result[0] for result in self.cursor.fetchall()]
    
    def get_status(self):
        self.cursor.execute("SELECT status from description;")
        return [result[0] for result in self.cursor.fetchall()]
    
    def get_address(self):
        self.cursor.execute("SELECT address from property;")
        return [result[0] for result in self.cursor.fetchall()]
        
    def get_property_locality(self,input):
        self.cursor.execute("SELECT * from property natural join locality natural join description where locality.name=%s;",(input,))
        return(self.cursor.fetchall())
    
    def get_property_size(self,input1):
        self.cursor.execute("SELECT * from property natural join locality natural join description where property.size=%s;",(input1,))
        return(self.cursor.fetchall())
    
    def get_property_bed(self,input2):
        self.cursor.execute("SELECT * from property natural join locality natural join description where description.bedroom=%s;",(input2,))
        return(self.cursor.fetchall())
    
    def get_property_bathroom(self,input3):
        self.cursor.execute("SELECT * from property natural join locality natural join description where description.bathroom=%s;",(input3,))
        return(self.cursor.fetchall())
    
    def get_property_kitchen(self,input4):
        self.cursor.execute("SELECT * from property natural join locality natural join description where description.kitchen=%s;",(input4,))
        return(self.cursor.fetchall())
    
    def get_property_hall(self,input5):
        self.cursor.execute("SELECT * from property natural join locality natural join description where description.hall=%s;",(input5,))
        return(self.cursor.fetchall())
    
    def get_property_type(self,input6):
        self.cursor.execute("SELECT * from property natural join locality natural join description where description.type=%s;",(input6,))
        return(self.cursor.fetchall())
    
    def get_property_rent(self,input7):
        self.cursor.execute("SELECT * from property natural join locality natural join description where property.rent=%s;",(input7,))
        return(self.cursor.fetchall())
    
    def get_property_status(self,input8):
        self.cursor.execute("SELECT * from property natural join locality natural join description where description.status=%s;",(input8,))
        return(self.cursor.fetchall())
    
    def get_property_address(self,input9):
        self.cursor.execute("SELECT * from property natural join locality natural join description where property.address=%s;",(input9,))
        return(self.cursor.fetchall())
    
    def get_property_price(self,input10):
        self.cursor.execute("SELECT * from property natural join locality natural join description where property.price=%s;",(input10,))
        return(self.cursor.fetchall())
    
    def add_property(self, **args) ->None:
        try:
            self.cursor.execute(
                "INSERT INTO property VALUES (%s, %s, %s, %s, %s, %s, %s);", (args['description_id'], args['property_image'], args['property_address'], args['property_size'], args['property_price'], args['property_rent'], args['property_locality'])
            )
            self.cursor.execute(
                "INSERT INTO description VALUES (%s, %s, %s, %s, %s, %s, %s);", (args['description_id'], args['description_type'], args['description_status'], args['description_bedroom'], args['description_bathroom'], args['description_kitchen'], args['description_hall'])
            )
            self.cursor.execute("INSERT INTO property_dealer VALUES (%s, %s);", (args['description_id'], args['dealer']))
            print("done")
            self.connection.commit()

        except mysql.Error as error:
            print("Failed to update record to database rollback: {}".format(error))
            self.connection.rollback()

    def modify_property(self, **args) ->None:
        try:
            self.cursor.execute(
                "UPDATE property SET images=%s, address=%s, size=%s, price=%s, rent=%s, locality_id=%s WHERE id = %s;", (args['property_image'], args['property_address'], args['property_size'], args['property_price'], args['property_rent'], args['property_locality'], args['description_id'])
            )
            self.cursor.execute(
                "UPDATE description SET type=%s, status=%s, bedroom=%s, bathroom=%s, kitchen=%s, hall=%s;", (args['description_type'], args['description_status'], args['description_bedroom'], args['description_bathroom'], args['description_kitchen'], args['description_hall'])
            )
            print("done")
            self.connection.commit()
        
        except mysql.Error as error:
            print("Failed to update record to database rollback: {}".format(error))
            self.connection.rollback()
        

    def delete_property(self, address:str):
        self.cursor.execute(
            "DELETE description, property, property_dealer FROM description INNER JOIN property INNER JOIN property_dealer WHERE address = %s;", (address,)
        )

    def get_property_locality(self,input):
        self.cursor.execute("SELECT * from property natural join locality natural join description where locality.name=%s;",(input,))
        return(self.cursor.fetchall())
    
    def get_property_size(self,input1):
        self.cursor.execute("SELECT * from property natural join locality natural join description where property.size=%s;",(input1,))
        return(self.cursor.fetchall())
    
    def get_property_bed(self,input2):
        self.cursor.execute("SELECT * from property natural join locality natural join description where description.bedroom=%s;",(input2,))
        return(self.cursor.fetchall())
    
    def get_property_all(self):
        self.cursor.execute("SELECT * from property natural join locality natural join description")
        return(self.cursor.fetchall())
