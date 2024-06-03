import re

def transform_sql_to_dict(sql_script):
  """
  Extracts table information from a SQL script with improved FOREIGN KEY handling.

  Args:
    sql_script: The SQL script containing CREATE TABLE statements.

  Returns:
    A dictionary representing the structure of extracted tables. 
  """

  table_structure = {}
  tables = sql_script.split(";")

  for table in tables:
    # remove leading & trailing whitespaces
    table = table.strip()
    
    # table empty --> skip
    if not table:
      continue

    # match create table --> group table name and columns
    match = re.match(r"CREATE TABLE\s+(\w+)\s*\((.*)\)", table, re.DOTALL | re.IGNORECASE)# re.DOTALL --> . matches any character (including newline)
    # not match --> warning
    if not match:
      print(f"Warning: Could not parse table definition: {table}")
      continue

    table_name = match.group(1) # (\w+)
    columns_str = match.group(2) # (.*)
    columns = {}

    # Splitting column definitions, handling FOREIGN KEY separately:
    column_defs = re.split(r',\s*(?![^()]*\))', columns_str) # [^()]* --> not match paratheses

    for column_str in column_defs:
      column_str = column_str.strip()
      if not column_str:
        continue
      
      # Split into max 3 parts: name, data type, constraints
      parts = re.split(r"\s+", column_str, 2)  
      col_name = parts[0]
      col_data_type = parts[1]
      col_constraints = parts[2] if len(parts) > 2 else ''

      constraints = {}
      if 'PRIMARY KEY' in col_constraints:
        constraints['constraint'] = 'PRIMARY KEY'
      elif 'FOREIGN KEY' in col_constraints:
        constraints['constraint'] = 'FOREIGN KEY'
        match = re.search(r'REFERENCES\s+(\w+)\((\w+)\)', col_constraints)
        if match:
          constraints['references'] = f"{match.group(1)}({match.group(2)})" 
      else:
        constraints['constraint'] = col_constraints.strip() 

      columns[col_name] = {
          'data_type': col_data_type,
          **constraints 
      }

    table_structure[table_name] = columns

  return table_structure


# test
'''

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(255) NOT NULL UNIQUE,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE,
    PhoneNumber VARCHAR(20)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE NOT NULL,
    TotalAmount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

'''
