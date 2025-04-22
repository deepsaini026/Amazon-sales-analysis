import pandas as pd
import os
import sqlalchemy as sq
import pymysql 
import warnings
import pyodbc 


filess=os.listdir(r"C:\Users\HP\Downloads\filessss")

df=pd.read_csv(r"C:\Users\HP\Downloads\filessss\orders.csv",na_values=['Not Available','unknown'])
print(df)

print(df['Ship Mode'].unique())
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(" ","_")

df['discount']=df['list_price']*df['discount_percent']*0.01
df['sale_price']=df['list_price']-df['discount']
df['profit']=df['sale_price']-df['cost_price']
df['order_date']=pd.to_datetime(df['order_date'],format='%Y-%m-%d')
df.drop(columns=['list_price','discount_percent','cost_price'],inplace=True)
print(df)

engine=sq.create_engine('mssql://NIDEE\SQLEXPRESS02/sql_python?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn=engine.connect()

df.to_sql('df_orders',con=conn,index=False,if_exists='replace')
 