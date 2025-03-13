import configparser
import csv
import yaml

from utils.get_file_path import *

test_csv_path = get_test_data_csv_path
test_yaml_path = get_test_data_yaml_path
settings_ini_path = get_settings_ini_path

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

def read_ini():
    config = configparser.ConfigParser()
    config.read(settings_ini_path, encoding='utf8')
    return config

if __name__ == '__main__':
    # print(read_yaml_file()["search_data"])
    # print(read_csv_credentials())
    print(read_ini()['hosts'])
