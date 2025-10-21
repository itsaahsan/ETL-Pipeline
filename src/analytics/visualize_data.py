import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(df, column, output_path=None):
    import os
    if output_path is None:
        # Default output path - needs to be defined from calling context
        output_path = os.path.join("data", "processed", "visualization.png")
    df[column].plot(kind="hist")
    plt.title(f"Distribution of {column}")
    plt.savefig(output_path)
    plt.close()  # Close the figure to free memory

if __name__ == "__main__":
    import os
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define paths relative to project root
    input_path = os.path.join(script_dir, "..", "..", "data", "processed", "transformed_api_data.csv")
    output_dir = os.path.join(script_dir, "..", "..", "data", "processed")
    output_path = os.path.join(output_dir, "visualization.png")
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    df = pd.read_csv(input_path)
    # Check if 'value' column exists, if not use first column
    column_to_visualize = "value"
    if column_to_visualize not in df.columns:
        # Use first column if 'value' doesn't exist
        column_to_visualize = df.columns[0] if len(df.columns) > 0 else df.columns[0]
    visualize_data(df, column_to_visualize, output_path)
