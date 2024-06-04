import mysql.connector



'''
更新script
def update_script(name, mail):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO `user` (`Name`, `Mail`) VALUES (%s, %s) """
        cursor.execute(sql_insert_query, (name, mail))
        connection.commit()
        print("資料已成功插入")
'''

'''
建立新script
def new_script(name, mail):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = 
        cursor.execute(sql_insert_query, (name, mail))
        connection.commit()
        print("資料已成功插入")
'''


'''
建立新使用者
def new_user(name, mail):
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO `user` (`Name`, `Mail`) VALUES (%s, %s) """
        cursor.execute(sql_insert_query, (name, mail))
        connection.commit()
        print("資料已成功插入")
'''

#新增使用者
def new_user():
    connection = connect_to_database()
    if connection.is_connected():
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO `user` (`Name`, `Mail`) VALUES ('John', 'john@example.com') """
        cursor.execute(sql_insert_query)
        connection.commit()
        print("Successfully inserted")



#連接到資料庫
def connect_to_database():
    connection = mysql.connector.connect(
        host="localhost",  # 通常為localhost
        user="admin",  # 輸入您的phpMyAdmin的使用者名稱
        password="123",  # 輸入您的phpMyAdmin的密碼
        database="graduate_project"  # 輸入您想要連接的資料庫名稱
    )

    if connection.is_connected():
        print("Successfully connected")
    else:
        print("Failed")
    return connection



