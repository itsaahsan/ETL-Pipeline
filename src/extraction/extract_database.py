import pandas as pd
import psycopg2

def extract_database_data(query, db_config):
    conn = psycopg2.connect(**db_config)
    df = pd.read_sql(query, conn)
    conn.close()
    return df

if __name__ == "__main__":
    db_config = {"host": "localhost", "database": "mydb", "user": "user", "password": "pass"}
    query = "SELECT * FROM mytable;"
    df = extract_database_data(query, db_config)
    df.to_csv("../data/raw/database_data.csv", index=False)
