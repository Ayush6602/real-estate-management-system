import mysql.connector as mysql

db = mysql.connect(
    host = "remotemysql.com",
    user = "AMLZ6ZziDM",
    passwd = "UQ5ebtcX8m",
    database = "AMLZ6ZziDM"
)

#print(db)
def executeQuery(query):
    cursor = db.cursor()
    cursor.execute(query)

    output = cursor.fetchall()

    for i in output:
        print(i)

#executeQuery("SHOW TABLES;")

def get_address_with_rent_city():
    city = input("Enter city: ")
    min_rent = input("Enter min range: ")
    max_rent = input("Enter max range: ")

    cursor = db.cursor(prepared = True)

    query = "SELECT DISTINCT address FROM transaction t INNER JOIN property p on(t.p_id = p.id) INNER JOIN locality_property lp ON(lp.p_id = p.id) INNER JOIN locality l ON(lp.l_id = l_id) WHERE (t.rent BETWEEN %s AND %s) AND l.locality = %s;"
    cursor.execute(query, (min_rent, max_rent, city))

    output = cursor.fetchall()

    for i in output:
        print(i)
    
#get_address_with_rent_city()