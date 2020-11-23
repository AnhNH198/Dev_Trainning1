import pandas as pd
import pyodbc

data = pd.read_csv(r'customer.csv')
df = pd.DataFrame(data, columns=['customerid', 'firstname', 'lastname',\
                                 'companyname', 'billingaddress1',\
                                 'billingaddress2', 'city', 'state',\
                                 'postalcode', 'country', 'phonenumber',\
                                 'emailaddress', 'createddate'])
conn = pyodbc.connect('Driver={SQL Server};')