import pandas as pd
import psycopg2
import os

def load_data(df, table_name, db_config):
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        
        # Create the placeholders for the SQL query
        placeholders = ','.join(['%s'] * len(df.columns))
        columns = ','.join(df.columns)
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        # Execute the query for each row in the dataframe
        for _, row in df.iterrows():
            cursor.execute(query, tuple(row))
        
        conn.commit()
        conn.close()
        print(f"Successfully loaded {len(df)} rows to database table {table_name}")
        return True
    except psycopg2.OperationalError as e:
        print(f"Database connection error: {e}")
        print("Skipping database load. Data is available in CSV format.")
        return False

def save_to_csv(df, output_path):
    """Fallback method to save to CSV if database connection fails"""
    df.to_csv(output_path, index=False)
    print(f"Saved {len(df)} rows to {output_path}")

if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define paths relative to project root
    input_path = os.path.join(script_dir, "..", "..", "data", "processed", "transformed_api_data.csv")
    
    # Define fallback output path
    output_path = os.path.join(script_dir, "..", "..", "data", "processed", "loaded_data.csv")
    
    df = pd.read_csv(input_path)
    
    # Try to load to database first
    db_config = {"host": "localhost", "database": "mydb", "user": "user", "password": "pass"}
    success = load_data(df, "transformed_data", db_config)
    
    # If database load failed, save to CSV as fallback
    if not success:
        save_to_csv(df, output_path)
