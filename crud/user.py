from connect_db import connect_to_database, close_connection



'''

--- CREATE ---

'''

def new_user(mail):
    
    try:
        connection = connect_to_database()
        if connection.is_connected():
            cursor = connection.cursor()
            sql_insert_query = """ INSERT INTO `tbl_user` ( `mail`) VALUES (%s) """
            cursor.execute(sql_insert_query, (mail,))
            connection.commit()
            user_id = cursor.lastrowid
            print(user_id)
            return {"status_code": 200, "message": "Successfully added new user!", "data": user_id}
    except Exception as e:
        return {"status_code": 500, "message": f"Failed to add new user: {e}"}
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


'''

--- READ ---

'''

def search_user(email):
    
    try:
        connection = connect_to_database()
        if connection.is_connected():
            cursor = connection.cursor()
            sql_search_query = """ SELECT * FROM `tbl_user` WHERE `mail` = %s"""
            cursor.execute(sql_search_query, (email,))
            records = cursor.fetchone()
            if records:
                return {"status_code": 200, "message": "Successfully searched user!", "data": records}
            else:
                return {"status_code": 404, "message": "User not found."}
    except Exception as e:
        return {"status_code": 500, "message": f"Failed to search user: {e}"}
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()