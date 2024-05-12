import re

def extract_table_info(sql_script):
    """
    from CREATE TABLE statement, extract table information and convert it to key-value format.
    
    key value pattern:
        {table: {attribute: {data_type, constraints}}}
    """

    table_name_match = re.search(r"(?i)CREATE TABLE\s+(\w+)\s*\(", sql_script)
    if not table_name_match:
        return {}
    table_name = table_name_match.group(1)

    # access the attributes part of the sql script
    attributes_str = sql_script[table_name_match.end():]
    # using regex to extract attributes
    attribute_pattern = r"\s*(\w+)\s+([\w\(\)]+(?:\s*\([\d,]+\))?)(.*?)(?:,|\))"  # 匹配属性，并以逗号结尾
    attributes = re.findall(attribute_pattern, attributes_str)

    table_info = {}
    for column_name, data_type, constraints_str in attributes:
        constraints = [c.strip() for c in constraints_str.split() if c.strip()]
        table_info[column_name] = {"data_type": data_type, "constraints": " ".join(constraints)}

    return {table_name: table_info}


# if multiple create table
def extract_multiple_table_info(sql):
    table_infos = {}
    for statement in sql.split(";"):
        statement = statement.strip()
        if statement.startswith("create table"):
            table_infos.update(extract_table_info(statement))
            
    return table_infos
    # return table_infos

