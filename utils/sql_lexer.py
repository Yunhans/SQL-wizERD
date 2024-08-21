import ply.lex as lex
import ply.yacc as yacc

from crud.table import get_all_tables_idname, get_specific_table_id, get_tables_position, delete_table
from schema.structed_object import add_table, alter_table

# Global variable to store tables and errors
parsed_tables = []
error_list = []


def add_error(message, lineno):
    error_msg = f"Syntax error at line {lineno}: {message}"
    if error_msg not in error_list:
        error_list.append(error_msg)

# Define tokens
tokens = (
    'CREATE', 'TABLE', 'IDENTIFIER', 'LPAREN', 'RPAREN', 'COMMA', 'SEMICOLON',
    'INT', 'VARCHAR', 'CHAR', 'TEXT', 'DATE', 'DATETIME', 'TIMESTAMP',
    'DECIMAL', 'FLOAT', 'BOOLEAN', 'BIGINT', 'SMALLINT', 'DOUBLE', 'ENUM',
    'PRIMARY', 'KEY', 'FOREIGN', 'NOT', 'NULL', 'UNIQUE', 'DEFAULT',
    'AUTO_INCREMENT', 'ON', 'DELETE', 'UPDATE', 'CASCADE', 'REFERENCES',
    'NUMBER', 'STRING', 'CURRENT_TIMESTAMP'
)


# Define keywords
keywords = {
    'create': 'CREATE',
    'table': 'TABLE',
    'int': 'INT',
    'varchar': 'VARCHAR',
    'char': 'CHAR',
    'text': 'TEXT',
    'date': 'DATE',
    'datetime': 'DATETIME',
    'timestamp': 'TIMESTAMP',
    'decimal': 'DECIMAL',
    'float': 'FLOAT',
    'boolean': 'BOOLEAN',
    'bigint': 'BIGINT',
    'smallint': 'SMALLINT',
    'double': 'DOUBLE',
    'enum': 'ENUM',
    'primary': 'PRIMARY',
    'key': 'KEY',
    'foreign': 'FOREIGN',
    'not': 'NOT',
    'null': 'NULL',
    'unique': 'UNIQUE',
    'default': 'DEFAULT',
    'auto_increment': 'AUTO_INCREMENT',
    'on': 'ON',
    'delete': 'DELETE',
    'update': 'UPDATE',
    'cascade': 'CASCADE',
    'references': 'REFERENCES',
    'current_timestamp': 'CURRENT_TIMESTAMP'
}

# Token definitions (same as before)
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_SEMICOLON = r';'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value.lower(), 'IDENTIFIER')
    return t

t_NUMBER = r'\d+'
t_STRING = r"'[^']*'"

t_ignore = ' \t\r'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    add_error(f"Illegal character '{t.value[0]}'", t.lineno)
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Grammar rules
def p_statements(p):
    '''statements : statement
                  | statements statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    'statement : CREATE TABLE IDENTIFIER LPAREN table_elements RPAREN SEMICOLON'
    table_name = p[3]
    table_elements = p[5]
    
    # Check for duplicate table names
    if any(table['name'] == table_name for table in parsed_tables):
        add_error(f"Duplicate table name: {table_name}", p.lineno(3))
    else:
        # Check for duplicate attribute names within the table
        attributes = [elem[1] for elem in table_elements if elem[0] == 'COLUMN']
        if len(attributes) != len(set(attributes)):
            add_error(f"Duplicate attribute names in table: {table_name}", p.lineno(3))
        
        # Create the current table object
        current_table = {
            'name': table_name,
            'elements': table_elements
        }
        
        # Set the current_table attribute for the parser
        p.parser.current_table = current_table
        
        # Add the table to parsed_tables
        parsed_tables.append(current_table)
    
    p[0] = ('CREATE_TABLE', table_name, table_elements)

def p_table_elements(p):
    '''table_elements : table_element
                      | table_elements COMMA table_element'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_table_element(p):
    '''table_element : column_definition
                     | table_constraint'''
    p[0] = p[1]

def p_column_definition(p):
    'column_definition : IDENTIFIER data_type column_constraints'
    p[0] = ('COLUMN', p[1], p[2], p[3])

def p_data_type(p):
    '''data_type : INT
                 | VARCHAR LPAREN NUMBER RPAREN
                 | CHAR LPAREN NUMBER RPAREN
                 | TEXT
                 | DATE
                 | DATETIME
                 | TIMESTAMP
                 | DECIMAL LPAREN NUMBER COMMA NUMBER RPAREN
                 | FLOAT
                 | BOOLEAN
                 | BIGINT
                 | SMALLINT
                 | DOUBLE
                 | ENUM LPAREN enum_values RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 5:
        p[0] = f"{p[1]}({p[3]})"
    elif len(p) == 7:
        p[0] = f"{p[1]}({p[3]},{p[5]})"

def p_enum_values(p):
    '''enum_values : STRING
                   | enum_values COMMA STRING'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]},{p[3]}"

def p_column_constraints(p):
    '''column_constraints : column_constraint
                          | column_constraints column_constraint
                          | empty'''
    if len(p) == 2:
        p[0] = [p[1]] if p[1] else []
    else:
        p[0] = p[1] + [p[2]]

def p_column_constraint(p):
    '''column_constraint : NOT NULL
                         | UNIQUE
                         | PRIMARY KEY
                         | DEFAULT default_value
                         | AUTO_INCREMENT'''
    p[0] = ' '.join(str(x) for x in p[1:])

def p_default_value(p):
    '''default_value : STRING
                     | NUMBER
                     | CURRENT_TIMESTAMP'''
    p[0] = p[1]

def p_table_constraint(p):
    '''table_constraint : PRIMARY KEY LPAREN column_list RPAREN
                        | FOREIGN KEY LPAREN column_list RPAREN REFERENCES IDENTIFIER LPAREN column_list RPAREN
                        | FOREIGN KEY LPAREN column_list RPAREN REFERENCES IDENTIFIER LPAREN column_list RPAREN ON DELETE CASCADE
                        | FOREIGN KEY LPAREN column_list RPAREN REFERENCES IDENTIFIER LPAREN column_list RPAREN ON UPDATE CASCADE'''
    if p[1] == 'PRIMARY':
        p[0] = ('TABLE_CONSTRAINT', 'PRIMARY_KEY', p[4])
    elif p[1] == 'FOREIGN':
        referencing_columns = p[4]
        referenced_table = p[7]
        referenced_columns = p[9]
        
        # Check if referencing columns exist in the current table
        current_table_columns = set(col[1] for col in p.parser.current_table['elements'] if col[0] == 'COLUMN')
        non_existent_columns = set(referencing_columns) - current_table_columns
        if non_existent_columns:
            add_error(f"Foreign key columns {', '.join(non_existent_columns)} do not exist in the current table", p.lineno(3))
        
        # Check if referenced table exists
        referenced_table_obj = next((table for table in parsed_tables if table['name'] == referenced_table), None)
        if not referenced_table_obj:
            add_error(f"Referenced table does not exist: {referenced_table}", p.lineno(7))
        else:
            # Check if referenced columns exist in the referenced table
            table_columns = set(col[1] for col in referenced_table_obj['elements'] if col[0] == 'COLUMN')
            if not set(referenced_columns).issubset(table_columns):
                non_existent_columns = set(referenced_columns) - table_columns
                add_error(f"Referenced columns {', '.join(non_existent_columns)} do not exist in table {referenced_table}", p.lineno(7))
            
            # Check if referenced columns are the primary key of the referenced table
            primary_key_columns = next((constraint[2] for constraint in referenced_table_obj['elements'] 
                                        if constraint[0] == 'TABLE_CONSTRAINT' and constraint[1] == 'PRIMARY_KEY'), None)
            if primary_key_columns is None:
                primary_key_columns = [col[1] for col in referenced_table_obj['elements'] 
                                       if col[0] == 'COLUMN' and any('PRIMARY KEY' in constraint for constraint in col[3])]
            
            if set(referenced_columns) != set(primary_key_columns):
                add_error(f"Referenced columns {', '.join(referenced_columns)} must be the primary key of table {referenced_table}", p.lineno(7))
        
        if len(p) == 11:
            p[0] = ('TABLE_CONSTRAINT', 'FOREIGN_KEY', p[4], referenced_table, referenced_columns)
        else:
            p[0] = ('TABLE_CONSTRAINT', 'FOREIGN_KEY', p[4], referenced_table, referenced_columns, p[11], p[12], p[13])

def p_column_list(p):
    '''column_list : IDENTIFIER
                   | column_list COMMA IDENTIFIER'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        add_error(f"Syntax error at token ({p.value})", p.lineno)
    else:
        add_error("Syntax error at EOF", lexer.lineno)

# Build the parser
parser = yacc.yacc()



#----------------------------------------------


# parse sql into middle form
def sql_parse_middle(sql):
    global error_list, parsed_tables
    error_list = []
    parsed_tables = []
    lexer.lineno = 1
    result = parser.parse(sql)

    return result, error_list


# convert parsed result to json
def middle_parse_json(file_id, parsed_result):
    tables = []
    
    existing_tables = get_all_tables_idname(file_id)
    existing_table_dict = {table[1]: table[0] for table in existing_tables}
    
    for table in parsed_result:
        table_name = table[1]
        columns_and_constraints = table[2]
        
        attributes = []
        foreign_keys = []
        # track composite primary key
        primary_key_columns = set()
        
        for item in columns_and_constraints:
            if item[0] == 'TABLE_CONSTRAINT' and item[1] == 'PRIMARY_KEY':
                primary_key_columns.update(item[2])
        
        for item in columns_and_constraints:
            if item[0] == 'COLUMN':
                column_name = item[1]
                column_type = item[2] if item[2] is not None else ""
                column_constraints = {
                    "primary_key": column_name in primary_key_columns,
                    "not_null": False,
                    "unique": False,
                    "auto_increment": False,
                    "default": None
                }
                
                for constraint in item[3]:
                    if 'PRIMARY KEY' in constraint:
                        column_constraints["primary_key"] = True
                    elif 'NOT NULL' in constraint:
                        column_constraints["not_null"] = True
                    elif 'UNIQUE' in constraint:
                        column_constraints["unique"] = True
                    elif 'AUTO_INCREMENT' in constraint:
                        column_constraints["auto_increment"] = True
                    elif 'DEFAULT' in constraint:
                        column_constraints["default"] = constraint.split(' ', 1)[1]
                
                attributes.append({
                    "name": column_name,
                    "type": column_type.lower(),
                    **column_constraints
                })
            elif item[0] == 'TABLE_CONSTRAINT' and item[1] == 'FOREIGN_KEY':
                foreign_keys.append({
                    "from": f"{table_name}.{item[2][0]}",
                    "references": f"{item[3]}.{item[4][0]}"
                })
        
        table_dict = {
            "name": table_name,
            "attributes": attributes
        }
        
        if foreign_keys:
            table_dict["foreign_keys"] = foreign_keys
            
            
        # Check if table already exists in the database
        
        # Table exists, alter it
        if table_name in existing_table_dict:
            table_id = existing_table_dict[table_name]
            alter_table(table_id, table_name, str(table_dict))
            
            del existing_table_dict[table_name]
        
        # New table, add it
        else:
            x, y = get_tables_position(file_id)
            if x == None or y == None:
                x, y = 0, 0
            
            add_table(table_name, str(table_dict), x, y, file_id)
        
        tables.append(table_dict)
        
    # Delete remaining tables that weren't altered
    for table_name, table_id in existing_table_dict.items():
        delete_table(table_id)
        

    return 1

# Example usage

sql = """
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(255) NOT NULL UNIQUE,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE,
    PhoneNumber VARCHAR(20),
    ddd DATE DEFAULT current_timestamp
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT NOT NULL,
    OrderDate DATE NOT NULL,
    TotalAmount DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
CREATE TABLE mapping (
    OrderID INT ,
    CustomerID INT NOT NULL,
    PRIMARY KEY (OrderID, CustomerID)
);
    """
