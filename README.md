# ETL Pipeline

## Overview
This project implements a comprehensive Extract, Transform, and Load (ETL) pipeline for data integration and analytics. The pipeline handles data extraction from multiple sources (API, database, flat files), transforms the data to clean and standardized format, loads it into a data warehouse, and performs basic analytics and visualization.

## Features
- **Multi-source data extraction**: Support for API, database, and flat file sources
- **Data transformation**: Data cleaning and standardization processes
- **Analytics and visualization**: Data summarization and chart generation
- **Modular architecture**: Separate modules for each ETL stage
- **Error handling**: Graceful fallback mechanisms when external services aren't available

## Project Structure
```
ETL Pipeline/
├── README.md
├── requirements.txt
├── .gitignore
├── config/
│   ├── api_config.yaml          # API configuration settings
│   └── database_config.yaml     # Database configuration settings
├── data/
│   ├── raw/                     # Raw extracted data
│   └── processed/               # Transformed and processed data
├── scripts/
│   └── run_pipeline.sh          # Shell script to run the full pipeline
├── run_pipeline.py              # Python script to run the full pipeline
└── src/
    ├── analytics/
    │   ├── analyze_data.py      # Data analysis functions
    │   └── visualize_data.py    # Data visualization functions
    ├── extraction/
    │   ├── extract_api.py       # API data extraction
    │   ├── extract_database.py  # Database data extraction
    │   └── extract_flat_files.py # Flat file data extraction
    ├── loading/
    │   └── load_data_warehouse.py # Data loading to warehouse
    └── transformation/
        ├── clean_data.py        # Data cleaning functions
        └── transform_data.py    # Data transformation functions
```

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/itsaahsan/ETL-Pipeline.git
   cd ETL-Pipeline
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure API and database settings in the `config/` directory if needed.

## Usage
### Run the full pipeline:
```bash
# Using Python script (cross-platform)
python run_pipeline.py

# Or using shell script (Linux/Mac)
bash scripts/run_pipeline.sh
```

### Run individual components:
```bash
# Extract data
python src/extraction/extract_api.py
python src/extraction/extract_database.py
python src/extraction/extract_flat_files.py

# Transform data
python src/transformation/clean_data.py
python src/transformation/transform_data.py

# Load data
python src/loading/load_data_warehouse.py

# Analyze and visualize
python src/analytics/analyze_data.py
python src/analytics/visualize_data.py
```

## Configuration
### API Configuration
Update `config/api_config.yaml` with your API endpoints and authentication details.

### Database Configuration
Update `config/database_config.yaml` with your database connection parameters.

## Dependencies
- pandas
- requests
- psycopg2-binary
- matplotlib
- pyyaml

See `requirements.txt` for the complete list of dependencies and versions.

## Output
The pipeline generates:
- Cleaned and transformed data in the `data/processed/` directory
- Summary statistics from the analysis step
- Visualizations saved as image files
- If database connection fails, data is saved as CSV in the fallback file

## Error Handling
- If an API is not available, the pipeline creates sample data
- If the database is unavailable, data is saved as CSV as a fallback
- Missing directories are created automatically

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Commit your changes
6. Push to the branch
7. Create a pull request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
