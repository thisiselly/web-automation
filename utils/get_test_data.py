import csv
import yaml

from utils.get_file_path import *

test_csv_path = get_test_data_csv_path
test_yaml_path = get_test_data_yaml_path

def read_yaml_file():
    with open(test_yaml_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
        return data

def read_csv_credentials():
    credentials = []
    with open(test_csv_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            credentials.append((row["username"], row["password"]))
    return credentials


if __name__ == '__main__':
    # print(read_yaml_file()["search_data"])
    print(read_csv_credentials())
