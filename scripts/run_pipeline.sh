#!/bin/bash
echo "Starting ETL Pipeline..."

echo "Step 1: Extracting API data..."
python src/extraction/extract_api.py

echo "Step 2: Cleaning data..."
python src/transformation/clean_data.py

echo "Step 3: Transforming data..."
python src/transformation/transform_data.py

echo "Step 4: Loading data to warehouse..."
python src/loading/load_data_warehouse.py

echo "Step 5: Analyzing data..."
python src/analytics/analyze_data.py

echo "Step 6: Visualizing data..."
python src/analytics/visualize_data.py

echo "ETL Pipeline completed!"
