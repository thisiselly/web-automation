import configparser
import csv
import pandas as pd

import yaml


class ConfigReader:
    @staticmethod
    def read_yaml(file_path, key_name=None):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
                if key_name:
                    return data[key_name]
                return data
        except FileNotFoundError:
            print(f"Error: YAML file not found: {file_path}")
            return None
        except yaml.YAMLError as e:
            print(f"Error: Invalid YAML format in {file_path}: {e}")
            return None

    @staticmethod
    def read_csv(file_path):
        try:
            return pd.read_csv(file_path).values.tolist()
        except FileNotFoundError:
            print(f"Error: CSV file not found: {file_path}")
            return None
        except csv.Error as e:
            print(f"Error: Invalid CSV format in {file_path}: {e}")
            return None

    @staticmethod
    def read_ini(file_path):
        try:
            config = configparser.ConfigParser()
            config.read(file_path, encoding='utf8')
            return config
        except FileNotFoundError:
            print(f"Error: INI file not found: {file_path}")
            return None
        except configparser.Error as e:
            print(f"Error: Invalid INI format in {file_path}: {e}")
            return None
