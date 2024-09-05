import pandas as pd
from sqlalchemy import create_engine

# Load the CSV into a DataFrame and skip the first row and column
df = pd.read_csv('List Of Water Falls.csv')


df = df.iloc[0:, 1:]  # Removing the first row (index 0) and first column (index 0)
df.columns = df.iloc[0]  # Set the first row as header
df = df[1:]

connection_string = "postgresql://postgres:Vishnu%402@localhost:5432/first"

engine = create_engine(connection_string)


try:
    
    df.to_sql('WaterFalls', engine, if_exists='replace', index=False)
    print("DataFrame inserted successfully!")
except Exception as e:
    print(f"Error inserting DataFrame: {e}")


