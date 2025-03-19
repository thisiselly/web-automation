from utils.file_reader import ConfigReader
from utils.get_file_path import *

def get_settings():
    reader = ConfigReader()
    return reader.read_ini(file_path=get_settings_ini_path)

def get_yaml_testdata():
    reader = ConfigReader()
    return reader.read_yaml(file_path=get_test_data_yaml_path)

def get_credential_by_csv():
    reader = ConfigReader()
    return reader.read_csv(file_path=get_test_data_credential_path)
