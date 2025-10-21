import pandas as pd
import os

def extract_flat_file_data(file_path):
    """
    Extract data from flat files (CSV, JSON, TXT)
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist")
    
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.json'):
        df = pd.read_json(file_path)
    elif file_path.endswith('.txt'):
        df = pd.read_csv(file_path, delimiter='\t')
    else:
        raise ValueError(f"Unsupported file format for {file_path}")
    
    return df

if __name__ == "__main__":
    # Example usage
    file_path = "../data/raw/sample_data.csv"  # This would be an existing file
    # For this example, we'll skip execution if file doesn't exist
    if os.path.exists(file_path):
        df = extract_flat_file_data(file_path)
        print("Data extracted successfully")
        print(df.head())
    else:
        print(f"Sample file {file_path} does not exist, skipping extraction.")