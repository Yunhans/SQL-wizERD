from connect_db import connect_to_database



'''

--- CREATE ---

'''

def new_file(file_name, user_id):
    
    try:
        connection = connect_to_database()
        if connection.is_connected():
            cursor = connection.cursor()
            sql_insert_query = """ INSERT INTO `tbl_file` (`file_name`, `user_id`) VALUES (%s, %s) """
            cursor.execute(sql_insert_query, (file_name, user_id))
            connection.commit()
            return cursor.lastrowid
    except Exception as e:
        return f"failed to add new file: {e}"
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
        
        
'''

--- READ ---

'''

def get_all_files(user_id):
    
    try:
        connection = connect_to_database()
        if connection.is_connected():
            cursor = connection.cursor()
            sql_search_query = """ SELECT `file_id`, `file_name` FROM `tbl_file` WHERE `user_id` = %s ORDER BY 1 DESC """
            cursor.execute(sql_search_query, (user_id,))
            records = cursor.fetchall()
            
            if records:
                return records
            else:
                return None
            # example records: [(1, 'file1'), (2, 'file2'), (3, 'file3')]
        
    except Exception as e:
        return f"Failed to retrieve files: {e}"
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


'''

--- UPDATE ---


'''

def update_file_name(file_id, file_name):
    
    try:
        connection = connect_to_database()
        if connection.is_connected():
            cursor = connection.cursor()
            sql_update_query = """ UPDATE `tbl_file` SET `file_name` = %s WHERE `file_id` = %s """
            cursor.execute(sql_update_query, (file_name, file_id))
            connection.commit()
            return 1
    except Exception as e:
        return f"Failed to update file name: {e}"
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            

'''

--- DELETE ---

'''

def delete_file(file_id):
    
    try:
        connection = connect_to_database()
        if connection.is_connected():
            cursor = connection.cursor()
            sql_delete_query = """ DELETE FROM `tbl_file` WHERE `file_id` = %s """
            cursor.execute(sql_delete_query, (file_id,))
            connection.commit()
            return 1
    except Exception as e:
        return f"Failed to delete file: {e}"
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()