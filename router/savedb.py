import mysql.connector
from starlette.requests import Request



'''
更新table
def update_script(x, y, t_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = """ UPDATE `Table` SET `x` = %s, `y` = %s WHERE `t_id` = %s"""
        cursor.execute(sql_update_query, (x, y, t_id))
        connection.commit()
        print("successfully updated table!")
'''

'''
建立新table
def new_script(x, y, u_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = 
        cursor.execute(sql_insert_query, (x, y, u_id))
        connection.commit()
        print("successfully added new table!")
'''


'''
更新script
def update_script(script, s_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = """ UPDATE `Script` SET `script` = %s WHERE `s_id` = %s"""
        cursor.execute(sql_update_query, (script, s_id))
        connection.commit()
        print("Successfully updated script!")
'''

'''
建立新script
def new_script(script):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = 
        cursor.execute(sql_insert_query, (script))
        connection.commit()
        print("Successfully added new script!")
'''


'''
建立新使用者
def new_user(name, mail):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO `user` (`Name`, `Mail`) VALUES (%s, %s) """
        cursor.execute(sql_insert_query, (name, mail))
        connection.commit()
        print("Successfully added new user!")
'''




# connect to database
def connect_to_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="boshiou",
        password="920108200387",
        database="graduated_project"
    )

    if connection.is_connected():
        print("Successfully connected")
    else:
        print("Failed")
    return connection


# close connection
def close_connection(connection):
    connection.close()
    print("Connection closed")







