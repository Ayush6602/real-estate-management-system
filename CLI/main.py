import mysql.connector as mysql
from mysql.connector.cursor import MySQLCursor

db = mysql.connect(
    host="remotemysql.com",
    user="AMLZ6ZziDM",
    passwd="UQ5ebtcX8m",
    database="AMLZ6ZziDM"
)


def print_output(output: list):
    for i in output:
        print(i)


def execute_query(query: str) -> list:
    cursor: MySQLCursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def get_address_with_rent_between(min_rent: int, max_rent: int) -> list:
    cursor = db.cursor(prepared=True)
    query = "SELECT address FROM property WHERE rent BETWEEN %s AND %s;"
    cursor.execute(query, (min_rent, max_rent))
    return cursor.fetchall()


def get_home_with_bedroom_rent(n_bedrooms: int, rent: int) -> list:
    cursor = db.cursor()
    query = "select contact_no, dl.name from dealer dl, property_dealer prp_dl, property prp, description des, locality loc where dl.username = prp_dl.d_username and prp.id = prp_dl.p_id and prp.id = des.id and prp.locality_id = loc.id and bedroom >= %s and rent < %s and loc.name = 'G.S. Road';"
    cursor.execute(query, (n_bedrooms, rent))
    return cursor.fetchall()


def get_agent_with_max_sale_of_year(year: int) -> list:
    cursor = db.cursor(prepared=True)
    query = "with dealer_sale AS(SELECT SUM(price) s,dealer FROM transaction WHERE year(date) = %s GROUP BY dealer) SELECT name FROM dealer_sale JOIN dealer WHERE dealer_sale.dealer = dealer.username AND s=(SELECT MAX(s) FROM dealer_sale);"
    cursor.execute(query, (year))
    return cursor.fetchall()


def get_most_expensive() -> list:
    cursor = db.cursor()
    query = "SELECT * FROM property WHERE price = (SELECT MAX(price) FROM property) OR rent = (SELECT MAX(rent) FROM property);"
    cursor.execute(query)
    return cursor.fetchall()


def main() -> None:
    while True:
        choice = input('Menu\n'
            + '1. Homes with rent range\n'
            + '2. Homes with no of bedrooms and rent\n'
            + '3. Agent with max sale of year\n'
            + '5. ')


if __name__ == '__main__':
    main()
