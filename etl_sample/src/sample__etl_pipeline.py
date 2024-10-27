import logging
from sqlalchemy import create_engine
from src.utils.data_ingestion import load_csv, load_json
from src.utils.data_transformation import transform_test_csv, transform_test_json
from src.utils.data_loading import load_to_sql, load_json_to_sql

# Configure logging
logging.basicConfig(level=logging.INFO)

def run_etl(csv_file, json_file, db_uri):
    logging.info("Starting ETL Process")
    
    # Ingest CSV
    df_csv = load_csv(csv_file)
    transformed_csv = transform_test_csv(df_csv)
    
    # Ingest JSON
    json_data = load_json(json_file)
    users, telephone_numbers, jobs_history = transform_test_json(json_data)
    
    # Create DB engine
    engine = create_engine(db_uri)

    # Load data into SQL
    load_to_sql(transformed_csv, 'test', engine)
    load_json_to_sql(users, telephone_numbers, jobs_history, engine)

    logging.info("ETL Process Completed")
