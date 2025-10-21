import pandas as pd

def analyze_data(df):
    summary = df.describe()
    return summary

if __name__ == "__main__":
    import os
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define paths relative to project root
    input_path = os.path.join(script_dir, "..", "..", "data", "processed", "transformed_api_data.csv")
    
    df = pd.read_csv(input_path)
    summary = analyze_data(df)
    print(summary)
