import pandas as pd

def transform_data(df):
    # Check if 'date' column exists, if not create it with current timestamp
    if 'date' not in df.columns:
        df['date'] = pd.Timestamp.now()
    else:
        df["date"] = pd.to_datetime(df["date"])
    
    # Check if 'value' column exists, if not try common numeric columns or create it
    if 'value' not in df.columns:
        # Look for common numeric columns that could be used as 'value'
        numeric_cols = df.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 0:
            # Use the first numeric column as 'value'
            df['value'] = df[numeric_cols[0]].astype(float)
        else:
            # If no numeric columns exist, create a dummy value column
            df['value'] = 1.0
    else:
        df["value"] = df["value"].astype(float)
    
    return df

if __name__ == "__main__":
    import os
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define paths relative to project root
    input_path = os.path.join(script_dir, "..", "..", "data", "processed", "cleaned_api_data.csv")
    output_dir = os.path.join(script_dir, "..", "..", "data", "processed")
    output_path = os.path.join(output_dir, "transformed_api_data.csv")
    
    # Ensure the output directory exists (though it should already exist from clean_data.py)
    os.makedirs(output_dir, exist_ok=True)
    
    df = pd.read_csv(input_path)
    transformed_df = transform_data(df)
    transformed_df.to_csv(output_path, index=False)
