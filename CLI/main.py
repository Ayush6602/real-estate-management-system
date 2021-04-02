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