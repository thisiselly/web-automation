import os

# this is project path
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# get log path
get_log_path = os.path.join(project_path, "logs")

# get test data csv path
get_test_data_credential_path = os.path.join(project_path, r"data\testdata_credentials.csv")

# get test data yaml path
get_test_data_yaml_path = os.path.join(project_path, r"data\test_data.yaml")

# get settings.ini path
get_settings_ini_path = os.path.join(project_path, "settings.ini")