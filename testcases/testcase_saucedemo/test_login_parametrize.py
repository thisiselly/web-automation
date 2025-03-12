import pytest

from pages.page_saucedemo.page_saucedemo import PageSourceDemo
from utils.get_test_data import *


class TestLoginByYaml:
    def test_aa(self):
        aa = read_csv_credentials()
        print(aa)
        print(aa)
        print(aa)
        print(aa)

    @pytest.mark.parametrize("username,password", read_csv_credentials())
    def test_login_by_read_csv(self, open_saucedemo, username, password):
        page_source_demo = PageSourceDemo(open_saucedemo)
        page_source_demo.verify_login_with_credential(username, password)

    @pytest.mark.parametrize("data", read_yaml_file()["login_info"])
    def test_login_by_read_yaml(self, open_saucedemo, data):
        username, password = data["username"], data["password"]
        page_source_demo = PageSourceDemo(open_saucedemo)
        page_source_demo.verify_login_with_credential(username, password)
