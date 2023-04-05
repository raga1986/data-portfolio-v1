import os
import pandas as pd
import warnings

from src.extract import extract_transactional_data
from src.transform import identify_and_remove_duplicated_values
from src.load_data_to_s3 import df_to_s3

from datetime import datetime
warnings.filterwarnings("ignore")
#from dotenv import load_dotenv

#load_dotenv()  # only for local testing

# import variables from .env file
dbname = os.getenv("dbname")
host = os.getenv("host")
port = os.getenv("port")
user = os.getenv("user")
password = os.getenv("password")
aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key_id = os.getenv("aws_secret_access_key_id")

os.system('clear')

def main():
    start_time = datetime.now()
    # Extract data
    print("extracting data")
    ot_data = extract_transactional_data(dbname, host, port, user, password)

    # Transform data
    print("transforming data - removing duplicates")
    ot_data_cleaned = identify_and_remove_duplicated_values(ot_data)
    ot_data_final = ot_data_cleaned.copy()

    # fix the invoice date
    print("transforming data - fixing date time")
    ot_data_final['invoice_date'] = pd.to_datetime(ot_data_final['invoice_date'])

    # load data into s3 bucket.
    print("Loading data")
    key = "online_transactions_transformation/final/rd_online_transactions.csv"
    s3_bucket = "waia-data-dump"
    df_to_s3(ot_data_final, key, s3_bucket, aws_access_key_id, aws_secret_access_key_id)

    execution_time = datetime.now() - start_time
    print(f"\nTotal execution time (hh:mm:ss.ms) {execution_time}")

if __name__ == "__main__":
    main()



