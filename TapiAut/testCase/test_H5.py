import pytest
import allure
import requests
from Core.BaseApi import ApiRequest
from Core.Logging import logger
import json
from Core.common import yaml_load, _path

@allure.feature("测试用例集备注说明")
class TestH5:   

        
    @allure.story("用户注册")
    def test_api_user_regist(self):
        print("ok")

        
if __name__=="__main__":
    pytest.main(["-sq",__file__])