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
def new_foreign_key(from_table, ref_table, from_column, ref_column, file_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO `foreign_key` ( `From_tbl`,`Ref_tbl`,`From_col`, `To_col`, `file_id`) VALUES (%s,%s,%s,%s,%s) """
        cursor.execute(sql_insert_query, (from_table, ref_table, from_column, ref_column, file_id))
        connection.commit()
        print("Successfully added new foreign key!")




#-------------------------修改功能---------------------------------#


#更新table
def update_table(x, y, table_name, script, table_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_update_query = """ UPDATE `table_list` SET `x` = %s, `y` = %s,`table_name`= %s, `script` = %s WHERE `table_id` = %s"""
        cursor.execute(sql_update_query, (x, y, table_name, script,table_id))
        connection.commit()
        print("successfully updated table!")



#更新foreign_key
def update_foreign_key(from_table, ref_table, from_column, ref_column, FK_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_update_query = """ UPDATE `foreign_key` SET `From_tbl` = %s, `Ref_tbl` = %s,`From_col` = %s, `To_col` = %s WHERE `FK_id` = %s"""
        cursor.execute(sql_update_query, (from_table, ref_table, from_column, ref_column, FK_id))
        connection.commit()
        print("successfully updated foreign_key !")
update_foreign_key(7,2,"測試","冊冊冊",2)


#更新file
def update_file(file_name, file_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_update_query = """ UPDATE `files` SET `File_name` = %s WHERE `file_id` = %s"""
        cursor.execute(sql_update_query, (file_name, file_id))
        connection.commit()
        print("successfully updated file!")




#-------------------------查詢功能---------------------------------#

#查詢table
def search_table(table_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_search_query = """ SELECT * FROM `table_list` WHERE `table_id` = %s"""
        cursor.execute(sql_search_query, (table_id,))
        print("successfully searched table!")
        records = cursor.fetchall()
        for row in records:
            print(row)

#查詢file
def search_file(file_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_search_query = """ SELECT * FROM `files` WHERE `file_id` = %s"""
        cursor.execute(sql_search_query, (file_id,))
        print("successfully searched file!")
        records = cursor.fetchall()
        for row in records:
            print(row)

#-------------------------刪除功能---------------------------------#





