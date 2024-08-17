import ast



'''

--- json format translation to mysql script ---

'''


def generate_sql_script(tables_data):
    script = ""
    
    for table_data in tables_data:
        table_str = table_data[1]
        
        # convert string representation to dictionary
        table = ast.literal_eval(table_str)
        
        table_name = table['name']
        columns = []
        primary_keys = []
        foreign_keys = []
        
        for attribute in table['attributes']:
            column_def = f"  {attribute['name']} {attribute['type']}"
            if attribute['not_null']:
                column_def += " NOT NULL"
            if attribute['unique']:
                column_def += " UNIQUE"
            if attribute['auto_increment']:
                column_def += " AUTO_INCREMENT"
            if attribute['default'] is not None:
                column_def += f" DEFAULT {attribute['default']}"
            columns.append(column_def)
            
            if attribute['primary_key']:
                primary_keys.append(attribute['name'])
        
        for fk in table['foreign_keys']:
            from_column = fk['from'].split('.')[-1].strip()
            ref_table, ref_column = fk['references'].split('.')
            foreign_keys.append(f"  FOREIGN KEY ({from_column}) REFERENCES {ref_table.strip()}({ref_column.strip()})")
        
        
        # generate to sql script
        script += f"CREATE TABLE {table_name} (\n"
        script += ",\n".join(columns)
        
        if primary_keys:
            script += f",\n  PRIMARY KEY ({', '.join(primary_keys)})"
        
        if foreign_keys:
            script += ",\n" + ",\n".join(foreign_keys)
        
        script += "\n);\n\n"
    
    return script

# Example usage
# tables_data = [
#     (5, "{'name': 'Customers', 'attributes': [{'name': 'CustomerID', 'type': 'INT', 'primary_key': True, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'FirstName', 'type': 'VARCHAR(255)', 'primary_key': False, 'not_null': True, 'unique': True, 'auto_increment': False, 'default': None}, {'name': 'LastName', 'type': 'VARCHAR(255)', 'primary_key': False, 'not_null': True, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'Email', 'type': 'VARCHAR(255)', 'primary_key': False, 'not_null': False, 'unique': True, 'auto_increment': False, 'default': None}, {'name': 'PhoneNumber', 'type': 'VARCHAR(20)', 'primary_key': False, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}], 'foreign_keys': []}", 0.0, 0.0),
#     (6, "{'name': 'Orders', 'attributes': [{'name': 'OrderID', 'type': 'INT', 'primary_key': True, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'CustomerID', 'type': 'INT', 'primary_key': False, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'OrderDate', 'type': 'DATE', 'primary_key': False, 'not_null': True, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'TotalAmount', 'type': 'DECIMAL(10,2)', 'primary_key': False, 'not_null': True, 'unique': False, 'auto_increment': False, 'default': None}], 'foreign_keys': [{'from': 'Orders.CustomerID', 'references': 'Customers.CustomerID'}]}", 400.0, 0.0)
# ]

# sql_script = generate_sql_script(tables_data)
# print(sql_script)