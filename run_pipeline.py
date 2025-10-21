import subprocess
import sys
import os

def run_pipeline():
    print("Starting ETL Pipeline...")
    
    steps = [
        ("Step 1: Extracting API data...", "src/extraction/extract_api.py"),
        ("Step 2: Cleaning data...", "src/transformation/clean_data.py"),
        ("Step 3: Transforming data...", "src/transformation/transform_data.py"),
        ("Step 4: Loading data to warehouse...", "src/loading/load_data_warehouse.py"),
        ("Step 5: Analyzing data...", "src/analytics/analyze_data.py"),
        ("Step 6: Visualizing data...", "src/analytics/visualize_data.py")
    ]
    
    for step_name, script_path in steps:
        print(step_name)
        try:
            result = subprocess.run([sys.executable, script_path], check=True, capture_output=True, text=True)
            print(f"SUCCESS: {script_path}")
            if result.stdout:
                print(f"Output: {result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"ERROR running {script_path}: {e}")
            print(f"Error output: {e.stderr}")
            return False
        except FileNotFoundError:
            print(f"WARNING: {script_path} not found, skipping...")
    
    print("ETL Pipeline completed!")
    return True

if __name__ == "__main__":
    run_pipeline()