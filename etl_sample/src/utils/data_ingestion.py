import pandas as pd
import json

# read csv
def load_csv(file_path):
    # Read the CSV file and handling quotes and potential issues with commas
    df = pd.read_csv(file_path, quotechar='"', on_bad_lines='warn')
    return df

# read json
def load_json(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            data.append(json.loads(line.strip()))
    return data




## DEFINED ADDITIONAL INGESTION FUNCTION FROM OTHER SOURCE HERE