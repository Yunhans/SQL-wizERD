from connect_db import connect_to_database, close_connection
from utils.extract_table_detail import extract_detail


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
            return "Successfully added new table."
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
            
            # extract detail from the records
            if records:
                records_dict = extract_detail(records)
                return records_dict
            else:
                return None
    except Exception as e:
        return f"Failed to retrieve tables: {e}"
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
      
 

# get specific table     
def get_specific_table(file_id, table_name):
    connection = None
    try:
        connection = connect_to_database()
        if connection.is_connected():
            cursor = connection.cursor()
            sql_search_query = """ SELECT `table_id` FROM `tbl_table` WHERE `file_id` = %s AND `table_name` = %s"""
            cursor.execute(sql_search_query, (file_id, table_name,))
            
            record = cursor.fetchone()
            if record:
                return record
            else:
                return None
    except Exception as e:
        return f"Failed to retrieve table: {e}"
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()




'''

--- UPDATE ---   

'''

# 
def update_table(table_id, table_name, script):
    try:
        connection = connect_to_database()
        if connection.is_connected():
            cursor = connection.cursor()
            sql_update_query = """ UPDATE `tbl_table` SET `table_name` = %s, `script` = %s WHERE `table_id` = %s"""
            cursor.execute(sql_update_query, (table_name, script, table_id,))
            connection.commit()
            return "Successfully updated table!"
    except Exception as error:
        return f"Failed to update table: {error}"
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()