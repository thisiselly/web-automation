import pytest

from pages.page_saucedemo.page_saucedemo import PageSourceDemo
from utils.get_file_data import get_yaml_testdata, get_credential_by_csv


class TestLoginByYaml:
    get_csv_test_data = get_credential_by_csv()
    get_yaml_test_data = get_yaml_testdata()

    @pytest.mark.parametrize("username,password", get_csv_test_data)
    def test_login_by_read_csv(self, open_saucedemo, username, password):
        page_source_demo = PageSourceDemo(open_saucedemo)
        page_source_demo.verify_login_with_credential(username, password)

    @pytest.mark.parametrize("data", get_yaml_test_data["login_info"])
    def test_login_by_read_yaml(self, open_saucedemo, data):
        username, password = data["username"], data["password"]
        page_source_demo = PageSourceDemo(open_saucedemo)
        page_source_demo.verify_login_with_credential(username, password)
