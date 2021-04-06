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

#first query
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

# second query
def get_home_with_bedroom_rent():
    bedroom = input("Enter the minimum desired bedrooms : ")
    rent = input("Enter the maximum desired rent : ")

    cursor = db.cursor()
    query = "SELECT * FROM property NATURAL JOIN description WHERE bedroom >= %s AND rent <= %s;"
    cursor.execute(query, (bedroom, rent))

    output = cursor.fetchall()

    for i in output:
        print(i)
# get_home_with_bedroom_rent()

#third query
def get_agent_with_date_money():
    year = input("Enter year: ")

    cursor = db.cursor(prepared = True)

    query = "with dealer_sale AS(SELECT SUM(price) s,dealer FROM transaction WHERE year(date) = %s GROUP BY dealer) SELECT name FROM dealer_sale JOIN dealer WHERE dealer_sale.dealer = dealer.username AND s=(SELECT MAX(s) FROM dealer_sale);"
    cursor.execute(query, (year,))

    output = cursor.fetchall()

    for i in output:
        print(i)
#get_agent_with_date_money()

#fifth query
def get_most_expensive():
    cursor = db.cursor()

    query = "SELECT * FROM property WHERE price = (SELECT MAX(price) FROM property) OR rent = (SELECT MAX(rent) FROM property);"
    cursor.execute(query)

    output = cursor.fetchall()

    for i in output:
        print(i)
# get_most_expensive()