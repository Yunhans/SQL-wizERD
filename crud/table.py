from connect_db import connect_to_database, close_connection



'''

--- CREATE---   

'''

def new_table (table_name, script, x, y, file_id):
    
    try:
        connection = connect_to_database()
        if connection.is_connected():
            cursor = connection.cursor()
            sql_insert_query = """ INSERT INTO `tbl_table` (`table_name`,`script`, `x`, `y`, `file_id`) VALUES (%s, %s, %s, %s,%s)"""
            cursor.execute(sql_insert_query, (table_name, script, x, y, file_id))
            connection.commit()
            return {"table_id": cursor.lastrowid}
    except Exception as e:
        return f"Failed to add new table: {e}"
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
        
        

'''

--- READ ---   

'''

# get ALL tables
def get_all_tables(file_id):
    
    try:
        connection = connect_to_database()
        if connection.is_connected():
            cursor = connection.cursor()
            sql_search_query = """
                    SELECT
                      `table_id`,
                      `script`,
                      `x`,
                      `y`
                    FROM 
                      `tbl_table`
                    WHERE 
                      `file_id` = %s
                    """
            cursor.execute(sql_search_query, (file_id,))
            records = cursor.fetchall()
            return records

    except Exception as e:
        return f"Failed to retrieve tables: {e}"
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
      
 

# get specific table (check)
def get_specific_table_id(file_id, table_name):
    connection = None
    try:
        connection = connect_to_database()
        if connection.is_connected():
            cursor = connection.cursor()
            sql_search_query = """ SELECT `table_id` FROM `tbl_table` WHERE `file_id` = %s AND `table_name` = %s"""
            cursor.execute(sql_search_query, (file_id, table_name,))
            
            record = cursor.fetchone()
            return record
            
    except Exception as e:
        return f"Failed to retrieve table: {e}"
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# get specific table (for update)
def get_table(table_id):
    try:
        connection = connect_to_database()
        if connection.is_connected():
            cursor = connection.cursor()
            sql_search_query = """ SELECT `table_id`,`table_name`, `script`, `x`, `y` FROM `tbl_table` WHERE `table_id` = %s"""
            cursor.execute(sql_search_query, (table_id,))
            record = cursor.fetchone()
            return record
    except Exception as error:
        return f"Failed to retrieve table: {error}"
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            
            
            
# get table position
def get_tables_position(file_id):
    try:
        connection = connect_to_database()
        if connection.is_connected():
            cursor = connection.cursor()
            sql_search_query = """ SELECT MAX(`x`) + 400, ROUND(AVG(`y`)) FROM `tbl_table` WHERE `file_id` = %s"""
            cursor.execute(sql_search_query, (file_id,))
            record = cursor.fetchone()
            return record
    except Exception as error:
        return f"Failed to retrieve table position: {error}"
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


'''

--- UPDATE ---   

'''

# update table from writing script
def update_table(table_id, table_name, script):
    
    try:
        connection = connect_to_database()
        if connection.is_connected():
            cursor = connection.cursor()
            sql_update_query = """ UPDATE `tbl_table` SET `table_name` = %s, `script` = %s WHERE `table_id` = %s"""
            cursor.execute(sql_update_query, (table_name, script, table_id,))
            connection.commit()
            return 1
    except Exception as error:
        return f"Failed to update table: {error}"
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            

# update table from moving position (erd)
def update_table_position(table_id, x, y):
    try:
        connection = connect_to_database()
        if connection.is_connected():
            cursor = connection.cursor()
            sql_update_query = """ UPDATE `tbl_table` SET `x` = %s, `y` = %s WHERE `table_id` = %s"""
            cursor.execute(sql_update_query, (x, y, table_id,))
            connection.commit()
            return 1
    except Exception as error:
        return f"Failed to update table position: {error}"
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            

# update table from changing table info (erd)
def update_table_info(table_id, table_name, script):
    try:
        connection = connect_to_database()
        if connection.is_connected():
            cursor = connection.cursor()
            sql_update_query = """ UPDATE `tbl_table` SET `table_name` = %s, `script` = %s WHERE `table_id` = %s"""
            cursor.execute(sql_update_query, (table_name, script, table_id,))
            connection.commit()
            return 1
    except Exception as error:
        return f"Failed to update table info: {error}"
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            
 
            
            
'''

--- DELETE ---   

'''

def delete_table(table_id):
    try:
        connection = connect_to_database()
        if connection.is_connected():
            cursor = connection.cursor()
            sql_delete_query = """ DELETE FROM `tbl_table` WHERE `table_id` = %s"""
            cursor.execute(sql_delete_query, (table_id,))
            connection.commit()
            return 1
    except Exception as error:
        return f"Failed to delete table: {error}"
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            

