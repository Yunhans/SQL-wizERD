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
        
    return formatted_records


def extract_detail(record):
    # convert the script from string to dict
    script = ast.literal_eval(record[2])
    
    formatted_record = {
        "id": record[0],
        "name": script.get("name"),
        "attribute": script.get("attributes"),
        "foreign_keys": script.get("foreign_keys", []),
        "location": {
            "x": record[3],
            "y": record[4]
        }
    }
    
    return formatted_record


def reverse_info(name, attributes, foreign_keys):
    
    
    # Construct the dictionary
    result = {
        'name': name,
        'attributes': attributes,
        'foreign_keys': foreign_keys
    }
    
    return result

# name = "product"
# attributes = [
#     {
#         "name": "product_id",
#         "type": "INT",
#         "primary_key": False,
#         "not_null": True,
#         "unique": True,
#         "auto_increment": False,
#         "default": None
#     },
#     {
#         "name": "quantity",
#         "type": "INT",
#         "primary_key": False,
#         "not_null": True,
#         "unique": False,
#         "auto_increment": False,
#         "default": None
#     },
#     {
#         "name": "product_type",
#         "type": "CHAR(10)",
#         "primary_key": False,
#         "not_null": True,
#         "unique": False,
#         "auto_increment": False,
#         "default": None
#     },
#     {
#         "name": "description",
#         "type": "TEXT",
#         "primary_key": False,
#         "not_null": False,
#         "unique": False,
#         "auto_increment": False,
#         "default": None
#     },
#     {
#         "name": "PRIMARY",
#         "type": "KEY(product_id)",
#         "primary_key": False,
#         "not_null": False,
#         "unique": False,
#         "auto_increment": False,
#         "default": None
#     }
# ]
# foreign_keys = []

