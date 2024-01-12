
import tkinter as tk
import pyodbc
import pandas as pd
import datetime

# Database connection 
conn_string = ("Driver={ODBC Driver 17 for SQL Server};"
               "Server=AnkushBL\\SQLEXPRESS;"  
               "Database=Inventory;"
               "Trusted_Connection=yes;")

conn = pyodbc.connect(conn_string)
cursor = conn.cursor()

# Generate client ID
def generate_client_id(name):
    now = datetime.datetime.now()  
    year_str = str(now.year)[-2:]  
    month_str = str(now.month).zfill(2)
    name_prefix = name[:3].upper()
    first_letter = name[0]   
    
    cursor.execute("""
        SELECT COUNT(*)
        FROM Client_Info
        WHERE ClientID LIKE ?
    """, (f"{year_str}{month_str}{first_letter}%",))
    
    count = cursor.fetchone()[0] + 1
    serial_num = str(count).zfill(2)
    
    return f"{year_str}{month_str}{name_prefix}{serial_num}"

# Insert client  
def insert_client(name, phone_num, gender, age, op_procedure, amount):
    client_id = generate_client_id(name)
    cursor.execute("""
        INSERT INTO Client_Info (ClientID, Name, PhoneNum, Gender, Age, OPProcedure, Amount)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (client_id, name, phone_num, gender, age, op_procedure, amount))
    conn.commit()

# Tkinter GUI
root = tk.Tk()
root.title("Add New Client")

# Name
name_label = tk.Label(root, text="Name:")  
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# Phone 
phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0)  
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

# Gender
gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row=2, column=0)
gender_var = tk.StringVar()
gender_menu = tk.OptionMenu(root, gender_var, "M", "F")
gender_menu.grid(row=2, column=1)

# Age
age_label = tk.Label(root, text="Age:")
age_label.grid(row=3, column=0)
age_entry = tk.Entry(root) 
age_entry.grid(row=3, column=1)

# Procedure 
proc_label = tk.Label(root, text="OP/Procedure:")
proc_label.grid(row=4, column=0)
proc_entry = tk.Entry(root)
proc_entry.grid(row=4, column=1)

# Amount
amount_label = tk.Label(root, text="Amount:")  
amount_label.grid(row=5, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=5, column=1)

# Save data
def save_client():
    name = name_entry.get()
    phone = phone_entry.get()
    gender = gender_var.get()
    age = int(age_entry.get())
    procedure = proc_entry.get()
    amount = float(amount_entry.get())  
    insert_client(name, phone, gender, age, procedure, amount)

# Save button
save_btn = tk.Button(root, text="Save", command=save_client)
save_btn.grid(row=6, column=1)


import tkinter as tk
import pyodbc
import pandas as pd
import datetime

# Database connection 
conn_string = ("Driver={ODBC Driver 17 for SQL Server};"
               "Server=AnkushBL\\SQLEXPRESS;"  
               "Database=Inventory;"
               "Trusted_Connection=yes;")

conn = pyodbc.connect(conn_string)
cursor = conn.cursor()

# Generate client ID
def generate_client_id(name):
    now = datetime.datetime.now()  
    year_str = str(now.year)[-2:]  
    month_str = str(now.month).zfill(2)
    name_prefix = name[:3].upper()
    first_letter = name[0]   
    
    cursor.execute("""
        SELECT COUNT(*)
        FROM Client_Info
        WHERE ClientID LIKE ?
    """, (f"{year_str}{month_str}{first_letter}%",))
    
    count = cursor.fetchone()[0] + 1
    serial_num = str(count).zfill(2)
    
    return f"{year_str}{month_str}{name_prefix}{serial_num}"

# Insert client  
def insert_client(name, phone_num, gender, age, op_procedure, amount):
    client_id = generate_client_id(name)
    cursor.execute("""
        INSERT INTO Client_Info (ClientID, Name, PhoneNum, Gender, Age, OPProcedure, Amount)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (client_id, name, phone_num, gender, age, op_procedure, amount))
    conn.commit()

# Tkinter GUI
root = tk.Tk()
root.title("Add New Client")

# Name
name_label = tk.Label(root, text="Name:")  
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# Phone 
phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0)  
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

# Gender
gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row=2, column=0)
gender_var = tk.StringVar()
gender_menu = tk.OptionMenu(root, gender_var, "M", "F")
gender_menu.grid(row=2, column=1)

# Age
age_label = tk.Label(root, text="Age:")
age_label.grid(row=3, column=0)
age_entry = tk.Entry(root) 
age_entry.grid(row=3, column=1)

# Procedure 
proc_label = tk.Label(root, text="OP/Procedure:")
proc_label.grid(row=4, column=0)
proc_entry = tk.Entry(root)
proc_entry.grid(row=4, column=1)

# Amount
amount_label = tk.Label(root, text="Amount:")  
amount_label.grid(row=5, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=5, column=1)

# Save data
def save_client():
    name = name_entry.get()
    phone = phone_entry.get()
    gender = gender_var.get()
    age = int(age_entry.get())
    procedure = proc_entry.get()
    amount = float(amount_entry.get())  
    insert_client(name, phone, gender, age, procedure, amount)

# Save button
save_btn = tk.Button(root, text="Save", command=save_client)
save_btn.grid(row=6, column=1)

root.mainloop()