import pandas as pd
import mysql.connector

# Read csv file and change to DataFrame
data = pd.read_csv(r'customer.csv')
df = pd.DataFrame(data, columns=['customerid', 'firstname', 'lastname',\
                                 'companyname', 'billingaddress1',\
                                 'billingaddress2', 'city', 'state',\
                                 'postalcode', 'country', 'phonenumber',\
                                 'emailaddress', 'createddate'])

# Connect to Database
db = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=127.0.0.1:3306;'
    'Database=mydb;'
    'Trusted_Connection=yes;'
)
cursor = db.cursor()

# Create table in sql server
cursor.execute(
    'CREATE TABLE customers (customerid int, firstname nvarchar(50),\
                        lastname nvarchar(50), companyname nvarchar(50),\
                        billingaddress1 varchar(50), billingaddress2\
                        varchar(50), city varchar(50), state varchar(50),\
                        postalcode int, country varchar(50), phonenumber int,\
                        emailaddress nvarchar(50), createddate date\
                        \)'
               )

# Insert DataFrame to Table
for row in df.intertuples():
    cursor.execute('''
    INSERT INTO mydb.dbo.customers(customerid, firstname, lastname,\
                companyname,)
    ''')