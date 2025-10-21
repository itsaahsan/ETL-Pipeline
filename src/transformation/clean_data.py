import pandas as pd

def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df

if __name__ == "__main__":
    import os
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define paths relative to project root
    input_path = os.path.join(script_dir, "..", "..", "data", "raw", "api_data.csv")
    output_dir = os.path.join(script_dir, "..", "..", "data", "processed")
    output_path = os.path.join(output_dir, "cleaned_api_data.csv")
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    df = pd.read_csv(input_path)
    cleaned_df = clean_data(df)
    cleaned_df.to_csv(output_path, index=False)
