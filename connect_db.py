import mysql.connector
from mysql.connector import Error


# connect to database
def connect_to_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="hugo92523",
        database="graduated_project"
    )

    if connection.is_connected():
        print("connection success")
    else:
        print("connection failed")
    return connection


# close connection
def close_connection(connection):
    connection.close()
    print("connection closed")