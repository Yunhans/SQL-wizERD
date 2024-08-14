import ast




'''

-- extract table detail from script ---

    -params: script
    -use for formatting the return records from db

'''

def extract_details(records):
    
    formatted_records = []
    for record in records:
        # convert the script from string to dict
        script = ast.literal_eval(record[1])
            
        formatted_record = {
            "id": record[0],
            "name": script.get("name"),
            "attribute": script.get("attributes"),
            "foreign_keys": script.get("foreign_keys", []),
            "location": {
                "x": record[2],
                "y": record[3]
            }
        }
        
        formatted_records.append(formatted_record)
        print(formatted_record)
        
    return formatted_records


def extract_detail(record):
    # convert the script from string to dict
    script = ast.literal_eval(record[1])
    
    formatted_record = {
        "id": record[0],
        "name": script.get("name"),
        "attribute": script.get("attributes"),
        "foreign_keys": script.get("foreign_keys", []),
        "location": {
            "x": record[2],
            "y": record[3]
        }
    }
    
    print(formatted_record)
    return formatted_record


table = [(1, "{'name': 'product', 'attributes': [{'name': 'product_id', 'type': 'INT', 'primary_key': False, 'not_null': True, 'unique': True, 'auto_increment': False, 'default': None}, {'name': 'quantity', 'type': 'INT', 'primary_key': False, 'not_null': True, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'product_type', 'type': 'CHAR(10)', 'primary_key': False, 'not_null': True, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'description', 'type': 'TEXT', 'primary_key': False, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'PRIMARY', 'type': 'KEY(product_id)', 'primary_key': False, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}], 'foreign_keys': []}", '0', '0'), (2, "{'name': 'Orders', 'attributes': [{'name': 'OrderID', 'type': 'INT', 'primary_key': True, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'CustomerID', 'type': 'INT', 'primary_key': False, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'OrderDate', 'type': 'DATE', 'primary_key': False, 'not_null': True, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'TotalAmount', 'type': 'DECIMAL(10,2)', 'primary_key': False, 'not_null': True, 'unique': False, 'auto_increment': False, 'default': None}], 'foreign_keys': [{'from': 'Orders. CustomerID ', 'references': 'Customers. CustomerID '}]}", '0', '0'), (3, "{'name': 'Customers', 'attributes': [{'name': 'CustomerID', 'type': 'INT', 'primary_key': True, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'FirstName', 'type': 'VARCHAR(255)', 'primary_key': False, 'not_null': True, 'unique': True, 'auto_increment': False, 'default': None}, {'name': 'LastName', 'type': 'VARCHAR(255)', 'primary_key': False, 'not_null': True, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'Email', 'type': 'VARCHAR(255)', 'primary_key': False, 'not_null': False, 'unique': True, 'auto_increment': False, 'default': None}, {'name': 'PhoneNumber', 'type': 'VARCHAR(20)', 'primary_key': False, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}], 'foreign_keys': []}", '0', '0'), (4, "{'name': 'Products', 'attributes': [{'name': 'ProductID', 'type': 'INT', 'primary_key': True, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'ProductName', 'type': 'VARCHAR(255)', 'primary_key': False, 'not_null': True, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'Description', 'type': 'TEXT', 'primary_key': False, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'Price', 'type': 'DECIMAL(10,2)', 'primary_key': False, 'not_null': True, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'Category', 'type': 'VARCHAR(255)', 'primary_key': False, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}], 'foreign_keys': []}", '0', '0')]
table2 = (1, "{'name': 'product', 'attributes': [{'name': 'product_id', 'type': 'INT', 'primary_key': False, 'not_null': True, 'unique': True, 'auto_increment': False, 'default': None}, {'name': 'quantity', 'type': 'INT', 'primary_key': False, 'not_null': True, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'product_type', 'type': 'CHAR(10)', 'primary_key': False, 'not_null': True, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'description', 'type': 'TEXT', 'primary_key': False, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}, {'name': 'PRIMARY', 'type': 'KEY(product_id)', 'primary_key': False, 'not_null': False, 'unique': False, 'auto_increment': False, 'default': None}], 'foreign_keys': []}", '0', '0')
extract_details(table)
print("\n")
extract_detail(table2)
