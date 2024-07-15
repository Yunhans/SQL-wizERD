from connect_db import connect_to_database, close_connection



'''

--- CREATE ---

'''

def new_file(file_name, user_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO `tbl_file` ( `file_name`,`user_id`) VALUES (%s,%s) """
        cursor.execute(sql_insert_query, (file_name, user_id))
        connection.commit()
        print("Successfully added new file!")
        
        
        
        
'''

--- READ ---

'''

def get_all_files(user_id):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_search_query = """ SELECT `file_id`,`file_name` FROM `tbl_file` WHERE `user_id` = %s"""
        cursor.execute(sql_search_query, (user_id,))
        records = cursor.fetchall()
        return records
    # example records: [(1, 'file1'), (2, 'file2'), (3, 'file3')]