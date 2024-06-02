import re

def extract_multiple_table_info(sql_script):

  table_structure = {}
  tables = sql_script.split(";")

  for table in tables:
    table = table.strip()
    if not table:
      continue

    match = re.match(r"CREATE TABLE\s+(\w+)\s*\((.*)\)", table, re.DOTALL| re.IGNORECASE)
    if not match:
      print(f"Warning: Could not parse table definition: {table}")
      continue

    table_name = match.group(1)
    columns_str = match.group(2)
    columns = {}

    for column_str in columns_str.split(","):
      column_str = column_str.strip()
      if not column_str:
        continue
      parts = re.split(r"\s+", column_str)
      col_name = parts[0]
      col_data_type = parts[1]
      col_constraints = ' '.join(parts[2:])  

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
    TotalAmount DECIMAL (10, 2) NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

'''
