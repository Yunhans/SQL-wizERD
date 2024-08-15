'''

--- json format translation to mysql script ---

'''


def generate_sql_script(tables):
    script = ""
    
    for table in tables:
        table_name = table['name']
        script += f"CREATE TABLE {table_name} (\n"
        
        columns = []
        primary_keys = []
        foreign_keys = []
        
        for attr in table['attributes']:
            column_def = f"  {attr['name']} {attr['type']}"
            
            if attr['not_null']:
                column_def += " NOT NULL"
            if attr['unique']:
                column_def += " UNIQUE"
            if attr['auto_increment']:
                column_def += " AUTO_INCREMENT"
            if attr['default'] is not None:
                default_value = attr['default']
                if isinstance(default_value, str):
                    default_value = f"'{default_value}'"
                column_def += f" DEFAULT {default_value}"
            if attr['primary_key']:
                primary_keys.append(attr['name'])
            
            columns.append(column_def)
        
        for fk in table['foreign_keys']:
            from_column = fk['from'].split('.')[-1].strip()
            ref_table, ref_column = fk['references'].split('.')
            foreign_keys.append(f"  FOREIGN KEY ({from_column}) REFERENCES {ref_table.strip()}({ref_column.strip()})")
        
        script += ",\n".join(columns)
        
        if primary_keys:
            script += f",\n  PRIMARY KEY ({', '.join(primary_keys)})"
        
        if foreign_keys:
            script += ",\n" + ",\n".join(foreign_keys)
        
        script += "\n);\n\n"
    
    return script

# Example usage
tables = [
    {
        'name': 'product',
        'attributes': [
            {
                'name': 'product_id',
                'type': 'INT',
                'primary_key': True,
                'not_null': True,
                'unique': True,
                'auto_increment': False,
                'default': None
            },
            {
                'name': 'quantity',
                'type': 'INT',
                'primary_key': False,
                'not_null': True,
                'unique': False,
                'auto_increment': False,
                'default': None
            },
            {
                'name': 'product_type',
                'type': 'CHAR(10)',
                'primary_key': False,
                'not_null': True,
                'unique': False,
                'auto_increment': False,
                'default': None
            },
            {
                'name': 'description',
                'type': 'TEXT',
                'primary_key': False,
                'not_null': False,
                'unique': False,
                'auto_increment': False,
                'default': None
            }
        ],
        'foreign_keys': []
    },
    {
        'name': 'orders',
        'attributes': [
            {
                'name': 'order_id',
                'type': 'INT',
                'primary_key': True,
                'not_null': False,
                'unique': False,
                'auto_increment': False,
                'default': None
            },
            {
                'name': 'product_id',
                'type': 'INT',
                'primary_key': True,
                'not_null': False,
                'unique': False,
                'auto_increment': False,
                'default': None
            },
            {
                'name': 'order_date',
                'type': 'DATE',
                'primary_key': False,
                'not_null': False,
                'unique': False,
                'auto_increment': False,
                'default': 'TIMESTAMP'
            }
        ],
        'foreign_keys': [
            {
                'from': 'orders.product_id',
                'references': 'product.product_id'
            }
        ]
    }
]

# table2 = []

# mysql_script = generate_sql_script(tables)
# print(mysql_script)