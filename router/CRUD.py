import mysql.connector

from .connect_db import connect_to_database, close_connection




#-------------------------新增功能---------------------------------#

#建立新table
def new_table (Table_name, script, x, y, file_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO `table_list` (`Table_name`,`Script`, `x`, `y`, `File`) VALUES (%s, %s, %s, %s,%s)"""
        cursor.execute(sql_insert_query, (Table_name, script, x, y, file_id))
        connection.commit()
        print("db: Successfully added new table!")
    
        

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
def new_foreign_key(from_table, ref_table, from_column, ref_column, file_id, table_id):
    connection = connect_to_database()
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            sql_insert_query = """INSERT INTO `foreign_key` (`From_tbl`, `Ref_tbl`, `From_col`, `To_col`, `File_id`, `table_id`) VALUES (%s, %s, %s, %s, %s, %s)"""
            params = (from_table, ref_table, from_column, ref_column, file_id, table_id)
            print(params)
            cursor.execute(sql_insert_query, params)
            connection.commit()
            print("Successfully added new foreign key!")
    except Exception as e:
        print(f"Failed to add new foreign key: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()




#-------------------------修改功能---------------------------------#


#更新table
def update_table(x, y, table_name, script, File):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_update_query = """ UPDATE `table_list` SET `x` = %s, `y` = %s,`table_name`= %s, `Script` = %s WHERE `File` = %s"""
        cursor.execute(sql_update_query, (x, y, table_name, script,File))
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
#update_foreign_key(7,2,"測試","冊冊冊",2)


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
def search_table(File, Table_id=None):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()       
        
        if Table_id is None:
            sql_search_query = """ SELECT * FROM `table_list` WHERE `File` = %s"""
            cursor.execute(sql_search_query, (File,))
       
        else:
            sql_search_query = """ SELECT * FROM `table_list` WHERE `File` = %s AND `Table_id` = %s"""
            cursor.execute(sql_search_query, (File, Table_id,))
        
        print("successfully searched table!")
        records = cursor.fetchall()
        for row in records:
            print(row)
        return records
    
# search specific table_id for create foreign key
def search_specific_table(table_name):
    connection = connect_to_database()
    cursor = connection.cursor()
    sql_search_query = """ SELECT `Table_id` FROM `table_list` WHERE `Table_name` = %s"""
    cursor.execute(sql_search_query, (table_name,))
    
    record = cursor.fetchone()
    
    return record
    




#查詢file
def search_file(user_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_search_query = """ SELECT `File_id`, `File_name` FROM `files` WHERE `User_id` = %s"""
        cursor.execute(sql_search_query, (user_id,))
        print("successfully searched file!")
        records = cursor.fetchall()
        
        
        
        return records
        
            
# search_user
def search_user(email):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_search_query = """ SELECT * FROM `users` WHERE `Mail` = %s"""
        cursor.execute(sql_search_query, (email,))
        print("successfully searched user!")
        records = cursor.fetchall()
        print("user_match:", records)
        
        return records

#-------------------------刪除功能---------------------------------#



#-------------------------Get all功能---------------------------------#

#獲取同一file內所有table與外來建
def get_all_tables(file_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_search_query = """ 
                        SELECT * FROM `table_list` , `FK_id` 
                        JOIN foreign_key ON table_list.File = foreign_key.File_id
                        WHERE `File` = %s"""
        cursor.execute(sql_search_query, (file_id,))
        records = cursor.fetchall()
        return records

#獲取同一user所有file
def get_all_files(user_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_search_query = """ SELECT * FROM `files` WHERE `User_id` = %s"""
        cursor.execute(sql_search_query, (user_id,))
        records = cursor.fetchall()
        return records
