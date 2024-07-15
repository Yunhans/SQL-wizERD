from router.CRUD import new_table, new_foreign_key 


'''

--table_list

'''

# insert new table
def table_list(Table_name, script, x, y, File):
    Table_name = Table_name
    script = script
    x = x
    y = y
    File = File
    
    new_table(Table_name, script, x, y, File)
    return "structed_boject: successfully added new table!"




'''

-- foreign_key

'''



# insert new foreign key
def foreign_key(From_tbl, Ref_tbl, From_col, to_col, File_id, Table_id):
    From_tbl = From_tbl
    Ref_tbl = Ref_tbl
    From_col = From_col
    to_col = to_col
    File_id = File_id
    Table_id = Table_id
    
    new_foreign_key(From_tbl, Ref_tbl, From_col, to_col, File_id, Table_id)
    return "structed_object: successfully added new foreign key!"
