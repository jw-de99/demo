1. PROJECT OVERVIEW:
    The goal of this project is to create an ETL pipeline in Python/SQL that demonstrate the ingestion, transformation, and loading of raw data from sources (CSV and JSON files) into a SQL database. The pipeline should be modular, reusable, and extensible, allowing for easy addition of new data sources and storage options.
___________________________________________________________________________________

2. ETL PROCESS:
    Extract: Read data from the specified CSV and JSON files.
    Transform: Clean and process the data by defining transformation functions.
    Load: Insert the transformed data into the appropriate SQL tables.
    Unit Test: Unit tests are created to validate the functionality of each component.
    Logging: Logging is implemented throughout the pipeline to track the flow of data and capture any errors that occur during execution.
___________________________________________________________________________________

3. THE PROJECT INCLUDES:
    Source Code: The ETL pipeline code is organized into modules and hosted in a public GitHub repository.
    Jupyter Notebooks: Notebooks demonstrate the execution of the ETL process on the requirement.
    Docker Containers: Containers are provided to run both the ETL pipeline and the SQL database.
___________________________________________________________________________________

4. PROJECT STRUCTURE:
    src/
    ├── utils/
    │   ├── data_ingestion.py
    │   ├── data_loading.py
    │   └── data_transformation.py
    │
    ├── {job_name}.py
    │
    ├── tests/
    │   └── data_transformation_test.py
    │
    ├── docker-compose.yml
    ├── Dockerfile
    ├── README.md
    ├── requirements.txt
    └── run_etl.ipynb
___________________________________________________________________________________

5. SETTING UP THE PROJECT:
    PREREQUISITES - 
    1. Ensure you have Python installed (preferably Python 3.6 or higher).
    2. Everything installed defined in "requirements.txt"
    3. Docker

    STEPS - 
    a. Build and Run Docker Containers:
        docker-compose up --build

    b. Execute the job from the notebook:
        Go to "ETL_SAMPLE/run_etl.ipynb"

    c. Accessing the SQL Database: 
        Connect to the PostgreSQL database using a client or a SQL command line tool with the credentials provided in docker-compose.yml.
        
        localhost:5432/testdb

DB_URI = 'postgresql://user:password@localhost:5432/testdb'
