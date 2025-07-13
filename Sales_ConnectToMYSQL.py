import pandas as pd
import mysql.connector

# Nustatymai jungimuisi prie MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'TAVO_SLAPTAZODIS',
    'database': 'sales_db'
}

# Įkeliame CSV
df = pd.read_csv('data/sales_data.csv')

# Prisijungiame prie MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Įkeliame po vieną eilutę
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO sales_data (
            Product_ID, Sale_Date, Sales_Rep, Region, Sales_Amount,
            Quantity_Sold, Product_Category, Unit_Cost, Unit_Price,
            Customer_Type, Discount, Payment_Method, Sales_Channel,
            Region_and_Sales_Rep
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
cursor.close()
conn.close()

print(" Duomenys įkelti į MySQL sėkmingai.")
