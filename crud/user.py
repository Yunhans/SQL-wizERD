from connect_db import connect_to_database, close_connection



'''

--- CREATE ---

'''

def new_user(mail):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO `tbl_user` ( `mail`) VALUES (%s) """
        cursor.execute(sql_insert_query, (mail,))
        connection.commit()
        print("Successfully added new user!")



'''

--- READ ---

'''

def search_user(email):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_search_query = """ SELECT * FROM `tbl_user` WHERE `mail` = %s"""
        cursor.execute(sql_search_query, (email,))
        print("successfully searched user!")
        records = cursor.fetchall()
        print("user_match:", records)
        
        return records