import csv
import pandas as pd
from sqlalchemy import create_engine, types
from sqlalchemy.types import Integer
from dateutil.parser import parse
engine = create_engine('mysql://root:Vishal@26@localhost/grafanatesting') # enter your password and database names here

df = pd.read_csv("food_demo.csv",error_bad_lines=False, dtype=object) # Replace Excel_file_name with your excel sheet name
b = list(df)
print(b)
for j in df['Date'].values:
	dt = parse(j)
print(dt)
# datetime.datetime(2010, 2, 15, 0, 0)
print(dt.strftime('%d/%m/%Y'))

df['Date']=pd.to_datetime(df['Date'])

for j in b[4:]:
	df[j] =df[j].replace(regex=True,to_replace=r'\D',value=r'')
	
	df[j]=pd.to_numeric(df[j], errors ='coerce',downcast ='integer')

df.to_sql('food_demos',con=engine,if_exists='replace') # Replace Table_name with your sql table name
