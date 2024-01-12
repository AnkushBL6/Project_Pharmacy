<<<<<<< HEAD
import pyodbc
import pandas as pd
import datetime

# Connection string (replace placeholders with your actual details)
conn_string = ("Driver={ODBC Driver 17 for SQL Server};"
             "Server=AnkushBL\SQLEXPRESS;"
             "Database=Inventory;"
             "Trusted_Connection=yes;")

# Connect to the database 
conn = pyodbc.connect(conn_string)
cursor = conn.cursor()

def generate_client_id(name):

    now = datetime.datetime.now()  
    year_str = str(now.year)[-2:]
    month_str = str(now.month).zfill(2)

    name_prefix = name[:3].upper() 
    first_letter = name[0]

    # Count IDs with same FIRST letter 
    cursor.execute("""
        SELECT COUNT(*)
        FROM Client_Info
        WHERE ClientID LIKE ? 
    """, (f"{year_str}{month_str}{first_letter}%", ))

    count = cursor.fetchone()[0] + 1
    serial_num = str(count).zfill(2)

    # ID contains first 3 letters    
    return f"{year_str}{month_str}{name_prefix}{serial_num}"

def insert_client(name, phone_num, gender, age, op_procedure, amount):
   client_id = generate_client_id(name)

   cursor.execute("INSERT INTO Client_Info (ClientID, Name, PhoneNum, Gender, Age, OPProcedure, Amount) VALUES (?, ?, ?, ?, ?, ?, ?)",
                 (client_id, name, phone_num, gender, age, op_procedure, amount))
   conn.commit()


# Gather client information
client_name = input("Enter client name: ")
client_phone_num = input("Enter phone number: ")
client_gender = input("Enter gender (M/F): ")
client_age = int(input("Enter age: "))
client_op_procedure = input("Enter procedure: ")
client_amount = float(input("Enter amount: "))

# Insert client information
insert_client(client_name, client_phone_num, client_gender, client_age, client_op_procedure, client_amount)
print("Client information saved successfully!")

# Display client data
dataframe = pd.read_sql("Select * from Client_Info", conn)
print(dataframe)

# Close the database connection
# cursor.close()

import pyodbc
import pandas as pd
import datetime

# Connection string (replace placeholders with your actual details)
conn_string = ("Driver={ODBC Driver 17 for SQL Server};"
             "Server=AnkushBL\SQLEXPRESS;"
             "Database=Inventory;"
             "Trusted_Connection=yes;")

# Connect to the database 
conn = pyodbc.connect(conn_string)
cursor = conn.cursor()

def generate_client_id(name):

    now = datetime.datetime.now()  
    year_str = str(now.year)[-2:]
    month_str = str(now.month).zfill(2)

    name_prefix = name[:3].upper() 
    first_letter = name[0]

    # Count IDs with same FIRST letter 
    cursor.execute("""
        SELECT COUNT(*)
        FROM Client_Info
        WHERE ClientID LIKE ? 
    """, (f"{year_str}{month_str}{first_letter}%", ))

    count = cursor.fetchone()[0] + 1
    serial_num = str(count).zfill(2)

    # ID contains first 3 letters    
    return f"{year_str}{month_str}{name_prefix}{serial_num}"

def insert_client(name, phone_num, gender, age, op_procedure, amount):
   client_id = generate_client_id(name)

   cursor.execute("INSERT INTO Client_Info (ClientID, Name, PhoneNum, Gender, Age, OPProcedure, Amount) VALUES (?, ?, ?, ?, ?, ?, ?)",
                 (client_id, name, phone_num, gender, age, op_procedure, amount))
   conn.commit()


# Gather client information
client_name = input("Enter client name: ")
client_phone_num = input("Enter phone number: ")
client_gender = input("Enter gender (M/F): ")
client_age = int(input("Enter age: "))
client_op_procedure = input("Enter procedure: ")
client_amount = float(input("Enter amount: "))

# Insert client information
insert_client(client_name, client_phone_num, client_gender, client_age, client_op_procedure, client_amount)
print("Client information saved successfully!")

# Display client data
dataframe = pd.read_sql("Select * from Client_Info", conn)
print(dataframe)

# Close the database connection
# cursor.close()
# conn.close()