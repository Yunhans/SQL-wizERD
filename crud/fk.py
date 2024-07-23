from connect_db import connect_to_database, close_connection



'''

--- CREATE ---

'''

def new_foreign_key(from_table, ref_table, from_column, ref_column, file_id, table_id):
    
    try:
        connection = connect_to_database()
        if connection.is_connected():
            cursor = connection.cursor()
            sql_insert_query = """INSERT INTO `tbl_fk` (`from_tbl`, `ref_tbl`, `from_col`, `ref_col`, `file_id`, `table_id`) VALUES (%s, %s, %s, %s, %s, %s)"""
            params = (from_table, ref_table, from_column, ref_column, file_id, table_id)
            cursor.execute(sql_insert_query, params)
            connection.commit()
            return "Successfully added new foreign key."
    except Exception as e:
        return f"Failed to add new foreign key: {e}"
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()