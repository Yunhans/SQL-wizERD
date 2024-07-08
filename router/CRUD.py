import mysql.connector

from connect_db import connect_to_database, close_connection




#-------------------------新增功能---------------------------------#

#建立新table
def new_table (Table_name, script, file_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO `table_list` (`x`, `y`,`Table_name`,`script`,`File`) VALUES (0, 0, %s, %s,%s)"""
        cursor.execute(sql_insert_query, (Table_name, script, file_id))
        connection.commit()
        print("successfully added new table!")

#建立新使用者
def new_user(mail):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO `users` ( `Mail`) VALUES (%s) """
        cursor.execute(sql_insert_query, (mail,))
        connection.commit()
        print("Successfully added new user!")

#建立新檔案
def new_file(file_name, user_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO `files` ( `File_name`,`User_id`) VALUES (%s,%s) """
        cursor.execute(sql_insert_query, (file_name, user_id))
        connection.commit()
        print("Successfully added new file!")

#建立新外鍵
def new_foreign_key(from_table, ref_table, from_column, ref_column, table_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO `foreign_key` ( `From_tbl`,`Ref_tbl`,`From_col`, `To_col`, `table_id`) VALUES (%s,%s,%s,%s,%s) """
        cursor.execute(sql_insert_query, (from_table, ref_table, from_column, ref_column, table_id))
        connection.commit()
        print("Successfully added new foreign key!")

new_user("123777@gmail.com")


#-------------------------修改功能---------------------------------#

'''
更新table
def update_table(x, y, script,t_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = """ UPDATE `Table` SET `x` = %s, `y` = %s,`script` = %s WHERE `t_id` = %s"""
        cursor.execute(sql_update_query, (x, y, script,t_id))
        connection.commit()
        print("successfully updated table!")
'''


#-------------------------刪除功能---------------------------------#





