from pyparsing import (
    Literal,
    Word,
    delimitedList,
    alphas,
    alphanums,
    OneOrMore,
    ZeroOrMore,
    CharsNotIn,
    replaceWith,
)



def field_act(tok):
    # attribute info & escape double quotes and backslashes. *str has these things
    return ("<" + tok[0] + "> " + " ".join(tok[1:])).replace('"', '\\"')


def field_list_act(toks):
    return "|".join(toks)


def create_table_act(toks):
    return (
        """[%(tablename)s|%(columns)s];"""
        % toks
    )

def sql_parse_middle(raw_sql):
    # rule: capture everything inside parentheses.
    inside_parentheses = "(" + ZeroOrMore(CharsNotIn(")")) + ")"
    # rule: capture field definition
    field_def = OneOrMore(Word(alphas, alphanums + "_\"':-") | inside_parentheses)


    field_def.setParseAction(field_act)

    field_list_def = delimitedList(field_def)
    
    field_list_def.setParseAction(field_list_act)

    create_table_def = (
        Literal("CREATE")
        + "TABLE"
        + Word(alphas, alphanums + "_").setResultsName("tablename")
        + "("
        + field_list_def.setResultsName("columns")
        + ")"
        + ";"
    )

    create_table_def.setParseAction(create_table_act)

    other_statement_def = OneOrMore(CharsNotIn(";")) + ";"
    other_statement_def.setParseAction(replaceWith(""))
    comment_def = "--" + ZeroOrMore(CharsNotIn("\n"))
    comment_def.setParseAction(replaceWith(""))

    statement_def = comment_def | create_table_def | other_statement_def
    defs = OneOrMore(statement_def)

    table_info_list = []

    for i in defs.parseString(raw_sql):
        if i != "":
            table_info_list.append(i)
    return table_info_list




# test 1
# raw_sql = 
"""
--tbl product
CREATE TABLE product (
        product_id INT PRIMARY KEY UNIQUE NOT NULL, 
        quantity INT NOT NULL,
        product_type CHAR(10) NOT NULL,
        description TEXT
    );
-- tbl order
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    product_id INT,
    order_date DATE DEFAULT TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);
"""


# test2
# raw_sql2 = """
# --tbl product
# CREATE TABLE product (
#         product_id INT PRIMARY KEY UNIQUE NOT NULL, 
#         quantity INT NOT NULL,
#         product_type CHAR(10) NOT NULL,
#         description TEXT DEFAULT 'No description'
#     );
# -- tbl order
# CREATE TABLE orders (
#     order_id INT PRIMARY KEY,
#     product_id INT,
#     order_date DATE,
#     FOREIGN KEY (product_id) REFERENCES product(product_id)
# );
# """