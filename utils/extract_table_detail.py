import ast




'''

-- extract table detail from script ---

    -params: script
    -use for formatting the return records from db

'''

def extract_detail(records):
    
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