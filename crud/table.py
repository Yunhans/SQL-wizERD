from connect_db import connect_to_database, close_connection
from utils.extract_table_detail import extract_detail


'''

--- CREATE---   

'''

def new_table (table_name, script, x, y, file_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO `tbl_table` (`table_name`,`script`, `x`, `y`, `file_id`) VALUES (%s, %s, %s, %s,%s)"""
        cursor.execute(sql_insert_query, (table_name, script, x, y, file_id))
        connection.commit()
        print("db: Successfully added new table!")
        
        
        

'''

--- READ ---   

'''

# get ALL tables
def get_all_tables(file_id):
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
        records_dict = extract_detail(records)
        
        return records_dict
      
 

# get specific table     
def get_specific_table(file_id, table_name):
    connection = connect_to_database()
    cursor = connection.cursor()
    sql_search_query = """ SELECT `table_id` FROM `tbl_table` WHERE `file_id` = %s AND `table_name` = %s"""
    cursor.execute(sql_search_query, (file_id, table_name,))
    
    record = cursor.fetchone()
    
    return record




'''

--- UPDATE ---   

'''

# 
def update_table(table_id, table_name, script):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_update_query = """ UPDATE `tbl_table` SET `table_name` = %s, `script` = %s WHERE `table_id` = %s"""
        cursor.execute(sql_update_query, (table_name, script, table_id,))
        connection.commit()
        print("Successfully updated table!")