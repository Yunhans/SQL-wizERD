import mysql.connector

from connect_db import connect_to_database, close_connection




#-------------------------新增功能---------------------------------#

#建立新table ok
def new_table (table_name, script, x, y, file_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO `table_list` (`Table_name`,`Script`, `x`, `y`, `file_id`) VALUES (%s, %s, %s, %s,%s)"""
        cursor.execute(sql_insert_query, (table_name, script, x, y, file_id))
        connection.commit()
        print("db: Successfully added new table!")
    
        

#建立新使用者 ok
def new_user(mail):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO `tbl_user` ( `mail`) VALUES (%s) """
        cursor.execute(sql_insert_query, (mail,))
        connection.commit()
        print("Successfully added new user!")

#建立新檔案 ok
def new_file(file_name, user_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO `tbl_file` ( `file_name`,`user_id`) VALUES (%s,%s) """
        cursor.execute(sql_insert_query, (file_name, user_id))
        connection.commit()
        print("Successfully added new file!")

#建立新外鍵 ok
def new_foreign_key(from_table, ref_table, from_column, ref_column, file_id, table_id):
    connection = connect_to_database()
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            sql_insert_query = """INSERT INTO `tbl_fk` (`from_tbl`, `ref_tbl`, `from_col`, `ref_col`, `file_id`, `table_id`) VALUES (%s, %s, %s, %s, %s, %s)"""
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
        sql_update_query = """ UPDATE `tbl_table` SET `x` = %s, `y` = %s,`table_name`= %s, `script` = %s WHERE `file_id` = %s"""
        cursor.execute(sql_update_query, (x, y, table_name, script,File))
        connection.commit()
        print("successfully updated table!")



#更新foreign_key
def update_foreign_key(from_table, ref_table, from_column, ref_column, fk_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_update_query = """ UPDATE `tbl_fk` SET `from_tbl` = %s, `ref_tbl` = %s,`from_col` = %s, `ref_col` = %s WHERE `fk_id` = %s"""
        cursor.execute(sql_update_query, (from_table, ref_table, from_column, ref_column, fk_id))
        connection.commit()
        print("successfully updated foreign_key !")
#update_foreign_key(7,2,"測試","冊冊冊",2)


#更新file
def update_file(file_name, file_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_update_query = """ UPDATE `tbl_file` SET `file_name` = %s WHERE `file_id` = %s"""
        cursor.execute(sql_update_query, (file_name, file_id))
        connection.commit()
        print("successfully updated file!")




#-------------------------查詢功能---------------------------------#

#查詢table
def search_table(file_id, table_id=None):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()       
        
        if table_id is None:
            sql_search_query = """ SELECT * FROM `tbl_table` WHERE `file_id` = %s"""
            cursor.execute(sql_search_query, (file_id,))
       
        else:
            sql_search_query = """ SELECT * FROM `tbl_table` WHERE `file_id` = %s AND `table_id` = %s"""
            cursor.execute(sql_search_query, (file_id, table_id,))
        
        print("successfully searched table!")
        records = cursor.fetchall()
        for row in records:
            print(row)
        return records
    
# search specific table_id for create foreign key
def search_specific_table(table_name):
    connection = connect_to_database()
    cursor = connection.cursor()
    sql_search_query = """ SELECT `table_id` FROM `tbl_table` WHERE `table_name` = %s"""
    cursor.execute(sql_search_query, (table_name,))
    
    record = cursor.fetchone()
    
    return record
    




#查詢file
def search_file(user_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_search_query = """ SELECT `file_id`, `file_name` FROM `tbl_file` WHERE `user_id` = %s"""
        cursor.execute(sql_search_query, (user_id,))
        print("successfully searched file!")
        records = cursor.fetchall()
        
        
        
        return records
        
            
# search_user ok
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

#-------------------------刪除功能---------------------------------#



#-------------------------Get all功能---------------------------------#

#獲取同一file內所有table與外來建 ok
def get_all_tables(file_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_search_query = """ 
                        SELECT * FROM `tbl_table` , `fk_id` 
                        JOIN `tbl_fk` ON `tbl_table`.`file_id` = `tbl_fk`.`file_id`
                        WHERE `tbl_table`.`file_id` = %s"""
        cursor.execute(sql_search_query, (file_id,))
        records = cursor.fetchall()
        return records

#獲取同一user所有file ok
def get_all_files(user_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_search_query = """ SELECT * FROM `tbl_file` WHERE `user_id` = %s"""
        cursor.execute(sql_search_query, (user_id,))
        records = cursor.fetchall()
        return records
