import mysql.connector


def create_aline_sql_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='uftcapstone-db.c1ddjzxizuua.us-east-1.rds.amazonaws.com',
            user='uftcapstone',
            passwd='!A&8vYOKSUO&X9Zt',
            database='alinedb'
        )
    except:
        print("No connection")

    return connection

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except:
        print("Could not read")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except:
        print("Query unsuccessful")