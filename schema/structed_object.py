from crud.table import new_table, update_table
from crud.fk import new_foreign_key 


'''

--tbl_table

'''

# insert new table
def add_table(Table_name, script, x, y, File):
    Table_name = Table_name
    script = script
    x = x
    y = y
    File = File
    
    new_table(Table_name, script, x, y, File)
    return "structed_boject: successfully added new table!"



def alter_table(Table_id, Table_name, script):
    Table_id = Table_id
    Table_name = Table_name
    script = script
    
    update_table(Table_id, Table_name, script)
    return "structed_boject: successfully update existed table!"


'''

-- tbl_fk

'''



# insert new foreign key
def add_fk(From_tbl, Ref_tbl, From_col, to_col, File_id, Table_id):
    From_tbl = From_tbl
    Ref_tbl = Ref_tbl
    From_col = From_col
    to_col = to_col
    File_id = File_id
    Table_id = Table_id
    
    new_foreign_key(From_tbl, Ref_tbl, From_col, to_col, File_id, Table_id)
    return "structed_object: successfully added new foreign key!"
