import re


from crud.table import get_specific_table_id, get_tables_position
from schema.structed_object import add_table, add_fk, alter_table


# The extracted information
# extracted_info = [
#     '[product|<product_id> INT PRIMARY KEY UNIQUE|<quantity> INT NOT NULL|<product_type> CHAR ( 10 )|<description> TEXT];',
#     '[orders|<order_id> INT PRIMARY KEY|<product_id> INT|<order_date> DATE|<FOREIGN> KEY ( product_id ) REFERENCES product ( product_id )];'
# ]

# extracted_info2 = [
#     '[product|<product_id> INT PRIMARY KEY UNIQUE NOT NULL|<quantity> INT NOT NULL|<product_type> CHAR ( 10 ) NOT NULL|<description> TEXT];', 
#     '[orders|<order_id> INT PRIMARY KEY|<product_id> INT|<order_date> DATE|<FOREIGN> KEY ( product_id ) REFERENCES product ( product_id )];'
# ]

KEY_WORDS = ["PRIMARY KEY", "UNIQUE", "NOT NULL", "AUTO_INCREMENT"]


def middle_parse_json(file_id, info):
    tables = []
    file_id = file_id
    
    for table in info:
        table_dict = {"name": "", "attributes": [], "foreign_keys": []}
        # aplit table definition into parts
        parts = table.strip("[];").split("|")
        # table name
        table_dict["name"] = parts[0]
        
        for part in parts[1:]:
            
            details = re.search(r"<(.+?)>\s*(\w+)\s*(.*)", part)
            
            # foreign key
            if details.group(1) == "FOREIGN":
                
                fk_details = re.search(r"\((.+?)\) REFERENCES (.+?) \((.+?)\)", details.group(3))
                if fk_details:
                    local_field, referenced_table, referenced_field = fk_details.groups()
                    fk_dict = {
                        "from": f"{table_dict['name']}.{local_field.strip()}",
                        "references": f"{referenced_table}.{referenced_field.strip()}"
                    }
                    table_dict["foreign_keys"].append(fk_dict)
            
            # attribute    
            else:
                attr_dict = {
                    "name": None,
                    "type": None,
                    "primary_key": False,
                    "not_null": False,
                    "unique": False,
                    "auto_increment": False,
                    "default": None
                }
                
                # extract attribute details
                attr_details = re.search(r"<(.+?)>\s*(\w+)\s*(.*)", part)
                if attr_details:
                    attr_name, attr_type, constraints = attr_details.groups()
                    attr_dict["name"] = attr_name
                    attr_dict["type"] = attr_type
                    
                    # check for constraints
                    if "PRIMARY KEY" in constraints:
                        attr_dict["primary_key"] = True
                        constraints = constraints.replace("PRIMARY KEY", "")
                        #attr_dict["not_null"] = True  # Primary key implies not null
                    if "UNIQUE" in constraints:
                        attr_dict["unique"] = True
                        constraints = constraints.replace("UNIQUE", "")
                    if "NOT NULL" in constraints:
                        attr_dict["not_null"] = True
                        constraints = constraints.replace("NOT NULL", "")
                    if "AUTO_INCREMENT" in constraints:
                        attr_dict["auto_increment"] = True
                        constraints = constraints.replace("AUTO_INCREMENT", "")
                    if "DEFAULT" in constraints:
                    # Updated regex to handle words or quoted strings
                        default_value = re.search(r"DEFAULT\s*(\'.+?\'|\".+?\"|\w+)", constraints)
                        if default_value:
                            # Extract the matched default value
                            attr_dict["default"] = default_value.group(1)
                            # Remove the matched default value expression from the constraints string
                            constraints = constraints.replace(default_value.group(0), "")
                    
                    # remove all space and add the remaining constraints behind the attribute type
                    attr_dict["type"] += constraints.replace(" ", "") 
                    
                    table_dict["attributes"].append(attr_dict)
        
             
        _Table_name = table_dict["name"]
        _Script = str(table_dict)
        foreign_keys = table_dict.get("foreign_keys", [])
        
        # search specific table and return id
        table_id = get_specific_table_id(file_id, _Table_name)
        
        # table don't exist
        if not table_id:
            x, y = get_tables_position(file_id)
            
            if x == None or y == None:
                x, y = 0, 0  
            
            # add new table
            add_table(_Table_name, _Script, x, y, file_id)
            
            # if nothing in foreign key[]
            if foreign_keys:
                
                for fk in table_dict["foreign_keys"]:
                    _From_tbl = fk["from"].split(".")[0]
                    _Ref_tbl = fk["references"].split(".")[0]
                    _From_col = fk["from"].split(".")[1]
                    _To_col = fk["references"].split(".")[1]

                    add_fk(_From_tbl, _Ref_tbl, _From_col, _To_col, file_id, table_id)
            else:  
                print("No foreign key in this table")
                
        # table already existed
        else:
            table_id = table_id[0]
            alter_table(table_id, _Table_name, _Script)
            
        
        tables.append(table_dict)
        
        # if no error, return 1 else 0
    return 1
    
    #return tables

# Parsing the extracted information
# parsed_tables = parse_info(extracted_info2)











# s = "( 10 ) NOT NULL PRIMARY KEY UNIQUE"
# keyword = ["PRIMARY KEY", "UNIQUE", "NOT NULL"]

# for k in keyword:
#     s = s.replace(k, "")
    

# print(s.replace(" ", ""))




# test1
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

# test2
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

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL (10, 2) NOT NULL,
    Category VARCHAR(255)
);

CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL (10, 2) NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(255) NOT NULL UNIQUE,
    Description TEXT
);

CREATE TABLE Shippers (
    ShipperID INT PRIMARY KEY,
    ShipperName VARCHAR(255) NOT NULL UNIQUE,
    Phone VARCHAR(20)
);

CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY,
    OrderID INT,
    PaymentDate DATE NOT NULL,
    Amount DECIMAL (10, 2) NOT NULL,
    PaymentMethod VARCHAR(50) NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);
'''