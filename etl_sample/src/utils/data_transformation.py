import pandas as pd
from datetime import datetime

# For the CSV data, created_at & last_login will be fixed to timestamps and paid_amount will be booleans, else NaN
def transform_test_csv(df):
    df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
    df['last_login'] = pd.to_datetime(df['last_login'], errors='coerce')
    df['is_claimed'] = df['is_claimed'].map({'True': True, 'False': False})
    
    # Convert 'paid_amount' to string first, then to numeric
    df['paid_amount'] = pd.to_numeric(df['paid_amount'], errors='coerce')  # Convert to numeric, invalid parsing will be NaN
    
    # df['paid_amount'] = df['paid_amount'].astype(str)

    return df

# For the JSON data, create into three tables (users, telephone_numbers, & jobs_history), linked through foreign key (user_id) relationships.
def transform_test_json(data):
    users = []
    telephone_numbers = []
    jobs_history = []

    for user in data:
        user_id = user['user_id']
        user_details = user['user_details']

        # Mask PII
        masked_name = user_details['name'][0] + "*****"
        users.append({
            'user_id': user_id,
            'name': masked_name,
            'dob': user_details.get('dob', None),
            'created_at': user.get('created_at', None),
            'updated_at': user.get('updated_at', None),
            'logged_at': user.get('logged_at', None)
        })

        for phone in user_details.get('telephone_numbers', []):
            telephone_numbers.append({
                'user_id': user_id,
                'telephone_number': phone
            })

        for job in user['jobs_history']:
            jobs_history.append({
                'user_id': user_id,
                'occupation': job.get('occupation', None),
                'start': job.get('start', None),
                'end': job.get('end', None)
            })

    return users, telephone_numbers, jobs_history




## MORE DATA TRANSFORMATION FUNCTION CAN BE WRITE HERE