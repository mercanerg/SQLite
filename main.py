import sqlite3
import pandas as pd

def conn_sql():
    try:
        country = 'USA'
        min_amount = 5
        # add apostrophes bothsides of country string
        country = "'" + country + "'"
        conn = sqlite3.connect('chinook.db')
        dbcursor = conn.cursor()
        query_string = """SELECT FirstName, LastName, Country FROM customers 
        WHERE Country =""" + country
        # convert min_amount value to string to concatenate end of query string
        q_string = "SELECT InvoiceId, CustomerID, BillingCountry, Total FROM invoices WHERE Total < "
        q_string += str(min_amount) + " and BillingCountry = " + country

        # fill sql data to pandas data frame
        df = pd.read_sql(q_string, conn)
    except Exception as err:
        print('Connection Error  ', err)
    else:
        print('Connected Database')
        print(df.head(50))
conn_sql()
