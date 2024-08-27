import ast
import re



'''

--- json format translation to mysql script ---

'''

def generate_sql_script(table_script):
    script = ""
    
    # define the regex for DECIMAL
    decimal_pattern = re.compile(r"^decimal\(\d+,\d+\)$", re.IGNORECASE)
    
    for table_tuple in table_script:
        table_info = ast.literal_eval(table_tuple[0])
        
        table_name = table_info['name']
        attributes = table_info['attributes']
        foreign_keys = table_info.get('foreign_keys', [])
        
        columns = []
        primary_keys = []
        
        # count the number of primary keys(for output)
        pk_count = sum(1 for attr in attributes if attr.get('primary_key'))
        
        for attr in attributes:

            column_def = f"    {attr['name']} {attr['type']}"
            constraints = []
            
            if attr.get('primary_key'):
                primary_keys.append(attr['name'])
            
            if attr.get('not_null'):
                constraints.append("NOT NULL")
            if attr.get('unique'):
                constraints.append("UNIQUE")
            if attr.get('auto_increment'):
                constraints.append("AUTO_INCREMENT")
            if attr.get('default') is not None:
                default_value = attr['default']
                if (default_value.lower() in ["current_timestamp", "current_date"] or
                    attr['type'].lower() in ["int", "float", "boolean"] or
                    decimal_pattern.match(attr['type'].lower())):
                    constraints.append(f"DEFAULT {default_value}")
                else:
                    constraints.append(f"DEFAULT '{default_value}'")
                    
            if constraints:
                column_def += " " + " ".join(constraints)
            
            if attr.get('primary_key') and pk_count == 1:
                column_def += " PRIMARY KEY"
            
            columns.append(column_def)
        
        foreign_key_defs = []
        for fk in foreign_keys:
            from_column = fk['from'].split('.')[1]
            to_table, to_column = fk['references'].split('.')
            foreign_key_defs.append(f"    FOREIGN KEY ({from_column}) REFERENCES {to_table}({to_column})")
        
        # Generate the SQL script
        script += f"CREATE TABLE {table_name} (\n"
        script += ",\n".join(columns)
        
        # add composite primary key if there are multiple primary keys' columns
        if pk_count > 1:
            script += f",\n    PRIMARY KEY ({', '.join(primary_keys)})"
        
        if foreign_key_defs:
            script += ",\n" + ",\n".join(foreign_key_defs)
        
        script += "\n);\n\n"
    
    return script

# Test the function
# table_script = [
#     ("{'name': 'Customers', 'attributes': [{'name': 'CustomerID', 'type': 'INT', 'primary_key': True, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'FirstName', 'type': 'VARCHAR(255)', 'primary_key': False, 'not_null': True, 'unique': True, 'auto_increment': False, 'default': None}, {'name': 'LastName', 'type': 'VARCHAR(255)', 'primary_key': False, 'not_null': True, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'Email', 'type': 'VARCHAR(255)', 'primary_key': False, 'not_null': False, 'unique': True, 'auto_increment': False, 'default': None}, {'name': 'PhoneNumber', 'type': 'VARCHAR(20)', 'primary_key': False, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}], 'foreign_keys': []}",),
#     ("{'name': 'Orders', 'attributes': [{'name': 'OrderID', 'type': 'INT', 'primary_key': True, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'CustomerID', 'type': 'INT', 'primary_key': False, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'OrderDate', 'type': 'DATE', 'primary_key': False, 'not_null': True, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'TotalAmount', 'type': 'DECIMAL(10,2)', 'primary_key': False, 'not_null': True, 'unique': False, 'auto_increment': False, 'default': None}], 'foreign_keys': [{'from': 'Orders.CustomerID', 'references': 'Customers.CustomerID'}]}",)
# ]

# Example usage
# tables_data = [
#     (5, "{'name': 'Customers', 'attributes': [{'name': 'CustomerID', 'type': 'INT', 'primary_key': True, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'FirstName', 'type': 'VARCHAR(255)', 'primary_key': False, 'not_null': True, 'unique': True, 'auto_increment': False, 'default': None}, {'name': 'LastName', 'type': 'VARCHAR(255)', 'primary_key': False, 'not_null': True, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'Email', 'type': 'VARCHAR(255)', 'primary_key': False, 'not_null': False, 'unique': True, 'auto_increment': False, 'default': None}, {'name': 'PhoneNumber', 'type': 'VARCHAR(20)', 'primary_key': False, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}], 'foreign_keys': []}", 0.0, 0.0),
#     (6, "{'name': 'Orders', 'attributes': [{'name': 'OrderID', 'type': 'INT', 'primary_key': True, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'CustomerID', 'type': 'INT', 'primary_key': False, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'OrderDate', 'type': 'DATE', 'primary_key': False, 'not_null': True, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'TotalAmount', 'type': 'DECIMAL(10,2)', 'primary_key': False, 'not_null': True, 'unique': False, 'auto_increment': False, 'default': None}], 'foreign_keys': [{'from': 'Orders.CustomerID', 'references': 'Customers.CustomerID'}]}", 400.0, 0.0)
# ]

# sql_script = generate_sql_script(tables_data)
# print(sql_script)