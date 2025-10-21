import requests
import pandas as pd

def extract_api_data(api_url, params=None):
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    import os
    # For this example, we'll use a public API that returns JSON data
    # Using JSONPlaceholder as a sample API
    api_url = "https://jsonplaceholder.typicode.com/posts"
    
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up two levels to the project root, then to data/raw
    data_raw_dir = os.path.join(script_dir, "..", "..", "data", "raw")
    output_path = os.path.join(data_raw_dir, "api_data.csv")
    
    # Ensure the output directory exists
    os.makedirs(data_raw_dir, exist_ok=True)
    
    try:
        data = extract_api_data(api_url)
        df = pd.DataFrame(data)
        df.to_csv(output_path, index=False)
        print(f"Data extracted successfully. Shape: {df.shape}")
    except Exception as e:
        print(f"Error extracting API data: {e}")
        # Create a sample data file if API call fails
        sample_data = {
            "userId": [1, 2, 3],
            "id": [1, 2, 3],
            "title": ["Title 1", "Title 2", "Title 3"],
            "body": ["Body 1", "Body 2", "Body 3"]
        }
        df = pd.DataFrame(sample_data)
        df.to_csv(output_path, index=False)
        print("Created sample data file due to API error.")
