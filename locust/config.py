import os
import csv

USER_FILE = os.getenv('USER_FILE', 'credentials')

def fetch_data_from_csv(file_name):
    with open(file_name, 'rU') as csv_file:
        csv_reader = csv.reader(csv_file)
        credentials_list = list(csv_reader)
    return credentials_list

USER_CREDENTAILS = fetch_data_from_csv('credentials.csv')
PASSWORD = 'ARbi12.,'
