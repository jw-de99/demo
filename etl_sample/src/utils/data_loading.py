import pandas as pd
from sqlalchemy import create_engine

# Load to SQL
def load_to_sql(df, table_name, engine):
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

def load_json_to_sql(users, telephone_numbers, jobs_history, engine):
    users_df = pd.DataFrame(users)
    telephone_numbers_df = pd.DataFrame(telephone_numbers)
    jobs_history_df = pd.DataFrame(jobs_history)

    users_df.to_sql('users', con=engine, if_exists='replace', index=False)
    telephone_numbers_df.to_sql('telephone_numbers', con=engine, if_exists='replace', index=False)
    jobs_history_df.to_sql('jobs_history', con=engine, if_exists='replace', index=False)
